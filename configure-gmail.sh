#!/bin/bash

echo "=== Configuration Gmail pour Paroisse Bon Pasteur ==="
echo ""
echo "Étapes à suivre :"
echo "1. Allez sur https://myaccount.google.com/security"
echo "2. Activez la 'Validation en 2 étapes' si pas déjà fait"
echo "3. Allez sur https://myaccount.google.com/apppasswords"
echo "4. Créez un mot de passe d'application pour 'Mail'"
echo "5. Copiez le mot de passe généré (16 caractères)"
echo ""

read -p "Entrez l'email Gmail (contact.bonpasteur@gmail.com): " GMAIL_EMAIL
GMAIL_EMAIL=${GMAIL_EMAIL:-contact.bonpasteur@gmail.com}

read -s -p "Entrez le mot de passe d'application Gmail: " GMAIL_PASSWORD
echo ""

echo ""
echo "=== Configuration des variables d'environnement ==="

# Créer le fichier .env pour le développement
cat > .env << EOF
GMAIL_USERNAME=$GMAIL_EMAIL
GMAIL_PASSWORD=$GMAIL_PASSWORD
EOF

echo "✅ Fichier .env créé avec succès"
echo ""
echo "=== Test de la configuration ==="
echo "Vous pouvez maintenant tester l'envoi d'email via le formulaire de contact"
echo "URL: http://localhost:8080/infos/contact"
echo ""
echo "=== Redémarrage du serveur ==="
echo "Le serveur Quarkus va redémarrer pour prendre en compte les nouvelles variables"
