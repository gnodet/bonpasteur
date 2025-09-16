"""
Configuration pour la création des pages WordPress
Modifiez ces valeurs selon votre installation WordPress
"""

# Configuration WordPress
WORDPRESS_CONFIG = {
    'url': 'https://bonpasteurcaen.wordpress.com',
    'username': 'gnodet',  # Remplacez par votre nom d'utilisateur WordPress
    'password': 'Ayl%F#Hl!an@h84A9^',  # Remplacez par votre mot de passe WordPress
}

# Fichiers à exclure de la création de pages
EXCLUDED_FILES = {
    'index.md',  # Page d'accueil généralement gérée différemment
    '404.html',  # Page d'erreur
}

# Mapping des slugs personnalisés (optionnel)
CUSTOM_SLUGS = {
    'baptême.md': 'bapteme',
    'catéchèse.md': 'catechese',
    'Intentions de prière.md': 'intentions-priere',
    'Jeunes (12-17 ans).md': 'jeunes-12-17-ans',
    'Pôle Jeunes (12-17 ans).md': 'pole-jeunes-12-17-ans',
}

# Configuration des pages parentes (pour créer une hiérarchie)
PAGE_HIERARCHY = {
    # 'enfant.md': 'parent.md',  # Exemple: la page enfant aura comme parent la page parent
}
