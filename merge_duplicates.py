#!/usr/bin/env python3
"""
Script pour fusionner intelligemment les derniers doublons.
Combine le meilleur contenu et les meilleures métadonnées.
"""

import os
import re
import yaml
from pathlib import Path

def extract_frontmatter_and_content(file_path):
    """Extrait le front matter et le contenu d'un fichier."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if content.startswith('---'):
            end_marker = content.find('---', 3)
            if end_marker != -1:
                frontmatter_text = content[3:end_marker]
                body = content[end_marker + 3:].strip()
                try:
                    frontmatter = yaml.safe_load(frontmatter_text)
                    return frontmatter or {}, body
                except:
                    pass
        
        return {}, content.strip()
    except Exception as e:
        print(f"Erreur lecture {file_path}: {e}")
        return {}, ""

def merge_etudiants():
    """Fusionne les fichiers étudiants."""
    file1 = Path('content/Étudiants.md')
    file2 = Path('content/etudiants.md')
    
    fm1, content1 = extract_frontmatter_and_content(file1)
    fm2, content2 = extract_frontmatter_and_content(file2)
    
    print("📚 Fusion des fichiers étudiants...")
    print(f"  {file1}: {len(content1)} caractères")
    print(f"  {file2}: {len(content2)} caractères")
    
    # Prendre les meilleures métadonnées (file2 a l'URL)
    merged_fm = {
        'title': fm2.get('title', fm1.get('title', 'Étudiants')),
        'description': fm2.get('description', fm1.get('description')),
        'layout': 'paroisse/page',
        'updated': '2025-09-16',
        'url': '/etudiants/'
    }
    
    # Fusionner le contenu (prendre le plus long mais nettoyer)
    if len(content2) > len(content1):
        merged_content = content2
        print("  → Contenu de etudiants.md conservé (plus long)")
    else:
        merged_content = content1
        print("  → Contenu de Étudiants.md conservé (plus long)")
    
    # Nettoyer le contenu
    merged_content = re.sub(r'# Étudiants\n', '', merged_content)  # Supprimer H1 dupliqué
    merged_content = re.sub(r'\[]\([^)]+\)', '', merged_content)   # Supprimer liens vides
    
    return merged_fm, merged_content

def merge_pole_jeunes():
    """Fusionne les fichiers pôle jeunes."""
    file1 = Path('content/Pôle Jeunes (12-17 ans).md')
    file2 = Path('content/jeunesse/pole-jeunes-12-17-ans.md')
    
    fm1, content1 = extract_frontmatter_and_content(file1)
    fm2, content2 = extract_frontmatter_and_content(file2)
    
    print("👥 Fusion des fichiers pôle jeunes...")
    print(f"  {file1}: {len(content1)} caractères")
    print(f"  {file2}: {len(content2)} caractères")
    
    # Prendre les meilleures métadonnées (file2 a l'URL et le bon layout)
    merged_fm = {
        'title': 'Pôle Jeunes (12-17 ans)',
        'description': fm1.get('description', fm2.get('description')),
        'layout': 'paroisse/jeunesse',  # Correct layout pour jeunesse
        'updated': '2025-09-16',
        'url': '/pole-jeunes-12-17-ans/'
    }
    
    # Prendre le contenu le plus long (file1 a 96 lignes vs 15)
    if len(content1) > len(content2):
        merged_content = content1
        print("  → Contenu de 'Pôle Jeunes (12-17 ans).md' conservé (plus complet)")
    else:
        merged_content = content2
        print("  → Contenu de 'jeunesse/pole-jeunes-12-17-ans.md' conservé")
    
    # Nettoyer le contenu
    merged_content = re.sub(r'# Jeunes \(12-17 ans\)\n', '', merged_content)  # Supprimer H1 dupliqué
    
    return merged_fm, merged_content

def write_merged_file(file_path, frontmatter, content):
    """Écrit le fichier fusionné."""
    try:
        frontmatter_yaml = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
        merged_file_content = f"---\n{frontmatter_yaml}---\n\n{content}"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(merged_file_content)
        
        print(f"✅ Fichier fusionné écrit: {file_path}")
        return True
    except Exception as e:
        print(f"❌ Erreur écriture {file_path}: {e}")
        return False

def main():
    """Fonction principale."""
    print("🔄 Fusion intelligente des derniers doublons...\n")
    
    # 1. Fusionner les fichiers étudiants
    fm_etudiants, content_etudiants = merge_etudiants()
    
    # Écrire le fichier fusionné (garder etudiants.md, supprimer Étudiants.md)
    if write_merged_file('content/etudiants.md', fm_etudiants, content_etudiants):
        try:
            os.remove('content/Étudiants.md')
            print("🗑️  Supprimé: content/Étudiants.md")
        except Exception as e:
            print(f"❌ Erreur suppression Étudiants.md: {e}")
    
    print()
    
    # 2. Fusionner les fichiers pôle jeunes
    fm_jeunes, content_jeunes = merge_pole_jeunes()
    
    # Écrire le fichier fusionné (garder jeunesse/pole-jeunes-12-17-ans.md, supprimer l'autre)
    if write_merged_file('content/jeunesse/pole-jeunes-12-17-ans.md', fm_jeunes, content_jeunes):
        try:
            os.remove('content/Pôle Jeunes (12-17 ans).md')
            print("🗑️  Supprimé: content/Pôle Jeunes (12-17 ans).md")
        except Exception as e:
            print(f"❌ Erreur suppression Pôle Jeunes (12-17 ans).md: {e}")
    
    print("\n🎉 Fusion terminée !")
    print("💡 Vérifiez les fichiers fusionnés et commitez les changements.")

if __name__ == "__main__":
    main()
