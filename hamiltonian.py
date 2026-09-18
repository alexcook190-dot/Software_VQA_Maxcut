# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2 — GROUP B: Cost Hamiltonian
# ─────────────────────────────────────────────────────────────────────────────
#
# Translate every graph edge (i, j) into the Pauli term ½(I − ZᵢZⱼ).
#
# Key points:
#   • Qiskit orders qubits RIGHT-TO-LEFT in Pauli strings.
#     For n=4, qubit 0 → rightmost character (index n-1-0 = 3 in the list).
#   • For each edge build two SparsePauliOp terms and add them.
#   • Use SparsePauliOp.sum(terms) at the end.
#
# Input : graph (networkx.Graph)
# Output: SparsePauliOp  — the cost Hamiltonian H_C

from imports import *

def build_hamiltonian(graph):
    nodes = len(graph)
    edges_list = list(graph.edges())

    terms = []
    for edge in edges_list:
        i, j = edge

        # Create the Pauli string for the term ½(I − ZᵢZⱼ)
        pauli_string = ['I'] * nodes
        pauli_string[nodes - 1 - i] = 'Z'
        pauli_string[nodes - 1 - j] = 'Z'
        pauli_term = SparsePauliOp.from_list([(''.join(pauli_string), 0.5)])
        terms.append(pauli_term)

    return SparsePauliOp.sum(terms)
