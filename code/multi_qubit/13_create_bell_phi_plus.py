#!/usr/bin/env python3
"""
Level 13: Create Bell State Φ⁺ - Task Specific

Creates one specific Bell state: |Φ⁺⟩ = (|00⟩ + |11⟩)/√2.
Task-specific (only this Bell state), but introduces entanglement!

Learning goal: First entangled state!
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create 2-qubit circuit
qc = QuantumCircuit(2)

# Create Bell state |Φ⁺⟩
qc.h(0)     # Hadamard on qubit 0
qc.cx(0, 1) # CNOT with control=0, target=1

# Get statevector
bell_state = Statevector(qc)

print("Bell state |Φ⁺⟩:")
print(bell_state)

# This is an ENTANGLED state!
# Can't be written as |ψ₁⟩ ⊗ |ψ₂⟩
# Measurement of one qubit instantly determines the other
