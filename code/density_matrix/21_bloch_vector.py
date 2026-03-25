"""
Level 21: Extract Bloch Vector from Density Matrix

Any single-qubit density matrix can be written as:
rho = 1/2(I + r . sigma)
where r is the Bloch vector.
"""

import numpy as np


def bloch_vector(rho):
    """Extract Bloch vector components from density matrix.
    
    Args:
        rho: 2x2 density matrix
        
    Returns:
        Bloch vector (r_x, r_y, r_z)
    """
    # Pauli matrices
    X = np.array([[0, 1], [1, 0]])
    Y = np.array([[0, -1j], [1j, 0]])
    Z = np.array([[1, 0], [0, -1]])
    
    # Bloch vector components: r_i = Tr(rho sigma_i)
    rx = np.trace(rho @ X).real
    ry = np.trace(rho @ Y).real
    rz = np.trace(rho @ Z).real
    
    return np.array([rx, ry, rz])


if __name__ == "__main__":
    # Pure state |+>
    psi_plus = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
    rho_plus = np.outer(psi_plus, psi_plus.conj())
    
    print("Bloch vector of |+>:")
    print(bloch_vector(rho_plus))
    print("Expected: [1, 0, 0] (on x-axis)")
    print()
    
    # Pure state |+i>
    psi_i = np.array([1/np.sqrt(2), 1j/np.sqrt(2)])
    rho_i = np.outer(psi_i, psi_i.conj())
    
    print("Bloch vector of |+i>:")
    print(bloch_vector(rho_i))
    print("Expected: [0, 1, 0] (on y-axis)")
    print()
    
    # Maximally mixed state
    rho_mix = np.eye(2) / 2
    
    print("Bloch vector of maximally mixed state:")
    print(bloch_vector(rho_mix))
    print("Expected: [0, 0, 0] (at center)")
