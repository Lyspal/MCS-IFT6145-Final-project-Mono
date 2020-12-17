# MCS-IFT6145-Final-project-Mono

Projet final sur la stéréoscopie à partir d'une seule image pour le cours IFT6145 - Vision tridimensionnelle.

Auteur: Sylvain Laporte  
Matricule: C3874

Date de remise: 2020-12-22  
Date de présentation: ???

## À propos de ce projet

Ce projet implémente l'article "Learning Stereo from Single Images", arXiv:2008.01484v2 [cs.CV].

## Contenu



## Prérequis

Les librairires suivantes ont éeé utilisées:

- `pytorch`: pour la construction et l'entraînement des réseaux.
- d

## Crédits

### Articles

L'article implémenté:

@inproceedings{watson-2020-stereo-from-mono,
 title   = {Learning Stereo from Single Images},
 author  = {Jamie Watson and
            Oisin Mac Aodha and
            Daniyar Turmukhambetov and
            Gabriel J. Brostow and
            Michael Firman
           },
 booktitle = {European Conference on Computer Vision ({ECCV})},
 year = {2020}
}

### Modèles

Pour le modèle MiDaS :

@article{Ranftl2020,
 author    = {Ren\'{e} Ranftl and Katrin Lasinger and David Hafner and Konrad Schindler and Vladlen Koltun},
 title     = {Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-shot Cross-dataset Transfer},
 journal   = {IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)},
 year      = {2020},
}

Pour le modèle PSMNet :

@inproceedings{chang2018pyramid,
  title={Pyramid Stereo Matching Network},
  author={Chang, Jia-Ren and Chen, Yong-Sheng},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={5410--5418},
  year={2018}
}

### Datasets

Pour le dataset SceneFlow :

@InProceedings{MIFDB16,
  author    = "N. Mayer and E. Ilg and P. H{\"a}usser and P. Fischer and D. Cremers and A. Dosovitskiy and T. Brox",
  title     = "A Large Dataset to Train Convolutional Networks for Disparity, Optical Flow, and Scene Flow Estimation",
  booktitle = "IEEE International Conference on Computer Vision and Pattern Recognition (CVPR)",
  year      = "2016",
  note      = "arXiv:1512.02134",
  url       = "http://lmb.informatik.uni-freiburg.de/Publications/2016/MIFDB16"
}

Pour le dataset KITTI 2015:

@ARTICLE{Menze2018JPRS,
  author = {Moritz Menze and Christian Heipke and Andreas Geiger},
  title = {Object Scene Flow},
  journal = {ISPRS Journal of Photogrammetry and Remote Sensing (JPRS)},
  year = {2018}
}
@INPROCEEDINGS{Menze2015ISA,
  author = {Moritz Menze and Christian Heipke and Andreas Geiger},
  title = {Joint 3D Estimation of Vehicles and Scene Flow},
  booktitle = {ISPRS Workshop on Image Sequence Analysis (ISA)},
  year = {2015}
}
