#!/usr/bin/env python3
"""
Level 8: Apply All Single-Qubit Gates - Task Specific

Applies all common single-qubit gates (X, Y, Z, H, S, T) to |0⟩.
Task-specific (only |0⟩), but demonstrates multiple gates.

Learning goal: Understand what each gate does!
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def apply_gate(gate_name, initial_state='0'):
    """
    Apply a single-qubit gate to a state.
    
    Args:
        gate_name: 'X', 'Y', 'Z', 'H', 'S', 'T'
        initial_state: '0' or '1'
    
    Returns:
        Final statevector
    """
    # Start with initial state
    psi = Statevector.from_label(initial_state)
    
    # Create circuit
    qc = QuantumCircuit(1)
    
    # Apply gate
    if gate_name == 'X':
        qc.x(0)
    elif gate_name == 'Y':
        qc.y(0)
    elif gate_name == 'Z':
        qc.z(0)
    elif gate_name == 'H':
        qc.h(0)
    elif gate_name == 'S':
        qc.s(0)
    elif gate_name == 'T':
        qc.t(0)
    else:
        raise ValueError(f"Unknown gate: {gate_name}")
    
    # Apply and return
    final = psi.evolve(qc)
    return final


# Test all gates on |0⟩
gates = ['X', 'Y', 'Z', 'H', 'S', 'T']

print("Applying all single-qubit gates to |0⟩:\n")

for gate in gates:
    final = apply_gate(gate, '0')
    print(f"{gate} gate: {final}")

# Notice:
# X: |0⟩ → |1⟩
# H: |0⟩ → |+⟩ (superposition!)
# Z: |0⟩ → |0⟩ (no change, but phase matters)
