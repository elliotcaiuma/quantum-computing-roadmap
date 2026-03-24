#!/usr/bin/env python3
"""
Level 2: Create Basis States - Task Specific

Creates both |0⟩ and |1⟩ states (computational basis).
Still task-specific, but now we're doing two things.

Beginner-friendly - copy-paste this code!
"""

from qiskit.quantum_info import Statevector

# Create |0⟩ state
zero = Statevector.from_label('0')
print("1. |0⟩ state:")
print(zero)

# Create |1⟩ state
one = Statevector.from_label('1')
print("\n2. |1⟩ state:")
print(one)

# Notice the difference?
# |0⟩ = [1, 0]  (100% chance of measuring 0)
# |1⟩ = [0, 1]  (100% chance of measuring 1)
