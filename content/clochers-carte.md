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

### Filtres par type de lieu

<div class="mb-4">
    <div class="btn-group" role="group" aria-label="Filtres des clochers">
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
</div>

### Carte interactive

<div id="clochers-map" style="height: 500px; width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></div>

## Légende

<div class="row mt-4">
    <div class="col-md-4">
        <div class="d-flex align-items-center mb-2">
            <div style="width: 32px; height: 32px; background: #8B4513; border-radius: 50%; margin-right: 12px; display: flex; align-items: center; justify-content: center;">
                <i class="fas fa-cross text-white" style="font-size: 14px;"></i>
            </div>
            <span><strong>Églises paroissiales</strong><br><small class="text-muted">Lieux de culte principaux</small></span>
        </div>
    </div>
    <div class="col-md-4">
        <div class="d-flex align-items-center mb-2">
            <div style="width: 36px; height: 36px; background: #4A5568; border-radius: 50%; margin-right: 12px; display: flex; align-items: center; justify-content: center;">
                <i class="fas fa-university text-white" style="font-size: 16px;"></i>
            </div>
            <span><strong>Abbayes</strong><br><small class="text-muted">Monuments historiques majeurs</small></span>
        </div>
    </div>
    <div class="col-md-4">
        <div class="d-flex align-items-center mb-2">
            <div style="width: 28px; height: 28px; background: #6B46C1; border-radius: 50%; margin-right: 12px; display: flex; align-items: center; justify-content: center;">
                <i class="fas fa-praying-hands text-white" style="font-size: 12px;"></i>
            </div>
            <span><strong>Chapelles</strong><br><small class="text-muted">Lieux de recueillement</small></span>
        </div>
    </div>
</div>

## Informations pratiques

### Comment utiliser la carte

1. **Naviguez** : Utilisez la souris pour déplacer et zoomer sur la carte
2. **Filtrez** : Cliquez sur les boutons de filtre pour afficher seulement certains types de lieux
3. **Découvrez** : Cliquez sur un marqueur pour voir les détails du lieu de culte
4. **Visitez** : Utilisez le lien "En savoir plus" pour accéder à la page dédiée

### Horaires des messes

Pour connaître les horaires détaillés des messes dans chaque lieu, consultez :
- [Horaires des messes](/infos/messes-horaires)
- La page dédiée de chaque église (accessible via la carte)

### Contact

Pour toute question sur nos lieux de culte :
- **Téléphone** : 02 31 86 13 11
- **Email** : paroisse.bonpasteur@bayeuxlisieux.catholique.fr

---

*Cette carte est mise à jour régulièrement. Si vous constatez une erreur, n'hésitez pas à nous contacter.*
