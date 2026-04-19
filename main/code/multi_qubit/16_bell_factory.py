#!/usr/bin/env python3
"""
Level 16: Bell State Factory - Generalized

Generalizes Bell state creation: any Bell state with parameters.
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np


def create_bell(bell_type='phi_plus'):
    """
    Create any of the 4 Bell states.
    
    Args:
        bell_type: 'phi_plus', 'phi_minus', 'psi_plus', 'psi_minus'
    
    Returns:
        Statevector and circuit
    """
    qc = QuantumCircuit(2, 2)
    
    # Start with |00⟩
    
    if bell_type == 'phi_plus':
        # |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
        qc.h(0)
        qc.cx(0, 1)
    
    elif bell_type == 'phi_minus':
        # |Φ⁻⟩ = (|00⟩ - |11⟩)/√2
        qc.h(0)
        qc.cx(0, 1)
        qc.z(1)
    
    elif bell_type == 'psi_plus':
        # |Ψ⁺⟩ = (|01⟩ + |10⟩)/√2
        qc.x(0)
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
    
    bell_state = Statevector(qc)
    return bell_state, qc


# Example 1: Create |Φ⁺⟩
print("1. Creating |Φ⁺⟩:")
bell, circuit = create_bell('phi_plus')
print(f"   State: {bell}")
print(f"   Circuit:\n{circuit}\n")

# Example 2: Create |Ψ⁺⟩
print("2. Creating |Ψ⁺⟩:")
bell, circuit = create_bell('psi_plus')
print(f"   State: {bell}")
print(f"   Circuit:\n{circuit}\n")

# Example 3: Create all 4
print("3. All Bell states:")
for bell_type in ['phi_plus', 'phi_minus', 'psi_plus', 'psi_minus']:
    bell, _ = create_bell(bell_type)
    print(f"   |{bell_type}⟩: {bell}")

# Now you can create ANY Bell state on demand!
