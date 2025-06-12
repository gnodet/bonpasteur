# Site Web de la Paroisse Bon Pasteur

Site web statique généré avec **Quarkus Roq** pour la paroisse Bon Pasteur, inspiré du site des paroisses de Saint-Malo.

## 🚀 Démarrage rapide

### Prérequis
- Java 17 ou supérieur
- Maven 3.8+

### Développement
```bash
# Démarrer le serveur de développement
./dev.sh

# Le site sera accessible sur http://localhost:8080
```

### Construction du site statique
```bash
# Générer le site statique
./build.sh

# Le site sera généré dans target/roq-site/
```

## 🏗️ Architecture

Ce projet utilise **Quarkus Roq**, un générateur de sites statiques moderne qui combine :
- **Contenu Markdown** : Pages écrites en Markdown avec métadonnées YAML
- **Templates Qute** : Templates HTML dynamiques
- **Génération statique** : Site HTML/CSS/JS optimisé pour la production

## 📁 Structure du projet

```
src/main/
├── java/                          # Code Java (optionnel)
├── resources/
│   ├── content/                   # Contenu Markdown
│   │   ├── index.md              # Page d'accueil
│   │   ├── bienvenue.md          # Page de bienvenue
│   │   ├── presentation.md       # Présentation de la paroisse
│   │   ├── contact.md            # Page de contact
│   │   ├── horaires-messes.md    # Horaires des messes
│   │   ├── clochers/             # Pages des clochers
│   │   │   └── sainte-trinite.md
│   │   └── demandes/             # Pages de demandes
│   │       └── bapteme.md
│   ├── templates/                # Templates HTML
│   │   ├── layout/
│   │   │   └── base.html         # Template de base
│   │   ├── index.html            # Template page d'accueil
│   │   ├── page.html             # Template page standard
│   │   └── clocher.html          # Template clocher
│   ├── static/                   # Ressources statiques
│   │   ├── css/styles.css        # Styles CSS
│   │   └── js/script.js          # JavaScript
│   ├── data/
│   │   └── site.yaml             # Configuration du site
│   └── application.properties    # Configuration Quarkus
├── build.sh                      # Script de build
├── dev.sh                        # Script de développement
└── pom.xml                       # Configuration Maven
```

## Structure du site

### Navigation principale

1. **Découvrir**
   - Bienvenue
   - Présentation de la paroisse

2. **Les Clochers** (23 lieux de culte)
   - Sainte Trinité / Saint-Gilles
   - Carmel de Caen
   - Chapelle de l'Oasis
   - Chapelle des Bénédictines
   - Chapelle de la Miséricorde
   - Chapelle du CHR
   - Monastère de la Visitation
   - Notre-Dame-de-l'Assomption (la Gloriette)
   - Saint-Clair d'Hérouville-Saint-Clair
   - Saint-François d'Hérouville-Saint-Clair
   - Saint-Gerbold de Blainville-sur-Orne
   - Saint-Germain de Saint-Germain-la-Blanche-Herbe
   - Saint-Joseph du chemin vert
   - Saint-Julien
   - Saint-Paul
   - Saint-André du Calvaire Saint-Pierre
   - Saint-Bernard de la Pierre-Heuzé
   - Saint-Étienne
   - Saint-Jean-Baptiste
   - Saint-Ouen
   - Saint-Pierre
   - Saint-Sauveur
   - Sainte-Claire de la Folie-Couvrechef

3. **Demandes**
   - Baptême
   - Catéchèse
   - Confirmation
   - Mariage
   - Obsèques
   - Rejoindre un groupe
   - Rencontrer un prêtre
   - Intentions de prière
   - Offrir une messe
   - Se confesser

4. **Propositions**
   - Enfance (0-11 ans)
   - Pôle Jeunes (11-17 ans)
   - Étudiants
   - Jeunes Pros
   - Familles
   - Solidarité
   - Malades et aînés
   - Rencontres bibliques

5. **Infos**
   - Messes (lieux et horaires)
   - Agenda
   - Actualités
   - Partitions / Carnet de chant
   - Contact

6. **Recherche**
   - Barre de recherche intégrée

## 📄 Pages créées avec Quarkus Roq

### ✅ Pages principales
- Page d'accueil (`src/main/resources/content/index.md`)
- Bienvenue (`src/main/resources/content/bienvenue.md`)
- Présentation (`src/main/resources/content/presentation.md`)
- Contact (`src/main/resources/content/contact.md`)
- Horaires des messes (`src/main/resources/content/horaires-messes.md`)

### ✅ Clochers
- Exemple : Sainte Trinité (`src/main/resources/content/clochers/sainte-trinite.md`)

### ✅ Demandes
- Baptême (`src/main/resources/content/demandes/bapteme.md`)

### ✅ Propositions
- Solidarité (`src/main/resources/content/propositions/solidarite.md`)

### ✅ Actualités
- Index (`src/main/resources/content/actualites.md`)
- Exemple : Noël 2024 (`src/main/resources/content/actualites/celebration-noel-2024.md`)

## 🛠️ Commandes utiles

```bash
# Développement avec rechargement automatique
./dev.sh

# Génération du site statique
./build.sh

# Déploiement (plusieurs options)
./deploy.sh
```

## 📚 Documentation

- **[Guide de contenu](CONTENT.md)** : Comment ajouter et modifier le contenu
- **[Quarkus Roq](https://docs.quarkiverse.io/quarkus-roq/)** : Documentation officielle

## 🚀 Avantages de Quarkus Roq

- **Performance** : Site statique ultra-rapide
- **SEO** : Optimisé pour le référencement
- **Sécurité** : Pas de base de données, pas de failles
- **Maintenance** : Contenu en Markdown, facile à éditer
- **Déploiement** : Compatible avec tous les hébergeurs

---

*Site développé avec ❤️ pour la Paroisse Bon Pasteur - 2024*
*Propulsé par Quarkus Roq*
