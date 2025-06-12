#!/bin/bash

echo "🚀 Déploiement du site de la paroisse Bon Pasteur"

# Configuration
SITE_DIR="target/roq-site"
BACKUP_DIR="backup-$(date +%Y%m%d-%H%M%S)"

# Vérification des prérequis
if [ ! -d "$SITE_DIR" ]; then
    echo "❌ Le site n'a pas été généré. Exécutez d'abord ./build.sh"
    exit 1
fi

echo "📁 Site à déployer : $SITE_DIR"

# Options de déploiement
echo ""
echo "Choisissez votre méthode de déploiement :"
echo "1) Serveur FTP"
echo "2) Serveur SSH/SCP"
echo "3) GitHub Pages"
echo "4) Netlify"
echo "5) Copie locale"
echo ""
read -p "Votre choix (1-5) : " choice

case $choice in
    1)
        echo "🌐 Déploiement FTP"
        read -p "Serveur FTP : " ftp_server
        read -p "Utilisateur : " ftp_user
        read -p "Répertoire distant : " ftp_dir
        
        echo "Uploading via FTP..."
        # Exemple avec lftp (à adapter selon vos besoins)
        # lftp -c "open -u $ftp_user $ftp_server; mirror -R $SITE_DIR $ftp_dir"
        echo "⚠️  Configurez votre client FTP pour uploader le contenu de $SITE_DIR"
        ;;
        
    2)
        echo "🔐 Déploiement SSH/SCP"
        read -p "Serveur SSH : " ssh_server
        read -p "Utilisateur : " ssh_user
        read -p "Répertoire distant : " ssh_dir
        
        echo "Uploading via SCP..."
        scp -r "$SITE_DIR/*" "$ssh_user@$ssh_server:$ssh_dir/"
        ;;
        
    3)
        echo "📚 Déploiement GitHub Pages"
        if [ ! -d ".git" ]; then
            echo "❌ Ce n'est pas un repository Git"
            exit 1
        fi
        
        # Créer une branche gh-pages
        git checkout --orphan gh-pages 2>/dev/null || git checkout gh-pages
        
        # Nettoyer et copier le site
        git rm -rf . 2>/dev/null || true
        cp -r "$SITE_DIR"/* .
        
        # Commit et push
        git add .
        git commit -m "Deploy site - $(date)"
        git push origin gh-pages
        
        echo "✅ Site déployé sur GitHub Pages"
        echo "🌐 URL : https://$(git config --get remote.origin.url | sed 's/.*github.com[:/]\(.*\)\.git/\1/').github.io"
        ;;
        
    4)
        echo "⚡ Déploiement Netlify"
        if command -v netlify &> /dev/null; then
            netlify deploy --prod --dir="$SITE_DIR"
            echo "✅ Site déployé sur Netlify"
        else
            echo "❌ Netlify CLI non installé"
            echo "💡 Installez avec : npm install -g netlify-cli"
            echo "📁 Ou uploadez manuellement le dossier $SITE_DIR sur netlify.com"
        fi
        ;;
        
    5)
        echo "📂 Copie locale"
        read -p "Répertoire de destination : " dest_dir
        
        if [ -d "$dest_dir" ]; then
            echo "💾 Sauvegarde de l'existant..."
            mv "$dest_dir" "$BACKUP_DIR"
        fi
        
        echo "📋 Copie du site..."
        cp -r "$SITE_DIR" "$dest_dir"
        echo "✅ Site copié vers $dest_dir"
        ;;
        
    *)
        echo "❌ Choix invalide"
        exit 1
        ;;
esac

echo ""
echo "🎉 Déploiement terminé !"
echo ""
echo "📊 Statistiques du site :"
echo "   - Pages HTML : $(find $SITE_DIR -name "*.html" | wc -l)"
echo "   - Fichiers CSS : $(find $SITE_DIR -name "*.css" | wc -l)"
echo "   - Fichiers JS : $(find $SITE_DIR -name "*.js" | wc -l)"
echo "   - Images : $(find $SITE_DIR -name "*.jpg" -o -name "*.png" -o -name "*.gif" -o -name "*.svg" | wc -l)"
echo "   - Taille totale : $(du -sh $SITE_DIR | cut -f1)"
