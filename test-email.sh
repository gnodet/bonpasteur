#!/bin/bash

# Script de test pour le formulaire de contact
echo "🧪 Test du formulaire de contact..."

# Test de l'API
curl -X POST http://localhost:8080/api/contact \
  -H "Content-Type: application/json" \
  -d '{
    "nom": "Test Configuration",
    "email": "test@example.com",
    "sujet": "Test Gmail Configuration",
    "message": "Ceci est un test de configuration Gmail pour vérifier que les emails sont bien envoyés."
  }' \
  -w "\n\nCode de réponse: %{http_code}\n"

echo ""
echo "✅ Si vous voyez un code 200, l'email a été envoyé !"
echo "📧 Vérifiez votre boîte mail : contact.bonpasteur@gmail.com"
echo "📧 Et aussi : test@example.com (pour la confirmation)"
