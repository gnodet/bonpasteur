// Menu JavaScript pour améliorer l'expérience utilisateur
// Style inspiré de paroisses-saintmalo.fr

document.addEventListener('DOMContentLoaded', function() {

    // Gestion du menu dropdown
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
            }

            // Mobile: Click behavior
            dropdownToggle.addEventListener('click', function(e) {
                if (window.innerWidth <= 991) {
                    e.preventDefault();

                    // Toggle this dropdown
                    const isOpen = dropdownMenu.style.display === 'block';

                    // Close all dropdowns first
                    document.querySelectorAll('.dropdown-menu').forEach(menu => {
                        menu.style.display = 'none';
                    });

                    // Open this one if it wasn't open
                    if (!isOpen) {
                        dropdownMenu.style.display = 'block';
                    }
                }
            });
        }
    });

    // Gestion du redimensionnement de la fenêtre
    window.addEventListener('resize', function() {
        // Fermer tous les menus ouverts lors du redimensionnement
        dropdownItems.forEach(function(item) {
            const dropdownToggle = item.querySelector('.dropdown-toggle');
            if (dropdownToggle) {
                const bsDropdown = bootstrap.Dropdown.getInstance(dropdownToggle);
                if (bsDropdown) {
                    bsDropdown.hide();
                }
            }
        });
    });

    // Amélioration de l'accessibilité
    dropdownItems.forEach(function(item) {
        const dropdownToggle = item.querySelector('.dropdown-toggle');

        if (dropdownToggle) {
            // Navigation au clavier
            dropdownToggle.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    const bsDropdown = new bootstrap.Dropdown(dropdownToggle);
                    bsDropdown.toggle();
                }
            });
        }
    });
});
