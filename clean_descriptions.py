#!/usr/bin/env python3
"""
Script pour nettoyer les descriptions dans le front matter.
Supprime le HTML/Markdown des descriptions existantes.
"""

import os
import re
import yaml
from pathlib import Path

def clean_description(description):
    """Nettoie une description en supprimant HTML/Markdown."""
    if not description:
        return description

    # Supprimer les URLs complètes (http/https)
    description = re.sub(r'https?://[^\s\)]+', '', description)

    # Supprimer les images et liens complexes
    description = re.sub(r'!\[.*?\]\([^\)]*\)', '', description)
    description = re.sub(r'\[([^\]]*)\]\([^\)]*\)', r'\1', description)

    # Supprimer les liens vides restants
    description = re.sub(r'\[\]\([^\)]*\)', '', description)

    # Supprimer les balises HTML
    description = re.sub(r'<[^>]+>', '', description)

    # Supprimer les caractères de formatage Markdown
    description = re.sub(r'\*\*([^*]+)\*\*', r'\1', description)  # Gras
    description = re.sub(r'\*([^*]+)\*', r'\1', description)      # Italique
    description = re.sub(r'`([^`]+)`', r'\1', description)        # Code

    # Supprimer les titres Markdown
    description = re.sub(r'^#{1,6}\s+', '', description, flags=re.MULTILINE)

    # Supprimer les emojis et caractères spéciaux
    description = re.sub(r'[💒🎉✨🙏⛪]', '', description)

    # Nettoyer les espaces multiples et caractères de contrôle
    description = re.sub(r'\s+', ' ', description).strip()

    # Supprimer les débuts de description vides ou avec seulement des caractères spéciaux
    if re.match(r'^[\s\[\]\(\)\.]+', description):
        description = re.sub(r'^[\s\[\]\(\)\.]+', '', description)

    # Si la description est maintenant vide ou trop courte, la régénérer
    if len(description.strip()) < 10:
        return None

    # Limiter la longueur
    words = [word for word in description.split() if word.strip()]
    if len(words) > 20:
        description = ' '.join(words[:20]) + '...'
    else:
        description = ' '.join(words)

    return description.strip()

def process_file(file_path):
    """Traite un fichier pour nettoyer sa description."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return {'file': file_path, 'status': 'no_frontmatter'}
        
        # Extraire le front matter
        end_marker = content.find('---', 3)
        if end_marker == -1:
            return {'file': file_path, 'status': 'invalid_frontmatter'}
        
        frontmatter_text = content[3:end_marker]
        content_body = content[end_marker + 3:]
        
        try:
            frontmatter = yaml.safe_load(frontmatter_text)
        except:
            return {'file': file_path, 'status': 'yaml_error'}
        
        if not frontmatter or 'description' not in frontmatter:
            return {'file': file_path, 'status': 'no_description'}
        
        old_description = frontmatter['description']
        new_description = clean_description(old_description)

        # Si la description nettoyée est vide, générer une nouvelle
        if not new_description:
            title = frontmatter.get('title', '')
            if 'église' in title.lower() or 'chapelle' in title.lower():
                new_description = f"Découvrez l'église {title} de la paroisse Bon Pasteur de Caen."
            elif 'jeune' in title.lower() or 'confirmation' in title.lower():
                new_description = f"Informations sur {title.lower()} dans notre paroisse Bon Pasteur de Caen."
            else:
                new_description = f"Découvrez {title.lower()} dans notre paroisse Bon Pasteur de Caen."

        # Vérifier si la description a changé
        if old_description == new_description:
            return {'file': file_path, 'status': 'no_change'}

        # Mettre à jour la description
        frontmatter['description'] = new_description
        
        # Reconstruire le fichier
        new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
        new_content = f"---\n{new_frontmatter}---{content_body}"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return {
            'file': file_path,
            'status': 'updated',
            'old_description': old_description[:100] + '...' if len(old_description) > 100 else old_description,
            'new_description': new_description
        }
        
    except Exception as e:
        return {'file': file_path, 'status': 'error', 'error': str(e)}

def main():
    """Fonction principale."""
    print("🧹 Nettoyage des descriptions dans le front matter...")
    
    content_dir = Path('content')
    markdown_files = list(content_dir.rglob('*.md'))
    
    results = []
    for file_path in markdown_files:
        result = process_file(file_path)
        results.append(result)
        
        status_icons = {
            'updated': '✅',
            'no_change': '⚪',
            'no_frontmatter': '⚠️',
            'no_description': '⚠️',
            'error': '❌'
        }
        
        icon = status_icons.get(result['status'], '❓')
        print(f"{icon} {result['file']}")
        
        if result['status'] == 'updated':
            print(f"    Avant: {result['old_description']}")
            print(f"    Après: {result['new_description']}")
        elif result['status'] == 'error':
            print(f"    Erreur: {result['error']}")
    
    # Statistiques
    updated_count = len([r for r in results if r['status'] == 'updated'])
    no_change_count = len([r for r in results if r['status'] == 'no_change'])
    error_count = len([r for r in results if r['status'] == 'error'])
    
    print(f"\n📊 Résultats:")
    print(f"✅ {updated_count} descriptions nettoyées")
    print(f"⚪ {no_change_count} descriptions déjà propres")
    print(f"❌ {error_count} erreurs")

if __name__ == "__main__":
    main()
