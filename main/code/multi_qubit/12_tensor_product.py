#!/usr/bin/env python3
"""
Level 11: Tensor Product - Task Specific

Computes tensor product of two specific states: |0⟩ ⊗ |1⟩ = |01⟩.
Task-specific (only this one case), but introduces tensor product concept.

Learning goal: Understand how to combine qubits!
"""

import numpy as np
from qiskit.quantum_info import Statevector

# Create individual states
psi1 = Statevector.from_label('0')  # |0⟩
psi2 = Statevector.from_label('1')  # |1⟩

# Compute tensor product
combined = np.kron(psi1, psi2)  # |0⟩ ⊗ |1⟩ = |01⟩

print("Tensor product: |0⟩ ⊗ |1⟩")
print("Result:", combined)

# Notice: |01⟩ = [0, 1, 0, 0]
# This is how we build multi-qubit states!
