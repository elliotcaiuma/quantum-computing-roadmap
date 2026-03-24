#!/usr/bin/env python3
"""
Level 3: Create Superposition States - Task Specific

Creates |+⟩ and |-⟩ superposition states.
Task-specific (only these two states), but introduces superposition concept.

Learning goal: Understand that qubits can be in multiple states at once!
"""

from qiskit.quantum_info import Statevector

# Create |+⟩ = (|0⟩ + |1⟩)/√2
plus = Statevector.from_label('+')
print("1. |+⟩ state (equal superposition):")
print(plus)
print("   Probability of 0:", abs(plus[0])**2)
print("   Probability of 1:", abs(plus[1])**2)

# Create |-⟩ = (|0⟩ - |1⟩)/√2
minus = Statevector.from_label('-')
print("\n2. |-⟩ state (superposition with phase):")
print(minus)
print("   Probability of 0:", abs(minus[0])**2)
print("   Probability of 1:", abs(minus[1])**2)

# Both have 50/50 measurement probability!
# But they're different states (different phases)
