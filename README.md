# MCS-IFT6145-Final-project-Mono

Projet final sur la stéréoscopie à partir d'une seule image pour le cours IFT6145 - Vision tridimensionnelle.

Auteur: Sylvain Laporte  

Date de remise: 2020-12-22  
Date de présentation: 2020-12-22 12h00

## À propos de ce projet

Ce projet implémente l'article "Learning Stereo from Single Images", arXiv:2008.01484v2 [cs.CV].

Un rapport est disponible au format PDF : `rapport.py`

Les notebooks et fichiers de code sont également annotés.

## Contenu

Le présent répertoire contient les éléments suivants :

- `M2S_results/` : contient les images obtenues de la génération de paires stéréo.
- `models/` : contient une copie du répertoire de l'implémentation officielle du modèle PSMNet à laquelle nous avons appliqué les correctifs nécessaires.
- `baseline_test_PSMNet_colab.ipynb` : notebook Jupyter/Colab utilisé pour effectuer le test de base pour la comparaison de notre implémentation. Voir ce notebook et le rapport pour plus de détails.
- `generate_training_pairs_colab.ipynb` : notebook Jupyter/Colab utilisé pour générer les paires stéréo selon notre implémentation. Voir ce notebook et le rapport pour plus de détails.
- `mono2stereo.py` : contient le code de notre implémentation de l'article.
- `validation.py` : contient les fonctions de comparaison pour les tests.
- `rapport.pdf` : le rapport de notre projet.

NOTE : pour une exécution correcte des notebooks, les fichiers `.py` doivent être importées dans la machine virtuelle Colab.

## Prérequis

Les librairires suivantes ont été utilisées :

- `PyTorch` : pour la construction et l'entraînement des réseaux.
- `openCV` : pour l'I/O des images (utilisée car déjà utilisé par le code tiers).
- `Matplotlib` : pour l'I/O des images.

Les modèles pré-entraînés suivants ont été utilisés :

- MiDaS : pour la génération de depth maps ([version incluse avec PyTorch](https://pytorch.org/hub/intelisl_midas_v2/)).
- PSMNet : pour la correspondance stéréo ([version officielle](https://github.com/JiaRenChang/PSMNet))

Les datasets suivants ont été utilisés :

- [COCO 2017](https://cocodataset.org/#captions-2015) : pour les images mono (le même utilisé par les auteurs de l'article).
- [KITTI 2015](http://www.cvlibs.net/datasets/kitti/) : pour les tests sur PSMNet (le même utilisé par les auteurs de l'article).

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

### Autres références

Zwerman, S., & Okun, J. (Eds.). (2020). The VES Handbook of Visual Effects: Industry Standard VFX Practices and Procedures (3nd ed.). Routledge.

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
