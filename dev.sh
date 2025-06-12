#!/bin/bash

echo "🚀 Démarrage du serveur de développement Quarkus Roq"
echo ""
echo "Le site sera accessible sur : http://localhost:8080"
echo "Les modifications seront rechargées automatiquement"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter le serveur"
echo ""

mvn quarkus:dev
