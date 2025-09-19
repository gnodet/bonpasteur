#!/bin/bash

echo "=== Test de l'API de contact ==="
echo ""

# Test avec des données valides
echo "📧 Test d'envoi d'un message de contact..."
echo ""

curl -X POST http://localhost:8080/api/contact \
  -H "Content-Type: application/json" \
  -d '{
    "nom": "Test Utilisateur",
    "email": "test@example.com", 
    "message": "Ceci est un message de test pour vérifier que le formulaire de contact fonctionne correctement."
  }' \
  -w "\n\nCode de réponse HTTP: %{http_code}\n" \
  -s

echo ""
echo "=== Résultats attendus ==="
echo "✅ Code 200 : Email envoyé avec succès"
echo "❌ Code 500 : Erreur de configuration Gmail"
echo "❌ Code 400 : Données invalides"
echo ""
echo "Si vous obtenez une erreur 500, vérifiez :"
echo "1. Les variables d'environnement Gmail"
echo "2. Le mot de passe d'application Gmail"
echo "3. Les logs du serveur Quarkus"
