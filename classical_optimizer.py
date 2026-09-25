# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3 — GROUP C: Classical Optimizer
# ─────────────────────────────────────────────────────────────────────────────
#
# Wire up COBYLA to maximize ⟨H_C⟩ by tuning the ansatz parameters.
#
# Steps inside run_vqa:
#   1. Define cost(params):
#        a. Call build_ansatz(n_qubits, params)
#        b. Run StatevectorEstimator to get ⟨H_C⟩
#        c. Append energy to a tracking list
#        d. Return −⟨H_C⟩   ← COBYLA *minimizes*, so we negate
#   2. Start from random initial params in [0, π]
#   3. Call scipy minimize with method='COBYLA'
#   4. Return the result and the energy history
#
# After convergence: use StatevectorSampler to find the best bitstring.

from imports import *
from ansatz import build_ansatz

def run_vqa(n_qubits: int, hamiltonian: SparsePauliOp):
    """
    Run the VQA optimization loop using COBYLA.
 
    Internally calls build_ansatz() on every iteration.
    COBYLA minimizes, so we pass −⟨H_C⟩ as the cost (negated).
 
    Parameters
    ----------
    n_qubits    : int
    hamiltonian : SparsePauliOp  — cost Hamiltonian from build_hamiltonian()
 
    Returns
    -------
    result   : scipy OptimizeResult
    energies : list[float]  — ⟨H_C⟩ recorded at each iteration
    """
    estimator = StatevectorEstimator()
    energies = []
 
    def cost(params: np.ndarray) -> float:
        qc = build_ansatz(n_qubits, params)
        expectation = float(
            estimator.run([(qc, hamiltonian)]).result()[0].data.evs
        )
        energies.append(expectation)
        return -expectation  # negate: COBYLA minimizes, we want to maximize
 
    rng = np.random.default_rng(seed=42)
    x0 = rng.uniform(0, np.pi, 2 * n_qubits)
 
    result = minimize(
        cost,
        x0,
        method="COBYLA",
        options={"maxiter": 500, "rhobeg": 0.5},
    )
    return result, energies
