#!/usr/bin/env python3
"""
Script pour les futures synchronisations WordPress → GitHub.
Ce script vérifie les modifications depuis la dernière synchronisation.
"""

import os
import subprocess
from datetime import datetime
from sync_wordpress_content import sync_wordpress_content

def get_last_sync_date():
    """Récupère la date de la dernière synchronisation depuis Git."""
    try:
        # Chercher le dernier commit contenant "Synchronisation"
        result = subprocess.run([
            'git', 'log', '--grep=Synchronisation', '--format=%cd', '--date=iso', '-1'
        ], capture_output=True, text=True, cwd='.')
        
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        else:
            return "Aucune synchronisation précédente trouvée"
    except Exception as e:
        return f"Erreur lors de la récupération de la date: {e}"

def check_git_status():
    """Vérifie l'état du repository Git."""
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, cwd='.')
        return result.stdout.strip()
    except Exception as e:
        return f"Erreur Git: {e}"

def main():
    """Fonction principale pour la synchronisation future."""
    print("🔄 Synchronisation WordPress → GitHub")
    print("=" * 50)
    
    # Vérifier la dernière synchronisation
    last_sync = get_last_sync_date()
    print(f"📅 Dernière synchronisation: {last_sync}")
    
    # Vérifier l'état Git
    git_status = check_git_status()
    if git_status:
        print("⚠️  Modifications non commitées détectées:")
        print(git_status[:500] + "..." if len(git_status) > 500 else git_status)
        
        response = input("\nVoulez-vous continuer malgré les modifications non commitées ? (y/N): ")
        if response.lower() != 'y':
            print("❌ Synchronisation annulée.")
            return
    
    print("\n🔄 Début de la synchronisation...")
    
    # Lancer la synchronisation
    try:
        sync_wordpress_content()
        
        # Vérifier les nouveaux changements
        new_git_status = check_git_status()
        if new_git_status:
            print(f"\n📝 {len(new_git_status.splitlines())} fichiers modifiés détectés.")
            
            response = input("Voulez-vous commiter ces changements ? (Y/n): ")
            if response.lower() != 'n':
                # Créer un commit automatique
                current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                commit_message = f"Synchronisation WordPress automatique - {current_date}"
                
                subprocess.run(['git', 'add', '.'], cwd='.')
                result = subprocess.run(['git', 'commit', '-m', commit_message], 
                                      capture_output=True, text=True, cwd='.')
                
                if result.returncode == 0:
                    print("✅ Changements commitées avec succès!")
                    print(f"📝 Message de commit: {commit_message}")
                else:
                    print(f"❌ Erreur lors du commit: {result.stderr}")
            else:
                print("⚠️  Changements non commitées. N'oubliez pas de les commiter manuellement.")
        else:
            print("✅ Aucun changement détecté. Le repository est à jour.")
            
    except Exception as e:
        print(f"❌ Erreur lors de la synchronisation: {e}")

if __name__ == "__main__":
    main()
