#!/usr/bin/env python3
"""
Level 8: Apply All Single-Qubit Gates

Applies all standard single-qubit gates (X, Y, Z, H, S, T)
to |0⟩ state and shows the results.
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Start with |0⟩
initial = Statevector.from_label('0')
print("Initial state: |0⟩")
print(initial)

# X Gate
qc_x = QuantumCircuit(1)
qc_x.x(0)
result_x = initial.evolve(qc_x)
print("\nAfter X gate:")
print(result_x)

# Y Gate
qc_y = QuantumCircuit(1)
qc_y.y(0)
result_y = initial.evolve(qc_y)
print("\nAfter Y gate:")
print(result_y)

# Z Gate
qc_z = QuantumCircuit(1)
qc_z.z(0)
result_z = initial.evolve(qc_z)
print("\nAfter Z gate:")
print(result_z)

# H Gate
qc_h = QuantumCircuit(1)
qc_h.h(0)
result_h = initial.evolve(qc_h)
print("\nAfter H gate:")
print(result_h)

# S Gate
qc_s = QuantumCircuit(1)
qc_s.s(0)
result_s = initial.evolve(qc_s)
print("\nAfter S gate:")
print(result_s)

# T Gate
qc_t = QuantumCircuit(1)
qc_t.t(0)
result_t = initial.evolve(qc_t)
print("\nAfter T gate:")
print(result_t)
