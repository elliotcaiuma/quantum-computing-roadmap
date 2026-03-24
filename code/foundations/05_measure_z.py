#!/usr/bin/env python3
"""
Level 5: Measure in Z Basis - Task Specific

Measures a state in the Z basis (computational basis).
Task-specific: only Z basis measurement.

Learning goal: Understand Born rule and measurement probabilities!
"""

import numpy as np
from qiskit.quantum_info import Statevector


def measure_z(psi):
    """
    Measure state in Z basis.
    
    Args:
        psi: Statevector
    
    Returns:
        Dictionary with probabilities for |0⟩ and |1⟩
    """
    prob_0 = np.abs(psi[0])**2  # |⟨0|ψ⟩|²
    prob_1 = np.abs(psi[1])**2  # |⟨1|ψ⟩|²
    
    return {'0': prob_0, '1': prob_1}


# Test with |+⟩ state
plus = Statevector.from_label('+')
print("Measuring |+⟩ in Z basis:")
results = measure_z(plus)
print(f"   P(0) = {results['0']:.2f} (50%)")
print(f"   P(1) = {results['1']:.2f} (50%)")

# Test with |0⟩ state
zero = Statevector.from_label('0')
print("\nMeasuring |0⟩ in Z basis:")
results = measure_z(zero)
print(f"   P(0) = {results['0']:.2f} (100%)")
print(f"   P(1) = {results['1']:.2f} (0%)")

# Born rule: P(i) = |⟨i|ψ⟩|²
