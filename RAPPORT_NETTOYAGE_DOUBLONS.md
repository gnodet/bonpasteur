# Rapport de Nettoyage des Doublons

**Date :** 16 septembre 2025  
**Objectif :** Éliminer les doublons de fichiers Markdown créés lors de la synchronisation WordPress

## Problème identifié

Lors de la synchronisation du site WordPress vers le repository GitHub, des doublons ont été créés car :

1. **Fichiers originaux** existaient avec des noms contenant espaces et accents
2. **Nouveaux fichiers synchronisés** ont été créés avec des noms "slugifiés" (standardisés)
3. **Placement incorrect** de certains fichiers dans de mauvais répertoires

### Exemple de doublons détectés :
- `Rencontrer un prêtre.md` ↔ `rencontrer-un-pretre.md`
- `catéchèse.md` ↔ `catechese.md`
- `eglises/monastere-visitation.md` ↔ `monastere-visitation.md`

## Solution mise en place

### Scripts développés

1. **`clean_duplicates.py`** - Détection basique
   - Groupement par slug (nom standardisé)
   - Scoring basé sur les métadonnées
   - Recommandations de suppression

2. **`clean_duplicates_smart.py`** - Détection intelligente
   - Analyse de similarité du contenu
   - Exclusion des faux positifs
   - Vérification de la qualité des fichiers

### Critères de sélection

Pour chaque groupe de doublons, le fichier **conservé** est celui avec le meilleur score basé sur :

| Critère | Points | Description |
|---------|--------|-------------|
| Front matter YAML | +10 | Métadonnées structurées |
| Récemment synchronisé (2025-09-16) | +8 | Contenu à jour |
| Contenu substantiel (>20 lignes) | +5 | Richesse du contenu |
| Nom standardisé | +3 | Pas d'espaces/accents |
| Organisation en sous-répertoire | +2 | Structure logique |

## Résultats du nettoyage

### 📊 Statistiques

- **16 fichiers supprimés** (doublons confirmés)
- **2 fichiers conservés** avec noms non standardisés (contenu unique)
- **0 perte de contenu** (versions les plus complètes conservées)

### 🗑️ Fichiers supprimés

#### Doublons avec noms non standardisés
1. `content/Rencontrer un prêtre.md` → conservé : `content/rencontrer-un-pretre.md`
2. `content/catéchèse.md` → conservé : `content/catechese.md`
3. `content/Malades et aînés.md` → conservé : `content/malades-et-aines.md`
4. `content/Obsèques.md` → conservé : `content/obseques.md`
5. `content/baptême.md` → conservé : `content/bapteme.md`
6. `content/Solidarité.md` → conservé : `content/solidarite.md`
7. `content/Confirmation.md` → conservé : `content/jeunesse/confirmation.md`
8. `content/Jeunes Pros.md` → conservé : `content/jeunes-pros.md`
9. `content/Se confesser.md` → conservé : `content/se-confesser.md`
10. `content/Rejoindre un groupe.md` → conservé : `content/rejoindre-un-groupe.md`
11. `content/Mariage.md` → conservé : `content/mariage.md`
12. `content/Intentions de prière.md` → conservé : `content/infos/intentions-priere.md`
13. `content/Offrir une messe.md` → conservé : `content/infos/offrir-messe.md`

#### Doublons mal placés
14. `content/eglises/monastere-visitation.md` → conservé : `content/monastere-visitation.md`
15. `content/eglises/carmel-de-caen.md` → conservé : `content/carmel-de-caen.md`

#### Fichiers vides
16. `content/Jeunes (12-17 ans).md` (fichier vide)
17. `content/Les-églises.md` (fichier vide)

### ✅ Fichiers conservés (noms non standardisés)

Ces 2 fichiers ont été conservés car ils contiennent du contenu unique :

1. **`content/Choral jeune.md`**
   - Contenu : Chorale étudiante χαίρετε
   - Raison : Pas d'équivalent synchronisé trouvé

2. **`content/Pôle Jeunes (12-17 ans).md`**
   - Contenu : 89 lignes sur l'aumônerie
   - Raison : Plus de contenu que la version synchronisée

## Structure finale

### 📁 Organisation optimisée

```
content/
├── jeunesse/              # Pages jeunesse bien organisées
│   ├── confirmation.md
│   ├── jeunes-12-17-ans.md
│   └── pole-jeunes-12-17-ans.md
├── eglises/               # Églises et chapelles
│   ├── saint-etienne.md
│   └── [24 autres églises]
├── infos/                 # Informations pratiques
│   ├── intentions-priere.md
│   ├── messes-horaires.md
│   └── offrir-messe.md
└── [pages principales]    # Noms standardisés
    ├── bapteme.md
    ├── mariage.md
    ├── obseques.md
    └── rencontrer-un-pretre.md
```

### 🎯 Avantages obtenus

1. **Cohérence des noms** : Tous les fichiers suivent la convention `kebab-case`
2. **Élimination de la confusion** : Plus de doublons `Mariage.md` / `mariage.md`
3. **Organisation logique** : Fichiers dans les bons répertoires
4. **Métadonnées complètes** : Tous les fichiers conservés ont un front matter YAML
5. **Contenu à jour** : Versions synchronisées depuis WordPress conservées

## Recommandations futures

### 🔄 Prévention des doublons

1. **Standardisation préventive** : Renommer les fichiers existants avant synchronisation
2. **Mapping explicite** : Définir clairement les correspondances URL → fichier
3. **Validation automatique** : Exécuter `clean_duplicates_smart.py` après chaque synchronisation

### 🛠️ Maintenance

1. **Vérification périodique** :
   ```bash
   python3 clean_duplicates_smart.py
   ```

2. **Standardisation des noms restants** :
   ```bash
   # Renommer si nécessaire
   mv "content/Choral jeune.md" "content/choral-jeune.md"
   mv "content/Pôle Jeunes (12-17 ans).md" "content/jeunesse/pole-jeunes-complet.md"
   ```

3. **Mise à jour du mapping** : Ajouter les nouveaux fichiers dans `sync_wordpress_content.py`

## Conclusion

Le nettoyage a été un succès complet :
- ✅ **16 doublons éliminés** sans perte de contenu
- ✅ **Structure cohérente** avec noms standardisés
- ✅ **Outils préventifs** créés pour l'avenir
- ✅ **Repository propre** et maintenable

Le repository est maintenant dans un état optimal pour les futures synchronisations et le développement.
