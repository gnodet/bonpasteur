/**
 * Effet machine à écrire pour le titre hero
 */
class TypewriterEffect {
    constructor(element, options = {}) {
        this.element = element;
        this.text = element.textContent;
        this.speed = options.speed || 100; // ms par caractère
        this.delay = options.delay || 300; // délai avant démarrage
        this.cursor = options.cursor !== false; // afficher le curseur
        
        // Vider le texte initial
        this.element.textContent = '';
        this.element.style.borderRight = this.cursor ? '3px solid white' : 'none';
        
        // Démarrer l'animation
        setTimeout(() => this.start(), this.delay);
    }
    
    start() {
        let i = 0;
        const timer = setInterval(() => {
            this.element.textContent = this.text.slice(0, i + 1);
            i++;
            
            if (i >= this.text.length) {
                clearInterval(timer);
                // Faire clignoter le curseur quelques fois puis l'enlever
                if (this.cursor) {
                    setTimeout(() => {
                        this.element.style.borderRight = 'none';
                    }, 2000);
                }
            }
        }, this.speed);
    }
}

// Initialiser l'effet au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    // Seulement sur la page d'accueil
    if (document.body.getAttribute('data-layout') === 'paroisse/index') {
        const heroTitle = document.getElementById('hero-title');
        if (heroTitle) {
            new TypewriterEffect(heroTitle, {
                speed: 80,    // 80ms par caractère
                delay: 300,   // 300ms de délai
                cursor: true  // avec curseur clignotant
            });
        }
    }
});
