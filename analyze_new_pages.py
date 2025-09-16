#!/usr/bin/env python3
"""
Script pour analyser les nouvelles pages du site WordPress et suggérer des mappings.
"""

import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET
from datetime import datetime

# Configuration
WORDPRESS_URL = "https://bonpasteurcaen.wordpress.com"
SITEMAP_URL = f"{WORDPRESS_URL}/sitemap.xml"
CONTENT_DIR = "content"

# Mapping existant (copié du script principal)
EXISTING_MAPPINGS = {
    "/": "index.md",
    "/bienvenue/": "bienvenue.md",
    "/presentation/": "presentation.md",
    "/les-eglises/": "eglises.md",
    "/bapteme/": "bapteme.md",
    "/mariage/": "mariage.md",
    "/obseques/": "obseques.md",
    "/confession/": "confession.md",
    "/catechese/": "catechese.md",
    "/catechese-2/": "catechese-2.md",
    "/etudiants/": "etudiants.md",
    "/jeunes-pros/": "jeunes-pros.md",
    "/grandir-dans-la-foi/": "grandir-dans-la-foi.md",
    "/solidarite/": "solidarite.md",
    "/demande-de-certificat/": "demande-de-certificat.md",
    "/horaires-des-messes/": "infos/horaires-messes.md",
    "/intentions-de-priere/": "infos/intentions-priere.md",
    "/offrir-une-messe/": "infos/offrir-messe.md",
    # Églises
    "/saint-etienne/": "eglises/saint-etienne.md",
    "/saint-jean-eudes/": "eglises/saint-jean-eudes.md",
    "/saint-julien/": "eglises/saint-julien.md",
    "/saint-nicolas/": "eglises/saint-nicolas.md",
    "/saint-paul/": "eglises/saint-paul.md",
    "/saint-pierre/": "eglises/saint-pierre.md",
    "/saint-sauveur/": "eglises/saint-sauveur.md",
    "/sainte-bernadette/": "eglises/sainte-bernadette.md",
    "/sainte-therese/": "eglises/sainte-therese.md",
    "/notre-dame-de-la-gloriette/": "eglises/notre-dame-de-la-gloriette.md",
    "/notre-dame-de-protection/": "eglises/notre-dame-de-protection.md",
    "/notre-dame-des-champs/": "eglises/notre-dame-des-champs.md",
    "/sacre-coeur/": "eglises/sacre-coeur.md",
    "/saint-joseph/": "eglises/saint-joseph.md",
    "/saint-michel/": "eglises/saint-michel.md",
    "/saint-ouen/": "eglises/saint-ouen.md",
    "/saint-remi/": "eglises/saint-remi.md",
    "/saint-vigor/": "eglises/saint-vigor.md",
    "/sainte-croix/": "eglises/sainte-croix.md",
    "/sainte-paix/": "eglises/sainte-paix.md",
    "/chapelle-misericorde/": "eglises/chapelle-misericorde.md",
    "/chapelle-saint-joseph/": "eglises/chapelle-saint-joseph.md",
    "/chapelle-sainte-ursule/": "eglises/chapelle-sainte-ursule.md",
}

def get_sitemap_urls():
    """Récupère toutes les URLs depuis le sitemap XML."""
    try:
        response = requests.get(SITEMAP_URL)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        urls = []
        
        # Namespace pour sitemap
        ns = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        for url_elem in root.findall('.//sitemap:url', ns):
            loc = url_elem.find('sitemap:loc', ns)
            lastmod = url_elem.find('sitemap:lastmod', ns)
            
            if loc is not None:
                url = loc.text
                last_modified = lastmod.text if lastmod is not None else None
                urls.append({
                    'url': url,
                    'lastmod': last_modified,
                    'path': urlparse(url).path
                })
        
        return urls
    except Exception as e:
        print(f"Erreur lors de la récupération du sitemap: {e}")
        return []

def get_page_title(url):
    """Récupère le titre d'une page."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        title_elem = soup.find('title')
        title = title_elem.get_text().strip() if title_elem else ""
        
        # Nettoyer le titre (enlever le nom du site)
        if " – " in title:
            title = title.split(" – ")[0].strip()
        
        return title
    except Exception as e:
        print(f"Erreur lors de la récupération du titre de {url}: {e}")
        return "Titre inconnu"

def suggest_file_path(path, title):
    """Suggère un chemin de fichier basé sur l'URL et le titre."""
    # Nettoyer le path
    clean_path = path.strip('/')
    
    # Catégoriser selon le contenu
    if any(saint in path.lower() for saint in ['saint-', 'sainte-', 'notre-dame', 'chapelle', 'sacre-']):
        return f"eglises/{clean_path}.md"
    elif any(keyword in path.lower() for keyword in ['horaire', 'messe', 'intention', 'priere']):
        return f"infos/{clean_path}.md"
    elif any(keyword in path.lower() for keyword in ['jeune', 'etudiant', 'catechese', 'confirmation']):
        return f"jeunesse/{clean_path}.md"
    else:
        return f"{clean_path}.md"

def analyze_new_pages():
    """Analyse les nouvelles pages et suggère des mappings."""
    print("🔍 Analyse des nouvelles pages WordPress...")
    
    # Récupérer les URLs du sitemap
    urls = get_sitemap_urls()
    print(f"📄 {len(urls)} URLs trouvées dans le sitemap")
    
    new_pages = []
    
    for url_info in urls:
        url = url_info['url']
        path = url_info['path']
        lastmod = url_info.get('lastmod', 'Unknown')
        
        # Ignorer les URLs de blog posts (contiennent des dates)
        if re.match(r'/\d{4}/\d{2}/\d{2}/', path):
            continue
            
        # Ignorer certaines pages système
        if path in ['/', '/about/', '/test/']:
            continue
            
        # Vérifier si on a déjà un mapping pour cette URL
        if path not in EXISTING_MAPPINGS:
            print(f"🆕 Nouvelle page trouvée: {path}")
            
            # Récupérer le titre
            title = get_page_title(url)
            
            # Suggérer un chemin de fichier
            suggested_path = suggest_file_path(path, title)
            
            new_pages.append({
                'path': path,
                'title': title,
                'suggested_file': suggested_path,
                'lastmod': lastmod,
                'url': url
            })
    
    # Afficher les résultats
    if new_pages:
        print(f"\n🆕 {len(new_pages)} nouvelles pages trouvées:")
        print("\n" + "="*80)
        
        for page in new_pages:
            print(f"URL: {page['path']}")
            print(f"Titre: {page['title']}")
            print(f"Fichier suggéré: {page['suggested_file']}")
            print(f"Dernière modification: {page['lastmod']}")
            print(f"URL complète: {page['url']}")
            print("-" * 40)
        
        # Générer le code de mapping à ajouter
        print("\n📝 Code de mapping à ajouter au script:")
        print("```python")
        for page in new_pages:
            print(f'    "{page["path"]}": "{page["suggested_file"]}",')
        print("```")
        
        # Créer un fichier de rapport
        with open('nouvelles_pages_rapport.md', 'w', encoding='utf-8') as f:
            f.write("# Rapport des nouvelles pages WordPress\n\n")
            f.write(f"Généré le: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**{len(new_pages)} nouvelles pages trouvées**\n\n")
            
            for page in new_pages:
                f.write(f"## {page['title']}\n\n")
                f.write(f"- **URL**: {page['path']}\n")
                f.write(f"- **Fichier suggéré**: `{page['suggested_file']}`\n")
                f.write(f"- **Dernière modification**: {page['lastmod']}\n")
                f.write(f"- **URL complète**: {page['url']}\n\n")
            
            f.write("\n## Code de mapping à ajouter\n\n")
            f.write("```python\n")
            for page in new_pages:
                f.write(f'    "{page["path"]}": "{page["suggested_file"]}",\n')
            f.write("```\n")
        
        print(f"\n📄 Rapport détaillé sauvegardé dans: nouvelles_pages_rapport.md")
    else:
        print("\n✅ Aucune nouvelle page trouvée. Toutes les pages sont déjà mappées.")

if __name__ == "__main__":
    analyze_new_pages()
