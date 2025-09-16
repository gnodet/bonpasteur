#!/usr/bin/env python3
"""
Script de test pour vérifier la connexion à WordPress
"""

import requests
import base64
import json

def test_wordpress_connection():
    """Test la connexion à WordPress et affiche les informations"""
    
    # Configuration
    wp_url = "http://localhost:8080"
    
    print("🔍 Test de connexion à WordPress...")
    print(f"URL: {wp_url}")
    
    # Test 1: Vérifier que WordPress répond
    try:
        response = requests.get(wp_url, timeout=10)
        if response.status_code == 200:
            print("✅ WordPress est accessible")
        else:
            print(f"❌ WordPress répond avec le code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Impossible d'accéder à WordPress: {e}")
        return False
    
    # Test 2: Vérifier l'API REST
    api_url = f"{wp_url}/wp-json/wp/v2"
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            print("✅ API REST WordPress accessible")
        else:
            print(f"❌ API REST répond avec le code: {response.status_code}")
    except Exception as e:
        print(f"❌ Erreur API REST: {e}")
    
    # Test 3: Lister les pages existantes (sans authentification)
    try:
        response = requests.get(f"{api_url}/pages", timeout=10)
        if response.status_code == 200:
            pages = response.json()
            print(f"✅ {len(pages)} pages trouvées dans WordPress")
            if pages:
                print("📄 Pages existantes:")
                for page in pages[:5]:  # Afficher les 5 premières
                    print(f"   - {page['title']['rendered']} (ID: {page['id']})")
                if len(pages) > 5:
                    print(f"   ... et {len(pages) - 5} autres")
        else:
            print(f"❌ Impossible de lister les pages: {response.status_code}")
    except Exception as e:
        print(f"❌ Erreur lors de la récupération des pages: {e}")
    
    # Test 4: Vérifier les utilisateurs (nécessite authentification)
    print("\n🔐 Test d'authentification...")
    print("Pour tester l'authentification, vous devez fournir vos identifiants WordPress.")
    
    username = input("Nom d'utilisateur WordPress (ou Entrée pour passer): ").strip()
    if username:
        password = input("Mot de passe WordPress: ").strip()
        
        if password:
            auth = base64.b64encode(f"{username}:{password}".encode()).decode()
            headers = {
                'Authorization': f'Basic {auth}',
                'Content-Type': 'application/json'
            }
            
            try:
                response = requests.get(f"{api_url}/users/me", headers=headers, timeout=10)
                if response.status_code == 200:
                    user_info = response.json()
                    print(f"✅ Authentification réussie pour: {user_info['name']}")
                    print(f"   Rôles: {', '.join(user_info['roles'])}")
                    
                    # Test de création d'une page de test
                    test_page_data = {
                        'title': 'Test Page - À supprimer',
                        'content': '<p>Ceci est une page de test créée automatiquement. Vous pouvez la supprimer.</p>',
                        'status': 'draft'  # Brouillon pour ne pas publier
                    }
                    
                    response = requests.post(f"{api_url}/pages", headers=headers, json=test_page_data, timeout=10)
                    if response.status_code == 201:
                        page_info = response.json()
                        print(f"✅ Test de création de page réussi (ID: {page_info['id']})")
                        print("   La page de test a été créée en brouillon")
                        
                        # Supprimer la page de test
                        delete_response = requests.delete(f"{api_url}/pages/{page_info['id']}", headers=headers, timeout=10)
                        if delete_response.status_code == 200:
                            print("✅ Page de test supprimée avec succès")
                        else:
                            print(f"⚠️  Page de test créée mais non supprimée (ID: {page_info['id']})")
                    else:
                        print(f"❌ Échec de création de page de test: {response.status_code}")
                        print(f"   Réponse: {response.text}")
                        
                elif response.status_code == 401:
                    print("❌ Identifiants incorrects")
                else:
                    print(f"❌ Erreur d'authentification: {response.status_code}")
                    print(f"   Réponse: {response.text}")
            except Exception as e:
                print(f"❌ Erreur lors du test d'authentification: {e}")
    
    print("\n📋 Résumé:")
    print("1. Assurez-vous que WordPress est accessible")
    print("2. Vérifiez que l'API REST est activée")
    print("3. Utilisez un compte avec les droits d'édition de pages")
    print("4. Modifiez wordpress_config.py avec vos identifiants")

if __name__ == "__main__":
    test_wordpress_connection()
