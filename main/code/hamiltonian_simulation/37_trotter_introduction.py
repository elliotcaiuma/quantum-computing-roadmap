"""
Level 37: Trotter Introduction - Commuting vs. Non-Commuting

Physical meaning:
Trotter formula allows approximating e^{-i(A+B)t} when [A,B] ≠ 0.
For commuting terms, the approximation is exact.
For non-commuting terms, error scales as O(1/n).
"""

import numpy as np
from scipy.linalg import expm

# Pauli matrices
X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])
I = np.eye(2)

def commutator(A, B):
    """Compute [A, B] = AB - BA."""
    return A @ B - B @ A

def trotter_error(A, B, t, n):
    """Compute error in Trotter approximation.
    
    Error = ||e^{-i(A+B)t} - (e^{-iAt/n}e^{-iBt/n})^n||
    
    Args:
        A, B: np.ndarray - Hamiltonian terms
        t: float - total evolution time
        n: int - number of Trotter steps
    
    Returns:
        float - Frobenius norm of error
    """
    # Exact evolution
    U_exact = expm(-1j * (A + B) * t)
    
    # Trotter approximation
    U_A = expm(-1j * A * t / n)
    U_B = expm(-1j * B * t / n)
    U_trotter = np.linalg.matrix_power(U_A @ U_B, n)
    
    # Error (Frobenius norm)
    return np.linalg.norm(U_exact - U_trotter, 'fro')

# Test 1: Commuting case (should be exact)
print("Test 1 - Commuting case (Z ⊗ I and I ⊗ Z):")
A = np.kron(Z, I)
B = np.kron(I, Z)
print(f"  [A, B] = 0? {np.allclose(commutator(A, B), 0)}")
for n in [1, 2, 5, 10]:
    err = trotter_error(A, B, 1.0, n)
    print(f"  n={n}: error = {err:.2e}")

# Test 2: Non-commuting case (X and Z)
print("\nTest 2 - Non-commuting case (X and Z):")
A = X
B = Z
print(f"  [A, B] = 0? {np.allclose(commutator(A, B), 0)}")
print(f"  [X, Z] = {commutator(X, Z)}")
for n in [1, 2, 5, 10, 20, 50, 100]:
    err = trotter_error(A, B, 1.0, n)
    print(f"  n={n}: error = {err:.2e}")

# Test 3: Error scaling (should be O(1/n))
print("\nTest 3 - Error scaling (log-log plot data):")
n_values = [10, 20, 40, 80, 160]
for n in n_values:
    err = trotter_error(X, Z, 1.0, n)
    print(f"  n={n}: error = {err:.2e}, n×error = {n*err:.2e}")
