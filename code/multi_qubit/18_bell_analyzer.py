#!/usr/bin/env python3
"""
Level 17: Bell State Analyzer - Generalized

Generalizes Bell state measurement: any Bell state, verify entanglement.
From task-specific to general analysis tool!

Learning goal: Build a complete Bell state analysis tool!
"""

from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector
import numpy as np


def create_bell(bell_type='phi_plus'):
    """Create any Bell state."""
    qc = QuantumCircuit(2, 2)
    
    if bell_type == 'phi_plus':
        qc.h(0)
        qc.cx(0, 1)
    elif bell_type == 'phi_minus':
        qc.h(0)
        qc.cx(0, 1)
        qc.z(1)
    elif bell_type == 'psi_plus':
        qc.x(0)
        qc.h(0)
        qc.cx(0, 1)
    elif bell_type == 'psi_minus':
        qc.x(0)
        qc.h(0)
        qc.cx(0, 1)
        qc.z(1)
    
    return qc


def measure_bell(qc, shots=1000):
    """Measure Bell state."""
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=shots).result()
    return result.get_counts()


def verify_entanglement(counts, bell_type):
    """
    Verify entanglement from measurement results.
    
    Args:
        counts: Measurement counts
        bell_type: Expected Bell state type
    
    Returns:
        Boolean: True if entanglement verified
    """
    total = sum(counts.values())
    
    # Phi states: should see 00 and 11 only
    if 'phi' in bell_type:
        correlated = counts.get('00', 0) + counts.get('11', 0)
        fraction = correlated / total
        if fraction > 0.95:
            return True, f"Phi-type correlation: {fraction:.2%}"
    
    # Psi states: should see 01 and 10 only
    elif 'psi' in bell_type:
        correlated = counts.get('01', 0) + counts.get('10', 0)
        fraction = correlated / total
        if fraction > 0.95:
            return True, f"Psi-type correlation: {fraction:.2%}"
    
    return False, "No clear entanglement pattern"


def analyze_bell(bell_type, shots=1000):
    """
    Complete Bell state analysis.
    
    Args:
        bell_type: Which Bell state to analyze
        shots: Number of measurement shots
    """
    print(f"\n{'='*60}")
    print(f"Analyzing |{bell_type}⟩")
    print(f"{'='*60}")
    
    # Create
    qc = create_bell(bell_type)
    print(f"Circuit:\n{qc.draw()}\n")
    
    # Measure
    counts = measure_bell(qc, shots)
    print(f"Measurement ({shots} shots):")
    for outcome, count in sorted(counts.items()):
        pct = count / shots * 100
        print(f"   |{outcome}⟩: {count} ({pct:.1f}%)")
    
    # Verify
    is_entangled, message = verify_entanglement(counts, bell_type)
    print(f"\nEntanglement verification:")
    print(f"   {'✓' if is_entangled else '✗'} {message}")
    
    return is_entangled


# Analyze all 4 Bell states
print("Bell State Analyzer")
print("="*60)

for bell_type in ['phi_plus', 'phi_minus', 'psi_plus', 'psi_minus']:
    analyze_bell(bell_type, shots=1000)

print("\n" + "="*60)
print("✓ All Bell states analyzed!")
print("="*60)
