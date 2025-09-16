# Import des fichiers Markdown vers WordPress

Ce projet contient des scripts pour automatiser l'import des fichiers markdown du dossier `content/` vers une installation WordPress.

## 📁 Fichiers créés

- `create_wordpress_pages.py` - Script d'import automatique via API REST
- `generate_wordpress_import.py` - Générateur de fichier XML d'import WordPress
- `check_wordpress_permissions.py` - Diagnostic des permissions WordPress
- `open_wordpress_admin.py` - Ouverture de l'interface d'administration
- `import_to_wordpress.py` - Script principal orchestrant tout le processus
- `wordpress_config.py` - Configuration (identifiants, exclusions, etc.)
- `wordpress_import.xml` - Fichier XML généré pour l'import

## 🚀 Utilisation rapide

### Option 1: Script principal (recommandé)
```bash
python3 import_to_wordpress.py
```

### Option 2: Import manuel étape par étape
```bash
# 1. Générer le fichier XML
python3 generate_wordpress_import.py

# 2. Ouvrir l'interface WordPress
python3 open_wordpress_admin.py
```

## ⚙️ Configuration

Modifiez le fichier `wordpress_config.py` pour personnaliser :

```python
WORDPRESS_CONFIG = {
    'url': 'http://localhost:8080',
    'username': 'votre_nom_utilisateur',
    'password': 'votre_mot_de_passe'
}

# Fichiers à exclure
EXCLUDED_FILES = {
    'index.md',
    '404.html',
}

# Slugs personnalisés
CUSTOM_SLUGS = {
    'baptême.md': 'bapteme',
    'catéchèse.md': 'catechese',
}
```

## 📋 Processus d'import manuel

1. **Connectez-vous à WordPress** : http://localhost:8080/wp-admin
2. **Allez dans Outils > Importer**
3. **Choisissez "WordPress"** et installez l'importeur si nécessaire
4. **Sélectionnez le fichier** `wordpress_import.xml`
5. **Lancez l'import** et suivez les instructions

## 📊 Résultats

Le script traite **42 fichiers markdown** et crée les pages suivantes :

### Pages principales
- Bienvenue
- Présentation
- Qui sommes-nous
- Catéchèse
- Baptême
- Confirmation
- Mariage
- Obsèques
- Se confesser
- Rencontrer un prêtre
- Rejoindre un groupe
- Offrir une messe
- Intentions de prière

### Pages des églises (sous-dossier `eglises/`)
- Saint-Étienne
- Saint-Pierre
- Saint-Paul
- Saint-Ouen
- Saint-Julien
- Saint-Jean-Baptiste
- Saint-Joseph du chemin vert
- Saint-André du Calvaire Saint-Pierre
- Saint-Bernard de la Pierre-Heuzé
- Saint-Clair d'Hérouville-Saint-Clair
- Saint-François d'Hérouville-Saint-Clair
- Saint-Gerbold de Blainville-sur-Orne
- Saint-Germain de Saint-Germain-la-Blanche-Herbe
- Saint-Sauveur
- Sainte-Claire de la Folie-Couvrechef
- Sainte-Trinité Saint-Gilles
- Notre-Dame-de-l'Assomption (la Gloriette)
- Chapelle des Bénédictines
- Chapelle de la Miséricorde
- Chapelle de l'Oasis
- Chapelle CHR
- Carmel de Caen
- Monastère de la Visitation

### Pages d'information (sous-dossier `infos/`)
- Horaires des messes

### Pages jeunesse
- Jeunes (12-17 ans)
- Pôle Jeunes (12-17 ans)

## 🔧 Fonctionnalités

### Conversion Markdown → HTML
- **Titres** : `#`, `##`, `###`, `####` → `<h1>`, `<h2>`, `<h3>`, `<h4>`
- **Gras** : `**texte**` → `<strong>texte</strong>`
- **Italique** : `*texte*` → `<em>texte</em>`
- **Liens** : `[texte](url)` → `<a href="url">texte</a>`
- **Listes** : `- item` → `<ul><li>item</li></ul>`
- **Citations** : `> texte` → `<blockquote>texte</blockquote>`
- **Paragraphes** : Conversion automatique

### Gestion des métadonnées
- Extraction du **front matter YAML**
- Génération automatique des **slugs** (URLs)
- Support des **descriptions** et **titres** personnalisés
- Gestion des **caractères spéciaux** français

### Génération des slugs
- Conversion automatique des accents : `é` → `e`, `à` → `a`, etc.
- Remplacement des espaces par des tirets
- Suppression des caractères spéciaux
- Slugs personnalisables via la configuration

## 🛠️ Dépannage

### Problème d'API REST
Si l'import automatique échoue :
1. Vérifiez que l'utilisateur a le rôle "Administrateur"
2. Activez les permaliens dans WordPress (Réglages > Permaliens)
3. Désactivez temporairement les plugins de sécurité
4. Utilisez l'import manuel via le fichier XML

### Problème de permissions
```bash
python3 check_wordpress_permissions.py
```

### Problème de connexion
Vérifiez que WordPress est accessible :
```bash
curl -I http://localhost:8080
```

## 📝 Structure du fichier XML généré

Le fichier `wordpress_import.xml` respecte le format standard WordPress WXR (WordPress eXtended RSS) :
- **Métadonnées** du site
- **Pages** avec titre, contenu, slug, statut
- **Dates** de création
- **Auteur** assigné
- **Commentaires** avec fichier source

## 🎯 Après l'import

1. **Vérifiez** que toutes les pages ont été créées
2. **Configurez** les menus de navigation
3. **Testez** les liens entre les pages
4. **Personnalisez** le contenu selon vos besoins
5. **Configurez** les widgets et la mise en page

## 📞 Support

En cas de problème :
1. Vérifiez les logs d'erreur
2. Testez la connexion WordPress
3. Vérifiez les permissions utilisateur
4. Consultez la documentation WordPress sur l'import/export
