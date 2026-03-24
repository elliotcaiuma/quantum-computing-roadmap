#!/usr/bin/env python3
"""
Level 10: Hello 2-Qubit - Task Specific

Creates a simple 2-qubit state |00⟩.
Task-specific, but now we're in multi-qubit land!

Learning goal: First step into multi-qubit systems!
"""

from qiskit.quantum_info import Statevector

# Create |00⟩ state (both qubits in ground state)
zero_zero = Statevector.from_label('00')

print("My first 2-qubit state:")
print(zero_zero)

# Notice: 4 components (2^2 = 4 dimensions)
# |00⟩ = [1, 0, 0, 0]
