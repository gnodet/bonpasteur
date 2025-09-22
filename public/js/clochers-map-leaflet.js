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
        url: "saint-pierre/",
        horaires: "Messes en semaine : 18h30 (mardi-vendredi)"
    },
    {
        name: "Abbaye Saint-Étienne (Hommes)",
        address: "Esplanade Jean-Marie Louvel, 14000 Caen",
        lat: 49.181842211636834,
        lng: -0.3734582275947242,
        type: "abbaye",
        description: "Abbatiale fondée par Guillaume le Conquérant (1063)",
        url: "saint-etienne/",
        horaires: "Messe dominicale : 11h00"
    },
    {
        name: "Église Saint-Julien",
        address: "Rue Saint-Julien, 14000 Caen",
        lat: 49.18956330803129,
        lng: -0.3688986414275461,
        type: "église",
        description: "Église paroissiale du centre-ville",
        url: "saint-julien/",
        horaires: "Messe dominicale : 11h00"
    },
    {
        name: "Abbatiale Sainte-Trinité (Dames)",
        address: "Place Reine Mathilde, 14000 Caen",
        lat: 49.18655030895399,
        lng: -0.35318209814533974,
        type: "abbaye",
        description: "Abbatiale fondée par la reine Mathilde (1062)",
        url: "sainte-trinite-saint-gilles/",
        horaires: "Messe dominicale : 9h30"
    },
    {
        name: "Église Saint-Joseph",
        address: "Avenue du Chemin Vert, 14000 Caen",
        lat: 49.19262941973663,
        lng: -0.39045399328054814,
        type: "église",
        description: "Église moderne du quartier Chemin Vert",
        url: "saint-joseph-chemin-vert/",
        horaires: "Messe dominicale : 9h30"
    },
    {
        name: "Église Saint-Sauveur",
        address: "Place Saint-Sauveur, 14000 Caen",
        lat: 49.1831371368633,
        lng: -0.364770702244062,
        type: "église",
        description: "Église historique du Vieux-Caen",
        url: "saint-sauveur/",
        horaires: "Consulter les horaires"
    },
    {
        name: "Monastère de la Visitation",
        address: "Rue de la Visitation, 14000 Caen",
        lat: 49.18119370742554,
        lng: -0.3754013321606875,
        type: "chapelle",
        description: "Monastère de contemplation",
        url: "monastere-visitation/",
        horaires: "Messe dominicale : 10h00"
    },
    {
        name: "Église Saint-Ouen",
        address: "Rue Saint-Ouen, 14000 Caen",
        lat: 49.1771212817479,
        lng: -0.37685808711673996,
        type: "église",
        description: "Église paroissiale historique",
        url: "saint-ouen/",
        horaires: "Consulter les horaires"
    },
    {
        name: "Chapelle des Bénédictines",
        address: "Rue du Petit Clos Saint-Marc, 14000 Caen",
        lat: 49.2103276,
        lng: -0.3744712,
        type: "chapelle",
        description: "Chapelle du monastère des Bénédictines",
        url: "chapelle-benedictines/",
        horaires: "Consulter la page"
    },
    {
        name: "Chapelle de la Miséricorde",
        address: "Rue Élie de Beaumont, 14000 Caen",
        lat: 49.1848879,
        lng: -0.3671658,
        type: "chapelle",
        description: "Chapelle historique de la Miséricorde",
        url: "chapelle-misericorde/",
        horaires: "Consulter la page"
    },
    {
        name: "Chapelle de l’Oasis",
        address: "18 Rue de l'Oratoire, 14000 Caen",
        lat: 49.1812100,
        lng: -0.3601837,
        type: "chapelle",
        description: "Chapelle de l’établissement L’Oasis",
        url: "chapelle-oasis/",
        horaires: "Consulter la page"
    },
    {
        name: "Carmel de Caen",
        address: "8 Rue du Clos Beaumois, 14000 Caen",
        lat: 49.1891283,
        lng: -0.3515156,
        type: "chapelle",
        description: "Communauté carmélitaine à Caen",
        url: "carmel-de-caen/",
        horaires: "Consulter la page"
    },
    {
        name: "Église Saint-Clair",
        address: "Rue de la Fontaine, 14200 Hérouville-Saint-Clair",
        lat: 49.2068110,
        lng: -0.3178363,
        type: "église",
        description: "Église paroissiale d’Hérouville-Saint-Clair",
        url: "saint-clair-herouville/",
        horaires: "Consulter les horaires"
    },
    {
        name: "Église Saint-Paul",
        address: "Place Saint-Paul, 14000 Caen",
        lat: 49.1864985,
        lng: -0.3890963,
        type: "église",
        description: "Église paroissiale — quartier Saint-Paul",
        url: "saint-paul/",
        horaires: "Consulter les horaires"
    },
    {
        name: "Église Sainte-Claire",
        address: "Place Wurzburg, 14000 Caen",
        lat: 49.2020285,
        lng: -0.3796828,
        type: "église",
        description: "Église paroissiale — Folie Couvrechef",
        url: "sainte-claire-folie-couvrechef/",
        horaires: "Consulter les horaires"
    },
    {
        name: "Église Saint-François",
        address: "Place François Mitterrand, 14200 Hérouville-Saint-Clair",
        lat: 49.2028060,
        lng: -0.3333894,
        type: "église",
        description: "Église paroissiale — Hérouville-Saint-Clair",
        url: "saint-francois-herouville/",
        horaires: "Consulter les horaires"
    },
    {
        name: "Église Saint-André",
        address: "Avenue de Thiès, 14000 Caen",
        lat: 49.1976052,
        lng: -0.3635628,
        type: "église",
        description: "Église paroissiale — Calvaire Saint-Pierre",
        url: "saint-andre-calvaire-saint-pierre/",
        horaires: "Consulter les horaires"
    },
    {
        name: "Église Saint-Germain",
        address: "Rue de la Sente aux Moines, 14280 Saint-Germain-la-Blanche-Herbe",
        lat: 49.1883763,
        lng: -0.4073675,
        type: "église",
        description: "Église paroissiale — Saint-Germain-la-Blanche-Herbe",
        url: "saint-germain-blanche-herbe/",
        horaires: "Consulter les horaires"
    },
    {
        name: "Église Saint-Gerbold",
        address: "Rue Albert Catherine, 14550 Blainville-sur-Orne",
        lat: 49.2287708,
        lng: -0.2999796,
        type: "église",
        description: "Église paroissiale — Blainville-sur-Orne",
        url: "saint-gerbold-blainville/",
        horaires: "Consulter les horaires"
    },
    {
        name: "Église Saint-Bernard",
        address: "Place Champlain, 14000 Caen",
        lat: 49.1981825,
        lng: -0.3462988,
        type: "église",
        description: "Église paroissiale — Pierre-Heuzé",
        url: "saint-bernard-pierre-heuze/",
        horaires: "Consulter les horaires"
    },
    {
        name: "Église Saint-Jean-Baptiste",
        address: "Rue des Équipes d’Urgence, 14000 Caen",
        lat: 49.1805880,
        lng: -0.3576459,
        type: "église",
        description: "Église paroissiale — Saint-Jean",
        url: "saint-jean-baptiste/",
        horaires: "Consulter les horaires"
    },
    {
        name: "Notre-Dame-de-l’Assomption (la Gloriette)",
        address: "8 Place du Parvis Notre-Dame, 14000 Caen",
        lat: 49.1808579,
        lng: -0.3664874,
        type: "église",
        description: "Église de la Gloriette (ancienne église des Jésuites)",
        url: "notre-dame-assomption-gloriette/",
        horaires: "Consulter les horaires"
    },
    {
        name: "Chapelle du CHR",
        address: "CHU - Côte de Nacre, 14000 Caen",
        lat: 49.189139,
        lng: -0.344972,
        type: "chapelle",
        description: "Chapelle du Centre Hospitalier (coordonnées fournies)",
        url: "chapelle-chr/",
        horaires: "Consulter la page"
    }
];

// Catégories d'usage (fréquence d'utilisation)
const USAGE = { PERMANENTE: 'permanente', OCCASIONNELLE: 'occasionnelle', RARE: 'rare' };

// Affectation de l'usage par URL
const usageByUrl = new Map([
  ['saint-joseph-chemin-vert/', USAGE.PERMANENTE],
  ['saint-julien/', USAGE.PERMANENTE],
  ['saint-andre-calvaire-saint-pierre/', USAGE.PERMANENTE],
  ['saint-pierre/', USAGE.PERMANENTE],
  ['saint-bernard-pierre-heuze/', USAGE.PERMANENTE],
  ['saint-etienne/', USAGE.PERMANENTE],
  ['saint-jean-baptiste/', USAGE.PERMANENTE],
  ['sainte-claire-folie-couvrechef/', USAGE.PERMANENTE],
  ['sainte-trinite-saint-gilles/', USAGE.PERMANENTE],
  ['monastere-visitation/', USAGE.PERMANENTE],
  ['saint-francois-herouville/', USAGE.PERMANENTE],
  ['saint-gerbold-blainville/', USAGE.PERMANENTE],
  ['carmel-de-caen/', USAGE.PERMANENTE],

  ['saint-paul/', USAGE.OCCASIONNELLE],
  ['saint-germain-blanche-herbe/', USAGE.OCCASIONNELLE],
  ['saint-clair-herouville/', USAGE.OCCASIONNELLE],
  ['notre-dame-assomption-gloriette/', USAGE.OCCASIONNELLE],

  ['chapelle-oasis/', USAGE.RARE],
  ['chapelle-misericorde/', USAGE.RARE],
  ['chapelle-chr/', USAGE.RARE],
  ['saint-sauveur/', USAGE.RARE],
  ['saint-ouen/', USAGE.RARE],
  ['chapelle-benedictines/', USAGE.RARE],
]);

// Ajoute le champ usage à chaque clocher (défaut: occasionnelle)
clochersData.forEach(c => { c.usage = usageByUrl.get(c.url) || USAGE.OCCASIONNELLE; });


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
                <a href="../eglises/${clocher.url}" class="btn btn-sm btn-primary" style="text-decoration: none; font-size: 0.8em;">
                    <i class="fas fa-info-circle"></i> En savoir plus
                </a>
            </div>
        </div>
    `;

    marker.bindPopup(popupContent);
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
