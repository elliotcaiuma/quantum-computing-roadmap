"""
Level 38: First-Order Trotterization

Physical meaning:
First-order Trotter approximates e^{-iHt} ≈ (∏ e^{-iHj t/n})^n.
Error scales as O(t²/n) - linear convergence.
Efficient for short-time evolution.
"""

import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt

# Pauli matrices
X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])
I = np.eye(2)

def kron(*args):
    """Kronecker product of multiple matrices."""
    result = args[0]
    for arg in args[1:]:
        result = np.kron(result, arg)
    return result

def first_order_trotter(H_terms, t, n):
    """First-order Trotter approximation.
    
    Args:
        H_terms: list of (coefficient, operator) tuples
        t: float - total evolution time
        n: int - number of Trotter steps
    
    Returns:
        np.ndarray - approximate evolution operator
    """
    delta_t = t / n
    U_step = np.eye(4, dtype=complex)
    
    # Apply each term sequentially
    for coeff, H_j in H_terms:
        U_step = U_step @ expm(-1j * coeff * H_j * delta_t)
    
    # Repeat n times
    return np.linalg.matrix_power(U_step, n)

def trotter_error(H_terms, H_total, t, n):
    """Compute Trotter error vs. exact evolution."""
    U_exact = expm(-1j * H_total * t)
    U_trotter = first_order_trotter(H_terms, t, n)
    return np.linalg.norm(U_exact - U_trotter, 'fro')

# Transverse Ising model: H = J*Z1*Z2 + h*(X1 + X2)
J = 1.0
h = 0.5

# Hamiltonian terms
H_ising = J * kron(Z, Z) + h * kron(X, I) + h * kron(I, X)
H_terms = [
    (J, kron(Z, Z)),      # J*Z1*Z2
    (h, kron(X, I)),      # h*X1
    (h, kron(I, X))       # h*X2
]

# Test 1: Error vs. number of steps
print("Test 1 - Error vs. Trotter steps (first-order):")
n_values = [1, 2, 5, 10, 20, 50, 100]
errors = []
for n in n_values:
    err = trotter_error(H_terms, H_ising, 1.0, n)
    errors.append(err)
    print(f"  n={n}: error = {err:.2e}")

# Test 2: Verify O(1/n) scaling
print("\nTest 2 - Verify O(1/n) scaling:")
for i in range(len(n_values) - 1):
    n1, n2 = n_values[i], n_values[i+1]
    ratio = errors[i] / errors[i+1]
    expected_ratio = n2 / n1
    print(f"  n={n1}→{n2}: error ratio = {ratio:.2f} (expected ≈ {expected_ratio:.2f})")

# Test 3: Time dependence (error should scale as t²)
print("\nTest 3 - Error vs. time (fixed n=10):")
t_values = [0.1, 0.5, 1.0, 2.0, 4.0]
for t in t_values:
    err = trotter_error(H_terms, H_ising, t, 10)
    print(f"  t={t}: error = {err:.2e}, error/t² = {err/(t**2):.2e}")

# Plot error scaling
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.loglog(n_values, errors, 'bo-', linewidth=2, markersize=8)
plt.loglog(n_values, [errors[0]*n_values[0]/n for n in n_values], 'r--', 
           label='O(1/n) reference', linewidth=2)
plt.xlabel('Number of Trotter steps (n)')
plt.ylabel('Error (Frobenius norm)')
plt.title('First-Order Trotter: Error Scaling')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.loglog(t_values, [trotter_error(H_terms, H_ising, t, 10) for t in t_values], 
           'go-', linewidth=2, markersize=8)
plt.loglog(t_values, [trotter_error(H_terms, H_ising, 0.1, 10)*(t/0.1)**2 for t in t_values], 
           'r--', label='O(t²) reference', linewidth=2)
plt.xlabel('Evolution time (t)')
plt.ylabel('Error')
plt.title('Error vs. Time (n=10 fixed)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('first_order_trotter_error.png', dpi=150)
print("\nPlot saved: first_order_trotter_error.png")
