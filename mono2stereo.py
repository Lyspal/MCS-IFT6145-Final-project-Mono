# author: Sylvain Laporte
# date: 2020-12-22
# program: mono2stereo.py
# object: Méthode de génération d'une paire d'images stéréo à partir d'une seule
# image. Basé sur l'article "Learning Stereo from Single Images", arXiv:2008.01484v2 [cs.CV].

import numpy as np
import torch

class Mono2Stereo():
    """Générateur de paire d'images stéréo à partir d'une seule image.
    
    Utilise le modèle de génération de depth map MiDaS.
    """

    def __init__(self, use_large_model=True):
        """Télécharge et initialise le modèle MiDaS sur le GPU.

        Args:
            use_large_model (bool, optional): Selectionne le modèle large. Par défaut: True.
        """
        # Télécharger le modèle MiDaS
        if use_large_model:
            self.midas = torch.hub.load("intel-isl/MiDaS", "MiDaS")
        else:
            self.midas = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")

        # Déplacer le modèle sur le GPU
        self.device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
        self.midas.to(self.device)

        # Initialiser le modèle
        self.midas.eval()

        # Télécharger les transformations incluses avec MiDaS
        midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

        if use_large_model:
            self.transform = midas_transforms.default_transform
        else:
            self.transform = midas_transforms.small_transform

    def generate_right_view(self, dataset, d_min=0, d_max=192):
        """Méthode copmplète pour générer une paire d'images stéréo à partir d'une seule image."""

        results = []

        for image in dataset:
            # Prétraitement de l'image pour inférence MiDaS
            # Applique la normalisation MiDaS et déplace l'image vers le GPU
            input_batch = self.transform(image).to(self.device)

            # Prédit le depth map
            with torch.no_grad():
                prediction = self.midas(input_batch)

                # Redimensione l'image à sa taille originale
                prediction = torch.nn.functional.interpolate(
                    prediction.unsqueeze(1),
                    size=image.shape[:2],
                    mode="bicubic",
                    align_corners=False,
                ).squeeze()
            
            Z = prediction.cpu().numpy()

            # Convertit le depth map en disparity map
            D_tilde = self.__compute_D_tilde(Z, d_min, d_max)
            D_tilde = np.clip(D_tilde, d_min, d_max)

            # Calcule la vue de droite
            right_image = self.__compute_right_view(image, D_tilde, d_max)

            # Crop images
            image = image[:, -d_max, :]
            right_image = right_image[:, -d_max, :]
            D_tilde = D_tilde[:, -d_max, :]

            results.append((image, right_image, D_tilde))
        
        return results

    def __compute_D_tilde(self, Z, d_min, d_max):
        """Convertit un depth map en disparity map"""

        s = np.random.randint(d_min, d_max)   # Randomly sampled scaling factor
        Z_max = np.max(Z)

        return (s * Z_max) / Z

    def __compute_right_view(self, img, disp_map, d_max):
        """Calcule la vue de droite à partir d'une image et de sa disparity map"""

        disp_map = disp_map.astype(int)
        right_image = img.copy()  # Pour interpolation

        for p_i in range(img.shape[0]):
            for p_j in range(img.shape[1]):
                # Forward warp
                new_p_j = p_j - disp_map[p_i, p_j]
                if new_p_j > 0:
                    right_image[p_i, new_p_j] = img[p_i, p_j]

                    # Interpolation
                    right_image[p_i, p_j] = img[p_i, p_j]

        return right_image