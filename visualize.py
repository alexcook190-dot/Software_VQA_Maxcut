"""
visualize.py — Visualization
Plots convergence curve and final MaxCut graph.
"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


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
