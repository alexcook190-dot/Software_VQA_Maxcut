"""
hamiltonian.py — GROUP B
Build the MaxCut cost Hamiltonian as a SparsePauliOp.
"""
import numpy as np
import networkx as nx
from qiskit.quantum_info import SparsePauliOp


def build_hamiltonian(graph: nx.Graph) -> SparsePauliOp:
    """
    Build the MaxCut cost Hamiltonian.

    H_C = Σ_{(i,j) ∈ E}  ½(I − ZᵢZⱼ)

    Each edge contributes +1 to the energy when its two endpoints
    are in different partitions (edge is cut) and 0 otherwise.

    Note: Qiskit orders qubits RIGHT-TO-LEFT in Pauli strings.
          Qubit k → position (n − 1 − k) in the string.

    Parameters
    ----------
    graph : nx.Graph

    Returns
    -------
    SparsePauliOp
    """
    n = graph.number_of_nodes()
    terms = []

    for (i, j) in graph.edges():
        # Build the ZZ Pauli string with Z at qubit positions i and j
        pauli_list = ["I"] * n
        pauli_list[n - 1 - i] = "Z"   # right-to-left ordering
        pauli_list[n - 1 - j] = "Z"
        zz_str = "".join(pauli_list)

        # ½(I − ZᵢZⱼ) = 0.5*I − 0.5*ZZ
        zz_term = SparsePauliOp(zz_str,  coeffs=[-0.5])
        id_term = SparsePauliOp("I" * n, coeffs=[ 0.5])
        terms.append(zz_term + id_term)

    return SparsePauliOp.sum(terms).simplify()
