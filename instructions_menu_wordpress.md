
# 📋 Instructions pour créer le menu WordPress

## 1. Accéder aux menus
1. Allez dans **Apparence > Menus**
2. Cliquez sur **"Créer un nouveau menu"**
3. Nommez-le **"Menu Principal"**
4. Cliquez sur **"Créer le menu"**

## 2. Ajouter les éléments

### Structure recommandée:

**Accueil** (Lien personnalisé)
- URL: http://localhost:8080
- Texte: Accueil

**Découvrir** (Lien personnalisé - parent)
- URL: #
- Texte: Découvrir
  └── **Bienvenue** (Page existante - ID: 9)
  └── **Présentation** (⚠️ Page manquante - créer un lien personnalisé)
  └── **Qui sommes-nous** (⚠️ Page manquante - créer un lien personnalisé)

**Églises** (Lien personnalisé - parent)
- URL: #
- Texte: Églises
- ⚠️ Configurer comme MEGA MENU
  └── **Chapelle de l&rsquo;Oasis** (Page existante - ID: 36)
  └── **Chapelle de la Miséricorde** (Page existante - ID: 48)
  └── **Chapelle des Bénédictines** (Page existante - ID: 34)
  └── **Chapelle du CHR** (Page existante - ID: 29)
  └── **Les Églises** (Page existante - ID: 15)
  └── **Notre-Dame-de-l&rsquo;Assomption (la Gloriette)** (Page existante - ID: 37)

**Sacrements** (Lien personnalisé - parent)
- URL: #
- Texte: Sacrements
  └── **Baptême** (⚠️ Page manquante - créer un lien personnalisé)
  └── **Mariage** (⚠️ Page manquante - créer un lien personnalisé)
  └── **Confirmation** (Page existante - ID: 13)
  └── **Obsèques** (Page existante - ID: 17)

**Vie paroissiale** (Lien personnalisé - parent)
- URL: #
- Texte: Vie paroissiale
  └── **Horaires des messes** (Page existante - ID: 49)
  └── **Catéchèse** (⚠️ Page manquante - créer un lien personnalisé)
  └── **Jeunes** (⚠️ Page manquante - créer un lien personnalisé)
  └── **Rejoindre un groupe** (⚠️ Page manquante - créer un lien personnalisé)
  └── **Rencontrer un prêtre** (⚠️ Page manquante - créer un lien personnalisé)

**Services** (Lien personnalisé - parent)
- URL: #
- Texte: Services
  └── **Se confesser** (⚠️ Page manquante - créer un lien personnalisé)
  └── **Offrir une messe** (Page existante - ID: 14)
  └── **Intentions de prière** (Page existante - ID: 8)

**Contact** (⚠️ Page manquante)

## 3. Configuration des sous-menus
- **Glissez** les éléments enfants vers la **droite** sous leur parent
- L'**indentation** indique la hiérarchie

## 4. Mega Menu (pour "Églises")
Si vous utilisez un plugin de mega menu:
1. Activez le mega menu pour l'élément "Églises"
2. Configurez en **2 ou 3 colonnes**
3. Organisez les églises par zone géographique si possible

## 5. Assigner le menu
1. Dans **"Réglages du menu"** (en bas de page)
2. Cochez **"Menu principal"** ou **"Primary Menu"**
3. Cliquez sur **"Enregistrer le menu"**

## 6. Configuration responsive
- Vérifiez l'affichage sur mobile
- Configurez le bouton hamburger si nécessaire
- Testez la navigation tactile
