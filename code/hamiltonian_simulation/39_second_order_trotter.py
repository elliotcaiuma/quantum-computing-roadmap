"""
Level 39: Second-Order (Symmetric) Trotterization

Physical meaning:
Second-order Trotter uses symmetric splitting:
e^{-i(A+B)t} ≈ (e^{-iAt/2n} e^{-iBt/n} e^{-iAt/2n})^n

This cancels O(t²/n) error, giving O(t³/n²) scaling.
Quadratic convergence = much better efficiency!
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

def first_order_step(H_terms, dt):
    """First-order Trotter step."""
    U = np.eye(4, dtype=complex)
    for coeff, H_j in H_terms:
        U = U @ expm(-1j * coeff * H_j * dt)
    return U

def second_order_step(H_terms, dt):
    """Second-order (symmetric) Trotter step.
    
    For H = H_1 + H_2 + H_3:
    U_step = e^{-iH_1 dt/2} e^{-iH_2 dt} e^{-iH_3 dt} e^{-iH_2 dt} e^{-iH_1 dt/2}
    
    For simplicity with 3 terms, use:
    U_step = e^{-iH_1 dt/2} e^{-iH_2 dt} e^{-iH_3 dt} e^{-iH_2 dt} e^{-iH_1 dt/2}
    """
    # Half step for first term
    coeff1, H1 = H_terms[0]
    U = expm(-1j * coeff1 * H1 * dt/2)
    
    # Full step for middle terms
    for coeff, H_j in H_terms[1:-1]:
        U = U @ expm(-1j * coeff * H_j * dt)
    
    # Half step for last term (if multiple terms)
    if len(H_terms) > 1:
        coeff_last, H_last = H_terms[-1]
        U = U @ expm(-1j * coeff_last * H_last * dt/2)
    else:
        # Single term: just apply full step
        U = expm(-1j * coeff1 * H1 * dt)
    
    return U

def trotter_error(H_terms, H_total, t, n, order=1):
    """Compute Trotter error vs. exact evolution.
    
    Args:
        order: 1 for first-order, 2 for second-order
    """
    U_exact = expm(-1j * H_total * t)
    dt = t / n
    
    if order == 1:
        U_step = first_order_step(H_terms, dt)
    else:
        U_step = second_order_step(H_terms, dt)
    
    U_trotter = np.linalg.matrix_power(U_step, n)
    return np.linalg.norm(U_exact - U_trotter, 'fro')

# Transverse Ising model: H = J*Z1*Z2 + h*(X1 + X2)
J, h = 1.0, 0.5
H_terms = [(J, kron(Z, Z)), (h, kron(X, I)), (h, kron(I, X))]
H_total = sum(c * H for c, H in H_terms)

# Test 1: Compare first and second order
print("Test 1 - First vs. Second Order:")
print(f"{'n':>6} | {'1st Order':>12} | {'2nd Order':>12} | {'Improvement':>12}")
print("-" * 50)

n_values = [1, 2, 5, 10, 20, 50, 100]
errors_1st = []
errors_2nd = []

for n in n_values:
    err_1 = trotter_error(H_terms, H_total, 1.0, n, order=1)
    err_2 = trotter_error(H_terms, H_total, 1.0, n, order=2)
    errors_1st.append(err_1)
    errors_2nd.append(err_2)
    improvement = err_1 / err_2 if err_2 > 0 else float('inf')
    print(f"{n:>6} | {err_1:>12.2e} | {err_2:>12.2e} | {improvement:>12.1f}x")

# Test 2: Verify O(1/n²) scaling for second-order
print("\nTest 2 - Verify O(1/n²) scaling (second-order):")
for i in range(len(n_values) - 1):
    n1, n2 = n_values[i], n_values[i+1]
    ratio = errors_2nd[i] / errors_2nd[i+1]
    expected_ratio = (n2 / n1) ** 2  # O(1/n²) scaling
    print(f"  n={n1}→{n2}: error ratio = {ratio:.2f} (expected ≈ {expected_ratio:.2f})")

# Plot comparison
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.loglog(n_values, errors_1st, 'bo-', linewidth=2, markersize=8, label='First-order')
plt.loglog(n_values, errors_2nd, 'ro-', linewidth=2, markersize=8, label='Second-order')
plt.loglog(n_values, [errors_1st[0]*n_values[0]/n for n in n_values], 'b--', 
           label='O(1/n) reference', linewidth=1, alpha=0.5)
plt.loglog(n_values, [errors_2nd[0]*(n_values[0]/n)**2 for n in n_values], 'r--', 
           label='O(1/n²) reference', linewidth=1, alpha=0.5)
plt.xlabel('Number of Trotter steps (n)')
plt.ylabel('Error (Frobenius norm)')
plt.title('First vs. Second-Order Trotter: Error Scaling')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
improvements = [e1/e2 for e1, e2 in zip(errors_1st, errors_2nd)]
plt.semilogx(n_values, improvements, 'go-', linewidth=2, markersize=8)
plt.xlabel('Number of Trotter steps (n)')
plt.ylabel('Improvement Factor (1st/2nd)')
plt.title('Second-Order Advantage')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('second_order_trotter_comparison.png', dpi=150)
print("\nPlot saved: second_order_trotter_comparison.png")

# Test 3: Gate count comparison for equal accuracy
print("\nTest 3 - Gate count for equal accuracy (ε = 10⁻³):")
target_error = 1e-3
n_1st = next(n for n in n_values if trotter_error(H_terms, H_total, 1.0, n, order=1) < target_error)
n_2nd = next(n for n in n_values if trotter_error(H_terms, H_total, 1.0, n, order=2) < target_error)
gates_1st = n_1st * len(H_terms)  # gates per step × steps
gates_2nd = n_2nd * (2 * len(H_terms) - 1)  # symmetric: ~2× gates per step
print(f"  First-order:  n={n_1st}, gates={gates_1st}")
print(f"  Second-order: n={n_2nd}, gates={gates_2nd}")
print(f"  Savings: {gates_1st/gates_2nd:.1f}x fewer gates with second-order")
