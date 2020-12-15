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
   1. Corriger les occlusions
   2. Corriger les collisions
3. Générer l'image droite.
   1. Forward warping.
   2. Background filling.
4. Entraîner le réseau de correspondance stéréo avec l'image original et l'image générée comme paire.

### Les outils

Datasets:

- COCO pour entrainer
- SINTEL pour tester

Réseaux:

- MiDaS entraîné pour estimer la profondeur
- GANet ou iResnet pour la correspondance stereo

### Difficultés rencontrées

## Résultats

### Problèmes connus et améliorations à apporter
