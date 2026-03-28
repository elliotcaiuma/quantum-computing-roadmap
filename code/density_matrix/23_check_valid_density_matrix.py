"""
Level 20: Check Valid Density Matrix

Verify that a matrix satisfies density matrix properties:
1. Hermitian: rho^dagger = rho
2. Unit trace: Tr(rho) = 1
3. Positive semi-definite: all eigenvalues >= 0
"""

import numpy as np


def is_valid_density_matrix(rho, tol=1e-10):
    """Check if matrix is valid density matrix.
    
    Args:
        rho: Matrix to check
        tol: Numerical tolerance
        
    Returns:
        Tuple (is_valid, message)
    """
    # Check Hermitian
    if not np.allclose(rho, rho.conj().T):
        return False, "Not Hermitian"
    
    # Check unit trace
    if not np.abs(np.trace(rho) - 1) < tol:
        return False, "Trace != 1"
    
    # Check positive semi-definite
    eigenvalues = np.linalg.eigvalsh(rho)
    if np.any(eigenvalues < -tol):
        return False, "Not positive semi-definite"
    
    return True, "Valid density matrix"


if __name__ == "__main__":
    # Test valid density matrix
    psi = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
    rho_valid = np.outer(psi, psi.conj())
    
    valid, msg = is_valid_density_matrix(rho_valid)
    print(f"|+> density matrix: {msg}")
    
    # Test invalid matrix (non-Hermitian)
    rho_invalid = np.array([[0.5, 0.5], [0.3, 0.5]])
    valid, msg = is_valid_density_matrix(rho_invalid)
    print(f"Invalid matrix: {msg}")
    
    # Test identity/2 (valid mixed state)
    rho_max_mixed = np.eye(2) / 2
    valid, msg = is_valid_density_matrix(rho_max_mixed)
    print(f"Maximally mixed state: {msg}")
