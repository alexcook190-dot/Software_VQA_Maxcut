"""
assemble.py — Assembly
Decodes the VQA result, plots convergence, and visualizes the final cut.
No tomography — VQA MaxCut only.
"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from qiskit.primitives import StatevectorSampler

from ansatz import build_ansatz


def decode_result(graph: nx.Graph, n_qubits: int, result) -> tuple:
    """
    Sample the optimized circuit to find the best bitstring and verify cut.

    Parameters
    ----------
    graph    : nx.Graph
    n_qubits : int
    result   : scipy OptimizeResult from run_vqa()

    Returns
    -------
    best_bitstring : str
    cut_val        : int
    """
    optimal_qc = build_ansatz(n_qubits, result.x)
    optimal_qc.measure_all()

    counts = (
        StatevectorSampler()
        .run([(optimal_qc,)], shots=1024)
        .result()[0].data.meas.get_counts()
    )
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    best_bitstring, best_count = sorted_counts[0]

    print("\nTop bitstrings:")
    for bitstring, count in sorted_counts[:5]:
        print(f"  {bitstring}  {count:4d}  {'█' * (count // 20)}")

    cut_val = sum(
        best_bitstring[-(i + 1)] != best_bitstring[-(j + 1)]
        for i, j in graph.edges()
    )
    print(f"\nBest bitstring : {best_bitstring}  ({best_count}/1024 shots)")
    print(f"Edges cut      : {cut_val}  (optimal = {graph.number_of_edges()})")

    return best_bitstring, cut_val


def plot_convergence(energies: list, n_edges: int) -> None:
    """
    Plot the VQA energy convergence curve.

    Parameters
    ----------
    energies : list[float]  — ⟨H_C⟩ at each optimizer iteration
    n_edges  : int          — optimal cut value (drawn as dashed line)
    """
    plt.figure(figsize=(8, 4))
    plt.plot(energies, color="#38bdf8", linewidth=2, label="⟨H_C⟩ per iteration")
    plt.axhline(y=n_edges, color="#34d399", linestyle="--",
                linewidth=1.5, label=f"Optimal = {n_edges}")
    plt.xlabel("Iteration", fontsize=13)
    plt.ylabel("⟨H_C⟩  (expected edges cut)", fontsize=13)
    plt.title("VQE Convergence — MaxCut on C4", fontsize=14)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()


def visualize_cut(graph: nx.Graph, n_qubits: int,
                  best_bitstring: str, cut_val: int) -> None:
    """
    Draw the graph with nodes colored by their partition.

    Blue nodes  → set S  (bitstring digit '0')
    Pink nodes  → set S̄ (bitstring digit '1')
    Green edges → cut edges
    """
    partition = {i: int(best_bitstring[-(i + 1)]) for i in range(n_qubits)}
    node_colors = ["#38bdf8" if partition[v] == 0 else "#f472b6"
                   for v in graph.nodes()]
    edge_colors = ["#34d399" if partition[u] != partition[v] else "#334155"
                   for u, v in graph.edges()]
    edge_widths = [4 if partition[u] != partition[v] else 1.5
                   for u, v in graph.edges()]

    plt.figure(figsize=(5, 5))
    nx.draw(graph, nx.circular_layout(graph),
            with_labels=True,
            node_color=node_colors, node_size=900,
            font_color="white", font_size=16,
            edge_color=edge_colors, width=edge_widths)
    plt.title(f"MaxCut result: '{best_bitstring}'  —  {cut_val} edges cut",
              fontsize=13)
    plt.tight_layout()
    plt.show()
