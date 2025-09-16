#!/usr/bin/env python3
"""
Script pour ajouter le front matter YAML complet à toutes les pages Markdown.
Inclut le layout ROQ et standardise les métadonnées.
"""

import os
import re
import yaml
from pathlib import Path
from datetime import datetime

def extract_title_from_content(content):
    """Extrait le titre depuis le contenu Markdown."""
    lines = content.split('\n')
    
    # Chercher le premier titre H1
    for line in lines:
        line = line.strip()
        if line.startswith('# '):
            return line[2:].strip()
    
    # Si pas de H1, chercher dans le front matter existant
    if content.startswith('---'):
        try:
            # Extraire le front matter existant
            end_marker = content.find('---', 3)
            if end_marker != -1:
                frontmatter_text = content[3:end_marker]
                frontmatter = yaml.safe_load(frontmatter_text)
                if frontmatter and 'title' in frontmatter:
                    return frontmatter['title']
        except:
            pass
    
    return None

def generate_description(content, title):
    """Génère une description basée sur le contenu."""
    # Supprimer le front matter
    content_clean = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)

    # Supprimer les titres H1, H2, H3
    content_clean = re.sub(r'^#{1,3} .+\n', '', content_clean, flags=re.MULTILINE)

    # Supprimer les images et liens complexes
    content_clean = re.sub(r'!\[.*?\]\(.*?\)', '', content_clean)
    content_clean = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content_clean)

    # Supprimer les balises HTML
    content_clean = re.sub(r'<[^>]+>', '', content_clean)

    # Supprimer les caractères de formatage Markdown
    content_clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', content_clean)  # Gras
    content_clean = re.sub(r'\*([^*]+)\*', r'\1', content_clean)      # Italique
    content_clean = re.sub(r'`([^`]+)`', r'\1', content_clean)        # Code

    # Supprimer les listes et puces
    content_clean = re.sub(r'^\s*[-*+]\s+', '', content_clean, flags=re.MULTILINE)
    content_clean = re.sub(r'^\s*\d+\.\s+', '', content_clean, flags=re.MULTILINE)

    # Nettoyer les espaces multiples et retours à la ligne
    content_clean = re.sub(r'\s+', ' ', content_clean).strip()

    if content_clean:
        # Prendre les premiers mots significatifs
        words = [word for word in content_clean.split() if len(word) > 2]
        if len(words) > 15:
            description = ' '.join(words[:15]) + '...'
        else:
            description = ' '.join(words)

        # Nettoyer la description finale
        description = description.replace('\n', ' ').strip()

        # Vérifier que la description est valide
        if len(description) > 10 and not description.startswith('http'):
            return description

    # Description par défaut basée sur le titre et le type de page
    if title:
        title_lower = title.lower()
        if 'église' in title_lower or 'chapelle' in title_lower:
            return f"Découvrez l'église {title} de la paroisse Bon Pasteur de Caen."
        elif 'jeune' in title_lower or 'confirmation' in title_lower:
            return f"Informations sur {title_lower} dans notre paroisse Bon Pasteur de Caen."
        else:
            return f"Découvrez {title_lower} dans notre paroisse Bon Pasteur de Caen."

    return "Page de la paroisse Bon Pasteur de Caen."

def determine_layout(file_path):
    """Détermine le layout approprié selon le fichier."""
    path_str = str(file_path)
    
    if 'index.md' in path_str and 'posts' not in path_str:
        return 'paroisse/index'
    elif '/eglises/' in path_str:
        return 'paroisse/eglise'
    elif '/jeunesse/' in path_str:
        return 'paroisse/jeunesse'
    elif '/infos/' in path_str:
        return 'paroisse/info'
    else:
        return 'paroisse/page'

def create_slug_from_path(file_path):
    """Crée un slug basé sur le chemin du fichier."""
    # Enlever l'extension et le répertoire content
    relative_path = file_path.relative_to(Path('content'))
    slug = str(relative_path.with_suffix(''))
    
    # Remplacer les séparateurs par des tirets
    slug = slug.replace('/', '-')
    slug = slug.replace('\\', '-')
    
    # Si c'est index, utiliser le nom du répertoire parent
    if slug.endswith('-index'):
        slug = slug[:-6]
    elif slug == 'index':
        slug = ''
    
    return slug

def process_file(file_path):
    """Traite un fichier Markdown pour ajouter/mettre à jour le front matter."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier si le fichier a déjà un front matter
        has_frontmatter = content.startswith('---')
        existing_frontmatter = {}
        content_without_frontmatter = content
        
        if has_frontmatter:
            # Extraire le front matter existant
            end_marker = content.find('---', 3)
            if end_marker != -1:
                frontmatter_text = content[3:end_marker]
                try:
                    existing_frontmatter = yaml.safe_load(frontmatter_text) or {}
                except:
                    existing_frontmatter = {}
                content_without_frontmatter = content[end_marker + 3:].lstrip()
        
        # Extraire ou générer le titre
        title = existing_frontmatter.get('title')
        if not title:
            title = extract_title_from_content(content)
        
        if not title:
            # Générer un titre basé sur le nom du fichier
            filename = file_path.stem
            title = filename.replace('-', ' ').replace('_', ' ').title()
            
            # Corrections spécifiques
            title = title.replace('Eglises', 'Églises')
            title = title.replace('Catechese', 'Catéchèse')
            title = title.replace('Obseques', 'Obsèques')
        
        # Créer le nouveau front matter
        new_frontmatter = {
            'title': title,
            'description': existing_frontmatter.get('description') or generate_description(content_without_frontmatter, title),
            'layout': existing_frontmatter.get('layout') or determine_layout(file_path),
            'updated': existing_frontmatter.get('updated') or datetime.now().strftime('%Y-%m-%d')
        }
        
        # Ajouter l'URL si elle existe
        if 'url' in existing_frontmatter:
            new_frontmatter['url'] = existing_frontmatter['url']
        
        # Ajouter d'autres champs existants spécifiques
        for key in ['name', 'simple-name', 'tags', 'author', 'image']:
            if key in existing_frontmatter:
                new_frontmatter[key] = existing_frontmatter[key]
        
        # Construire le nouveau contenu
        frontmatter_yaml = yaml.dump(new_frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
        new_content = f"---\n{frontmatter_yaml}---\n\n{content_without_frontmatter}"
        
        # Écrire le fichier mis à jour
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return {
            'file': file_path,
            'status': 'updated' if has_frontmatter else 'added',
            'title': title,
            'layout': new_frontmatter['layout']
        }
        
    except Exception as e:
        return {
            'file': file_path,
            'status': 'error',
            'error': str(e)
        }

def main():
    """Fonction principale."""
    print("🔧 Ajout du front matter YAML à toutes les pages...")
    
    content_dir = Path('content')
    markdown_files = list(content_dir.rglob('*.md'))
    
    # Exclure certains fichiers
    excluded_patterns = [
        r'posts/.*',  # Articles de blog (ont déjà leur format)
        r'404\.md',   # Page d'erreur
        r'test\.md',  # Pages de test
    ]
    
    filtered_files = []
    for file_path in markdown_files:
        relative_path = str(file_path.relative_to(content_dir))
        if not any(re.match(pattern, relative_path) for pattern in excluded_patterns):
            filtered_files.append(file_path)
    
    print(f"📄 {len(filtered_files)} fichiers Markdown trouvés")
    
    results = []
    for file_path in filtered_files:
        result = process_file(file_path)
        results.append(result)
        
        status_icon = {
            'added': '✅',
            'updated': '🔄',
            'error': '❌'
        }.get(result['status'], '❓')
        
        print(f"{status_icon} {result['file']}")
        if result['status'] == 'error':
            print(f"    Erreur: {result['error']}")
        else:
            print(f"    Titre: {result['title']}")
            print(f"    Layout: {result['layout']}")
    
    # Statistiques finales
    added_count = len([r for r in results if r['status'] == 'added'])
    updated_count = len([r for r in results if r['status'] == 'updated'])
    error_count = len([r for r in results if r['status'] == 'error'])
    
    print(f"\n📊 Résultats:")
    print(f"✅ {added_count} fichiers avec front matter ajouté")
    print(f"🔄 {updated_count} fichiers avec front matter mis à jour")
    print(f"❌ {error_count} erreurs")
    
    # Afficher les layouts utilisés
    layouts = {}
    for result in results:
        if result['status'] != 'error':
            layout = result['layout']
            layouts[layout] = layouts.get(layout, 0) + 1
    
    print(f"\n🎨 Layouts utilisés:")
    for layout, count in sorted(layouts.items()):
        print(f"  {layout}: {count} fichiers")

if __name__ == "__main__":
    main()
