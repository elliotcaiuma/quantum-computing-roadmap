#!/usr/bin/env python3
"""
Level 7: Apply X Gate - Task Specific

Applies X gate (NOT gate) to |0⟩ state.
Task-specific: only X gate on one specific state.

Learning goal: See how gates transform states!
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Start with |0⟩
initial = Statevector.from_label('0')
print("Initial state: |0⟩")
print(initial)

# Create circuit and apply X gate
qc = QuantumCircuit(1)
qc.x(0)  # X gate (NOT)

# Apply circuit to state
final = initial.evolve(qc)
print("\nAfter X gate:")
print(final)

# X gate flipped |0⟩ to |1⟩!
# That's why X is called the "NOT" gate
