#!/usr/bin/env python3
"""
Script pour ouvrir l'interface d'administration WordPress et guider l'import
"""

import webbrowser
import os
from pathlib import Path

def open_wordpress_admin():
    """Ouvre l'interface d'administration WordPress"""
    
    wp_admin_url = "http://localhost:8080/wp-admin"
    import_url = "http://localhost:8080/wp-admin/import.php"
    
    print("🌐 Ouverture de l'interface d'administration WordPress...")
    
    # Vérifier que le fichier XML existe
    xml_file = Path("wordpress_import.xml")
    if not xml_file.exists():
        print("❌ Le fichier wordpress_import.xml n'existe pas.")
        print("   Exécutez d'abord: python3 generate_wordpress_import.py")
        return
    
    print(f"✅ Fichier XML trouvé: {xml_file.absolute()}")
    
    # Ouvrir l'interface d'administration
    print(f"🔗 Ouverture de: {wp_admin_url}")
    webbrowser.open(wp_admin_url)
    
    print("\n📋 Instructions d'import:")
    print("1. Connectez-vous avec vos identifiants WordPress")
    print("2. Dans le menu de gauche, allez dans 'Outils' > 'Importer'")
    print("3. Cherchez 'WordPress' dans la liste des importeurs")
    print("4. Si ce n'est pas déjà fait, cliquez sur 'Installer maintenant'")
    print("5. Une fois installé, cliquez sur 'Lancer l'importeur'")
    print(f"6. Sélectionnez le fichier: {xml_file.absolute()}")
    print("7. Cliquez sur 'Téléverser le fichier et l'importer'")
    print("8. Assignez les articles à un utilisateur existant ou créez-en un nouveau")
    print("9. Cochez 'Télécharger et importer les fichiers joints' si souhaité")
    print("10. Cliquez sur 'Lancer l'importeur'")
    
    print(f"\n📊 Le fichier contient 42 pages à importer")
    print("\n⚠️  Notes importantes:")
    print("- L'import peut prendre quelques minutes")
    print("- Les pages seront créées avec le statut 'Publié'")
    print("- Vous pourrez modifier les pages après l'import")
    print("- Les slugs (URLs) seront générés automatiquement")
    
    print(f"\n🔗 Lien direct vers l'importeur: {import_url}")
    
    # Demander si l'utilisateur veut ouvrir directement la page d'import
    try:
        response = input("\nVoulez-vous ouvrir directement la page d'import ? (o/N): ").strip().lower()
        if response in ['o', 'oui', 'y', 'yes']:
            print(f"🔗 Ouverture de: {import_url}")
            webbrowser.open(import_url)
    except KeyboardInterrupt:
        print("\n👋 Au revoir !")

if __name__ == "__main__":
    open_wordpress_admin()
