# 🎯 Guide étape par étape : Configuration du menu WordPress

## 📋 Étape 1 : Accéder à l'interface des menus

### 1.1 Connexion à WordPress
1. Ouvrez votre navigateur
2. Allez sur : `http://localhost:8080/wp-admin`
3. Connectez-vous avec vos identifiants

### 1.2 Accéder aux menus
1. Dans le menu de gauche, cliquez sur **"Apparence"**
2. Cliquez sur **"Menus"**

## 🔧 Étape 2 : Créer un nouveau menu

### 2.1 Création
1. En haut de la page, cliquez sur **"Créer un nouveau menu"**
2. Dans le champ "Nom du menu", tapez : **"Menu Principal"**
3. Cliquez sur **"Créer le menu"**

### 2.2 Configuration de base
Vous verrez maintenant l'interface de construction du menu avec :
- **Colonne de gauche** : Pages, articles, liens disponibles
- **Colonne de droite** : Structure du menu en cours de création

## 📄 Étape 3 : Ajouter les éléments principaux

### 3.1 Ajouter "Accueil" (lien personnalisé)
1. Dans la colonne de gauche, cliquez sur **"Liens personnalisés"**
2. Remplissez :
   - **URL** : `http://localhost:8080`
   - **Texte du lien** : `Accueil`
3. Cliquez sur **"Ajouter au menu"**

### 3.2 Ajouter les pages existantes
1. Dans la colonne de gauche, cliquez sur **"Pages"**
2. Cochez les pages suivantes (si disponibles) :
   - ✅ Bienvenue
   - ✅ Confirmation
   - ✅ Obsèques
   - ✅ Horaires des messes
   - ✅ Offrir une messe
   - ✅ Intentions de prière
3. Cliquez sur **"Ajouter au menu"**

### 3.3 Ajouter les éléments parents (liens personnalisés)
Pour chaque section principale, ajoutez un lien personnalisé :

**Découvrir :**
- URL : `#`
- Texte : `Découvrir`

**Églises :**
- URL : `#`
- Texte : `Églises`

**Sacrements :**
- URL : `#`
- Texte : `Sacrements`

**Vie paroissiale :**
- URL : `#`
- Texte : `Vie paroissiale`

**Services :**
- URL : `#`
- Texte : `Services`

## 🏗️ Étape 4 : Organiser la hiérarchie

### 4.1 Créer les sous-menus
1. **Glissez-déposez** les éléments pour les organiser
2. **Décalez vers la droite** les éléments enfants sous leurs parents

**Structure finale :**
```
Accueil
Découvrir
├── Bienvenue
├── Présentation (à créer)
└── Qui sommes-nous (à créer)
Églises
├── Chapelle de l'Oasis
├── Chapelle de la Miséricorde
├── Chapelle des Bénédictines
├── Chapelle du CHR
├── Les Églises
└── Notre-Dame-de-l'Assomption
Sacrements
├── Baptême (à créer)
├── Mariage (à créer)
├── Confirmation
└── Obsèques
Vie paroissiale
├── Horaires des messes
├── Catéchèse (à créer)
├── Jeunes (à créer)
└── Rejoindre un groupe (à créer)
Services
├── Se confesser (à créer)
├── Offrir une messe
└── Intentions de prière
```

### 4.2 Techniques de glisser-déposer
- **Déplacer verticalement** : Change l'ordre
- **Déplacer horizontalement** : Change le niveau (parent/enfant)
- **Indentation** : Plus c'est décalé à droite, plus c'est un sous-élément

## ⚙️ Étape 5 : Configuration avancée

### 5.1 Assigner le menu à un emplacement
1. Descendez en bas de la page
2. Dans **"Réglages du menu"**, cochez :
   - **Menu principal** ou **Primary Menu**
   - **Menu d'en-tête** (selon votre thème)
3. Cliquez sur **"Enregistrer le menu"**

### 5.2 Options d'affichage (optionnel)
En haut de la page, cliquez sur **"Options de l'écran"** pour afficher :
- **Description des liens**
- **Classes CSS**
- **Relation de lien (XFN)**
- **Cible du lien**

## 🎨 Étape 6 : Configuration du Mega Menu (optionnel)

### 6.1 Installation d'un plugin Mega Menu
1. Allez dans **Extensions > Ajouter**
2. Recherchez **"Max Mega Menu"**
3. Installez et activez le plugin

### 6.2 Configuration du Mega Menu
1. Allez dans **Mega Menu > Menu Locations**
2. Activez le mega menu pour votre emplacement
3. Pour l'élément "Églises" :
   - Cliquez sur l'icône **"Mega Menu"**
   - Configurez en **2 ou 3 colonnes**
   - Organisez les églises par zone

## 📱 Étape 7 : Test et optimisation

### 7.1 Test desktop
1. Visitez votre site : `http://localhost:8080`
2. Vérifiez que le menu s'affiche correctement
3. Testez tous les liens

### 7.2 Test mobile
1. Redimensionnez votre navigateur
2. Vérifiez le menu hamburger
3. Testez la navigation tactile

### 7.3 Ajustements
Si nécessaire, retournez dans **Apparence > Menus** pour :
- Réorganiser les éléments
- Modifier les libellés
- Ajouter/supprimer des éléments

## 🔧 Étape 8 : Personnalisation CSS (optionnel)

### 8.1 Accéder au CSS personnalisé
1. Allez dans **Apparence > Personnaliser**
2. Cliquez sur **"CSS additionnel"**

### 8.2 CSS de base pour le menu
```css
/* Améliorer l'apparence du menu */
.main-navigation {
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.main-navigation a {
    transition: all 0.3s ease;
}

.main-navigation a:hover {
    color: #0073aa;
    background-color: #f8f9fa;
}

/* Mega menu pour les églises */
.mega-menu .sub-menu {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    padding: 20px;
}
```

## ✅ Checklist finale

- [ ] Menu créé et nommé "Menu Principal"
- [ ] Tous les éléments principaux ajoutés
- [ ] Hiérarchie organisée (parents/enfants)
- [ ] Menu assigné à l'emplacement principal
- [ ] Test sur desktop réussi
- [ ] Test sur mobile réussi
- [ ] Liens fonctionnels vérifiés
- [ ] Mega menu configuré (si souhaité)
- [ ] Apparence satisfaisante

## 🆘 Dépannage

### Problèmes courants

**Le menu ne s'affiche pas :**
- Vérifiez que le menu est assigné à un emplacement
- Vérifiez que votre thème supporte les menus

**Les sous-menus ne fonctionnent pas :**
- Vérifiez l'indentation dans l'interface
- Testez avec un thème par défaut

**Menu mobile cassé :**
- Vérifiez les CSS du thème
- Testez avec les plugins désactivés

**Pages manquantes :**
- Créez les pages manquantes
- Ou utilisez des liens personnalisés temporaires

## 📞 Ressources supplémentaires

- **Documentation WordPress** : https://wordpress.org/support/article/wordpress-menu-user-guide/
- **Plugin Max Mega Menu** : https://wordpress.org/plugins/megamenu/
- **Tutoriels vidéo** : Recherchez "WordPress menu tutorial" sur YouTube
