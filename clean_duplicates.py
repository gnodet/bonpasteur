#!/usr/bin/env python3
"""
Script pour nettoyer les doublons de fichiers Markdown.
Identifie les fichiers avec des noms similaires et propose de supprimer les anciens.
"""

import os
import re
import unicodedata
from pathlib import Path

def slugify(text):
    """Convertit un texte en slug (comme WordPress)."""
    # Normaliser les caractères Unicode
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    
    # Convertir en minuscules et remplacer les espaces/caractères spéciaux
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[-\s]+', '-', text)
    
    return text.strip('-')

def find_duplicates():
    """Trouve les fichiers en doublon."""
    content_dir = Path('content')
    all_files = list(content_dir.rglob('*.md'))
    
    # Grouper les fichiers par slug
    slug_groups = {}
    
    for file_path in all_files:
        # Calculer le slug du nom de fichier (sans extension)
        filename = file_path.stem
        slug = slugify(filename)
        
        if slug not in slug_groups:
            slug_groups[slug] = []
        
        slug_groups[slug].append(file_path)
    
    # Identifier les doublons
    duplicates = {}
    for slug, files in slug_groups.items():
        if len(files) > 1:
            duplicates[slug] = files
    
    return duplicates

def analyze_file_content(file_path):
    """Analyse le contenu d'un fichier pour déterminer sa qualité."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier la présence de front matter YAML
        has_frontmatter = content.startswith('---')
        
        # Compter les lignes de contenu
        lines = content.split('\n')
        content_lines = len([line for line in lines if line.strip()])
        
        # Vérifier la date de mise à jour dans le front matter
        updated_date = None
        if has_frontmatter:
            frontmatter_match = re.search(r'updated:\s*[\'"]?([^\'"]+)[\'"]?', content)
            if frontmatter_match:
                updated_date = frontmatter_match.group(1)
        
        return {
            'has_frontmatter': has_frontmatter,
            'content_lines': content_lines,
            'updated_date': updated_date,
            'size': len(content)
        }
    except Exception as e:
        return {
            'has_frontmatter': False,
            'content_lines': 0,
            'updated_date': None,
            'size': 0,
            'error': str(e)
        }

def recommend_file_to_keep(files):
    """Recommande quel fichier garder parmi les doublons."""
    file_scores = []
    
    for file_path in files:
        analysis = analyze_file_content(file_path)
        
        score = 0
        reasons = []
        
        # Préférer les fichiers avec front matter YAML
        if analysis['has_frontmatter']:
            score += 10
            reasons.append("Front matter YAML")
        
        # Préférer les fichiers plus récents
        if analysis['updated_date'] == '2025-09-16':
            score += 8
            reasons.append("Récemment synchronisé")
        
        # Préférer les fichiers avec plus de contenu
        score += min(analysis['content_lines'] / 10, 5)
        if analysis['content_lines'] > 20:
            reasons.append("Contenu substantiel")
        
        # Préférer les noms de fichiers slugifiés (sans espaces, accents)
        filename = file_path.name
        if not re.search(r'[À-ÿ\s\(\)]', filename):
            score += 3
            reasons.append("Nom de fichier standardisé")
        
        # Préférer les fichiers dans des sous-répertoires organisés
        if len(file_path.parts) > 2:  # content/subdir/file.md
            score += 2
            reasons.append("Organisation en sous-répertoire")
        
        file_scores.append({
            'file': file_path,
            'score': score,
            'reasons': reasons,
            'analysis': analysis
        })
    
    # Trier par score décroissant
    file_scores.sort(key=lambda x: x['score'], reverse=True)
    
    return file_scores

def main():
    """Fonction principale."""
    print("🔍 Recherche des fichiers en doublon...")
    
    duplicates = find_duplicates()
    
    if not duplicates:
        print("✅ Aucun doublon trouvé !")
        return
    
    print(f"⚠️  {len(duplicates)} groupes de doublons trouvés :\n")
    
    files_to_remove = []
    
    for slug, files in duplicates.items():
        print(f"📁 Groupe '{slug}' ({len(files)} fichiers):")
        
        recommendations = recommend_file_to_keep(files)
        
        for i, rec in enumerate(recommendations):
            file_path = rec['file']
            score = rec['score']
            reasons = rec['reasons']
            analysis = rec['analysis']
            
            status = "🟢 GARDER" if i == 0 else "🔴 SUPPRIMER"
            
            print(f"  {status} {file_path}")
            print(f"    Score: {score:.1f}")
            print(f"    Raisons: {', '.join(reasons) if reasons else 'Aucune'}")
            print(f"    Contenu: {analysis['content_lines']} lignes, {analysis['size']} caractères")
            if analysis['updated_date']:
                print(f"    Mis à jour: {analysis['updated_date']}")
            print()
            
            # Ajouter à la liste de suppression (sauf le premier = celui à garder)
            if i > 0:
                files_to_remove.append(file_path)
        
        print("-" * 60)
    
    # Proposer la suppression
    if files_to_remove:
        print(f"\n📋 Résumé: {len(files_to_remove)} fichiers à supprimer")
        
        for file_path in files_to_remove:
            print(f"  🗑️  {file_path}")
        
        print(f"\n⚠️  Cette action supprimera définitivement {len(files_to_remove)} fichiers.")
        response = input("Voulez-vous procéder à la suppression ? (y/N): ")
        
        if response.lower() == 'y':
            removed_count = 0
            for file_path in files_to_remove:
                try:
                    os.remove(file_path)
                    print(f"✅ Supprimé: {file_path}")
                    removed_count += 1
                except Exception as e:
                    print(f"❌ Erreur lors de la suppression de {file_path}: {e}")
            
            print(f"\n🎉 {removed_count} fichiers supprimés avec succès !")
            print("💡 N'oubliez pas de commiter ces changements avec Git.")
        else:
            print("❌ Suppression annulée.")
    else:
        print("✅ Aucun fichier à supprimer.")

if __name__ == "__main__":
    main()
