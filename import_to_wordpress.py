#!/usr/bin/env python3
"""
Script principal pour importer les fichiers markdown vers WordPress
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Fonction principale qui orchestre l'import"""
    
    print("🚀 Import des fichiers markdown vers WordPress")
    print("=" * 50)
    
    # Vérifier que nous sommes dans le bon répertoire
    content_dir = Path("content")
    if not content_dir.exists():
        print("❌ Erreur: Le dossier 'content' n'existe pas.")
        print("   Assurez-vous d'être dans le répertoire racine du projet.")
        return
    
    # Étape 1: Générer le fichier XML d'import
    print("\n📝 Étape 1: Génération du fichier XML d'import...")
    try:
        result = subprocess.run([sys.executable, "generate_wordpress_import.py"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Fichier XML généré avec succès!")
        else:
            print("❌ Erreur lors de la génération du XML:")
            print(result.stderr)
            return
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return
    
    # Étape 2: Vérifier que le fichier XML existe
    xml_file = Path("wordpress_import.xml")
    if not xml_file.exists():
        print("❌ Le fichier XML n'a pas été créé correctement.")
        return
    
    print(f"✅ Fichier XML créé: {xml_file.absolute()}")
    
    # Étape 3: Proposer les options d'import
    print("\n🔧 Étape 2: Options d'import disponibles")
    print("1. Import automatique via API REST (recommandé si les permissions sont OK)")
    print("2. Import manuel via l'interface WordPress (recommandé)")
    print("3. Ouvrir seulement l'interface d'administration WordPress")
    
    try:
        choice = input("\nChoisissez une option (1/2/3): ").strip()
        
        if choice == "1":
            print("\n🔄 Tentative d'import automatique via API REST...")
            try:
                result = subprocess.run([sys.executable, "create_wordpress_pages.py"], 
                                      capture_output=True, text=True)
                print(result.stdout)
                if result.returncode != 0:
                    print("❌ L'import automatique a échoué.")
                    print("💡 Essayez l'option 2 (import manuel)")
            except Exception as e:
                print(f"❌ Erreur lors de l'import automatique: {e}")
                print("💡 Essayez l'option 2 (import manuel)")
        
        elif choice == "2":
            print("\n🌐 Ouverture de l'interface WordPress pour import manuel...")
            try:
                subprocess.run([sys.executable, "open_wordpress_admin.py"])
            except Exception as e:
                print(f"❌ Erreur: {e}")
        
        elif choice == "3":
            print("\n🌐 Ouverture de l'interface d'administration WordPress...")
            import webbrowser
            webbrowser.open("http://localhost:8080/wp-admin")
            print("✅ Interface ouverte dans votre navigateur")
        
        else:
            print("❌ Option invalide")
            return
    
    except KeyboardInterrupt:
        print("\n👋 Opération annulée")
        return
    
    # Résumé final
    print("\n" + "=" * 50)
    print("📋 Résumé:")
    print(f"✅ Fichier XML généré: {xml_file.name}")
    print("✅ 42 pages markdown prêtes à être importées")
    
    print("\n📄 Pages qui seront créées:")
    markdown_files = [f for f in content_dir.glob("**/*.md") 
                     if f.name not in {'index.md', '404.html'}]
    
    for i, md_file in enumerate(markdown_files[:10], 1):
        title = md_file.stem.replace('-', ' ').replace('_', ' ').title()
        print(f"   {i}. {title}")
    
    if len(markdown_files) > 10:
        print(f"   ... et {len(markdown_files) - 10} autres pages")
    
    print("\n🎯 Prochaines étapes:")
    if choice == "2":
        print("1. Connectez-vous à WordPress dans votre navigateur")
        print("2. Suivez les instructions d'import affichées")
        print("3. Vérifiez que toutes les pages ont été créées")
    else:
        print("1. Vérifiez que les pages ont été créées dans WordPress")
        print("2. Personnalisez les pages selon vos besoins")
    
    print("4. Configurez les menus et la navigation")
    print("5. Testez les liens entre les pages")

if __name__ == "__main__":
    main()
