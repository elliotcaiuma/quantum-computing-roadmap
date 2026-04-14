#!/usr/bin/env python3
"""
Create and visualize single-qubit quantum states.

Demonstrates:
- Statevector representation
- Bloch sphere visualization
- Measurement probabilities
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt


def create_custom_state(alpha, beta):
    """
    Create a custom single-qubit state.
    
    Args:
        alpha: Complex amplitude for |0⟩
        beta: Complex amplitude for |1⟩
    
    Returns:
        Statevector object
    """
    # Normalize
    norm = np.sqrt(np.abs(alpha)**2 + np.abs(beta)**2)
    alpha_norm = alpha / norm
    beta_norm = beta / norm
    
    # Create statevector
    psi = Statevector([alpha_norm, beta_norm])
    return psi


def create_basis_states():
    """Create computational basis states."""
    zero = Statevector.from_label('0')
    one = Statevector.from_label('1')
    return zero, one


def create_superposition_states():
    """Create common superposition states."""
    # |+⟩ = (|0⟩ + |1⟩)/√2
    plus = Statevector.from_label('+')
    
    # |-⟩ = (|0⟩ - |1⟩)/√2
    minus = Statevector.from_label('-')
    
    return plus, minus


def measure_state(psi, basis='Z'):
    """
    Measure a state in given basis.
    
    Args:
        psi: Statevector
        basis: 'Z', 'X', or 'Y'
    
    Returns:
        Dictionary of probabilities
    """
    if basis == 'Z':
        prob_0 = np.abs(psi[0])**2
        prob_1 = np.abs(psi[1])**2
        return {'0': prob_0, '1': prob_1}
    
    elif basis == 'X':
        # Transform to X basis
        plus_amp = (psi[0] + psi[1]) / np.sqrt(2)
        minus_amp = (psi[0] - psi[1]) / np.sqrt(2)
        return {'+': np.abs(plus_amp)**2, '-': np.abs(minus_amp)**2}
    
    elif basis == 'Y':
        # Transform to Y basis
        plus_y_amp = (psi[0] - 1j*psi[1]) / np.sqrt(2)
        minus_y_amp = (psi[0] + 1j*psi[1]) / np.sqrt(2)
        return {'+i': np.abs(plus_y_amp)**2, '-i': np.abs(minus_y_amp)**2}


def visualize_on_bloch(psi):
    """Visualize state on Bloch sphere."""
    qc = QuantumCircuit(1)
    # Initialize to custom state (Qiskit doesn't support direct init in viz)
    # This is a workaround - in practice, use gates to create state
    plot_bloch_multivector(qc)
    plt.show()


def main():
    print("="*60)
    print("Single-Qubit State Creator")
    print("="*60)
    
    # Create basis states
    zero, one = create_basis_states()
    print("\n1. Basis States:")
    print(f"   |0⟩ = {zero}")
    print(f"   |1⟩ = {one}")
    
    # Create superposition states
    plus, minus = create_superposition_states()
    print("\n2. Superposition States:")
    print(f"   |+⟩ = {plus}")
    print(f"   |-⟩ = {minus}")
    
    # Create custom state
    alpha, beta = 1/np.sqrt(2), 1/np.sqrt(2)  # |+⟩
    custom = create_custom_state(alpha, beta)
    print(f"\n3. Custom State (|+⟩):")
    print(f"   ψ = {custom}")
    
    # Measure in different bases
    print("\n4. Measurement Probabilities:")
    print(f"   Z-basis: {measure_state(custom, 'Z')}")
    print(f"   X-basis: {measure_state(custom, 'X')}")
    print(f"   Y-basis: {measure_state(custom, 'Y')}")
    
    print("\n" + "="*60)
    print("✓ State creation complete!")
    print("="*60)


if __name__ == "__main__":
    main()
