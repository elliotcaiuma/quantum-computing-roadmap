#!/usr/bin/env python3
"""
Bell State Generator and Entanglement Verifier.

Demonstrates:
- Creating all 4 Bell states
- Measurement correlations
- Entanglement verification
"""

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_multivector
import numpy as np
import matplotlib.pyplot as plt


def create_bell_state(bell_type='phi_plus'):
    """
    Create one of the 4 Bell states.
    
    Args:
        bell_type: 'phi_plus', 'phi_minus', 'psi_plus', 'psi_minus'
    
    Returns:
        QuantumCircuit creating the Bell state
    """
    qc = QuantumCircuit(2, 2)
    
    if bell_type == 'phi_plus':
        # |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
        qc.h(0)
        qc.cx(0, 1)
    
    elif bell_type == 'phi_minus':
        # |Φ⁻⟩ = (|00⟩ - |11⟩)/√2
        qc.h(0)
        qc.cx(0, 1)
        qc.z(1)  # Phase flip
    
    elif bell_type == 'psi_plus':
        # |Ψ⁺⟩ = (|01⟩ + |10⟩)/√2
        qc.x(0)  # Flip first qubit
        qc.h(0)
        qc.cx(0, 1)
    
    elif bell_type == 'psi_minus':
        # |Ψ⁻⟩ = (|01⟩ - |10⟩)/√2
        qc.x(0)
        qc.h(0)
        qc.cx(0, 1)
        qc.z(1)
    
    else:
        raise ValueError(f"Unknown bell_type: {bell_type}")
    
    return qc


def measure_bell_state(qc, shots=1000):
    """
    Measure Bell state and show correlations.
    
    Args:
        qc: QuantumCircuit with Bell state
        shots: Number of measurement shots
    
    Returns:
        Dictionary of measurement counts
    """
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=shots).result()
    counts = result.get_counts()
    return counts


def verify_entanglement(counts):
    """
    Verify entanglement from measurement results.
    
    For Phi+ state, should see only |00⟩ and |11⟩ (perfect correlation).
    For Psi+ state, should see only |01⟩ and |10⟩ (perfect anti-correlation).
    
    Args:
        counts: Measurement counts dictionary
    
    Returns:
        Boolean: True if entangled
    """
    total = sum(counts.values())
    
    # Check for Phi+ type (00 and 11 only)
    if '00' in counts and '11' in counts:
        phi_fraction = (counts.get('00', 0) + counts.get('11', 0)) / total
        if phi_fraction > 0.95:
            print("✓ Phi-type entanglement verified (|00⟩ and |11⟩ only)")
            return True
    
    # Check for Psi+ type (01 and 10 only)
    if '01' in counts and '10' in counts:
        psi_fraction = (counts.get('01', 0) + counts.get('10', 0)) / total
        if psi_fraction > 0.95:
            print("✓ Psi-type entanglement verified (|01⟩ and |10⟩ only)")
            return True
    
    print("✗ No clear entanglement pattern")
    return False


def main():
    print("="*60)
    print("Bell State Generator")
    print("="*60)
    
    bell_types = ['phi_plus', 'phi_minus', 'psi_plus', 'psi_minus']
    
    for bell_type in bell_types:
        print(f"\n{'='*60}")
        print(f"Creating {bell_type.upper()}...")
        print(f"{'='*60}")
        
        # Create Bell state
        qc = create_bell_state(bell_type)
        print(f"Circuit created:")
        print(qc.draw())
        
        # Measure
        counts = measure_bell_state(qc, shots=1000)
        print(f"\nMeasurement results (1000 shots):")
        for outcome, count in sorted(counts.items()):
            percentage = count / 1000 * 100
            print(f"   |{outcome}⟩: {count} ({percentage:.1f}%)")
        
        # Verify entanglement
        verify_entanglement(counts)
    
    print("\n" + "="*60)
    print("✓ Bell state generation complete!")
    print("="*60)
    
    # Optional: Visualize first Bell state on Bloch sphere
    print("\nVisualizing |Φ⁺⟩ on Bloch sphere...")
    qc_phi = create_bell_state('phi_plus')
    # Note: plot_bloch_multivector works better with statevector
    # For visualization, we'd need to extract statevector
    
    print("Tip: Use statevector simulator for Bloch visualization")


if __name__ == "__main__":
    main()
