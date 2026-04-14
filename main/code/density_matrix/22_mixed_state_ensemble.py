"""
Level 19: Create Mixed State from Ensemble

Create density matrix from ensemble {p_i, |psi_i>}.
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


def mixed_state_ensemble(states, probs):
    """Create density matrix from ensemble {p_i, |psi_i>}.
    
    Args:
        states: List of state vectors
        probs: List of probabilities (should sum to 1)
        
    Returns:
        Density matrix as 2D numpy array
    """
    rho = np.zeros((2, 2), dtype=complex)
    for p, psi in zip(probs, states):
        rho += p * density_matrix(psi)
    return rho


if __name__ == "__main__":
    # 50% |0>, 50% |1> (classical mixture)
    states = [np.array([1, 0]), np.array([0, 1])]
    probs = [0.5, 0.5]
    rho_mix = mixed_state_ensemble(states, probs)
    
    print("Mixed state density matrix (50% |0>, 50% |1>):")
    print(rho_mix)
    print()
    
    # Compare with pure state
    psi_plus = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
    rho_plus = density_matrix(psi_plus)
    
    print("Pure state |+> density matrix:")
    print(rho_plus)
    print()
    
    print("Key difference:")
    print("- Same diagonal (measurement probabilities)")
    print("- Different off-diagonal (coherences)")
