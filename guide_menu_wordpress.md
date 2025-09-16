# Guide de configuration des menus WordPress

## 🎯 Étapes de base

### 1. Accéder aux menus
1. **Connectez-vous** à l'administration WordPress : `http://localhost:8080/wp-admin`
2. Dans le menu de gauche, allez dans **Apparence > Menus**
3. Ou utilisez le **Customizer** : **Apparence > Personnaliser > Menus**

### 2. Créer un nouveau menu
1. Cliquez sur **"Créer un nouveau menu"**
2. Donnez un **nom** au menu (ex: "Menu principal")
3. Cliquez sur **"Créer le menu"**

### 3. Ajouter des éléments au menu

#### Pages
- Cochez les pages que vous voulez ajouter
- Cliquez sur **"Ajouter au menu"**

#### Liens personnalisés
- **URL** : `http://localhost:8080/ma-page/`
- **Texte du lien** : "Ma Page"
- Cliquez sur **"Ajouter au menu"**

#### Catégories
- Sélectionnez les catégories à ajouter
- Cliquez sur **"Ajouter au menu"**

### 4. Organiser le menu

#### Créer des sous-menus
- **Glissez-déposez** un élément vers la droite sous un autre
- L'indentation indique la hiérarchie

#### Réorganiser
- **Glissez-déposez** pour changer l'ordre
- Utilisez les **flèches** pour déplacer

### 5. Assigner le menu à un emplacement
1. Dans **"Réglages du menu"** (en bas)
2. Cochez l'emplacement souhaité :
   - **Menu principal**
   - **Menu pied de page**
   - **Menu mobile** (selon le thème)
3. Cliquez sur **"Enregistrer le menu"**

## 🎨 Configuration avancée

### Mega Menu (avec plugin)

#### Installation du plugin Max Mega Menu
```bash
# Via l'admin WordPress
Plugins > Ajouter > Rechercher "Max Mega Menu"
```

#### Configuration
1. **Mega Menu > Menu Locations**
2. Activez le mega menu pour votre emplacement
3. **Mega Menu > Menu Themes** pour personnaliser l'apparence

### Menu responsive

#### Options du thème
- **Apparence > Personnaliser > Menu**
- Configurez le **point de rupture mobile**
- Choisissez le **style du bouton hamburger**

## 📋 Structure recommandée pour une paroisse

### Menu principal
```
Accueil
Découvrir
├── Bienvenue
├── Qui sommes-nous
├── Histoire
Églises (MEGA MENU)
├── Colonne 1:
│   ├── Saint-Étienne
│   ├── Saint-Pierre
│   ├── Saint-Paul
├── Colonne 2:
│   ├── Saint-Jean
│   ├── Sainte-Marie
│   ├── Notre-Dame
Sacrements
├── Baptême
├── Mariage
├── Confirmation
├── Obsèques
Vie paroissiale
├── Horaires des messes
├── Groupes
├── Jeunes
├── Catéchèse
Actualités
Contact
```

## 🛠️ Code CSS pour personnaliser

### Menu horizontal simple
```css
/* Menu principal */
.main-navigation {
    background: #fff;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.main-navigation ul {
    display: flex;
    list-style: none;
    margin: 0;
    padding: 0;
}

.main-navigation li {
    position: relative;
}

.main-navigation a {
    display: block;
    padding: 15px 20px;
    text-decoration: none;
    color: #333;
    transition: background 0.3s;
}

.main-navigation a:hover {
    background: #f0f0f0;
    color: #0073aa;
}

/* Sous-menus */
.main-navigation ul ul {
    position: absolute;
    top: 100%;
    left: 0;
    background: #fff;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    min-width: 200px;
    opacity: 0;
    visibility: hidden;
    transform: translateY(-10px);
    transition: all 0.3s;
}

.main-navigation li:hover > ul {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

/* Menu mobile */
@media (max-width: 768px) {
    .main-navigation ul {
        flex-direction: column;
        display: none;
    }
    
    .main-navigation.active ul {
        display: flex;
    }
    
    .menu-toggle {
        display: block;
        background: none;
        border: none;
        font-size: 18px;
        padding: 15px;
    }
}
```

### Mega menu CSS
```css
/* Mega menu pour les églises */
.mega-menu {
    position: static !important;
}

.mega-menu .sub-menu {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    padding: 20px;
    background: #fff;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    max-width: 1200px;
    margin: 0 auto;
}

.mega-menu .sub-menu li {
    margin: 0;
}

.mega-menu .sub-menu a {
    padding: 10px 0;
    border-bottom: 1px solid #eee;
}
```

## 📱 Configuration mobile

### Bouton hamburger
```php
// Dans functions.php
function add_menu_toggle_button() {
    ?>
    <button class="menu-toggle" aria-controls="primary-menu" aria-expanded="false">
        <span class="hamburger-line"></span>
        <span class="hamburger-line"></span>
        <span class="hamburger-line"></span>
    </button>
    <?php
}
```

### JavaScript pour le menu mobile
```javascript
// Menu mobile toggle
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navigation = document.querySelector('.main-navigation');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            navigation.classList.toggle('active');
            const expanded = menuToggle.getAttribute('aria-expanded') === 'true';
            menuToggle.setAttribute('aria-expanded', !expanded);
        });
    }
});
```

## 🎯 Bonnes pratiques

### Structure
- **Maximum 7 éléments** dans le menu principal
- **Hiérarchie claire** avec sous-menus logiques
- **Noms courts** et explicites

### Accessibilité
- Utilisez les **attributs ARIA**
- **Navigation au clavier** fonctionnelle
- **Contrastes** suffisants

### SEO
- **URLs descriptives** pour les liens
- **Structure logique** pour les moteurs de recherche
- **Fil d'Ariane** pour la navigation

## 🔧 Plugins recommandés

### Gratuits
- **Max Mega Menu** - Mega menus avancés
- **Responsive Menu** - Menu mobile personnalisable
- **WP Mobile Menu** - Menu mobile avec animations

### Premium
- **UberMenu** - Menu avancé très personnalisable
- **Hero Menu** - Menu avec effets visuels
- **Elementor Pro** - Constructor de menus visuels

## 📊 Test et optimisation

### Points à vérifier
- ✅ **Responsive** sur tous les appareils
- ✅ **Vitesse** de chargement
- ✅ **Accessibilité** (WCAG)
- ✅ **Navigation intuitive**
- ✅ **Compatibilité** navigateurs

### Outils de test
- **Google PageSpeed Insights**
- **GTmetrix**
- **WAVE Web Accessibility Evaluator**
- **BrowserStack** pour les tests multi-navigateurs
