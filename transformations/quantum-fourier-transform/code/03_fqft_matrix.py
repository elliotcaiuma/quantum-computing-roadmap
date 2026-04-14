"""
FQFT Code Module 1: FQFT Matrix Construction via Determinants

What This Code Does:
- Builds the single-particle DFT matrix
- Constructs the full FQFT matrix using determinant lifting
- Verifies unitarity
- Shows block-diagonal structure

Corresponds to: Section 7 of fqft.pdf
"""

import numpy as np
from itertools import combinations


def create_single_particle_dft(n):
    """
    Create the n x n DFT matrix for single-particle transformation.
    
    Args:
        n (int): Number of fermionic modes
        
    Returns:
        np.ndarray: n x n DFT matrix (complex)
    """
    u = np.zeros((n, n), dtype=complex)
    for j in range(n):
        for k in range(n):
            u[k, j] = np.exp(2j * np.pi * j * k / n) / np.sqrt(n)
    return u


def get_occupied_sites(n_in, n):
    """
    Extract occupied sites from integer bitstring.
    
    Args:
        n_in (int): Integer representing bitstring
        n (int): Number of modes
        
    Returns:
        list: List of occupied site indices
    """
    return [i for i in range(n) if (n_in >> i) & 1]


def create_fqft_matrix(n):
    """
    Build the full 2^n x 2^n FQFT matrix.
    
    The matrix element U[out, in] is:
    - det(u[occ_out, occ_in]) if |occ_out| = |occ_in|
    - 0 otherwise
    
    Args:
        n (int): Number of fermionic modes
        
    Returns:
        np.ndarray: 2^n x 2^n FQFT matrix (complex)
    """
    N = 2**n
    U = np.zeros((N, N), dtype=complex)
    u = create_single_particle_dft(n)
    
    for n_in in range(N):
        occ_in = get_occupied_sites(n_in, n)
        p = len(occ_in)  # Particle number
        
        for n_out in range(N):
            occ_out = get_occupied_sites(n_out, n)
            
            # Only connect states with same particle number
            if len(occ_out) != p:
                continue
            
            # Compute determinant of p x p submatrix
            submatrix = u[np.ix_(occ_out, occ_in)]
            U[n_out, n_in] = np.linalg.det(submatrix)
    
    return U


def verify_fqft(n):
    """
    Verify FQFT matrix is unitary.
    
    Args:
        n (int): Number of modes
        
    Returns:
        tuple: (U, unitarity_error)
    """
    print(f"\n=== FQFT Verification for {n} modes ===")
    
    U = create_fqft_matrix(n)
    
    # Check unitarity
    N = 2**n
    I = np.eye(N, dtype=complex)
    unitarity_error = np.max(np.abs(U.conj().T @ U - I))
    print(f"Unitarity error: {unitarity_error:.2e}")
    
    return U, unitarity_error


if __name__ == "__main__":
    print("=" * 60)
    print("FQFT CODE MODULE 1: Matrix Construction")
    print("=" * 60)
    
    # Test for 3 modes
    n = 3
    U, error = verify_fqft(n)
    
    print(f"\nFQFT matrix for {n} modes ({2**n} x {2**n}):")
    np.set_printoptions(precision=3, suppress=True)
    print(U)
    
    # Show block structure
    print("\n" + "=" * 60)
    print("Block structure by particle number:")
    N = 2**n
    for p in range(n + 1):
        states_with_p = [i for i in range(N) if bin(i).count('1') == p]
        print(f"  {p} particles: {len(states_with_p)} states")
    
    print("\n" + "=" * 60)
    print("Code Module 3 complete!")
    print("=" * 60)
