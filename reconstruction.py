"""
reconstruction.py — GROUP B
Reconstruct single-qubit density matrices from measurement counts.
Two methods: linear inversion (required) and MLE (bonus).
"""
from imports import *

def reconstruct_density_matrix(counts_dict: dict, n_qubits: int) -> list:
    """
    Single-qubit state tomography via linear inversion.
 
    Reconstructs an independent 2×2 density matrix for each qubit using:
        ρ = ½ (I + ⟨X⟩σX + ⟨Y⟩σY + ⟨Z⟩σZ)
 
    Parameters
    ----------
    counts_dict : dict
        Keys 'X', 'Y', 'Z'; values are counts dicts from Sampler.
    n_qubits : int
 
    Returns
    -------
    list of n_qubits complex 2×2 numpy arrays (one per qubit)
    """
  
