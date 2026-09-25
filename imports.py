# imports.py
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import minimize

from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp, DensityMatrix, state_fidelity
from qiskit.primitives import StatevectorEstimator, StatevectorSampler


"""
imports.py — shared imports for all tomography modules
"""
# Pauli matrices — used by reconstruction and analysis
I2 = np.eye(2, dtype=complex)
X  = np.array([[0, 1], [1, 0]], dtype=complex)
Y  = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z  = np.array([[1, 0], [0, -1]], dtype=complex)
PAULIS = {"X": X, "Y": Y, "Z": Z}
