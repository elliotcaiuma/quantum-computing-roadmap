"""
Level 18: Create Density Matrix from State Vector

Create density matrix ρ = |ψ⟩⟨ψ| from a state vector.
"""

import numpy as np


def density_matrix(psi):
    """Create density matrix from state vector.
    
    Args:
        psi: State vector as numpy array
        
    Returns:
        Density matrix as 2D numpy array
    """
    return np.outer(psi, psi.conj())


if __name__ == "__main__":
    # Pure state |+⟩
    psi_plus = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
    rho_plus = density_matrix(psi_plus)
    
    print("Density matrix of |+>:")
    print(rho_plus)
    print()
    
    # Verify properties
    print("Hermitian:", np.allclose(rho_plus, rho_plus.conj().T))
    print("Trace:", np.trace(rho_plus))
    print("Purity (Tr(rho^2)):", np.trace(rho_plus @ rho_plus).real)
