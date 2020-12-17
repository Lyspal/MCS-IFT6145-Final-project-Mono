# Apprendre la stéréo à partir d'images seules - Projet final

## Notre projet

### Motivation



## L'article

Le problème

Travaux précédents

La solution

## Notre implémentation

### Les étapes

À partir d'images mono

1. Estimer la profondeur avec un réseau préentraîné.
2. Convertir la depth map en disparity map.
   1. Depth map sharpening
   2. Corriger les occlusions
   3. Corriger les collisions
3. Générer l'image droite.
   1. Forward warping.
   2. Background filling.
4. Entraîner le réseau de correspondance stéréo avec l'image original et l'image générée comme paire.
5. Tester

### Tests

EPE = end-point error = $||V_{est} - V_{gt}||$

Thresholded error rate = the % of pixels with predicted disparity more than $\tau$ pixels from the ground truth: > 3px

### Les outils

Datasets:

- COCO pour entrainer
- SINTEL pour tester

Réseaux:

- MiDaS entraîné pour estimer la profondeur
- PSMNet pour la correspondance stereo

### Difficultés rencontrées

## Résultats

Comparaison entre :
- SceneFlow pre-trained, test on KITTI
- COCO trained + mono, test on KITTI

### Problèmes connus et améliorations à apporter
