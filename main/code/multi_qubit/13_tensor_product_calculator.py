#!/usr/bin/env python3
"""
Level 13: Tensor Product Calculator - Generalized

Generalizes tensor product: any two single-qubit states.
"""

import numpy as np
from qiskit.quantum_info import Statevector


def tensor_product(state1, state2):
    """
    Compute tensor product of two single-qubit states.
    
    Args:
        state1: First state label ('0', '1', '+', etc.)
        state2: Second state label
    
    Returns:
        Combined 2-qubit statevector
    """
    # Create individual states
    psi1 = Statevector.from_label(state1)
    psi2 = Statevector.from_label(state2)
    
    # Compute tensor product
    combined = np.kron(psi1, psi2)
    
    return combined


# Example 1: |0⟩ ⊗ |0⟩ = |00⟩
result1 = tensor_product('0', '0')
print("1. |0⟩ ⊗ |0⟩:")
print(f"   {result1}")

# Example 2: |0⟩ ⊗ |1⟩ = |01⟩
result2 = tensor_product('0', '1')
print("\n2. |0⟩ ⊗ |1⟩:")
print(f"   {result2}")

# Example 3: |1⟩ ⊗ |0⟩ = |10⟩
result3 = tensor_product('1', '0')
print("\n3. |1⟩ ⊗ |0⟩:")
print(f"   {result3}")

# Example 4: |1⟩ ⊗ |1⟩ = |11⟩
result4 = tensor_product('1', '1')
print("\n4. |1⟩ ⊗ |1⟩:")
print(f"   {result4}")

# Example 5: |+⟩ ⊗ |0⟩ (superposition ⊗ basis)
result5 = tensor_product('+', '0')
print("\n5. |+⟩ ⊗ |0⟩:")
print(f"   {result5}")

# Now you can compute ANY tensor product!
