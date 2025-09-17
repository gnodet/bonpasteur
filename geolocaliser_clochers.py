#!/usr/bin/env python3
"""
Script pour géolocaliser automatiquement les clochers de Caen
Utilise l'API de géocodage pour obtenir les coordonnées précises
"""

import requests
import json
import time
from typing import Dict, List, Tuple, Optional

# Liste des églises et chapelles de Caen à géolocaliser
CLOCHERS_CAEN = [
    {
        "name": "Église Saint-Pierre",
        "search_terms": ["Église Saint-Pierre Caen", "Place Saint-Pierre Caen"],
        "type": "église"
    },
    {
        "name": "Église Saint-Étienne (Abbaye aux Hommes)",
        "search_terms": ["Abbaye Saint-Étienne Caen", "Abbaye aux Hommes Caen"],
        "type": "abbaye"
    },
    {
        "name": "Église Saint-Julien",
        "search_terms": ["Église Saint-Julien Caen", "Rue Saint-Julien Caen"],
        "type": "église"
    },
    {
        "name": "Abbatiale Sainte-Trinité (Abbaye aux Dames)",
        "search_terms": ["Abbaye Sainte-Trinité Caen", "Abbaye aux Dames Caen"],
        "type": "abbaye"
    },
    {
        "name": "Église Saint-Joseph",
        "search_terms": ["Église Saint-Joseph Caen Chemin Vert", "Saint-Joseph Caen"],
        "type": "église"
    },
    {
        "name": "Église Saint-Paul",
        "search_terms": ["Église Saint-Paul Caen", "Saint-Paul Caen"],
        "type": "église"
    },
    {
        "name": "Église Saint-Sauveur",
        "search_terms": ["Église Saint-Sauveur Caen", "Place Saint-Sauveur Caen"],
        "type": "église"
    },
    {
        "name": "Chapelle de la Visitation",
        "search_terms": ["Monastère Visitation Caen", "Chapelle Visitation Caen"],
        "type": "chapelle"
    },
    {
        "name": "Église Saint-Ouen",
        "search_terms": ["Église Saint-Ouen Caen", "Saint-Ouen Caen"],
        "type": "église"
    },
    {
        "name": "Église Saint-Jean-Baptiste",
        "search_terms": ["Église Saint-Jean-Baptiste Caen", "Saint-Jean-Baptiste Caen"],
        "type": "église"
    }
]

def geocode_with_nominatim(query: str) -> Optional[Tuple[float, float, str]]:
    """
    Géocode une adresse avec Nominatim (OpenStreetMap) - gratuit
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': query,
        'format': 'json',
        'limit': 1,
        'countrycodes': 'fr',
        'city': 'Caen'
    }
    
    headers = {
        'User-Agent': 'ClochersCaen/1.0 (contact@example.com)'
    }
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        if data:
            result = data[0]
            lat = float(result['lat'])
            lng = float(result['lon'])
            address = result.get('display_name', '')
            return lat, lng, address
            
    except Exception as e:
        print(f"Erreur géocodage Nominatim pour '{query}': {e}")
    
    return None

def geocode_with_google(query: str, api_key: str) -> Optional[Tuple[float, float, str]]:
    """
    Géocode une adresse avec Google Geocoding API (payant mais plus précis)
    """
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        'address': query,
        'key': api_key,
        'region': 'fr',
        'components': 'locality:Caen|country:FR'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data['status'] == 'OK' and data['results']:
            result = data['results'][0]
            location = result['geometry']['location']
            lat = location['lat']
            lng = location['lng']
            address = result['formatted_address']
            return lat, lng, address
            
    except Exception as e:
        print(f"Erreur géocodage Google pour '{query}': {e}")
    
    return None

def find_best_coordinates(clocher: Dict) -> Optional[Dict]:
    """
    Trouve les meilleures coordonnées pour un clocher
    """
    print(f"\n🔍 Géolocalisation de {clocher['name']}...")
    
    best_result = None
    
    # Essayer chaque terme de recherche
    for search_term in clocher['search_terms']:
        print(f"   Recherche: {search_term}")
        
        # Essayer Nominatim (gratuit)
        result = geocode_with_nominatim(search_term)
        if result:
            lat, lng, address = result
            print(f"   ✅ Trouvé: {lat:.6f}, {lng:.6f}")
            print(f"      Adresse: {address}")
            
            # Vérifier que c'est bien à Caen
            if 'caen' in address.lower():
                best_result = {
                    'name': clocher['name'],
                    'lat': lat,
                    'lng': lng,
                    'address': address,
                    'type': clocher['type'],
                    'search_term': search_term
                }
                break
        
        # Pause pour respecter les limites de l'API
        time.sleep(1)
    
    if not best_result:
        print(f"   ❌ Aucune coordonnée trouvée pour {clocher['name']}")
    
    return best_result

def generate_javascript_data(results: List[Dict]) -> str:
    """
    Génère le code JavaScript avec les coordonnées trouvées
    """
    js_code = "// Données des clochers de Caen - générées automatiquement\n"
    js_code += "const clochersData = [\n"
    
    for result in results:
        js_code += f"""    {{
        name: "{result['name']}",
        address: "{result['address'].split(',')[0]}, 14000 Caen",
        lat: {result['lat']:.6f},
        lng: {result['lng']:.6f},
        type: "{result['type']}",
        description: "À compléter",
        url: "/{result['name'].lower().replace(' ', '-').replace('(', '').replace(')', '').replace('é', 'e').replace('è', 'e')}/",
        horaires: "Consulter les horaires"
    }},\n"""
    
    js_code += "];\n"
    return js_code

def main():
    """
    Fonction principale
    """
    print("🗺️  Géolocalisation automatique des clochers de Caen")
    print("=" * 60)
    
    results = []
    
    # Géolocaliser chaque clocher
    for clocher in CLOCHERS_CAEN:
        result = find_best_coordinates(clocher)
        if result:
            results.append(result)
    
    # Afficher les résultats
    print(f"\n📊 Résultats: {len(results)}/{len(CLOCHERS_CAEN)} clochers géolocalisés")
    print("=" * 60)
    
    for result in results:
        print(f"✅ {result['name']}")
        print(f"   📍 {result['lat']:.6f}, {result['lng']:.6f}")
        print(f"   📧 {result['address']}")
        print()
    
    # Générer le code JavaScript
    if results:
        js_code = generate_javascript_data(results)
        
        # Sauvegarder dans un fichier
        with open('clochers_coordinates.js', 'w', encoding='utf-8') as f:
            f.write(js_code)
        
        print("📄 Code JavaScript généré dans 'clochers_coordinates.js'")
        print("\n🔧 Pour utiliser ces coordonnées:")
        print("1. Copiez le contenu de 'clochers_coordinates.js'")
        print("2. Remplacez la variable 'clochersData' dans votre fichier JS")
        print("3. Mettez à jour les descriptions et URLs si nécessaire")

if __name__ == "__main__":
    main()
