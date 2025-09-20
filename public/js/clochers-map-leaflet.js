/**
 * Carte interactive des clochers de Caen avec Leaflet (OpenStreetMap)
 * Alternative gratuite à Google Maps
 */

// Données des clochers de Caen avec coordonnées GPS précises
const clochersData = [
    {
        name: "Église Saint-Pierre",
        address: "Place Saint-Pierre, 14000 Caen",
        lat: 49.18406053636972,
        lng: -0.36078675159326973,
        type: "église",
        description: "Monument historique gothique flamboyant (XIVe-XVe siècles)",
        url: "/saint-pierre/",
        horaires: "Messes en semaine : 18h30 (mardi-vendredi)"
    },
    {
        name: "Abbaye Saint-Étienne (Hommes)",
        address: "Esplanade Jean-Marie Louvel, 14000 Caen",
        lat: 49.181842211636834,
        lng: -0.3734582275947242,
        type: "abbaye",
        description: "Abbatiale fondée par Guillaume le Conquérant (1063)",
        url: "/saint-etienne/",
        horaires: "Messe dominicale : 11h00"
    },
    {
        name: "Église Saint-Julien",
        address: "Rue Saint-Julien, 14000 Caen",
        lat: 49.18956330803129,
        lng: -0.3688986414275461,
        type: "église",
        description: "Église paroissiale du centre-ville",
        url: "/saint-julien/",
        horaires: "Messe dominicale : 11h00"
    },
    {
        name: "Abbatiale Sainte-Trinité (Dames)",
        address: "Place Reine Mathilde, 14000 Caen",
        lat: 49.18655030895399,
        lng: -0.35318209814533974,
        type: "abbaye",
        description: "Abbatiale fondée par la reine Mathilde (1062)",
        url: "/sainte-trinite-saint-gilles/",
        horaires: "Messe dominicale : 9h30"
    },
    {
        name: "Église Saint-Joseph",
        address: "Avenue du Chemin Vert, 14000 Caen",
        lat: 49.19262941973663, 
        lng: -0.39045399328054814,
        type: "église",
        description: "Église moderne du quartier Chemin Vert",
        url: "/saint-joseph-chemin-vert/",
        horaires: "Messe dominicale : 9h30"
    },
    {
        name: "Église Saint-Sauveur",
        address: "Place Saint-Sauveur, 14000 Caen",
        lat: 49.1831371368633, 
        lng: -0.364770702244062,
        type: "église",
        description: "Église historique du Vieux-Caen",
        url: "/saint-sauveur/",
        horaires: "Consulter les horaires"
    },
    {
        name: "Monastère de la Visitation",
        address: "Rue de la Visitation, 14000 Caen",
        lat: 49.18119370742554, 
        lng: -0.3754013321606875,
        type: "chapelle",
        description: "Monastère de contemplation",
        url: "/monastere-visitation/",
        horaires: "Messe dominicale : 10h00"
    },
    {
        name: "Église Saint-Ouen",
        address: "Rue Saint-Ouen, 14000 Caen",
        lat: 49.1771212817479, 
        lng: -0.37685808711673996,
        type: "église",
        description: "Église paroissiale historique",
        url: "/saint-ouen/",
        horaires: "Consulter les horaires"
    }
];

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
    
    // Contenu du popup
    const popupContent = `
        <div class="clocher-info" style="max-width: 250px;">
            <h6 style="margin: 0 0 8px 0; color: #2c3e50;">${clocher.name}</h6>
            <p style="margin: 4px 0; color: #7f8c8d; font-size: 0.85em;">
                <i class="fas fa-map-marker-alt"></i> ${clocher.address}
            </p>
            <p style="margin: 8px 0; font-size: 0.85em;">${clocher.description}</p>
            <p style="margin: 4px 0; color: #27ae60; font-size: 0.8em;">
                <i class="fas fa-clock"></i> ${clocher.horaires}
            </p>
            <div style="margin-top: 10px;">
                <a href="${clocher.url}" class="btn btn-sm btn-primary" style="text-decoration: none; font-size: 0.8em;">
                    <i class="fas fa-info-circle"></i> En savoir plus
                </a>
            </div>
        </div>
    `;
    
    marker.bindPopup(popupContent);
    markers.push(marker);
}

// Fonction pour filtrer les marqueurs par type
function filterMarkersLeaflet(type) {
    markers.forEach((marker, index) => {
        const clocher = clochersData[index];
        
        if (type === 'all' || clocher.type === type) {
            map.addLayer(marker);
        } else {
            map.removeLayer(marker);
        }
    });
}

// Exposer les fonctions globalement
window.initClochersMapLeaflet = initClochersMapLeaflet;
window.filterMarkersLeaflet = filterMarkersLeaflet;
