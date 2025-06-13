#!/bin/bash

echo "🏗️  Construction du site de la paroisse Bon Pasteur avec Quarkus Roq"

# Configuration du PATH pour Maven
export PATH=/opt/maven/bin:$PATH

# Vérification de Maven
if ! command -v mvn &> /dev/null; then
    echo "❌ Maven n'est pas installé ou pas dans le PATH."
    exit 1
fi

echo "📋 Versions utilisées :"
mvn -version | head -3

# Nettoyage et construction
echo "🧹 Nettoyage et construction..."
mvn clean package -DskipTests

if [ $? -eq 0 ]; then
    echo "✅ Site construit avec succès !"
    echo ""
    echo "📁 Fichiers générés :"
    echo "   - Application Quarkus : target/quarkus-app/"
    echo "   - JAR exécutable : target/bonpasteur-site-1.0.0-SNAPSHOT.jar"
    echo ""
    echo "🚀 Pour tester le site :"
    echo "   ./run.sh"
    echo ""
    echo "📊 Statistiques :"
    echo "   - Pages de contenu : $(find content -name "*.md" | wc -l)"
    echo "   - Classes Java : $(find src/main/java -name "*.java" | wc -l)"
else
    echo "❌ Erreur lors de la construction"
    exit 1
fi
