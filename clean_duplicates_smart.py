#!/usr/bin/env python3
"""
Script intelligent pour nettoyer les doublons de fichiers Markdown.
Évite les faux positifs et se concentre sur les vrais doublons.
"""

import os
import re
import unicodedata
from pathlib import Path

def slugify(text):
    """Convertit un texte en slug (comme WordPress)."""
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def analyze_file_content(file_path):
    """Analyse le contenu d'un fichier."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        has_frontmatter = content.startswith('---')
        lines = content.split('\n')
        content_lines = len([line for line in lines if line.strip()])
        
        updated_date = None
        if has_frontmatter:
            frontmatter_match = re.search(r'updated:\s*[\'"]?([^\'"]+)[\'"]?', content)
            if frontmatter_match:
                updated_date = frontmatter_match.group(1)
        
        return {
            'has_frontmatter': has_frontmatter,
            'content_lines': content_lines,
            'updated_date': updated_date,
            'size': len(content),
            'content': content
        }
    except Exception as e:
        return {'error': str(e)}

def are_similar_content(content1, content2, threshold=0.7):
    """Vérifie si deux contenus sont similaires."""
    # Nettoyer les contenus pour la comparaison
    def clean_content(content):
        # Supprimer le front matter
        content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
        # Normaliser les espaces
        content = re.sub(r'\s+', ' ', content)
        return content.strip().lower()
    
    clean1 = clean_content(content1)
    clean2 = clean_content(content2)
    
    if not clean1 or not clean2:
        return False
    
    # Calculer la similarité basique
    shorter = min(len(clean1), len(clean2))
    longer = max(len(clean1), len(clean2))
    
    if shorter == 0:
        return False
    
    # Si un contenu est beaucoup plus long, ils ne sont probablement pas similaires
    if longer / shorter > 3:
        return False
    
    # Comparer les mots communs
    words1 = set(clean1.split())
    words2 = set(clean2.split())
    
    if not words1 or not words2:
        return False
    
    common_words = words1.intersection(words2)
    total_words = words1.union(words2)
    
    similarity = len(common_words) / len(total_words)
    return similarity >= threshold

def find_real_duplicates():
    """Trouve les vrais doublons (même contenu, noms similaires)."""
    content_dir = Path('content')
    all_files = list(content_dir.rglob('*.md'))
    
    # Exclure certains fichiers spéciaux
    excluded_patterns = [
        r'posts/.*',  # Articles de blog
        r'404\.html?',  # Pages d'erreur
        r'about\.md',  # Page à propos générique
        r'test\.md',  # Pages de test
    ]
    
    filtered_files = []
    for file_path in all_files:
        relative_path = str(file_path.relative_to(content_dir))
        if not any(re.match(pattern, relative_path) for pattern in excluded_patterns):
            filtered_files.append(file_path)
    
    # Grouper par slug
    slug_groups = {}
    for file_path in filtered_files:
        filename = file_path.stem
        slug = slugify(filename)
        
        if slug not in slug_groups:
            slug_groups[slug] = []
        slug_groups[slug].append(file_path)
    
    # Identifier les vrais doublons
    real_duplicates = {}
    for slug, files in slug_groups.items():
        if len(files) > 1:
            # Vérifier si les contenus sont similaires
            analyses = [analyze_file_content(f) for f in files]
            
            # Filtrer les fichiers avec erreurs
            valid_files = []
            valid_analyses = []
            for f, a in zip(files, analyses):
                if 'error' not in a:
                    valid_files.append(f)
                    valid_analyses.append(a)
            
            if len(valid_files) > 1:
                # Vérifier la similarité du contenu
                similar_pairs = []
                for i in range(len(valid_files)):
                    for j in range(i + 1, len(valid_files)):
                        content1 = valid_analyses[i]['content']
                        content2 = valid_analyses[j]['content']
                        
                        if are_similar_content(content1, content2):
                            similar_pairs.append((valid_files[i], valid_files[j]))
                
                if similar_pairs:
                    real_duplicates[slug] = {
                        'files': valid_files,
                        'analyses': valid_analyses,
                        'similar_pairs': similar_pairs
                    }
    
    return real_duplicates

def main():
    """Fonction principale."""
    print("🔍 Recherche des vrais doublons (contenu similaire)...")
    
    duplicates = find_real_duplicates()
    
    if not duplicates:
        print("✅ Aucun vrai doublon trouvé !")
        return
    
    print(f"⚠️  {len(duplicates)} groupes de vrais doublons trouvés :\n")
    
    files_to_remove = []
    
    for slug, data in duplicates.items():
        files = data['files']
        analyses = data['analyses']
        
        print(f"📁 Groupe '{slug}' ({len(files)} fichiers similaires):")
        
        # Calculer les scores pour chaque fichier
        file_scores = []
        for file_path, analysis in zip(files, analyses):
            score = 0
            reasons = []
            
            # Préférer les fichiers avec front matter YAML récent
            if analysis['has_frontmatter']:
                score += 10
                reasons.append("Front matter YAML")
            
            if analysis['updated_date'] == '2025-09-16':
                score += 8
                reasons.append("Récemment synchronisé")
            
            # Préférer les fichiers avec plus de contenu
            score += min(analysis['content_lines'] / 10, 5)
            if analysis['content_lines'] > 20:
                reasons.append("Contenu substantiel")
            
            # Préférer les noms standardisés
            filename = file_path.name
            if not re.search(r'[À-ÿ\s\(\)]', filename):
                score += 3
                reasons.append("Nom standardisé")
            
            # Préférer l'organisation en sous-répertoires
            if len(file_path.parts) > 2:
                score += 2
                reasons.append("Bien organisé")
            
            file_scores.append({
                'file': file_path,
                'score': score,
                'reasons': reasons,
                'analysis': analysis
            })
        
        # Trier par score
        file_scores.sort(key=lambda x: x['score'], reverse=True)
        
        for i, rec in enumerate(file_scores):
            file_path = rec['file']
            score = rec['score']
            reasons = rec['reasons']
            analysis = rec['analysis']
            
            status = "🟢 GARDER" if i == 0 else "🔴 SUPPRIMER"
            
            print(f"  {status} {file_path}")
            print(f"    Score: {score:.1f} | Lignes: {analysis['content_lines']} | Taille: {analysis['size']}")
            print(f"    Raisons: {', '.join(reasons) if reasons else 'Aucune'}")
            if analysis['updated_date']:
                print(f"    Mis à jour: {analysis['updated_date']}")
            print()
            
            if i > 0:  # Ajouter à la suppression (sauf le premier)
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
                    print(f"❌ Erreur: {file_path}: {e}")
            
            print(f"\n🎉 {removed_count} fichiers supprimés !")
        else:
            print("❌ Suppression annulée.")

if __name__ == "__main__":
    main()
