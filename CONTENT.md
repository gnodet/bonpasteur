# Guide de gestion du contenu

Ce guide explique comment ajouter et modifier le contenu du site de la paroisse Bon Pasteur.

## 📝 Ajouter une nouvelle page

### 1. Créer le fichier Markdown

Créez un nouveau fichier `.md` dans `src/main/resources/content/` :

```markdown
---
title: Titre de la page
subtitle: Sous-titre (optionnel)
description: Description pour le SEO
template: page
---

# Contenu de la page

Votre contenu en Markdown...
```

### 2. Métadonnées (Front Matter)

Les métadonnées en YAML au début du fichier définissent :

- `title` : Titre de la page (obligatoire)
- `subtitle` : Sous-titre affiché sous le titre
- `description` : Description pour le référencement
- `template` : Template à utiliser (`page`, `clocher`, `actualite`)
- `date` : Date (pour les actualités)
- `author` : Auteur (pour les actualités)

### 3. Templates disponibles

#### Template `page` (par défaut)
Pour les pages standard avec header et contenu.

#### Template `clocher`
Pour les pages de clochers avec informations structurées :

```yaml
---
title: Nom du clocher
template: clocher
adresse: |
  Adresse complète
  Code postal Ville
contact: |
  Téléphone : XX XX XX XX XX
  Email : email@example.com
horaires_messes:
  - jour: Dimanche
    heure: 10h30
    type: Messe dominicale
activites:
  - nom: Catéchèse
    icon: fa-child
    description: Description de l'activité
---
```

#### Template `actualite`
Pour les articles d'actualité avec partage social.

## 📁 Organisation des dossiers

```
src/main/resources/content/
├── index.md                    # Page d'accueil
├── bienvenue.md               # Pages principales
├── presentation.md
├── contact.md
├── horaires-messes.md
├── actualites.md              # Index des actualités
├── actualites/                # Articles d'actualité
│   └── mon-article.md
├── clochers/                  # Pages des clochers
│   ├── sainte-trinite.md
│   └── saint-pierre.md
├── demandes/                  # Pages de demandes
│   ├── bapteme.md
│   └── mariage.md
└── propositions/              # Pages des propositions
    ├── solidarite.md
    └── jeunes.md
```

## ✍️ Syntaxe Markdown

### Titres
```markdown
# Titre niveau 1
## Titre niveau 2
### Titre niveau 3
```

### Texte
```markdown
**Gras**
*Italique*
[Lien](https://example.com)
```

### Listes
```markdown
- Élément 1
- Élément 2

1. Élément numéroté 1
2. Élément numéroté 2
```

### Citations
```markdown
> Citation importante
```

### Code HTML
Vous pouvez inclure du HTML directement :

```html
<div class="alert">
    <strong>Important :</strong> Message important
</div>
```

## 🎨 Styles CSS personnalisés

Vous pouvez ajouter des styles CSS directement dans vos pages :

```html
<style>
.ma-classe {
    color: #3498db;
    padding: 1rem;
}
</style>
```

## 📋 Formulaires

Exemple de formulaire de contact :

```html
<form class="contact-form">
    <div class="form-group">
        <label for="nom">Nom *</label>
        <input type="text" id="nom" name="nom" required>
    </div>
    
    <div class="form-group">
        <label for="email">Email *</label>
        <input type="email" id="email" name="email" required>
    </div>
    
    <div class="form-group">
        <label for="message">Message *</label>
        <textarea id="message" name="message" required></textarea>
    </div>
    
    <button type="submit" class="submit-btn">Envoyer</button>
</form>
```

## 🖼️ Images

### Ajouter des images

1. Placez vos images dans `src/main/resources/static/images/`
2. Référencez-les dans vos pages :

```markdown
![Description](images/mon-image.jpg)
```

### Images avec styles
```html
<img src="/images/mon-image.jpg" alt="Description" class="img-responsive">
```

## 📅 Actualités

### Créer une actualité

1. Créez un fichier dans `src/main/resources/content/actualites/`
2. Utilisez le template `actualite`
3. Ajoutez les métadonnées date et author

```markdown
---
title: Mon actualité
date: 2024-12-15
author: Paroisse Bon Pasteur
template: actualite
---

Contenu de l'actualité...
```

### Mettre à jour l'index des actualités

Ajoutez votre actualité dans `src/main/resources/content/actualites.md`

## 🏗️ Génération du site

Après avoir modifié le contenu :

```bash
# Développement (rechargement automatique)
./dev.sh

# Génération du site statique
./build.sh
```

## 📊 Configuration du site

Modifiez `src/main/resources/data/site.yaml` pour :
- Informations générales du site
- Coordonnées de contact
- Liste des clochers
- Réseaux sociaux

## 🔧 Dépannage

### Page non générée
- Vérifiez la syntaxe YAML du front matter
- Assurez-vous que le template existe
- Consultez les logs de génération

### Styles non appliqués
- Vérifiez que les fichiers CSS sont dans `src/main/resources/static/css/`
- Rechargez le cache du navigateur

### Liens brisés
- Utilisez des chemins relatifs : `/ma-page` au lieu de `ma-page.html`
- Vérifiez l'arborescence des fichiers

## 📞 Support

Pour toute question sur la gestion du contenu, consultez la documentation Quarkus Roq ou contactez l'administrateur du site.
