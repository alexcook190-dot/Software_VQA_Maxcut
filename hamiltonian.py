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
