#!/usr/bin/env python3
"""
Script pour synchroniser le contenu du site WordPress vers le repository GitHub.
Ce script récupère les pages du site WordPress et met à jour les fichiers Markdown correspondants.
"""

import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET
from datetime import datetime
import html2text
import yaml

# Configuration
WORDPRESS_URL = "https://bonpasteurcaen.wordpress.com"
SITEMAP_URL = f"{WORDPRESS_URL}/sitemap.xml"
CONTENT_DIR = "content"

# Mapping des URLs WordPress vers les fichiers Markdown
URL_TO_FILE_MAPPING = {
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
    # Nouvelles pages ajoutées
    "/rejoindre-un-groupe/": "rejoindre-un-groupe.md",
    "/jeunes-12-17-ans/": "jeunesse/jeunes-12-17-ans.md",
    "/confirmation/": "jeunesse/confirmation.md",
    "/messes-horaires/": "infos/messes-horaires.md",
    "/confirmation-2/": "jeunesse/confirmation-2.md",
    "/demander-la-confirmation/": "jeunesse/demander-la-confirmation.md",
    "/malades-et-aines/": "malades-et-aines.md",
    "/se-confesser/": "se-confesser.md",
    "/rencontrer-un-pretre/": "rencontrer-un-pretre.md",
    "/pole-jeunes-12-17-ans/": "jeunesse/pole-jeunes-12-17-ans.md",
    "/qui-sommes-nous/": "qui-sommes-nous.md",
    "/monastere-visitation/": "monastere-visitation.md",
    "/intentions-priere/": "infos/intentions-priere.md",
    "/carmel-de-caen/": "carmel-de-caen.md",
}

# Mapping des églises
EGLISES_MAPPING = {
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
    # Nouvelles églises et chapelles
    "/sainte-claire-folie-couvrechef/": "eglises/sainte-claire-folie-couvrechef.md",
    "/sainte-trinite-saint-gilles/": "eglises/sainte-trinite-saint-gilles.md",
    "/saint-joseph-chemin-vert/": "eglises/saint-joseph-chemin-vert.md",
    "/saint-jean-baptiste/": "eglises/saint-jean-baptiste.md",
    "/saint-germain-blanche-herbe/": "eglises/saint-germain-blanche-herbe.md",
    "/saint-gerbold-blainville/": "eglises/saint-gerbold-blainville.md",
    "/saint-francois-herouville/": "eglises/saint-francois-herouville.md",
    "/saint-clair-herouville/": "eglises/saint-clair-herouville.md",
    "/saint-bernard-pierre-heuze/": "eglises/saint-bernard-pierre-heuze.md",
    "/saint-andre-calvaire-saint-pierre/": "eglises/saint-andre-calvaire-saint-pierre.md",
    "/notre-dame-assomption-gloriette/": "eglises/notre-dame-assomption-gloriette.md",
    "/chapelle-chr/": "eglises/chapelle-chr.md",
    "/chapelle-benedictines/": "eglises/chapelle-benedictines.md",
    "/chapelle-oasis/": "eglises/chapelle-oasis.md",
}

# Fusionner les mappings
URL_TO_FILE_MAPPING.update(EGLISES_MAPPING)

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

def extract_content_from_html(html_content):
    """Extrait le contenu principal d'une page HTML."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Récupérer le titre
    title_elem = soup.find('title')
    title = title_elem.get_text().strip() if title_elem else ""
    
    # Nettoyer le titre (enlever le nom du site)
    if " – " in title:
        title = title.split(" – ")[0].strip()
    
    # Chercher le contenu principal
    content_selectors = [
        '.wp-block-post-content',
        'main .entry-content',
        'article .content',
        '.post-content',
        'main'
    ]
    
    content_elem = None
    for selector in content_selectors:
        content_elem = soup.select_one(selector)
        if content_elem:
            break
    
    if not content_elem:
        print("Impossible de trouver le contenu principal")
        return title, ""
    
    # Convertir HTML en Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # Pas de limite de largeur
    
    # Nettoyer le HTML avant conversion
    # Supprimer les scripts, styles, etc.
    for script in content_elem(["script", "style", "nav", "footer", "header"]):
        script.decompose()
    
    content_html = str(content_elem)
    content_markdown = h.handle(content_html)
    
    # Nettoyer le markdown
    content_markdown = re.sub(r'\n\s*\n\s*\n', '\n\n', content_markdown)  # Réduire les lignes vides multiples
    content_markdown = content_markdown.strip()
    
    return title, content_markdown

def get_page_content(url):
    """Récupère le contenu d'une page WordPress."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        title, content = extract_content_from_html(response.text)
        return title, content
    except Exception as e:
        print(f"Erreur lors de la récupération de {url}: {e}")
        return None, None

def create_markdown_file(file_path, title, content, url_path):
    """Crée un fichier Markdown avec front matter."""
    
    # Créer le front matter
    front_matter = {
        'title': title,
        'url': url_path,
        'updated': datetime.now().strftime('%Y-%m-%d')
    }
    
    # Créer le contenu complet
    markdown_content = "---\n"
    markdown_content += yaml.dump(front_matter, default_flow_style=False, allow_unicode=True)
    markdown_content += "---\n\n"
    markdown_content += content
    
    # Créer le répertoire si nécessaire
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Écrire le fichier
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"✅ Créé/mis à jour: {file_path}")

def sync_wordpress_content():
    """Synchronise le contenu WordPress vers les fichiers Markdown."""
    print("🔄 Début de la synchronisation du contenu WordPress...")

    # Récupérer les URLs du sitemap
    urls = get_sitemap_urls()
    print(f"📄 {len(urls)} URLs trouvées dans le sitemap")

    updated_files = []
    new_files = []
    unmapped_urls = []

    for url_info in urls:
        url = url_info['url']
        path = url_info['path']

        # Ignorer les URLs de blog posts (contiennent des dates)
        if re.match(r'/\d{4}/\d{2}/\d{2}/', path):
            continue

        # Vérifier si on a un mapping pour cette URL
        if path in URL_TO_FILE_MAPPING:
            file_path = os.path.join(CONTENT_DIR, URL_TO_FILE_MAPPING[path])

            print(f"🔍 Traitement de {path} -> {file_path}")

            # Récupérer le contenu
            title, content = get_page_content(url)

            if title and content:
                # Vérifier si le fichier existe déjà
                file_exists = os.path.exists(file_path)

                # Créer/mettre à jour le fichier
                create_markdown_file(file_path, title, content, path)

                if file_exists:
                    updated_files.append(file_path)
                else:
                    new_files.append(file_path)
        else:
            # Ignorer certaines pages système
            if path not in ['/', '/about/', '/test/']:
                unmapped_urls.append((path, url_info.get('lastmod', 'Unknown')))
            print(f"⚠️  Pas de mapping pour {path}")

    print(f"\n✅ Synchronisation terminée!")
    print(f"📝 {len(new_files)} nouveaux fichiers créés")
    print(f"🔄 {len(updated_files)} fichiers mis à jour")
    print(f"⚠️  {len(unmapped_urls)} URLs sans mapping")

    if new_files:
        print("\n📝 Nouveaux fichiers:")
        for f in new_files:
            print(f"  - {f}")

    if updated_files:
        print("\n🔄 Fichiers mis à jour:")
        for f in updated_files:
            print(f"  - {f}")

    if unmapped_urls:
        print("\n⚠️  URLs sans mapping (à traiter manuellement):")
        for path, lastmod in unmapped_urls:
            print(f"  - {path} (modifié: {lastmod})")

if __name__ == "__main__":
    sync_wordpress_content()
