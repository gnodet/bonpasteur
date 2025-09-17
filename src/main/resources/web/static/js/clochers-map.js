/**
 * Carte interactive des clochers de Caen
 * Utilise Google Maps API pour afficher les églises et clochers
 */

// Données des clochers de Caen avec coordonnées GPS
const clochersData = [
    {
        name: "Église Saint-Pierre",
        address: "Place Saint-Pierre, 14000 Caen",
        lat: 49.1829,
        lng: -0.3707,
        type: "église",
        description: "Monument historique gothique flamboyant",
        url: "/saint-pierre/",
        horaires: "Messes en semaine : 18h30 (mardi-vendredi)"
    },
    {
        name: "Église Saint-Étienne (Abbaye aux Hommes)",
        address: "Esplanade Jean-Marie Louvel, 14000 Caen",
        lat: 49.1808,
        lng: -0.3751,
        type: "abbaye",
        description: "Abbatiale fondée par Guillaume le Conquérant",
        url: "/saint-etienne/",
        horaires: "Messe dominicale : 11h00"
    },
    {
        name: "Église Saint-Julien",
        address: "Rue Saint-Julien, 14000 Caen",
        lat: 49.1856,
        lng: -0.3689,
        type: "église",
        description: "Église paroissiale du centre-ville",
        url: "/saint-julien/",
        horaires: "Messe dominicale : 11h00"
    },
    {
        name: "Abbatiale Sainte-Trinité (Abbaye aux Dames)",
        address: "Place Reine Mathilde, 14000 Caen",
        lat: 49.1867,
        lng: -0.3634,
        type: "abbaye",
        description: "Abbatiale fondée par la reine Mathilde",
        url: "/sainte-trinite-saint-gilles/",
        horaires: "Messe dominicale : 9h30"
    },
    {
        name: "Église Saint-Joseph",
        address: "Avenue du Chemin Vert, 14000 Caen",
        lat: 49.1923,
        lng: -0.3456,
        type: "église",
        description: "Église moderne du quartier Chemin Vert",
        url: "/saint-joseph-chemin-vert/",
        horaires: "Messe dominicale : 9h30"
    },
    {
        name: "Église Saint-Paul",
        address: "Rue de la Folie, 14000 Caen",
        lat: 49.1745,
        lng: -0.3612,
        type: "église",
        description: "Église du quartier Saint-Paul",
        url: "/saint-paul/",
        horaires: "Consulter les horaires"
    },
    {
        name: "Église Saint-Sauveur",
        address: "Place Saint-Sauveur, 14000 Caen",
        lat: 49.1834,
        lng: -0.3745,
        type: "église",
        description: "Église historique du Vieux-Caen",
        url: "/saint-sauveur/",
        horaires: "Consulter les horaires"
    },
    {
        name: "Chapelle de la Visitation",
        address: "Rue de la Visitation, 14000 Caen",
        lat: 49.1812,
        lng: -0.3623,
        type: "chapelle",
        description: "Monastère de la Visitation",
        url: "/monastere-visitation/",
        horaires: "Messe dominicale : 10h00"
    }
];

// Configuration de la carte
const mapConfig = {
    center: { lat: 49.1829, lng: -0.3707 }, // Centre sur Saint-Pierre
    zoom: 13,
    styles: [
        {
            featureType: "poi.place_of_worship",
            elementType: "labels",
            stylers: [{ visibility: "on" }]
        }
    ]
};

// Icônes personnalisées pour différents types (initialisées après chargement de Google Maps)
let icons = {};

let map;
let markers = [];
let infoWindow;

// Initialiser les icônes après chargement de Google Maps
function initIcons() {
    icons = {
        église: {
            url: 'data:image/svg+xml;charset=UTF-8,' + encodeURIComponent(`
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="32" height="32">
                    <circle cx="12" cy="12" r="10" fill="#8B4513" stroke="#654321" stroke-width="2"/>
                    <path d="M12 4v4M8 8h8M10 12h4v6h-4z" stroke="white" stroke-width="2" fill="none"/>
                    <circle cx="12" cy="6" r="1" fill="white"/>
                </svg>
            `),
            scaledSize: new google.maps.Size(32, 32)
        },
        abbaye: {
            url: 'data:image/svg+xml;charset=UTF-8,' + encodeURIComponent(`
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="36" height="36">
                    <circle cx="12" cy="12" r="11" fill="#4A5568" stroke="#2D3748" stroke-width="2"/>
                    <path d="M12 3v5M7 8h10M9 13h6v7h-6z" stroke="white" stroke-width="2" fill="none"/>
                    <circle cx="12" cy="5.5" r="1.5" fill="white"/>
                    <rect x="10" y="15" width="4" height="3" fill="white"/>
                </svg>
            `),
            scaledSize: new google.maps.Size(36, 36)
        },
        chapelle: {
            url: 'data:image/svg+xml;charset=UTF-8,' + encodeURIComponent(`
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28">
                    <circle cx="12" cy="12" r="9" fill="#6B46C1" stroke="#553C9A" stroke-width="2"/>
                    <path d="M12 5v3M9 8h6M10 11h4v5h-4z" stroke="white" stroke-width="2" fill="none"/>
                    <circle cx="12" cy="6.5" r="0.8" fill="white"/>
                </svg>
            `),
            scaledSize: new google.maps.Size(28, 28)
        }
    };
}

// Initialisation de la carte
function initClochersMap() {
    // Initialiser les icônes
    initIcons();

    // Créer la carte
    map = new google.maps.Map(document.getElementById('clochers-map'), mapConfig);
    
    // Créer une seule InfoWindow réutilisable
    infoWindow = new google.maps.InfoWindow();
    
    // Ajouter les marqueurs
    clochersData.forEach(clocher => {
        addMarker(clocher);
    });
    
    // Ajuster la vue pour inclure tous les marqueurs
    if (markers.length > 0) {
        const bounds = new google.maps.LatLngBounds();
        markers.forEach(marker => bounds.extend(marker.getPosition()));
        map.fitBounds(bounds);
        
        // Limiter le zoom maximum
        google.maps.event.addListenerOnce(map, 'bounds_changed', function() {
            if (map.getZoom() > 14) {
                map.setZoom(14);
            }
        });
    }
}

// Ajouter un marqueur
function addMarker(clocher) {
    const marker = new google.maps.Marker({
        position: { lat: clocher.lat, lng: clocher.lng },
        map: map,
        title: clocher.name,
        icon: icons[clocher.type] || icons.église,
        animation: google.maps.Animation.DROP
    });
    
    // Contenu de l'InfoWindow
    const infoContent = `
        <div class="clocher-info" style="max-width: 300px;">
            <h5 style="margin: 0 0 8px 0; color: #2c3e50;">${clocher.name}</h5>
            <p style="margin: 4px 0; color: #7f8c8d; font-size: 0.9em;">
                <i class="fas fa-map-marker-alt"></i> ${clocher.address}
            </p>
            <p style="margin: 8px 0; font-size: 0.9em;">${clocher.description}</p>
            <p style="margin: 4px 0; color: #27ae60; font-size: 0.85em;">
                <i class="fas fa-clock"></i> ${clocher.horaires}
            </p>
            <div style="margin-top: 12px;">
                <a href="${clocher.url}" class="btn btn-sm btn-primary" style="text-decoration: none;">
                    <i class="fas fa-info-circle"></i> En savoir plus
                </a>
            </div>
        </div>
    `;
    
    // Événement click sur le marqueur
    marker.addListener('click', () => {
        infoWindow.setContent(infoContent);
        infoWindow.open(map, marker);
    });
    
    markers.push(marker);
}

// Fonction pour filtrer les marqueurs par type
function filterMarkers(type) {
    markers.forEach(marker => {
        const clocher = clochersData.find(c => 
            c.lat === marker.getPosition().lat() && 
            c.lng === marker.getPosition().lng()
        );
        
        if (type === 'all' || clocher.type === type) {
            marker.setVisible(true);
        } else {
            marker.setVisible(false);
        }
    });
}

// Initialiser quand Google Maps est chargé
window.initClochersMap = initClochersMap;
