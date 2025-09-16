#!/usr/bin/env python3
"""
Script pour générer un fichier XML d'import WordPress à partir des fichiers markdown
"""

import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
import yaml
from datetime import datetime
from typing import Dict, Any
from wordpress_config import EXCLUDED_FILES, CUSTOM_SLUGS

def parse_markdown_file(file_path: Path) -> Dict[str, Any]:
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
    html_content = markdown_to_html(markdown_content)
    
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
        'slug': generate_slug(file_path.name),
        'front_matter': front_matter,
        'file_path': str(file_path)
    }

def markdown_to_html(markdown_content: str) -> str:
    """Conversion basique du markdown en HTML"""
    html = markdown_content

    # Supprimer les titres H1 qui font doublon avec le titre de la page
    html = re.sub(r'^# .+$', '', html, flags=re.MULTILINE)

    # Titres (en commençant par H2 puisque H1 est le titre de la page)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    
    # Gras et italique
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # Liens (avec gestion des classes CSS)
    html = re.sub(r'\[(.+?)\]\((.+?)\)\{\.btn \.btn-primary\}', r'<a href="\2" class="btn btn-primary">\1</a>', html)
    html = re.sub(r'\[(.+?)\]\((.+?)\)\{\.btn \.btn-outline-primary\}', r'<a href="\2" class="btn btn-outline-primary">\1</a>', html)
    html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html)
    
    # Listes à puces (amélioration pour gérer - et *)
    lines = html.split('\n')
    in_list = False
    result_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('- ') or stripped.startswith('* '):
            if not in_list:
                result_lines.append('<ul>')
                in_list = True
            # Enlever le marqueur de liste et traiter le contenu
            content = stripped[2:].strip()
            # Traiter le gras/italique dans les éléments de liste
            content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
            content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', content)
            result_lines.append(f'<li>{content}</li>')
        else:
            if in_list:
                result_lines.append('</ul>')
                in_list = False
            if stripped:  # Ne pas ajouter les lignes vides
                result_lines.append(line)

    if in_list:
        result_lines.append('</ul>')

    html = '\n'.join(result_lines)
    
    # Citations
    html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)
    
    # Paragraphes
    paragraphs = html.split('\n\n')
    html_paragraphs = []
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<'):
            p = f'<p>{p}</p>'
        if p:
            html_paragraphs.append(p)
    
    return '\n'.join(html_paragraphs)

def generate_slug(filename: str) -> str:
    """Génère un slug à partir du nom de fichier"""
    # Vérifier s'il y a un slug personnalisé
    if filename in CUSTOM_SLUGS:
        return CUSTOM_SLUGS[filename]
    
    slug = filename.lower()
    if slug.endswith('.md'):
        slug = slug[:-3]
    
    slug = re.sub(r'[àáâãäå]', 'a', slug)
    slug = re.sub(r'[èéêë]', 'e', slug)
    slug = re.sub(r'[ìíîï]', 'i', slug)
    slug = re.sub(r'[òóôõö]', 'o', slug)
    slug = re.sub(r'[ùúûü]', 'u', slug)
    slug = re.sub(r'[ç]', 'c', slug)
    slug = re.sub(r'[^a-z0-9\-]', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')

def create_wordpress_xml(pages_data: list) -> str:
    """Crée un fichier XML d'import WordPress"""
    
    # Créer l'élément racine
    rss = ET.Element('rss', version='2.0')
    rss.set('xmlns:excerpt', 'http://wordpress.org/export/1.2/excerpt/')
    rss.set('xmlns:content', 'http://purl.org/rss/1.0/modules/content/')
    rss.set('xmlns:wfw', 'http://wellformedweb.org/CommentAPI/')
    rss.set('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
    rss.set('xmlns:wp', 'http://wordpress.org/export/1.2/')
    
    channel = ET.SubElement(rss, 'channel')
    
    # Métadonnées du site
    ET.SubElement(channel, 'title').text = 'Paroisse du Bon Pasteur - Import'
    ET.SubElement(channel, 'link').text = 'http://localhost:8080'
    ET.SubElement(channel, 'description').text = 'Import des pages depuis les fichiers markdown'
    ET.SubElement(channel, 'pubDate').text = datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0000')
    ET.SubElement(channel, 'language').text = 'fr-FR'
    ET.SubElement(channel, 'wp:wxr_version').text = '1.2'
    ET.SubElement(channel, 'wp:base_site_url').text = 'http://localhost:8080'
    ET.SubElement(channel, 'wp:base_blog_url').text = 'http://localhost:8080'

    # Ajouter les informations d'auteur
    author = ET.SubElement(channel, 'wp:author')
    ET.SubElement(author, 'wp:author_id').text = '1'
    ET.SubElement(author, 'wp:author_login').text = 'gnodet'
    ET.SubElement(author, 'wp:author_email').text = 'gnodet@gmail.com'
    ET.SubElement(author, 'wp:author_display_name').text = 'Guillaume Nodet'
    ET.SubElement(author, 'wp:author_first_name').text = 'Guillaume'
    ET.SubElement(author, 'wp:author_last_name').text = 'Nodet'

    # Ajouter les pages
    for i, page_data in enumerate(pages_data, 1):
        item = ET.SubElement(channel, 'item')
        
        ET.SubElement(item, 'title').text = page_data['title']
        ET.SubElement(item, 'link').text = f"http://localhost:8080/{page_data['slug']}/"
        ET.SubElement(item, 'pubDate').text = datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0000')
        ET.SubElement(item, 'dc:creator').text = 'gnodet'
        ET.SubElement(item, 'guid', isPermaLink='false').text = f"http://localhost:8080/?page_id={i}"
        ET.SubElement(item, 'description').text = ''
        ET.SubElement(item, 'content:encoded').text = page_data["content"]
        ET.SubElement(item, 'excerpt:encoded').text = page_data["description"]
        ET.SubElement(item, 'wp:post_id').text = str(i)
        ET.SubElement(item, 'wp:post_date').text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ET.SubElement(item, 'wp:post_date_gmt').text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ET.SubElement(item, 'wp:comment_status').text = 'closed'
        ET.SubElement(item, 'wp:ping_status').text = 'closed'
        ET.SubElement(item, 'wp:post_name').text = page_data['slug']
        ET.SubElement(item, 'wp:status').text = 'publish'
        ET.SubElement(item, 'wp:post_parent').text = '0'
        ET.SubElement(item, 'wp:menu_order').text = '0'
        ET.SubElement(item, 'wp:post_type').text = 'page'
        ET.SubElement(item, 'wp:post_password').text = ''
        ET.SubElement(item, 'wp:is_sticky').text = '0'
        
        # Ajouter un commentaire avec le fichier source
        comment = ET.Comment(f' Source: {page_data["file_path"]} ')
        item.insert(0, comment)
    
    return ET.tostring(rss, encoding='unicode', method='xml')

def main():
    """Fonction principale"""
    print("📝 Génération du fichier XML d'import WordPress...")
    
    # Recherche des fichiers markdown
    content_dir = Path("content")
    if not content_dir.exists():
        print("❌ Le dossier 'content' n'existe pas")
        return
    
    markdown_files = [f for f in content_dir.glob("**/*.md") if f.name not in EXCLUDED_FILES]
    print(f"📁 {len(markdown_files)} fichiers markdown trouvés (après exclusions)")
    
    # Traitement des fichiers
    pages_data = []
    for md_file in markdown_files:
        print(f"📄 Traitement de: {md_file}")
        try:
            page_data = parse_markdown_file(md_file)
            pages_data.append(page_data)
        except Exception as e:
            print(f"❌ Erreur lors du traitement de {md_file}: {e}")
    
    if not pages_data:
        print("❌ Aucune page à exporter")
        return
    
    # Génération du XML
    print(f"🔧 Génération du XML pour {len(pages_data)} pages...")
    xml_content = create_wordpress_xml(pages_data)
    
    # Sauvegarde du fichier
    output_file = "wordpress_import.xml"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
        f.write(xml_content)
    
    print(f"✅ Fichier XML généré: {output_file}")
    print(f"📊 {len(pages_data)} pages prêtes à être importées")
    
    print("\n📋 Instructions d'import:")
    print("1. Connectez-vous à l'admin WordPress (http://localhost:8080/wp-admin)")
    print("2. Allez dans Outils > Importer")
    print("3. Choisissez 'WordPress' et installez l'importeur si nécessaire")
    print("4. Sélectionnez le fichier 'wordpress_import.xml'")
    print("5. Suivez les instructions d'import")
    
    print(f"\n📄 Pages qui seront créées:")
    for page_data in pages_data:
        print(f"   - {page_data['title']} (slug: {page_data['slug']})")

if __name__ == "__main__":
    main()
