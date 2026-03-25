"""
Level 24: Compute Reduced Density Matrix

For composite system AB, trace out one subsystem:
rho_A = Tr_B(rho_AB)
"""

import numpy as np


def reduced_density_matrix(rho_ab, keep='A', dim=2):
    """Trace out one subsystem from density matrix.
    
    Args:
        rho_ab: Density matrix of composite system
        keep: Which subsystem to keep ('A' or 'B')
        dim: Dimension of each subsystem
        
    Returns:
        Reduced density matrix
    """
    # Reshape to tensor form (dim, dim, dim, dim)
    rho_tensor = rho_ab.reshape(dim, dim, dim, dim)
    
    if keep == 'A':
        # Trace out B (axes 1 and 3)
        rho_a = np.trace(rho_tensor, axis1=1, axis2=3)
    else:
        # Trace out A (axes 0 and 2)
        rho_a = np.trace(rho_tensor, axis1=0, axis2=2)
    
    return rho_a


if __name__ == "__main__":
    # Bell state |Phi+>
    bell_phi_plus = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
    rho_bell = np.outer(bell_phi_plus, bell_phi_plus.conj())
    
    print("Bell state density matrix:")
    print(rho_bell)
    print()
    
    # Trace out B
    rho_a = reduced_density_matrix(rho_bell, keep='A')
    
    print("Reduced density matrix (trace out B):")
    print(rho_a)
    print()
    print("Result: Maximally mixed state I/2")
    print("Key insight: Pure global state -> Mixed local state")
    print("This is the signature of entanglement!")
