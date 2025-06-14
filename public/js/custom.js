// Menu JavaScript pour améliorer l'expérience utilisateur
// Style inspiré de paroisses-saintmalo.fr avec hover dropdowns

document.addEventListener('DOMContentLoaded', function() {

    // Gestion du menu dropdown avec hover sur desktop
    const dropdownItems = document.querySelectorAll('.nav-item.dropdown');

    dropdownItems.forEach(function(item) {
        const dropdownMenu = item.querySelector('.dropdown-menu');
        const dropdownToggle = item.querySelector('.dropdown-toggle');

        if (dropdownMenu && dropdownToggle) {

            // Desktop: Hover behavior (CSS handles the display, JS prevents Bootstrap interference)
            if (window.innerWidth > 991) {
                dropdownToggle.addEventListener('click', function(e) {
                    e.preventDefault(); // Prevent Bootstrap click behavior on desktop
                });

                // Ensure hover works properly
                item.addEventListener('mouseenter', function() {
                    dropdownMenu.classList.add('show');
                });

                item.addEventListener('mouseleave', function() {
                    dropdownMenu.classList.remove('show');
                });
            }

            // Mobile: Click behavior
            dropdownToggle.addEventListener('click', function(e) {
                if (window.innerWidth <= 991) {
                    e.preventDefault();

                    // Toggle this dropdown
                    const isOpen = dropdownMenu.classList.contains('show');

                    // Close all dropdowns first
                    document.querySelectorAll('.dropdown-menu').forEach(menu => {
                        menu.classList.remove('show');
                    });

                    // Open this one if it wasn't open
                    if (!isOpen) {
                        dropdownMenu.classList.add('show');
                    }
                }
            });
        }
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.dropdown')) {
            document.querySelectorAll('.dropdown-menu').forEach(menu => {
                menu.classList.remove('show');
            });
        }
    });

    // Handle window resize
    window.addEventListener('resize', function() {
        if (window.innerWidth > 991) {
            // Desktop mode: remove all show classes, let CSS handle hover
            document.querySelectorAll('.dropdown-menu').forEach(menu => {
                menu.classList.remove('show');
            });
        }
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Search functionality (if search form exists)
    const searchForm = document.querySelector('form[role="search"]');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const searchInput = this.querySelector('input[type="search"]');
            const searchTerm = searchInput.value.trim();
            
            if (searchTerm) {
                // Redirect to search page with query parameter
                window.location.href = '/recherche?q=' + encodeURIComponent(searchTerm);
            }
        });
    }

    // Add active class to current page navigation
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // Enhance cards with hover effects
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

});
