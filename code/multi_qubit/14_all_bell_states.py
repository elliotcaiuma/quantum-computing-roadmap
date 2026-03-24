#!/usr/bin/env python3
"""
Level 14: All Bell States - Task Specific

Creates all 4 Bell states.
Task-specific (only Bell states), but demonstrates all 4 types.

Learning goal: Understand the complete Bell basis!
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def create_bell(bell_type):
    """
    Create one of the 4 Bell states.
    
    Args:
        bell_type: 'phi_plus', 'phi_minus', 'psi_plus', 'psi_minus'
    
    Returns:
        Statevector of Bell state
    """
    qc = QuantumCircuit(2)
    
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
        qc.x(0)  # Flip first
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
    
    return Statevector(qc)


# Create all 4 Bell states
bell_types = ['phi_plus', 'phi_minus', 'psi_plus', 'psi_minus']

print("All 4 Bell States:\n")

for i, bell_type in enumerate(bell_types, 1):
    bell = create_bell(bell_type)
    print(f"{i}. |{bell_type.replace('_', ' ').title()}⟩:")
    print(f"   {bell}")
    print()

# All Bell states are maximally entangled!
