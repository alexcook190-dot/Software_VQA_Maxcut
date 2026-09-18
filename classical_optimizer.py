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
