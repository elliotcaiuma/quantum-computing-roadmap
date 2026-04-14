"""
Level 25: Check Entanglement via Schmidt Rank

For pure bipartite states:
- Schmidt rank = 1: Product state (not entangled)
- Schmidt rank > 1: Entangled state
"""

import numpy as np


def schmidt_decomposition(psi, dim_a=2, dim_b=2):
    """Compute Schmidt decomposition of bipartite state."""
    psi_matrix = psi.reshape(dim_a, dim_b)
    U, s, Vh = np.linalg.svd(psi_matrix)
    return s, U, Vh.conj().T


def is_entangled(psi, dim_a=2, dim_b=2):
    """Check if pure state is entangled.
    
    Args:
        psi: State vector
        dim_a: Dimension of subsystem A
        dim_b: Dimension of subsystem B
        
    Returns:
        True if entangled, False otherwise
    """
    lambdas, _, _ = schmidt_decomposition(psi, dim_a, dim_b)
    schmidt_rank = np.sum(lambdas > 1e-10)
    return schmidt_rank > 1


if __name__ == "__main__":
    # Test product states
    print("Product states:")
    print("|00> entangled:", is_entangled(np.array([1, 0, 0, 0])))
    print("|01> entangled:", is_entangled(np.array([0, 1, 0, 0])))
    print("|10> entangled:", is_entangled(np.array([0, 0, 1, 0])))
    print("|11> entangled:", is_entangled(np.array([0, 0, 0, 1])))
    print()
    
    # Test Bell states
    print("Bell states:")
    bell_phi_plus = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
    bell_phi_minus = np.array([1/np.sqrt(2), 0, 0, -1/np.sqrt(2)])
    bell_psi_plus = np.array([0, 1/np.sqrt(2), 1/np.sqrt(2), 0])
    bell_psi_minus = np.array([0, 1/np.sqrt(2), -1/np.sqrt(2), 0])
    
    print("|Phi+> entangled:", is_entangled(bell_phi_plus))
    print("|Phi-> entangled:", is_entangled(bell_phi_minus))
    print("|Psi+> entangled:", is_entangled(bell_psi_plus))
    print("|Psi-> entangled:", is_entangled(bell_psi_minus))
    print()
    
    # Test partially entangled state
    partial = np.array([0.6, 0, 0, 0.8])
    print("Partially entangled (0.6|00> + 0.8|11>):")
    print("Entangled:", is_entangled(partial))
