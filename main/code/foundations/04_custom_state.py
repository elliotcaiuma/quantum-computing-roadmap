#!/usr/bin/env python3
"""
Level 4: Custom State Creator - Generalized

Now we generalize! Instead of hardcoding specific states,
we create a function that can make ANY single-qubit state.
"""

import numpy as np
from qiskit.quantum_info import Statevector


def create_state(alpha, beta):
    """
    Create any single-qubit state from amplitudes.
    
    Args:
        alpha: Complex amplitude for |0⟩
        beta: Complex amplitude for |1⟩
    
    Returns:
        Statevector object (normalized)
    """
    # Normalize (ensure |α|² + |β|² = 1)
    norm = np.sqrt(np.abs(alpha)**2 + np.abs(beta)**2)
    alpha_norm = alpha / norm
    beta_norm = beta / norm
    
    # Create and return state
    psi = Statevector([alpha_norm, beta_norm])
    return psi


# Example 1: Create |0⟩
psi0 = create_state(1, 0)
print("1. |0⟩ state:")
print(psi0)

# Example 2: Create |1⟩
psi1 = create_state(0, 1)
print("\n2. |1⟩ state:")
print(psi1)

# Example 3: Create |+⟩
psi_plus = create_state(1/np.sqrt(2), 1/np.sqrt(2))
print("\n3. |+⟩ state:")
print(psi_plus)

# Example 4: Create custom state
psi_custom = create_state(0.6, 0.8)
print("\n4. Custom state (α=0.6, β=0.8):")
print(psi_custom)
print("   Probability of 0:", abs(psi_custom[0])**2)
print("   Probability of 1:", abs(psi_custom[1])**2)
