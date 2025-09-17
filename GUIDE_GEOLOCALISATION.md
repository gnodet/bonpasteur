# 🗺️ Guide de géolocalisation des clochers de Caen

## Méthodes recommandées

### 1. Google Maps (le plus précis)

1. **Aller sur** : https://maps.google.com
2. **Rechercher** : "Église Saint-Pierre Caen"
3. **Cliquer** sur le marqueur de l'église
4. **Clic droit** → "Que trouve-t-on ici ?"
5. **Copier** les coordonnées qui apparaissent (format: 49.1829, -0.3707)

### 2. OpenStreetMap + Nominatim

1. **Aller sur** : https://www.openstreetmap.org
2. **Rechercher** l'église dans la barre de recherche
3. **Cliquer** sur le résultat
4. **Regarder l'URL** : les coordonnées sont dans l'URL
   - Exemple: `#map=19/49.18290/-0.37070`
   - Lat: 49.18290, Lng: -0.37070

### 3. GPS Coordinates (outil en ligne)

1. **Aller sur** : https://www.gps-coordinates.net
2. **Entrer l'adresse** de l'église
3. **Cliquer** "Get GPS Coordinates"
4. **Copier** les coordonnées décimales

## Liste des clochers à géolocaliser

### Églises principales
- [ ] **Église Saint-Pierre** - Place Saint-Pierre, Caen
- [ ] **Église Saint-Julien** - Rue Saint-Julien, Caen  
- [ ] **Église Saint-Joseph** - Avenue du Chemin Vert, Caen
- [ ] **Église Saint-Paul** - Rue de la Folie, Caen
- [ ] **Église Saint-Sauveur** - Place Saint-Sauveur, Caen
- [ ] **Église Saint-Ouen** - Rue Saint-Ouen, Caen
- [ ] **Église Saint-Jean-Baptiste** - Caen

### Abbayes historiques
- [ ] **Abbaye Saint-Étienne** (Hommes) - Esplanade Jean-Marie Louvel, Caen
- [ ] **Abbatiale Sainte-Trinité** (Dames) - Place Reine Mathilde, Caen

### Chapelles et monastères
- [ ] **Chapelle de la Visitation** - Rue de la Visitation, Caen
- [ ] **Chapelle de l'Oasis** - Caen
- [ ] **Chapelle des Bénédictines** - Caen
- [ ] **Chapelle de la Miséricorde** - Caen
- [ ] **Chapelle du CHR** - Avenue de la Côte de Nacre, Caen

## Format des coordonnées

### Coordonnées décimales (recommandé)
```
Latitude: 49.182900 (Nord)
Longitude: -0.370700 (Ouest)
```

### Conversion en JavaScript
```javascript
{
    name: "Église Saint-Pierre",
    lat: 49.182900,
    lng: -0.370700,
    address: "Place Saint-Pierre, 14000 Caen"
}
```

## Vérification de précision

### Critères de qualité
1. **Précision** : Au moins 6 décimales (mètre près)
2. **Localisation** : Le marqueur doit être sur le clocher/église
3. **Cohérence** : Toutes les coordonnées dans la zone de Caen
4. **Validation** : Vérifier sur 2 sources différentes

### Coordonnées de référence Caen
- **Centre-ville** : ~49.183, -0.370
- **Zone acceptable** : 
  - Lat: 49.15 à 49.22
  - Lng: -0.45 à -0.30

## Script automatique

Pour automatiser le processus :

```bash
# Installer les dépendances
pip install requests

# Lancer le script
python3 geolocaliser_clochers.py
```

Le script génère automatiquement les coordonnées et le code JavaScript.

## Ressources utiles

### APIs de géocodage
- **Nominatim** (gratuit) : https://nominatim.openstreetmap.org
- **Google Geocoding** (payant) : https://developers.google.com/maps/documentation/geocoding
- **MapBox** (freemium) : https://docs.mapbox.com/api/search/geocoding/

### Outils en ligne
- **GPS Coordinates** : https://www.gps-coordinates.net
- **LatLong.net** : https://www.latlong.net
- **Maps.ie** : https://www.maps.ie/coordinates.html

### Validation
- **Google Maps** : Vérifier visuellement
- **OpenStreetMap** : Comparer les résultats
- **Street View** : Confirmer l'emplacement

## Exemple complet

### Église Saint-Pierre
1. **Recherche Google Maps** : "Église Saint-Pierre Caen"
2. **Coordonnées trouvées** : 49.1829, -0.3707
3. **Vérification OSM** : Cohérent
4. **Code JavaScript** :
```javascript
{
    name: "Église Saint-Pierre",
    address: "Place Saint-Pierre, 14000 Caen",
    lat: 49.1829,
    lng: -0.3707,
    type: "église",
    description: "Monument historique gothique flamboyant",
    url: "/saint-pierre/",
    horaires: "Messes en semaine : 18h30 (mardi-vendredi)"
}
```
