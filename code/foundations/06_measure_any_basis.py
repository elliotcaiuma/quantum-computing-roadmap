#!/usr/bin/env python3
"""
Level 6: Measure in Any Basis - Generalized

Generalizes measurement to X, Y, or Z basis.
From task-specific (Z only) to general tool!

Learning goal: Understand that measurement basis matters!
"""

import numpy as np
from qiskit.quantum_info import Statevector


def measure_basis(psi, basis='Z'):
    """
    Measure state in any basis (X, Y, or Z).
    
    Args:
        psi: Statevector
        basis: 'Z', 'X', or 'Y'
    
    Returns:
        Dictionary of probabilities
    """
    if basis == 'Z':
        # Z basis: |0⟩, |1⟩
        prob_0 = np.abs(psi[0])**2
        prob_1 = np.abs(psi[1])**2
        return {'0': prob_0, '1': prob_1}
    
    elif basis == 'X':
        # X basis: |+⟩, |-⟩
        # Transform to X basis
        plus_amp = (psi[0] + psi[1]) / np.sqrt(2)
        minus_amp = (psi[0] - psi[1]) / np.sqrt(2)
        return {'+': np.abs(plus_amp)**2, '-': np.abs(minus_amp)**2}
    
    elif basis == 'Y':
        # Y basis: |+i⟩, |-i⟩
        # Transform to Y basis
        plus_y_amp = (psi[0] - 1j*psi[1]) / np.sqrt(2)
        minus_y_amp = (psi[0] + 1j*psi[1]) / np.sqrt(2)
        return {'+i': np.abs(plus_y_amp)**2, '-i': np.abs(minus_y_amp)**2}
    
    else:
        raise ValueError("Basis must be 'Z', 'X', or 'Y'")


# Test with |+⟩ state in different bases
plus = Statevector.from_label('+')
print("Measuring |+⟩ in different bases:")
print(f"   Z basis: {measure_basis(plus, 'Z')}")  # 50/50
print(f"   X basis: {measure_basis(plus, 'X')}")  # 100% +
print(f"   Y basis: {measure_basis(plus, 'Y')}")  # 50/50

# Test with |0⟩ state
zero = Statevector.from_label('0')
print("\nMeasuring |0⟩ in different bases:")
print(f"   Z basis: {measure_basis(zero, 'Z')}")  # 100% 0
print(f"   X basis: {measure_basis(zero, 'X')}")  # 50/50
print(f"   Y basis: {measure_basis(zero, 'Y')}")  # 50/50

# Key insight: Measurement depends on basis!
