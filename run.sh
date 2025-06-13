#!/bin/bash

echo "🚀 Démarrage du site de la paroisse Bon Pasteur"

# Configuration du PATH pour Maven
export PATH=/opt/maven/bin:$PATH

# Vérification que l'application est construite
if [ ! -f "target/quarkus-app/quarkus-run.jar" ]; then
    echo "❌ L'application n'est pas construite. Exécutez d'abord ./build.sh"
    exit 1
fi

echo "🌐 Le site sera accessible sur : http://localhost:8080"
echo "📄 Pages disponibles :"
echo "   - Accueil : http://localhost:8080/"
echo "   - Présentation : http://localhost:8080/presentation"
echo "   - Contact : http://localhost:8080/contact"
echo "   - Clocher exemple : http://localhost:8080/clochers/sainte-trinite"
echo "   - Baptême : http://localhost:8080/demandes/bapteme"
echo "   - Solidarité : http://localhost:8080/propositions/solidarite"
echo ""
echo "⏹️  Appuyez sur Ctrl+C pour arrêter le serveur"
echo ""

# Démarrage avec timeout pour éviter que ça tourne indéfiniment
timeout 30s mvn quarkus:run || echo "Application arrêtée"
