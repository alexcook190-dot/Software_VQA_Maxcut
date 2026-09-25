Measurement circuits · PY
"""
measurement_circuits.py — GROUP A
Build the three Pauli-basis measurement circuits for single-qubit QST.
"""
from imports import *
 
 
def build_tomography_circuits(vqa_circuit: QuantumCircuit) -> dict:
    """
    Produce three copies of the optimized VQA circuit, each rotated
    into a different Pauli measurement basis before measuring.
 
    Basis rotations
    ---------------
    Z — no rotation  (|0⟩/|1⟩ are already Z eigenstates)
    X — H gate       (rotates |+⟩/|−⟩ into the Z basis)
    Y — Sdg then H   (rotates |+i⟩/|−i⟩ into the Z basis)
 
    Parameters
    ----------
    vqa_circuit : QuantumCircuit
        The optimized ansatz circuit (no measurements attached).
 
    Returns
    -------
    dict with keys 'X', 'Y', 'Z', each a QuantumCircuit with measure_all()
    """
  
