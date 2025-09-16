# Rapport de Synchronisation WordPress → GitHub

**Date de synchronisation :** 16 septembre 2025  
**Site WordPress :** https://bonpasteurcaen.wordpress.com  
**Repository GitHub :** https://github.com/gnodet/bonpasteur

## Résumé

La synchronisation a été effectuée avec succès, récupérant le contenu de **48 pages** du site WordPress et les intégrant dans le repository GitHub sous forme de fichiers Markdown avec front matter YAML.

## Statistiques

- **📝 12 nouveaux fichiers créés**
- **🔄 36 fichiers mis à jour**
- **📄 48 pages synchronisées au total**
- **🏛️ 25 églises et chapelles documentées**
- **👥 5 pages dédiées à la jeunesse**
- **ℹ️ 3 pages d'informations pratiques**

## Structure des fichiers créés

### Nouveaux fichiers créés

1. **Pages principales**
   - `content/rejoindre-un-groupe.md`
   - `content/malades-et-aines.md`
   - `content/se-confesser.md`
   - `content/rencontrer-un-pretre.md`
   - `content/monastere-visitation.md`
   - `content/carmel-de-caen.md`

2. **Jeunesse** (nouveau répertoire `content/jeunesse/`)
   - `content/jeunesse/jeunes-12-17-ans.md`
   - `content/jeunesse/confirmation.md`
   - `content/jeunesse/confirmation-2.md`
   - `content/jeunesse/demander-la-confirmation.md`
   - `content/jeunesse/pole-jeunes-12-17-ans.md`

3. **Informations pratiques**
   - `content/infos/intentions-priere.md`

### Fichiers mis à jour

#### Pages principales
- `content/bienvenue.md`
- `content/presentation.md`
- `content/bapteme.md`
- `content/mariage.md`
- `content/obseques.md`
- `content/catechese.md`
- `content/catechese-2.md`
- `content/etudiants.md`
- `content/jeunes-pros.md`
- `content/grandir-dans-la-foi.md`
- `content/solidarite.md`
- `content/demande-de-certificat.md`
- `content/qui-sommes-nous.md`

#### Églises et chapelles (16 nouvelles)
- `content/eglises/sainte-claire-folie-couvrechef.md`
- `content/eglises/sainte-trinite-saint-gilles.md`
- `content/eglises/saint-joseph-chemin-vert.md`
- `content/eglises/saint-jean-baptiste.md`
- `content/eglises/saint-germain-blanche-herbe.md`
- `content/eglises/saint-gerbold-blainville.md`
- `content/eglises/saint-francois-herouville.md`
- `content/eglises/saint-clair-herouville.md`
- `content/eglises/saint-bernard-pierre-heuze.md`
- `content/eglises/saint-andre-calvaire-saint-pierre.md`
- `content/eglises/notre-dame-assomption-gloriette.md`
- `content/eglises/chapelle-chr.md`
- `content/eglises/chapelle-benedictines.md`
- `content/eglises/chapelle-oasis.md`
- Plus les églises existantes mises à jour

#### Informations pratiques
- `content/infos/messes-horaires.md`
- `content/infos/offrir-messe.md`

## Contenu récupéré

### Nouvelles sections identifiées

1. **Jeunesse et formation**
   - Catéchèse pour différents âges
   - Confirmation pour adultes et jeunes
   - Pôle jeunes 12-17 ans
   - Étudiants et jeunes professionnels

2. **Accompagnement spirituel**
   - Rencontrer un prêtre
   - Se confesser
   - Malades et aînés
   - Intentions de prière

3. **Lieux de culte étendus**
   - 16 nouvelles églises et chapelles
   - Monastères et carmels
   - Chapelles spécialisées (CHR, Bénédictines, Oasis)

4. **Vie communautaire**
   - Rejoindre un groupe
   - Solidarité et actions caritatives
   - Horaires des messes actualisés

## Format des fichiers

Tous les fichiers Markdown incluent :

```yaml
---
title: [Titre de la page]
updated: '2025-09-16'
url: [URL WordPress originale]
---
```

Suivi du contenu converti du HTML vers Markdown avec :
- Listes à puces correctement formatées (`<ul>/<li>`)
- Liens préservés
- Structure des titres (H2, H3, etc.)
- Images avec URLs complètes

## Scripts créés

1. **`sync_wordpress_content.py`** - Script principal de synchronisation
2. **`analyze_new_pages.py`** - Analyse et suggestion de mappings
3. **`nouvelles_pages_rapport.md`** - Rapport détaillé des nouvelles pages

## Prochaines étapes recommandées

1. **Révision du contenu** - Vérifier la qualité de la conversion HTML→Markdown
2. **Optimisation des images** - Télécharger les images localement si nécessaire
3. **Liens internes** - Vérifier et corriger les liens entre pages
4. **Automatisation** - Configurer une synchronisation périodique
5. **Tests** - Vérifier le rendu des pages dans l'environnement de développement

## Commandes utilisées

```bash
# Installation des dépendances
python3 -m pip install requests beautifulsoup4 html2text pyyaml

# Analyse des nouvelles pages
python3 analyze_new_pages.py

# Synchronisation complète
python3 sync_wordpress_content.py
```

## Conclusion

La synchronisation s'est déroulée avec succès. Le repository GitHub contient maintenant une copie complète et structurée du contenu du site WordPress, organisée de manière logique avec une hiérarchie claire (jeunesse, églises, infos, etc.).

Le contenu est prêt pour être utilisé dans un générateur de site statique ou pour toute autre utilisation nécessitant une version Markdown du site WordPress.
