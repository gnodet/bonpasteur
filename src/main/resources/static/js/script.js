// Script principal pour le site de la paroisse

document.addEventListener('DOMContentLoaded', function() {
    // Gestion des menus déroulants
    initDropdownMenus();
    
    // Gestion de la recherche
    initSearch();
    
    // Gestion du menu mobile
    initMobileMenu();
    
    // Animation au scroll
    initScrollAnimations();
});

// Gestion des menus déroulants
function initDropdownMenus() {
    const dropdownItems = document.querySelectorAll('.nav-item.dropdown');
    
    dropdownItems.forEach(item => {
        const menu = item.querySelector('.dropdown-menu');
        let timeout;
        
        item.addEventListener('mouseenter', () => {
            clearTimeout(timeout);
            menu.style.opacity = '1';
            menu.style.visibility = 'visible';
            menu.style.transform = 'translateY(0)';
        });
        
        item.addEventListener('mouseleave', () => {
            timeout = setTimeout(() => {
                menu.style.opacity = '0';
                menu.style.visibility = 'hidden';
                menu.style.transform = 'translateY(-10px)';
            }, 150);
        });
    });
}

// Gestion de la recherche
function initSearch() {
    const searchInput = document.querySelector('.search-input');
    const searchBtn = document.querySelector('.search-btn');
    
    if (searchInput && searchBtn) {
        searchBtn.addEventListener('click', performSearch);
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                performSearch();
            }
        });
    }
}

function performSearch() {
    const searchInput = document.querySelector('.search-input');
    const query = searchInput.value.trim();
    
    if (query) {
        // Ici vous pouvez implémenter la logique de recherche
        // Pour l'instant, on simule une recherche simple
        console.log('Recherche pour:', query);
        
        // Exemple de recherche simple dans le contenu de la page
        highlightSearchResults(query);
    }
}

function highlightSearchResults(query) {
    // Supprime les anciens highlights
    removeHighlights();
    
    if (!query) return;
    
    const walker = document.createTreeWalker(
        document.body,
        NodeFilter.SHOW_TEXT,
        null,
        false
    );
    
    const textNodes = [];
    let node;
    
    while (node = walker.nextNode()) {
        textNodes.push(node);
    }
    
    textNodes.forEach(textNode => {
        const parent = textNode.parentNode;
        if (parent.tagName === 'SCRIPT' || parent.tagName === 'STYLE') return;
        
        const text = textNode.textContent;
        const regex = new RegExp(`(${query})`, 'gi');
        
        if (regex.test(text)) {
            const highlightedText = text.replace(regex, '<mark class="search-highlight">$1</mark>');
            const wrapper = document.createElement('span');
            wrapper.innerHTML = highlightedText;
            parent.replaceChild(wrapper, textNode);
        }
    });
}

function removeHighlights() {
    const highlights = document.querySelectorAll('.search-highlight');
    highlights.forEach(highlight => {
        const parent = highlight.parentNode;
        parent.replaceChild(document.createTextNode(highlight.textContent), highlight);
        parent.normalize();
    });
}

// Gestion du menu mobile
function initMobileMenu() {
    // Créer un bouton hamburger pour mobile si nécessaire
    if (window.innerWidth <= 768) {
        createMobileMenuButton();
    }
    
    window.addEventListener('resize', () => {
        if (window.innerWidth <= 768) {
            createMobileMenuButton();
        } else {
            removeMobileMenuButton();
        }
    });
}

function createMobileMenuButton() {
    const existingButton = document.querySelector('.mobile-menu-btn');
    if (existingButton) return;
    
    const nav = document.querySelector('.main-nav');
    const button = document.createElement('button');
    button.className = 'mobile-menu-btn';
    button.innerHTML = '<i class="fas fa-bars"></i>';
    button.style.cssText = `
        background: none;
        border: none;
        color: white;
        font-size: 1.5rem;
        cursor: pointer;
        padding: 0.5rem;
    `;
    
    nav.insertBefore(button, nav.firstChild);
    
    button.addEventListener('click', toggleMobileMenu);
}

function removeMobileMenuButton() {
    const button = document.querySelector('.mobile-menu-btn');
    if (button) {
        button.remove();
    }
}

function toggleMobileMenu() {
    const navMenu = document.querySelector('.nav-menu');
    const button = document.querySelector('.mobile-menu-btn');
    
    navMenu.classList.toggle('mobile-open');
    
    if (navMenu.classList.contains('mobile-open')) {
        navMenu.style.display = 'flex';
        button.innerHTML = '<i class="fas fa-times"></i>';
    } else {
        navMenu.style.display = 'none';
        button.innerHTML = '<i class="fas fa-bars"></i>';
    }
}

// Animations au scroll
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);
    
    // Observer les cartes de section
    const sectionCards = document.querySelectorAll('.section-card');
    sectionCards.forEach(card => {
        observer.observe(card);
    });
    
    // Observer les articles d'actualités
    const newsItems = document.querySelectorAll('.news-item');
    newsItems.forEach(item => {
        observer.observe(item);
    });
}

// Fonction utilitaire pour smooth scroll
function smoothScrollTo(target) {
    const element = document.querySelector(target);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Gestion des formulaires (pour les pages de demande)
function initForms() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Validation basique
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                } else {
                    field.classList.remove('error');
                }
            });
            
            if (isValid) {
                // Ici vous pouvez ajouter la logique d'envoi du formulaire
                showMessage('Votre demande a été envoyée avec succès!', 'success');
            } else {
                showMessage('Veuillez remplir tous les champs obligatoires.', 'error');
            }
        });
    });
}

// Affichage de messages
function showMessage(text, type = 'info') {
    const message = document.createElement('div');
    message.className = `message message-${type}`;
    message.textContent = text;
    message.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 2rem;
        border-radius: 5px;
        color: white;
        font-weight: 600;
        z-index: 10000;
        animation: slideIn 0.3s ease;
    `;
    
    switch(type) {
        case 'success':
            message.style.backgroundColor = '#27ae60';
            break;
        case 'error':
            message.style.backgroundColor = '#e74c3c';
            break;
        default:
            message.style.backgroundColor = '#3498db';
    }
    
    document.body.appendChild(message);
    
    setTimeout(() => {
        message.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            message.remove();
        }, 300);
    }, 3000);
}

// Styles CSS additionnels injectés via JavaScript
const additionalStyles = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
    
    .animate-in {
        animation: fadeInUp 0.6s ease forwards;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .search-highlight {
        background-color: #fff3cd;
        padding: 2px 4px;
        border-radius: 3px;
    }
    
    .error {
        border-color: #e74c3c !important;
        box-shadow: 0 0 5px rgba(231, 76, 60, 0.3) !important;
    }
    
    @media (max-width: 768px) {
        .nav-menu {
            display: none;
            flex-direction: column;
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: rgba(44, 62, 80, 0.95);
            padding: 1rem;
            border-radius: 0 0 10px 10px;
        }
        
        .nav-menu.mobile-open {
            display: flex !important;
        }
        
        .dropdown-menu {
            position: static !important;
            opacity: 1 !important;
            visibility: visible !important;
            transform: none !important;
            box-shadow: none !important;
            background: rgba(255,255,255,0.1) !important;
            margin-top: 0.5rem !important;
        }
    }
`;

// Injecter les styles additionnels
const styleSheet = document.createElement('style');
styleSheet.textContent = additionalStyles;
document.head.appendChild(styleSheet);
