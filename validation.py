# author: Sylvain Laporte
# date: 2020-12-22
# program: validation.py
# object: Fonctions de tests pour valider les résultats

import numpy as np
from numpy.linalg import norm

def compute_EPE(predicted_disp, ground_truth):
    return np.mean(norm(predicted_disp - ground_truth, ord="fro", axis=(1, 2)))

def compute_TER(predicted_disp, ground_truth):
    tau = 3

    height, width, depth = predicted_disp.shape
    nb_pixels = height * width * depth

    diff = np.abs(predicted_disp - ground_truth)
    return diff[np.where(diff > tau)].size / nb_pixels * 100

# Tests

arr1 = np.arange(8)
# arr2 = np.array([5, 5, 2, 9, 5, 11, 12, 8])
arr2 = arr1 + np.random.randint(-1, 2, 8)

tensor1 = arr1.reshape(2, 2, 2)
tensor2 = arr2.reshape(2, 2, 2)

print(tensor1)
print(tensor2)
print(compute_EPE(tensor1, tensor2))
print(compute_TER(tensor1, tensor2))