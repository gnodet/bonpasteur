# Guide de Synchronisation WordPress ↔ GitHub

Ce repository contient les outils pour synchroniser le contenu entre le site WordPress [bonpasteurcaen.wordpress.com](https://bonpasteurcaen.wordpress.com) et ce repository GitHub.

## 📁 Structure des fichiers

```
├── content/                          # Contenu Markdown synchronisé
│   ├── jeunesse/                     # Pages dédiées aux jeunes
│   ├── eglises/                      # Églises et chapelles
│   ├── infos/                        # Informations pratiques
│   └── *.md                          # Pages principales
├── sync_wordpress_content.py         # Script principal de synchronisation
├── analyze_new_pages.py              # Analyse des nouvelles pages
├── sync_future.py                    # Synchronisation future automatisée
├── generate_wordpress_import.py      # Génération XML pour import WordPress
└── wordpress_config.py               # Configuration WordPress
```

## 🚀 Utilisation rapide

### Synchronisation WordPress → GitHub

```bash
# Synchronisation complète (recommandé)
python3 sync_wordpress_content.py

# Synchronisation avec gestion Git automatique
python3 sync_future.py
```

### Import GitHub → WordPress

```bash
# Générer le fichier XML d'import
python3 generate_wordpress_import.py

# Le fichier wordpress_import.xml sera créé
# Puis l'importer manuellement dans WordPress.com
```

## 📋 Scripts disponibles

### 1. `sync_wordpress_content.py` - Synchronisation principale

**Fonction :** Récupère le contenu du site WordPress et met à jour les fichiers Markdown.

**Utilisation :**
```bash
python3 sync_wordpress_content.py
```

**Ce qu'il fait :**
- Récupère le sitemap XML du site WordPress
- Télécharge le contenu de chaque page
- Convertit HTML → Markdown
- Crée/met à jour les fichiers avec front matter YAML
- Organise les fichiers dans la structure appropriée

### 2. `analyze_new_pages.py` - Analyse des nouvelles pages

**Fonction :** Identifie les nouvelles pages WordPress non encore mappées.

**Utilisation :**
```bash
python3 analyze_new_pages.py
```

**Sortie :** Génère `nouvelles_pages_rapport.md` avec les suggestions de mapping.

### 3. `sync_future.py` - Synchronisation automatisée

**Fonction :** Synchronisation avec gestion Git intégrée.

**Utilisation :**
```bash
python3 sync_future.py
```

**Fonctionnalités :**
- Vérifie la dernière synchronisation
- Détecte les modifications non commitées
- Propose de commiter automatiquement les changements
- Gestion interactive des conflits

### 4. `generate_wordpress_import.py` - Export vers WordPress

**Fonction :** Génère un fichier XML pour importer le contenu GitHub vers WordPress.

**Utilisation :**
```bash
python3 generate_wordpress_import.py
```

**Sortie :** Crée `wordpress_import.xml` compatible WordPress.

## ⚙️ Configuration

### Prérequis

```bash
pip install requests beautifulsoup4 html2text pyyaml
```

### Configuration WordPress

Modifier `wordpress_config.py` si nécessaire :

```python
WORDPRESS_URL = "https://bonpasteurcaen.wordpress.com"
AUTHOR_INFO = {
    "login": "gnodet",
    "email": "gnodet@gmail.com",
    "display_name": "Guillaume Nodet"
}
```

## 📊 Format des fichiers

### Structure Markdown

Chaque fichier Markdown contient :

```yaml
---
title: Titre de la page
updated: '2025-09-16'
url: /url-wordpress/
---

Contenu de la page en Markdown...
```

### Mapping des URLs

Le mapping URL WordPress → fichier Markdown est défini dans `sync_wordpress_content.py` :

```python
URL_TO_FILE_MAPPING = {
    "/bapteme/": "bapteme.md",
    "/eglises/saint-etienne/": "eglises/saint-etienne.md",
    "/jeunes-12-17-ans/": "jeunesse/jeunes-12-17-ans.md",
    # ...
}
```

## 🔄 Workflow recommandé

### Synchronisation régulière

1. **Vérifier les modifications WordPress :**
   ```bash
   python3 analyze_new_pages.py
   ```

2. **Synchroniser le contenu :**
   ```bash
   python3 sync_future.py
   ```

3. **Réviser les changements :**
   ```bash
   git diff
   ```

4. **Commiter si nécessaire :**
   ```bash
   git add .
   git commit -m "Synchronisation WordPress - [date]"
   ```

### Ajout de nouvelles pages

1. **Identifier les nouvelles pages :**
   ```bash
   python3 analyze_new_pages.py
   ```

2. **Mettre à jour le mapping dans `sync_wordpress_content.py`**

3. **Relancer la synchronisation :**
   ```bash
   python3 sync_wordpress_content.py
   ```

## 🛠️ Dépannage

### Erreurs courantes

**Erreur de connexion :**
```bash
# Vérifier la connectivité
curl -I https://bonpasteurcaen.wordpress.com
```

**Pages manquantes :**
- Vérifier le sitemap : https://bonpasteurcaen.wordpress.com/sitemap.xml
- Ajouter le mapping dans `URL_TO_FILE_MAPPING`

**Conversion HTML défaillante :**
- Vérifier les sélecteurs CSS dans `extract_content_from_html()`
- Tester manuellement avec BeautifulSoup

### Logs et débogage

Activer le mode verbose en modifiant les scripts :

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📈 Statistiques actuelles

- **48 pages synchronisées**
- **25 églises et chapelles**
- **5 pages jeunesse**
- **3 pages d'informations pratiques**
- **Dernière synchronisation :** 16 septembre 2025

## 🔮 Améliorations futures

- [ ] Synchronisation bidirectionnelle automatique
- [ ] Détection des conflits de contenu
- [ ] Optimisation des images (téléchargement local)
- [ ] Webhook WordPress pour synchronisation en temps réel
- [ ] Interface web pour la gestion des mappings
- [ ] Tests automatisés des scripts

## 📞 Support

Pour toute question ou problème :
- Consulter les logs des scripts
- Vérifier la connectivité au site WordPress
- Examiner le fichier `SYNCHRONISATION_RAPPORT.md` pour les détails

---

**Dernière mise à jour :** 16 septembre 2025
