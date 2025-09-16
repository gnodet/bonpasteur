# Rapport - Architecture ROQ Corrigée

**Date :** 16 septembre 2025  
**Objectif :** Corriger l'architecture et utiliser correctement les templates ROQ

## ❌ Erreur Initiale

J'avais créé des fichiers HTML dans le mauvais répertoire :
- ❌ `partials/paroisse/index.html` (incorrect)
- ❌ `partials/paroisse/page.html` (incorrect)  
- ❌ `partials/paroisse/eglise.html` (incorrect)

## ✅ Architecture ROQ Correcte

### Structure des Templates ROQ
```
templates/
├── layouts/paroisse/          # Layouts spécialisés
│   ├── index.html            # Page d'accueil avec hero
│   ├── page.html             # Pages standard
│   └── 404.html              # Page d'erreur
└── partials/paroisse/         # Composants réutilisables
    └── layout.html           # Layout de base avec navigation
```

### Fichiers Modifiés

#### 1. `templates/layouts/paroisse/index.html`
**Rôle :** Layout spécialisé pour la page d'accueil avec section hero

**Contenu :**
- Section hero conditionnelle (`{#if page.hero_image}`)
- Boutons d'action flottants avec icônes
- Navigation secondaire optionnelle
- Fallback vers design Bootstrap si pas d'image hero
- Syntaxe ROQ native (`{page.title}`, `{#if}`, `{/if}`)

**Code clé :**
```html
{#include partials/paroisse/layout.html}
  {#insert content}
    {#if page.hero_image and page.hero_title}
    <section class="hero-section" role="banner">
        <div class="hero-image-container">
            <img src="{page.hero_image}" alt="Église {page.simple-name ?: page.name}" />
            <!-- ... hero content ... -->
        </div>
        <nav class="hero-buttons">
            <!-- ... 5 boutons d'action ... -->
        </nav>
    </section>
    {/if}
    <!-- ... contenu principal ... -->
  {/insert}
{/include}
```

#### 2. `templates/partials/paroisse/layout.html`
**Rôle :** Layout de base avec navigation, head, footer

**Améliorations ajoutées :**
- ✅ **Google Fonts** : Cardo (serif) + Inter (sans-serif)
- ✅ **CSS Hero** : Lien vers `/styles/hero.css`
- ✅ **CSS Main** : Lien vers `/styles/main.css`
- ✅ **Preload image** : Performance optimisée
- ✅ **Open Graph** : Métadonnées sociales
- ✅ **Twitter Card** : Partage optimisé
- ✅ **JavaScript** : Amélioration progressive

**Métadonnées ajoutées :**
```html
<!-- Open Graph -->
<meta property="og:title" content="{page.hero_title ?: page.title}">
<meta property="og:image" content="{page.hero_image}">

<!-- Preload -->
{#if page.hero_image}
<link rel="preload" as="image" href="{page.hero_image}">
{/if}

<!-- Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Cardo:wght@400;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
```

#### 3. `content/index.md`
**Rôle :** Contenu Markdown pur sans HTML

**Front Matter enrichi :**
```yaml
---
title: Paroisse Bon Pasteur de Caen
description: Découvrez notre communauté paroissiale, nos églises et nos activités.
layout: paroisse/index                    # ← Layout spécialisé
hero_image: https://bonpasteurcaen.files.wordpress.com/2024/12/img_20241201_113654.jpg
hero_title: Paroisse du Bon Pasteur de Caen
hero_subtitle: Communauté catholique de Caen et ses alentours
show_secondary_nav: true                   # ← Navigation secondaire
---
```

**Contenu :** Markdown pur, plus de HTML inline

## 🎯 Avantages de l'Architecture Correcte

### 1. **Séparation des Responsabilités**
- **Templates** : Structure et présentation
- **Content** : Contenu Markdown pur
- **Styles** : CSS séparés et modulaires

### 2. **Réutilisabilité ROQ**
- Layout de base réutilisé par tous les layouts spécialisés
- Composants modulaires dans `partials/`
- CSS partagés entre toutes les pages

### 3. **Performance Optimisée**
- Preload des images critiques
- Fonts optimisées avec `display=swap`
- CSS et JS minifiés par ROQ

### 4. **SEO et Accessibilité**
- Métadonnées Open Graph automatiques
- Schema.org intégré
- Attributs ARIA sur les boutons hero
- Support clavier natif

## 🛠️ Fonctionnalités ROQ Utilisées

### Syntaxe de Template
```html
{page.title}                    # Variable simple
{page.hero_title ?: page.title} # Opérateur ternaire
{#if page.hero_image}           # Condition
{#include partials/layout.html} # Inclusion
{#insert content}               # Insertion de contenu
```

### Front Matter Dynamique
```yaml
layout: paroisse/index          # Layout spécialisé
hero_image: [URL]               # Image conditionnelle
show_secondary_nav: true        # Feature toggle
```

### CSS et Assets
```html
<link href="{site.url}styles/hero.css" rel="stylesheet">
<img src="{page.hero_image}" alt="..." />
```

## 📊 Comparaison Avant/Après

| Aspect | ❌ Avant (Incorrect) | ✅ Après (ROQ) |
|--------|---------------------|----------------|
| **Architecture** | HTML dans `partials/` | Templates dans `layouts/` |
| **Contenu** | HTML inline dans `.md` | Markdown pur |
| **Réutilisabilité** | Fichiers dupliqués | Layout de base partagé |
| **Performance** | CSS inline | CSS externes optimisés |
| **Maintenance** | Code dispersé | Structure claire |
| **ROQ Compliance** | Non conforme | 100% conforme |

## 🚀 Résultat Final

### Page d'Accueil Moderne
- ✅ **Photo hero** 501px pleine largeur
- ✅ **Titre overlay** "Paroisse du Bon Pasteur de Caen"
- ✅ **5 boutons flottants** avec icônes
- ✅ **Design responsive** mobile/tablette/desktop
- ✅ **Navigation secondaire** avec 4 cartes

### Architecture ROQ Native
- ✅ **Templates** dans `templates/layouts/`
- ✅ **Partials** dans `templates/partials/`
- ✅ **Content** Markdown pur dans `content/`
- ✅ **Styles** CSS séparés dans `content/styles/`

### Performance et SEO
- ✅ **Preload** image hero
- ✅ **Open Graph** métadonnées
- ✅ **Twitter Card** support
- ✅ **Schema.org** données structurées
- ✅ **Accessibilité** ARIA et clavier

## 🔧 Instructions d'Utilisation

### Modifier le Hero
1. **Image :** Changer `hero_image` dans le front matter
2. **Titre :** Modifier `hero_title` et `hero_subtitle`
3. **Boutons :** Éditer le template `layouts/paroisse/index.html`

### Ajouter une Page
1. **Créer** `content/nouvelle-page.md`
2. **Front matter :** `layout: paroisse/page`
3. **Contenu :** Markdown pur

### Personnaliser le Style
1. **Hero :** Modifier `content/styles/hero.css`
2. **Global :** Modifier `content/styles/main.css`
3. **Bootstrap :** Surcharger dans `css/custom.css`

## 📝 Bonnes Pratiques ROQ

### 1. **Layouts Hiérarchiques**
```
layout.html (base)
  ├── index.html (accueil)
  ├── page.html (standard)
  └── eglise.html (spécialisé)
```

### 2. **Front Matter Structuré**
```yaml
# Métadonnées de base
title: [Titre]
description: [Description]
layout: paroisse/[type]

# Fonctionnalités spécifiques
hero_image: [URL]
show_secondary_nav: true
custom_css: [Chemin]
```

### 3. **CSS Modulaire**
```
styles/
├── main.css      # Styles de base
├── hero.css      # Section hero
└── components.css # Composants
```

## Conclusion

🎯 **Architecture ROQ correctement implémentée !**

Le design hero moderne est maintenant intégré dans l'architecture ROQ native :
- ✅ **Templates** dans le bon répertoire
- ✅ **Syntaxe ROQ** respectée
- ✅ **Performance** optimisée
- ✅ **Maintenance** facilitée
- ✅ **Évolutivité** assurée

La page d'accueil conserve son design moderne inspiré de Saint-Malo tout en respectant parfaitement les conventions ROQ ! 🚀
