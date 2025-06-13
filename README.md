# Site Web de la Paroisse Bon Pasteur

Site web statique généré avec **Quarkus Roq** pour la paroisse Bon Pasteur.

## 🚀 Démarrage rapide

### Prérequis
- Java 21
- Maven 3.9.9 (installé dans `/opt/maven/`)

### Construction et test
```bash
# Construire le site
./build.sh

# Tester le site localement
./run.sh
```

Le site sera accessible sur http://localhost:8080

## 🏗️ Architecture

Ce projet utilise **Quarkus Roq**, un générateur de sites statiques moderne qui combine :
- **Contenu Markdown** : Pages écrites en Markdown avec métadonnées YAML
- **Thème par défaut** : Interface utilisateur responsive
- **Beans CDI** : Menu et auteurs configurés en Java
- **Génération statique** : Site optimisé pour la production

## 📁 Structure du projet

```
├── pom.xml                           # Configuration Maven avec Quarkus 3.23.3
├── build.sh                         # Script de construction
├── run.sh                           # Script de test local
├── content/                         # Contenu Markdown
│   ├── index.md                     # Page d'accueil
│   ├── presentation.md              # Présentation de la paroisse
│   ├── contact.md                   # Page de contact
│   ├── posts/                       # Articles/actualités
│   │   └── bienvenue.md
│   ├── clochers/                    # Pages des clochers
│   │   └── sainte-trinite.md
│   ├── demandes/                    # Pages de demandes
│   │   └── bapteme.md
│   └── propositions/                # Pages des propositions
│       └── solidarite.md
├── src/main/java/fr/paroisse/bonpasteur/
│   ├── Menu.java                    # Configuration du menu
│   └── Authors.java                 # Configuration des auteurs
└── target/                          # Fichiers générés
    └── quarkus-app/                 # Application Quarkus
```

## 📄 Pages créées

### ✅ Pages principales
- **Accueil** (`content/index.md`) : Page d'accueil avec présentation
- **Présentation** (`content/presentation.md`) : Histoire et mission de la paroisse
- **Contact** (`content/contact.md`) : Coordonnées et informations de contact

### ✅ Clochers
- **Sainte Trinité** (`content/clochers/sainte-trinite.md`) : Exemple de clocher avec horaires et activités

### ✅ Demandes
- **Baptême** (`content/demandes/bapteme.md`) : Informations et démarches pour le baptême

### ✅ Propositions
- **Solidarité** (`content/propositions/solidarite.md`) : Actions de solidarité et bénévolat

### ✅ Actualités
- **Bienvenue** (`content/posts/bienvenue.md`) : Article d'exemple

## 🎨 Fonctionnalités

- **Design responsive** : Compatible mobile et desktop
- **Navigation structurée** : Menu avec sous-menus pour les 23 clochers
- **Thème moderne** : Interface utilisateur propre et accessible
- **Contenu en Markdown** : Facile à éditer et maintenir
- **SEO optimisé** : Métadonnées automatiques

## 🛠️ Commandes utiles

```bash
# Construction complète
./build.sh

# Test local (30 secondes)
./run.sh

# Construction Maven directe
export PATH=/opt/maven/bin:$PATH
mvn clean package -DskipTests

# Exécution Maven directe
mvn quarkus:run
```

## 📚 Technologies utilisées

- **Quarkus 3.23.3** : Framework Java moderne
- **Roq 1.6.1** : Générateur de sites statiques
- **Thème par défaut Roq** : Interface utilisateur responsive
- **Java 21** : Langage de programmation
- **Maven 3.9.9** : Gestionnaire de dépendances

## 🔧 Personnalisation

### Ajouter une nouvelle page
1. Créez un fichier `.md` dans le répertoire `content/`
2. Ajoutez les métadonnées YAML en en-tête
3. Reconstruisez avec `./build.sh`

### Modifier le menu
Éditez `src/main/java/fr/paroisse/bonpasteur/Menu.java`

### Ajouter un clocher
1. Créez `content/clochers/nom-clocher.md`
2. Ajoutez le lien dans `Menu.java`

## 🎯 Avantages de Quarkus Roq

- **Performance** : Site statique ultra-rapide
- **Sécurité** : Pas de base de données, pas de failles
- **Maintenance** : Contenu en Markdown, facile à éditer
- **Évolutivité** : Peut être étendu avec Java si nécessaire
- **Déploiement** : Compatible avec tous les hébergeurs

## 📞 Support

- **Documentation Roq** : https://iamroq.com/docs/
- **Documentation Quarkus** : https://quarkus.io/guides/

---

*Site développé avec ❤️ pour la Paroisse Bon Pasteur - 2025*  
*Propulsé par Quarkus Roq 1.6.1*
