#!/usr/bin/env python3
"""
Script pour vérifier les permissions WordPress et diagnostiquer les problèmes
"""

import requests
import base64
import json
from wordpress_config import WORDPRESS_CONFIG

def check_wordpress_permissions():
    """Vérifie les permissions WordPress et propose des solutions"""
    
    wp_url = WORDPRESS_CONFIG['url']
    username = WORDPRESS_CONFIG['username']
    password = WORDPRESS_CONFIG['password']
    
    print("🔍 Diagnostic des permissions WordPress...")
    print(f"URL: {wp_url}")
    print(f"Utilisateur: {username}")
    
    # Configuration de l'authentification
    auth = base64.b64encode(f"{username}:{password}".encode()).decode()
    headers = {
        'Authorization': f'Basic {auth}',
        'Content-Type': 'application/json'
    }
    
    # URLs d'API à tester
    api_urls = [
        f"{wp_url}/wp-json/wp/v2",
        f"{wp_url}/index.php?rest_route=/wp/v2"
    ]
    
    working_api_url = None
    
    # Test des URLs d'API
    for api_url in api_urls:
        print(f"\n🔗 Test de l'API: {api_url}")
        try:
            response = requests.get(f"{api_url}/users/me", headers=headers, timeout=10)
            if response.status_code == 200:
                working_api_url = api_url
                user_info = response.json()
                print(f"✅ Connexion réussie!")
                print(f"   Nom: {user_info.get('name', 'N/A')}")
                print(f"   Email: {user_info.get('email', 'N/A')}")
                print(f"   Rôles: {', '.join(user_info.get('roles', []))}")
                print(f"   Capacités: {len(user_info.get('capabilities', {}))} permissions")
                
                # Vérifier les capacités importantes
                capabilities = user_info.get('capabilities', {})
                important_caps = [
                    'edit_pages', 'publish_pages', 'delete_pages',
                    'edit_posts', 'publish_posts', 'delete_posts',
                    'manage_options', 'edit_others_pages'
                ]
                
                print("\n📋 Permissions importantes:")
                for cap in important_caps:
                    status = "✅" if capabilities.get(cap) else "❌"
                    print(f"   {status} {cap}")
                
                break
            elif response.status_code == 401:
                print("❌ Authentification échouée")
            else:
                print(f"❌ Erreur: {response.status_code}")
        except Exception as e:
            print(f"❌ Erreur de connexion: {e}")
    
    if not working_api_url:
        print("\n❌ Aucune API WordPress fonctionnelle trouvée")
        return False
    
    # Test de création d'une page
    print(f"\n🧪 Test de création d'une page...")
    test_page_data = {
        'title': 'Test Page - À supprimer',
        'content': '<p>Page de test créée automatiquement. Vous pouvez la supprimer.</p>',
        'status': 'draft'  # Brouillon pour ne pas publier
    }
    
    try:
        response = requests.post(f"{working_api_url}/pages", headers=headers, json=test_page_data, timeout=10)
        if response.status_code == 201:
            page_info = response.json()
            print(f"✅ Création de page réussie! (ID: {page_info['id']})")
            
            # Supprimer la page de test
            delete_response = requests.delete(f"{working_api_url}/pages/{page_info['id']}", headers=headers, timeout=10)
            if delete_response.status_code == 200:
                print("✅ Page de test supprimée")
            else:
                print(f"⚠️  Page de test non supprimée (ID: {page_info['id']})")
            
            return True
        else:
            error_info = response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text
            print(f"❌ Échec de création: {response.status_code}")
            print(f"   Erreur: {error_info}")
            
            # Analyser l'erreur
            if response.status_code == 401:
                print("\n💡 Solutions possibles:")
                print("1. Vérifiez que l'utilisateur a le rôle 'Administrateur' ou 'Éditeur'")
                print("2. Vérifiez que l'API REST est activée dans WordPress")
                print("3. Vérifiez qu'il n'y a pas de plugin de sécurité bloquant l'API")
                print("4. Essayez de créer une page manuellement dans l'admin WordPress")
            
            return False
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        return False

def suggest_solutions():
    """Propose des solutions pour résoudre les problèmes de permissions"""
    print("\n🛠️  Solutions recommandées:")
    print("\n1. Vérifier le rôle utilisateur:")
    print("   - Connectez-vous à l'admin WordPress (http://localhost:8080/wp-admin)")
    print("   - Allez dans Utilisateurs > Tous les utilisateurs")
    print("   - Vérifiez que votre utilisateur a le rôle 'Administrateur'")
    
    print("\n2. Activer l'API REST:")
    print("   - Dans l'admin WordPress, allez dans Réglages > Permaliens")
    print("   - Choisissez une structure autre que 'Simple'")
    print("   - Cliquez sur 'Enregistrer les modifications'")
    
    print("\n3. Vérifier les plugins de sécurité:")
    print("   - Désactivez temporairement les plugins de sécurité")
    print("   - Testez à nouveau la création de pages")
    
    print("\n4. Alternative: Import manuel")
    print("   - Utilisez l'outil d'import WordPress")
    print("   - Convertissez les fichiers markdown en XML WordPress")
    
    print("\n5. Créer un utilisateur API dédié:")
    print("   - Créez un nouvel utilisateur avec le rôle 'Administrateur'")
    print("   - Utilisez ces identifiants pour l'API")

if __name__ == "__main__":
    success = check_wordpress_permissions()
    if not success:
        suggest_solutions()
