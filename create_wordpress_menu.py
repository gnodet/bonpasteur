#!/usr/bin/env python3
"""
Script pour créer automatiquement un menu WordPress avec les pages importées
"""

import requests
import json
from wordpress_config import WORDPRESS_CONFIG

class WordPressMenuCreator:
    def __init__(self, wp_url: str, username: str, password: str):
        self.wp_url = wp_url
        self.api_url_alt = f"{wp_url}/index.php?rest_route=/wp/v2"
        self.auth = (username, password)
        self.headers = {'Content-Type': 'application/json'}
    
    def get_pages(self):
        """Récupère toutes les pages WordPress"""
        try:
            response = requests.get(
                f"{self.api_url_alt}/pages",
                auth=self.auth,
                params={'per_page': 100, 'status': 'publish'}
            )
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Erreur lors de la récupération des pages: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Erreur: {e}")
            return []
    
    def create_menu_structure(self, pages):
        """Crée la structure du menu basée sur les pages disponibles"""
        
        # Structure du menu pour une paroisse
        menu_structure = {
            "Accueil": {"url": self.wp_url, "type": "custom"},
            "Découvrir": {
                "type": "parent",
                "children": [
                    "Bienvenue",
                    "Présentation", 
                    "Qui sommes-nous"
                ]
            },
            "Églises": {
                "type": "parent", 
                "mega_menu": True,
                "children": []  # Sera rempli avec les églises
            },
            "Sacrements": {
                "type": "parent",
                "children": [
                    "Baptême",
                    "Mariage", 
                    "Confirmation",
                    "Obsèques"
                ]
            },
            "Vie paroissiale": {
                "type": "parent",
                "children": [
                    "Horaires des messes",
                    "Catéchèse",
                    "Jeunes",
                    "Rejoindre un groupe",
                    "Rencontrer un prêtre"
                ]
            },
            "Services": {
                "type": "parent", 
                "children": [
                    "Se confesser",
                    "Offrir une messe",
                    "Intentions de prière"
                ]
            },
            "Contact": {"type": "single"}
        }
        
        # Mapper les pages aux éléments du menu
        page_map = {}
        for page in pages:
            title = page['title']['rendered']
            slug = page['slug']
            page_map[title.lower()] = {
                'id': page['id'],
                'title': title,
                'url': page['link'],
                'slug': slug
            }
        
        # Remplir les églises
        eglises = []
        for page in pages:
            title = page['title']['rendered'].lower()
            if any(keyword in title for keyword in ['saint-', 'sainte-', 'église', 'chapelle', 'cathédrale', 'notre-dame']):
                eglises.append(page['title']['rendered'])
        
        menu_structure["Églises"]["children"] = sorted(eglises)
        
        return menu_structure, page_map
    
    def print_menu_preview(self, menu_structure, page_map):
        """Affiche un aperçu de la structure du menu"""
        print("\n📋 Structure du menu proposée:")
        print("=" * 50)
        
        for main_item, config in menu_structure.items():
            if config.get("type") == "custom":
                print(f"🏠 {main_item} (Page d'accueil)")
            elif config.get("type") == "parent":
                mega_indicator = " [MEGA MENU]" if config.get("mega_menu") else ""
                print(f"📁 {main_item}{mega_indicator}")
                
                children = config.get("children", [])
                for i, child in enumerate(children):
                    is_last = i == len(children) - 1
                    prefix = "└── " if is_last else "├── "
                    
                    # Vérifier si la page existe
                    if child.lower() in page_map:
                        status = "✅"
                    else:
                        status = "❌"
                    
                    print(f"   {prefix}{status} {child}")
            else:
                # Page simple
                if main_item.lower() in page_map:
                    status = "✅"
                else:
                    status = "❌"
                print(f"📄 {status} {main_item}")
        
        print("\n✅ = Page trouvée dans WordPress")
        print("❌ = Page manquante (sera créée comme lien personnalisé)")
    
    def generate_menu_instructions(self, menu_structure, page_map):
        """Génère les instructions pour créer le menu manuellement"""
        
        instructions = """
# 📋 Instructions pour créer le menu WordPress

## 1. Accéder aux menus
1. Allez dans **Apparence > Menus**
2. Cliquez sur **"Créer un nouveau menu"**
3. Nommez-le **"Menu Principal"**
4. Cliquez sur **"Créer le menu"**

## 2. Ajouter les éléments

### Structure recommandée:
"""
        
        for main_item, config in menu_structure.items():
            if config.get("type") == "custom":
                instructions += f"""
**{main_item}** (Lien personnalisé)
- URL: {config['url']}
- Texte: {main_item}
"""
            elif config.get("type") == "parent":
                instructions += f"""
**{main_item}** (Lien personnalisé - parent)
- URL: #
- Texte: {main_item}
"""
                if config.get("mega_menu"):
                    instructions += "- ⚠️ Configurer comme MEGA MENU\n"
                
                children = config.get("children", [])
                for child in children:
                    if child.lower() in page_map:
                        page_info = page_map[child.lower()]
                        instructions += f"  └── **{child}** (Page existante - ID: {page_info['id']})\n"
                    else:
                        instructions += f"  └── **{child}** (⚠️ Page manquante - créer un lien personnalisé)\n"
            else:
                if main_item.lower() in page_map:
                    page_info = page_map[main_item.lower()]
                    instructions += f"""
**{main_item}** (Page existante - ID: {page_info['id']})
"""
                else:
                    instructions += f"""
**{main_item}** (⚠️ Page manquante)
"""
        
        instructions += """
## 3. Configuration des sous-menus
- **Glissez** les éléments enfants vers la **droite** sous leur parent
- L'**indentation** indique la hiérarchie

## 4. Mega Menu (pour "Églises")
Si vous utilisez un plugin de mega menu:
1. Activez le mega menu pour l'élément "Églises"
2. Configurez en **2 ou 3 colonnes**
3. Organisez les églises par zone géographique si possible

## 5. Assigner le menu
1. Dans **"Réglages du menu"** (en bas de page)
2. Cochez **"Menu principal"** ou **"Primary Menu"**
3. Cliquez sur **"Enregistrer le menu"**

## 6. Configuration responsive
- Vérifiez l'affichage sur mobile
- Configurez le bouton hamburger si nécessaire
- Testez la navigation tactile
"""
        
        return instructions

def main():
    """Fonction principale"""
    print("🎯 Création du menu WordPress pour la paroisse")
    print("=" * 50)
    
    # Initialisation
    creator = WordPressMenuCreator(
        WORDPRESS_CONFIG['url'],
        WORDPRESS_CONFIG['username'], 
        WORDPRESS_CONFIG['password']
    )
    
    # Récupération des pages
    print("📄 Récupération des pages WordPress...")
    pages = creator.get_pages()
    
    if not pages:
        print("❌ Aucune page trouvée. Assurez-vous que l'import a été effectué.")
        return
    
    print(f"✅ {len(pages)} pages trouvées")
    
    # Création de la structure du menu
    print("\n🔧 Génération de la structure du menu...")
    menu_structure, page_map = creator.create_menu_structure(pages)
    
    # Aperçu du menu
    creator.print_menu_preview(menu_structure, page_map)
    
    # Génération des instructions
    instructions = creator.generate_menu_instructions(menu_structure, page_map)
    
    # Sauvegarde des instructions
    with open("instructions_menu_wordpress.md", "w", encoding="utf-8") as f:
        f.write(instructions)
    
    print(f"\n📝 Instructions détaillées sauvegardées dans: instructions_menu_wordpress.md")
    
    # Résumé
    total_items = len(menu_structure)
    found_pages = sum(1 for item, config in menu_structure.items() 
                     if config.get("type") != "custom" and item.lower() in page_map)
    
    print(f"\n📊 Résumé:")
    print(f"   - {total_items} éléments principaux dans le menu")
    print(f"   - {found_pages} pages WordPress trouvées")
    print(f"   - {len(page_map)} pages totales disponibles")
    
    print(f"\n🎯 Prochaines étapes:")
    print("1. Ouvrez WordPress Admin: http://localhost:8080/wp-admin")
    print("2. Allez dans Apparence > Menus")
    print("3. Suivez les instructions dans le fichier généré")
    print("4. Testez le menu sur desktop et mobile")

if __name__ == "__main__":
    main()
