from qiskit.quantum_info import state_fidelity

from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error

aer_simulator = AerSimulator()

# assuming qc has no measurement gates applied
def QST(qc):
    # qc_measuring_all = qc.measure_all()
  # qc_measuring_only_qubit_0 = qc.measure(0)
  
  n_qubits = qc.num_qubits
  
  noise_model = NoiseModel()

  for gate in ["x", "y", "z", "h", "rx", "ry", "rz"]:
    depolarizing_error_gate = depolarizing_error(0.05, 1)
    for q in range(n_qubits):
        noise_model.add_quantum_error(depolarizing_error_gate, [gate], [q], warnings=False)

    total_counts = {}
    for i in range(max_iterations_step_1):
    qc_transpiled = transpile(qc)
    res = aer_simulator.run(qc_transpiled, noise_model=noise_model, shots=1)

    counts = res.result().get_counts()
    # { "0": 0, "1": 1 }
  # find the lowest values in total_counts and add them to a filter
  
  return correct_state_estimate

correct_state_true = ...
correct_state_estimate = QST(qc)

# 0 <= F <= 1
fidelity = state_fidelity(correct_state_true, correct_state_estimate)
  
