#!/usr/bin/env python3
"""
Script pour créer des pages WordPress à partir des fichiers markdown dans content/
"""

import os
import re
import json
import requests
import base64
from pathlib import Path
import yaml
from typing import Dict, Any, Optional

# Import de la configuration
try:
    from wordpress_config import WORDPRESS_CONFIG, EXCLUDED_FILES, CUSTOM_SLUGS, PAGE_HIERARCHY
except ImportError:
    # Configuration par défaut si le fichier de config n'existe pas
    WORDPRESS_CONFIG = {
        'url': 'http://localhost:8080',
        'username': 'admin',
        'password': 'password'
    }
    EXCLUDED_FILES = {'index.md', '404.html'}
    CUSTOM_SLUGS = {}
    PAGE_HIERARCHY = {}

class WordPressPageCreator:
    def __init__(self, wp_url: str, username: str, password: str):
        self.wp_url = wp_url
        # Essayer d'abord l'URL standard, puis l'URL avec index.php
        self.api_url = f"{wp_url}/wp-json/wp/v2"
        self.api_url_alt = f"{wp_url}/index.php?rest_route=/wp/v2"
        self.auth = base64.b64encode(f"{username}:{password}".encode()).decode()
        self.headers = {
            'Authorization': f'Basic {self.auth}',
            'Content-Type': 'application/json'
        }
        self.use_alt_url = False
    
    def test_connection(self) -> bool:
        """Test la connexion à l'API WordPress"""
        try:
            # Essayer l'URL standard
            response = requests.get(f"{self.api_url}/pages", headers=self.headers)
            if response.status_code == 200:
                return True

            # Essayer l'URL alternative avec index.php
            response = requests.get(f"{self.api_url_alt}/pages", headers=self.headers)
            if response.status_code == 200:
                self.use_alt_url = True
                print("ℹ️  Utilisation de l'URL alternative pour l'API REST")
                return True

            return False
        except Exception as e:
            print(f"Erreur de connexion: {e}")
            return False
    
    def parse_markdown_file(self, file_path: Path) -> Dict[str, Any]:
        """Parse un fichier markdown et extrait les métadonnées et le contenu"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extraction du front matter YAML
        front_matter = {}
        markdown_content = content
        
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    front_matter = yaml.safe_load(parts[1]) or {}
                    markdown_content = parts[2].strip()
                except yaml.YAMLError:
                    pass
        
        # Conversion basique du markdown en HTML
        html_content = self.markdown_to_html(markdown_content)
        
        # Détermination du titre
        title = front_matter.get('title')
        if not title:
            # Extraire le premier titre H1 du contenu
            h1_match = re.search(r'^#\s+(.+)$', markdown_content, re.MULTILINE)
            if h1_match:
                title = h1_match.group(1)
            else:
                # Utiliser le nom du fichier comme titre
                title = file_path.stem.replace('-', ' ').replace('_', ' ').title()
        
        return {
            'title': title,
            'content': html_content,
            'description': front_matter.get('description', ''),
            'slug': self.generate_slug(file_path.stem),
            'front_matter': front_matter
        }
    
    def markdown_to_html(self, markdown_content: str) -> str:
        """Conversion basique du markdown en HTML"""
        html = markdown_content
        
        # Titres
        html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
        html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
        html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
        
        # Gras et italique
        html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
        html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
        
        # Liens
        html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html)
        
        # Listes à puces
        html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
        html = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', html, flags=re.DOTALL)
        html = re.sub(r'</ul>\s*<ul>', '', html)
        
        # Citations
        html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)
        
        # Paragraphes
        paragraphs = html.split('\n\n')
        html_paragraphs = []
        for p in paragraphs:
            p = p.strip()
            if p and not p.startswith('<'):
                p = f'<p>{p}</p>'
            html_paragraphs.append(p)
        
        return '\n'.join(html_paragraphs)
    
    def generate_slug(self, filename: str) -> str:
        """Génère un slug à partir du nom de fichier"""
        # Vérifier s'il y a un slug personnalisé
        if filename in CUSTOM_SLUGS:
            return CUSTOM_SLUGS[filename]

        slug = filename.lower()
        slug = re.sub(r'[àáâãäå]', 'a', slug)
        slug = re.sub(r'[èéêë]', 'e', slug)
        slug = re.sub(r'[ìíîï]', 'i', slug)
        slug = re.sub(r'[òóôõö]', 'o', slug)
        slug = re.sub(r'[ùúûü]', 'u', slug)
        slug = re.sub(r'[ç]', 'c', slug)
        slug = re.sub(r'[^a-z0-9\-]', '-', slug)
        slug = re.sub(r'-+', '-', slug)
        return slug.strip('-')
    
    def page_exists(self, slug: str) -> Optional[int]:
        """Vérifie si une page avec ce slug existe déjà"""
        try:
            api_url = self.api_url_alt if self.use_alt_url else self.api_url
            response = requests.get(
                f"{api_url}/pages",
                headers=self.headers,
                params={'slug': slug}
            )
            if response.status_code == 200:
                pages = response.json()
                return pages[0]['id'] if pages else None
        except Exception as e:
            print(f"Erreur lors de la vérification de l'existence de la page: {e}")
        return None
    
    def create_or_update_page(self, page_data: Dict[str, Any]) -> bool:
        """Crée ou met à jour une page WordPress"""
        existing_page_id = self.page_exists(page_data['slug'])
        
        wp_page_data = {
            'title': page_data['title'],
            'content': page_data['content'],
            'slug': page_data['slug'],
            'status': 'publish'
        }
        
        if page_data['description']:
            wp_page_data['excerpt'] = page_data['description']
        
        try:
            api_url = self.api_url_alt if self.use_alt_url else self.api_url

            if existing_page_id:
                # Mise à jour de la page existante
                response = requests.post(
                    f"{api_url}/pages/{existing_page_id}",
                    headers=self.headers,
                    json=wp_page_data
                )
                action = "mise à jour"
            else:
                # Création d'une nouvelle page
                response = requests.post(
                    f"{api_url}/pages",
                    headers=self.headers,
                    json=wp_page_data
                )
                action = "création"
            
            if response.status_code in [200, 201]:
                page_info = response.json()
                print(f"✅ {action.capitalize()} réussie: {page_data['title']} (ID: {page_info['id']})")
                print(f"   URL: {page_info['link']}")
                return True
            else:
                print(f"❌ Erreur lors de la {action}: {page_data['title']}")
                print(f"   Code: {response.status_code}")
                print(f"   Réponse: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Exception lors de la {action}: {e}")
            return False

def main():
    """Fonction principale"""
    print("🚀 Création des pages WordPress à partir des fichiers markdown...")

    # Initialisation du créateur de pages
    creator = WordPressPageCreator(
        WORDPRESS_CONFIG['url'],
        WORDPRESS_CONFIG['username'],
        WORDPRESS_CONFIG['password']
    )
    
    # Test de la connexion
    print("🔗 Test de la connexion à WordPress...")
    if not creator.test_connection():
        print("❌ Impossible de se connecter à WordPress. Vérifiez:")
        print("   - L'URL WordPress")
        print("   - Les identifiants")
        print("   - Que WordPress est démarré")
        return
    
    print("✅ Connexion à WordPress réussie!")
    
    # Recherche des fichiers markdown
    content_dir = Path("content")
    if not content_dir.exists():
        print("❌ Le dossier 'content' n'existe pas")
        return
    
    markdown_files = [f for f in content_dir.glob("**/*.md") if f.name not in EXCLUDED_FILES]
    print(f"📁 {len(markdown_files)} fichiers markdown trouvés (après exclusions)")

    # Traitement des fichiers
    success_count = 0
    for md_file in markdown_files:
        print(f"\n📄 Traitement de: {md_file}")

        try:
            page_data = creator.parse_markdown_file(md_file)
            if creator.create_or_update_page(page_data):
                success_count += 1
        except Exception as e:
            print(f"❌ Erreur lors du traitement de {md_file}: {e}")
    
    print(f"\n🎉 Terminé! {success_count}/{len(markdown_files)} pages créées/mises à jour avec succès")

if __name__ == "__main__":
    main()
