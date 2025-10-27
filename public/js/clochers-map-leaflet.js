/**
 * Carte interactive des clochers de Caen avec Leaflet (OpenStreetMap)
 * Alternative gratuite à Google Maps
 */

// Données des clochers de Caen avec coordonnées GPS précises
let clochersData = window.CLOCHERS;

// Icônes personnalisées pour Leaflet
const icons = {
    église: L.divIcon({
        html: `<div style="background: #8B4513; border: 2px solid #654321; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center;">
                <i class="fas fa-cross" style="color: white; font-size: 14px;"></i>
               </div>`,
        className: 'custom-div-icon',
        iconSize: [32, 32],
        iconAnchor: [16, 16]
    }),
    abbaye: L.divIcon({
        html: `<div style="background: #4A5568; border: 2px solid #2D3748; border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center;">
                <i class="fas fa-university" style="color: white; font-size: 16px;"></i>
               </div>`,
        className: 'custom-div-icon',
        iconSize: [36, 36],
        iconAnchor: [18, 18]
    }),
    chapelle: L.divIcon({
        html: `<div style="background: #6B46C1; border: 2px solid #553C9A; border-radius: 50%; width: 28px; height: 28px; display: flex; align-items: center; justify-content: center;">
                <i class="fas fa-praying-hands" style="color: white; font-size: 12px;"></i>
               </div>`,
        className: 'custom-div-icon',
        iconSize: [28, 28],
        iconAnchor: [14, 14]
    })
};

let map;
let markers = [];

// Initialisation de la carte Leaflet
function initClochersMapLeaflet() {
    // Créer la carte
    map = L.map('clochers-map').setView([49.1829, -0.3707], 13);

    // Ajouter les tuiles OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Ajouter les marqueurs
    clochersData.forEach(clocher => {
        addMarkerLeaflet(clocher);
    });

    // Ajuster la vue pour inclure tous les marqueurs
    if (markers.length > 0) {
        const group = new L.featureGroup(markers);
        map.fitBounds(group.getBounds().pad(0.1));
    }
}

// Ajouter un marqueur Leaflet
function addMarkerLeaflet(clocher) {
    const marker = L.marker([clocher.lat, clocher.lng], {
        icon: icons[clocher.type] || icons.église
    }).addTo(map);

    // Contenu du popup (masque les champs non fournis)
    const addressHtml = clocher.address ? `
            <p style="margin: 4px 0; color: #7f8c8d; font-size: 0.85em;">
                <i class="fas fa-map-marker-alt"></i> ${clocher.address}
            </p>` : '';
    const descHtml = clocher.description ? `
            <p style="margin: 8px 0; font-size: 0.85em;">${clocher.description}</p>` : '';
    const horairesHtml = clocher.horaires ? `
            <p style="margin: 4px 0; color: #27ae60; font-size: 0.8em;">
                <i class="fas fa-clock"></i> ${clocher.horaires}
            </p>` : '';

    const popupContent = `
        <div class="clocher-info" style="max-width: 250px;">
            <h6 style="margin: 0 0 8px 0; color: #2c3e50;">${clocher.name}</h6>
            ${addressHtml}
            ${descHtml}
            ${horairesHtml}
            <div style="margin-top: 10px;">
                <a href="../eglises/${clocher.url}" class="btn btn-sm btn-primary" style="text-decoration: none; font-size: 0.8em;">
                    <i class="fas fa-info-circle"></i> En savoir plus
                </a>
            </div>
        </div>
    `;

    // Afficher le popup au hover (mouseover) et le fermer au mouseleave
    marker.bindPopup(popupContent);

    let popupTimeout;
    let isPopupHovered = false;

    marker.on('mouseover', function() {
        clearTimeout(popupTimeout);
        this.openPopup();
    });

    marker.on('mouseout', function() {
        const popup = this.getPopup();
        if (popup && !isPopupHovered) {
            popupTimeout = setTimeout(() => {
                this.closePopup();
            }, 100);
        }
    });

    // Garder aussi le click pour ouvrir/fermer le popup
    marker.on('click', function() {
        clearTimeout(popupTimeout);
        if (this.isPopupOpen()) {
            this.closePopup();
        } else {
            this.openPopup();
        }
    });

    // Ajouter des événements au popup pour le garder ouvert au hover
    marker.on('popupopen', function() {
        const popup = this.getPopup();
        if (popup && popup._contentNode) {
            const popupElement = popup._contentNode.closest('.leaflet-popup');
            if (popupElement) {
                popupElement.addEventListener('mouseenter', function() {
                    isPopupHovered = true;
                    clearTimeout(popupTimeout);
                });

                popupElement.addEventListener('mouseleave', function() {
                    isPopupHovered = false;
                    popupTimeout = setTimeout(() => {
                        marker.closePopup();
                    }, 100);
                });
            }
        }
    });

    markers.push(marker);
}

// Filtres combinés par type et par usage
let currentTypeFilter = 'all';
let currentUsageFilter = 'all';

function applyFiltersLeaflet() {
    markers.forEach((marker, index) => {
        const clocher = clochersData[index];
        const typeOk = currentTypeFilter === 'all' || clocher.type === currentTypeFilter;
        const usageOk = currentUsageFilter === 'all' || clocher.usage === currentUsageFilter;
        if (typeOk && usageOk) {
            map.addLayer(marker);
        } else {
            map.removeLayer(marker);
        }
    });
}

// Filtre par type (API existante)
function filterMarkersLeaflet(type) {
    currentTypeFilter = type || 'all';
    applyFiltersLeaflet();
}

// Nouveau filtre par usage (permanente | occasionnelle | rare | all)
function filterMarkersByUsageLeaflet(usage) {
    currentUsageFilter = usage || 'all';
    applyFiltersLeaflet();
}

// Exposer les fonctions globalement
window.initClochersMapLeaflet = initClochersMapLeaflet;
window.filterMarkersLeaflet = filterMarkersLeaflet;
window.filterMarkersByUsageLeaflet = filterMarkersByUsageLeaflet;
