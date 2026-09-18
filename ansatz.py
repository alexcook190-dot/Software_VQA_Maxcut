# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1 — GROUP A: Hardware-Efficient Ansatz
# ─────────────────────────────────────────────────────────────────────────────
#
# Build a parameterized quantum circuit with three layers:
#   Layer 1 : Ry(params[i])   on every qubit  i
#   Layer 2 : CNOT(i, i+1)    on each neighboring pair
#   Layer 3 : Ry(params[n+i]) on every qubit  i (second rotation)
#
# Input : n_qubits (int), params (numpy array of length 2*n_qubits)
# Output: QuantumCircuit  — no measurements attached yet
#
# This circuit has NO knowledge of the graph structure.
# It is a general-purpose parameterized circuit.


from imports import *

def build_ansatz(n_qubits, parameters):
    circuit = QuantumCircuit(n_qubits)

    for i in range(n_qubits):
        circuit.ry(parameters[i], i)

    for i in range(n_qubits - 1):
        circuit.cx(i, i+1)

    for i in range(n_qubits):
        circuit.ry(parameters[n_qubits+i], i)

    return circuit