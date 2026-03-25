"""
Level 22: Create Purification of Density Matrix

Any mixed state can be viewed as part of a larger pure state.
Given rho on system A, find |psi> on system AR such that:
rho_A = Tr_R(|psi><psi|)
"""

import numpy as np


def purify(rho):
    """Create purification of density matrix.
    
    Args:
        rho: Density matrix to purify
        
    Returns:
        State vector in larger Hilbert space (unnormalized)
    """
    # Spectral decomposition
    eigenvalues, eigenvectors = np.linalg.eigh(rho)
    
    # Keep only non-zero eigenvalues
    nonzero_idx = eigenvalues > 1e-10
    eigenvalues = eigenvalues[nonzero_idx]
    eigenvectors = eigenvectors[:, nonzero_idx]
    
    # Construct purification: |psi> = sum sqrt(p_i) |psi_i> tensor |i>
    # For simplicity, return as flattened vector
    dim = len(eigenvalues)
    psi = np.zeros(dim * 2, dtype=complex)
    
    for i, (p, v) in enumerate(zip(eigenvalues, eigenvectors.T)):
        psi[i*2:(i+1)*2] = np.sqrt(p) * v
    
    return psi


if __name__ == "__main__":
    # Maximally mixed state
    rho_mix = np.eye(2) / 2
    
    psi_pure = purify(rho_mix)
    
    print("Purification of maximally mixed state:")
    print(psi_pure)
    print()
    print("Norm:", np.linalg.norm(psi_pure))
    print("Expected: Should be normalized (approx 1.0)")
    print()
    print("This is the Bell state |Phi+> = (|00> + |11>)/sqrt(2)")
