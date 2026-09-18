from imports import *

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 5 — Visualize the final cut on the graph
# ─────────────────────────────────────────────────────────────────────────────
 
def visualize_cut(graph: nx.Graph, bitstring: str) -> None:
    """Draw the graph coloring nodes by their partition."""
    # Qiskit bitstring: rightmost char = qubit 0
    partition = {i: int(bitstring[-(i+1)]) for i in range(len(bitstring))}
    colors = ["#38bdf8" if partition[n] == 0 else "#f472b6"
              for n in graph.nodes()]
    edge_colors = [
        "#34d399" if partition[u] != partition[v] else "#334155"
        for u, v in graph.edges()
    ]
    edge_widths = [
        4 if partition[u] != partition[v] else 1.5
        for u, v in graph.edges()
    ]
    pos = nx.circular_layout(graph)
    nx.draw(graph, pos, with_labels=True,
            node_color=colors, node_size=900,
            font_color="white", font_size=16,
            edge_color=edge_colors, width=edge_widths)
    plt.title(
        f"MaxCut result: '{bitstring}'  —  {cut_val} edges cut",
        fontsize=14
    )
    plt.show()
 
visualize_cut(G, best_bitstring)
