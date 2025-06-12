#!/bin/bash

echo "🏗️  Construction du site de la paroisse Bon Pasteur avec Quarkus Roq"

# Vérification de Maven
if ! command -v mvn &> /dev/null; then
    echo "❌ Maven n'est pas installé. Veuillez installer Maven pour continuer."
    exit 1
fi

# Nettoyage des anciens builds
echo "🧹 Nettoyage des anciens builds..."
mvn clean

# Compilation et génération du site
echo "🔨 Compilation et génération du site statique..."
mvn compile quarkus:build

# Vérification que le site a été généré
if [ -d "target/roq-site" ]; then
    echo "✅ Site généré avec succès dans target/roq-site/"
    echo ""
    echo "📁 Structure générée :"
    find target/roq-site -type f -name "*.html" | head -10
    echo ""
    echo "🌐 Pour voir le site :"
    echo "   - Ouvrez target/roq-site/index.html dans votre navigateur"
    echo "   - Ou servez le dossier avec un serveur web local"
    echo ""
    echo "🚀 Pour déployer :"
    echo "   - Copiez le contenu de target/roq-site/ vers votre serveur web"
else
    echo "❌ Erreur lors de la génération du site"
    exit 1
fi
