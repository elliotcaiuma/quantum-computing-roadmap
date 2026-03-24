#!/usr/bin/env python3
"""
Level 9: Gate Transformer - Generalized

Generalizes gate application: any gate, any state, any sequence.
From task-specific to fully general tool!

Learning goal: Build reusable quantum circuit tools!
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np


def apply_gates(initial_state, gates):
    """
    Apply a sequence of gates to any initial state.
    
    Args:
        initial_state: '0', '1', '+', '-', etc.
        gates: List of gate names ['H', 'X', 'Z', ...]
    
    Returns:
        Final statevector and circuit
    """
    # Start with initial state
    psi = Statevector.from_label(initial_state)
    
    # Create circuit
    qc = QuantumCircuit(1)
    
    # Apply each gate in sequence
    for gate in gates:
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
        elif gate == 'Rx':
            qc.rx(np.pi/2, 0)  # π/2 rotation
        elif gate == 'Ry':
            qc.ry(np.pi/2, 0)
        elif gate == 'Rz':
            qc.rz(np.pi/2, 0)
        else:
            raise ValueError(f"Unknown gate: {gate}")
    
    # Apply circuit
    final = psi.evolve(qc)
    return final, qc


# Example 1: H then Z
print("1. |0⟩ --[H]--> --[Z]-->")
final, circuit = apply_gates('0', ['H', 'Z'])
print(f"   Result: {final}")
print(f"   Circuit:\n{circuit}")

# Example 2: X then H then S
print("\n2. |0⟩ --[X]--> --[H]--> --[S]-->")
final, circuit = apply_gates('0', ['X', 'H', 'S'])
print(f"   Result: {final}")

# Example 3: Start from |1⟩
print("\n3. |1⟩ --[H]--> --[X]-->")
final, circuit = apply_gates('1', ['H', 'X'])
print(f"   Result: {final}")

# Now you can apply ANY gate sequence to ANY state!
