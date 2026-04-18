#!/usr/bin/env python3
"""
Level 9: Gate Transformer - Generalized

Apply ANY sequence of gates to ANY initial state.
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def apply_gates(initial_state, gate_sequence):
    """
    Apply sequence of gates to initial state.
    
    Args:
        initial_state: Starting Statevector
        gate_sequence: List of gate names ('X', 'Y', 'Z', 'H', 'S', 'T')
    
    Returns:
        Final Statevector after all gates
    """
    # Create circuit
    qc = QuantumCircuit(1)
    
    # Apply each gate in sequence
    for gate in gate_sequence:
        if gate == 'X':
            qc.x(0)
        elif gate == 'Y':
            qc.y(0)
        elif gate == 'Z':
            qc.z(0)
        elif gate == 'H':
            qc.h(0)
        elif gate == 'S':
            qc.s(0)
        elif gate == 'T':
            qc.t(0)
    
    # Evolve state through circuit
    final_state = initial_state.evolve(qc)
    return final_state


# Example 1: |0⟩ -> X -> |1⟩
result1 = apply_gates(Statevector.from_label('0'), ['X'])
print("1. |0⟩ --X--> |1⟩:")
print(result1)

# Example 2: |0⟩ -> H -> |+⟩
result2 = apply_gates(Statevector.from_label('0'), ['H'])
print("\n2. |0⟩ --H--> |+⟩:")
print(result2)

# Example 3: |0⟩ -> H -> Z -> H -> |1⟩
result3 = apply_gates(Statevector.from_label('0'), ['H', 'Z', 'H'])
print("\n3. |0⟩ --H Z H--> |1⟩:")
print(result3)

# Example 4: Custom sequence
result4 = apply_gates(Statevector.from_label('0'), ['H', 'S', 'T'])
print("\n4. |0⟩ --H S T--> custom state:")
print(result4)
