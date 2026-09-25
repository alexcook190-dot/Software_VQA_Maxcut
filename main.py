# main.py
from imports import *
from ansatz import build_ansatz
from hamiltonian import build_hamiltonian
from classical_optimizer import run_vqa
from assemble import decode_result
from visualize import plot_convergence, visualize_cut


def main():
    # Step 1 — Define the graph
    G = nx.cycle_graph(4)
    n_qubits = G.number_of_nodes()

    print("=" * 55)
    print("VQE + MaxCut  |  Hardware-Efficient Ansatz")
    print("=" * 55)
    print(f"Graph          : C4 cycle ({n_qubits} nodes, {G.number_of_edges()} edges)")
    print(f"HEA parameters : {2 * n_qubits}")

    # Step 2 — Build the Hamiltonian (Group B)
    print("\nBuilding Hamiltonian...")
    H_C = build_hamiltonian(G)
    print(f"Hamiltonian Pauli terms: {len(H_C)}")

    # Step 3 — Run VQA optimizer (Group C, calls Group A inside)
    print("\nRunning VQE optimization...")
    result, energies = run_vqa(n_qubits, H_C)

    # Step 4 — Decode the result (Assembly)
    print("\nDecoding result...")
    best_bitstring, cut_val = decode_result(G, n_qubits, result)

    # Step 5 — Plot and visualize (Visualization)
    plot_convergence(energies, G.number_of_edges())
    visualize_cut(G, n_qubits, best_bitstring, cut_val)

    print(f"\nDone. Best partition: {best_bitstring}  |  {cut_val} edges cut")


if __name__ == "__main__":
    main()
