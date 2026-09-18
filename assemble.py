from imports import *
# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4 — Assembly: wire up and run
# ─────────────────────────────────────────────────────────────────────────────
 
print("\n" + "=" * 60)
print("RUNNING VQA ON C4 MAXCUT")
print("=" * 60)
 
# Build the Hamiltonian (Group B's work)
H_C = build_hamiltonian(G)
 
# Run the optimizer (Group C's work, calls Group A internally)
result, energies = run_vqa(n_qubits, H_C)
 
print(f"\nOptimization converged: {result.success}")
print(f"Final ⟨H_C⟩        : {-result.fun:.4f}  (max possible = 4.0)")
print(f"Iterations          : {len(energies)}")
print(f"Optimal params      : {np.round(result.x, 3)}")
 
# ── Plot convergence ─────────────────────────────────────────────────────────
plt.figure(figsize=(8, 4))
plt.plot(energies, color="#38bdf8", linewidth=2)
plt.axhline(y=4.0, color="#34d399", linestyle="--", linewidth=1.5,
            label="Optimal (= 4)")
plt.xlabel("Iteration", fontsize=13)
plt.ylabel("⟨H_C⟩ (cut value)", fontsize=13)
plt.title("VQA Convergence — MaxCut on C4", fontsize=14)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
 
# ── Decode the best bitstring ────────────────────────────────────────────────
# Add measurements to the final optimized circuit and sample
optimal_qc = build_ansatz(n_qubits, result.x)
optimal_qc.measure_all()
 
sampler = StatevectorSampler()
sample_job = sampler.run([(optimal_qc,)], shots=1024)
counts = sample_job.result()[0].data.meas.get_counts()
 
# Sort by frequency
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
best_bitstring, best_count = sorted_counts[0]
 
print(f"\nTop 5 measured bitstrings:")
for bitstring, count in sorted_counts[:5]:
    bar = "█" * (count // 20)
    print(f"  {bitstring}  {count:4d}  {bar}")
 
print(f"\nBest bitstring: {best_bitstring}  (seen {best_count}/1024 times)")
print("Expected: '0101' or '1010'  ← both are optimal cuts for C4")
 
# Verify the cut value manually
def count_cut_edges(bitstring: str, graph: nx.Graph) -> int:
    """Count how many edges cross the cut defined by the bitstring."""
    cut = 0
    for (i, j) in graph.edges():
        # Qiskit bitstrings are also right-to-left
        if bitstring[-(i+1)] != bitstring[-(j+1)]:
            cut += 1
    return cut
 
cut_val = count_cut_edges(best_bitstring, G)
print(f"Verified cut value for '{best_bitstring}': {cut_val} edges cut")
