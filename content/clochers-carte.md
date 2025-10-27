---
title: Carte des Clochers de Caen
description: Découvrez les églises, abbatiales et chapelles de Caen sur une carte interactive. Localisez facilement les lieux de culte de la paroisse Bon Pasteur.
layout: paroisse/carte-leaflet
updated: '2025-09-16'
url: /clochers-carte/
hero_image: images/clochers-caen-hero.jpg
hero_subtitle: Carte interactive des lieux de culte
---

## Découvrez les clochers de Caen

Cette carte interactive vous permet de localiser facilement toutes les églises, abbatiales et chapelles de la paroisse Bon Pasteur de Caen. Cliquez sur les marqueurs pour obtenir plus d'informations sur chaque lieu de culte.

<div id="clochers-map" style="height: 500px; width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></div>


<div class="mb-4 filter-group">
    <div class="btn-group" id="type-filter-group" role="group" aria-label="Filtres des clochers">
        <button type="button" class="btn btn-outline-primary active" onclick="filterMarkers('all')" id="filter-all">
            <i class="fas fa-church"></i> Tous
        </button>
        <button type="button" class="btn btn-outline-primary" onclick="filterMarkers('église')" id="filter-eglise">
            <i class="fas fa-cross"></i> Églises
        </button>
        <button type="button" class="btn btn-outline-primary" onclick="filterMarkers('abbaye')" id="filter-abbaye">
            <i class="fas fa-university"></i> Abbayes
        </button>
        <button type="button" class="btn btn-outline-primary" onclick="filterMarkers('chapelle')" id="filter-chapelle">
            <i class="fas fa-praying-hands"></i> Chapelles
        </button>
    </div>

  <div class="btn-group" id="usage-filter-group" role="group" aria-label="Filtre par usage">
    <button type="button" class="btn btn-outline-secondary active" onclick="filterUsage('all')" id="filter-usage-all">
      Tous
    </button>
    <button type="button" class="btn btn-outline-secondary" onclick="filterUsage('permanente')" id="filter-usage-permanente">
      Régulier
    </button>
    <button type="button" class="btn btn-outline-secondary" onclick="filterUsage('occasionnelle')" id="filter-usage-occasionnelle">
      Occasionnel
    </button>
    <button type="button" class="btn btn-outline-secondary" onclick="filterUsage('rare')" id="filter-usage-rare">
      Rare
    </button>
  </div>
</div>
