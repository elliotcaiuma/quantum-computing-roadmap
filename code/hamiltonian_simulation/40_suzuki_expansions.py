"""
Level 40: Higher-Order Suzuki Expansions

Physical meaning:
Suzuki recursive construction builds higher-order formulas:
S₂(t) = e^{-iAt/2}e^{-iBt}e^{-iAt/2}
S₄(t) = S₂(p t)² S₂((1-4p)t) S₂(p t)²  where p = 1/(4-4^{1/3})

Higher order = better accuracy but more complex circuits.
Optimal order depends on target precision.
"""

import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt

# Pauli matrices
X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])

def kron(*args):
    """Kronecker product."""
    result = args[0]
    for arg in args[1:]:
        result = np.kron(result, arg)
    return result

def second_order_step(H_terms, dt):
    """S₂(t) - Second-order symmetric Trotter."""
    if len(H_terms) == 2:
        # Simple case: A + B
        c1, H1 = H_terms[0]
        c2, H2 = H_terms[1]
        U = expm(-1j * c1 * H1 * dt/2)
        U = U @ expm(-1j * c2 * H2 * dt)
        U = U @ expm(-1j * c1 * H1 * dt/2)
    else:
        # Multiple terms: sequential symmetric
        U = np.eye(4, dtype=complex)
        # First half-steps
        for coeff, H_j in H_terms[:-1]:
            U = U @ expm(-1j * coeff * H_j * dt/2)
        # Middle term (full step)
        U = U @ expm(-1j * H_terms[-1][0] * H_terms[-1][1] * dt)
        # Last half-steps (reverse order)
        for coeff, H_j in reversed(H_terms[:-1]):
            U = U @ expm(-1j * coeff * H_j * dt/2)
    return U

def fourth_order_step(H_terms, dt):
    """S₄(t) - Fourth-order Suzuki formula.
    
    S₄(t) = S₂(p t)² S₂((1-4p)t) S₂(p t)²
    where p = 1/(4 - 4^{1/3}) ≈ 0.4145
    """
    p = 1.0 / (4.0 - 4.0**(1.0/3.0))  # ≈ 0.4145
    
    # S₂(p t)
    U_p = second_order_step(H_terms, p * dt)
    
    # S₂((1-4p)t)
    U_mid = second_order_step(H_terms, (1.0 - 4.0*p) * dt)
    
    # S₄(t) = S₂(p t)² S₂((1-4p)t) S₂(p t)²
    U = U_p @ U_p @ U_mid @ U_p @ U_p
    return U

def trotter_error(H_terms, H_total, t, n, order=2):
    """Compute Trotter error."""
    U_exact = expm(-1j * H_total * t)
    dt = t / n
    
    if order == 2:
        U_step = second_order_step(H_terms, dt)
    elif order == 4:
        U_step = fourth_order_step(H_terms, dt)
    else:
        raise ValueError(f"Unsupported order: {order}")
    
    U_trotter = np.linalg.matrix_power(U_step, n)
    return np.linalg.norm(U_exact - U_trotter, 'fro')

# Transverse Ising model
J, h = 1.0, 0.5
H_terms = [(J, kron(Z, Z)), (h, kron(X, I)), (h, kron(I, X))]
H_total = sum(c * H for c, H in H_terms)

# Test 1: Compare 2nd and 4th order
print("Test 1 - Second vs. Fourth Order:")
print(f"{'n':>6} | {'2nd Order':>12} | {'4th Order':>12} | {'Improvement':>12}")
print("-" * 50)

n_values = [1, 2, 5, 10, 20, 50]
errors_2nd = []
errors_4th = []

for n in n_values:
    err_2 = trotter_error(H_terms, H_total, 1.0, n, order=2)
    err_4 = trotter_error(H_terms, H_total, 1.0, n, order=4)
    errors_2nd.append(err_2)
    errors_4th.append(err_4)
    improvement = err_2 / err_4 if err_4 > 0 else float('inf')
    print(f"{n:>6} | {err_2:>12.2e} | {err_4:>12.2e} | {improvement:>12.1f}x")

# Test 2: Verify O(1/n⁴) scaling for fourth-order
print("\nTest 2 - Verify O(1/n⁴) scaling (fourth-order):")
for i in range(len(n_values) - 1):
    n1, n2 = n_values[i], n_values[i+1]
    ratio = errors_4th[i] / errors_4th[i+1]
    expected_ratio = (n2 / n1) ** 4  # O(1/n⁴) scaling
    print(f"  n={n1}→{n2}: error ratio = {ratio:.2f} (expected ≈ {expected_ratio:.2f})")

# Test 3: Optimal order for different precisions
print("\nTest 3 - Optimal order for target precision:")
targets = [1e-1, 1e-2, 1e-3, 1e-4, 1e-6]
for target in targets:
    # Find minimum n for each order
    n_2nd = next((n for n in range(1, 200) if trotter_error(H_terms, H_total, 1.0, n, order=2) < target), None)
    n_4th = next((n for n in range(1, 50) if trotter_error(H_terms, H_total, 1.0, n, order=4) < target), None)
    
    if n_2nd and n_4th:
        # Gate count estimate (2nd: 3n gates, 4th: ~15n gates due to composition)
        gates_2nd = 3 * n_2nd
        gates_4th = 15 * n_4th
        better = "2nd" if gates_2nd < gates_4th else "4th"
        print(f"  ε={target:.0e}: 2nd(n={n_2nd}, gates≈{gates_2nd}) vs 4th(n={n_4th}, gates≈{gates_4th}) → {better}-order optimal")

# Plot
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.loglog(n_values, errors_2nd, 'bo-', linewidth=2, markersize=8, label='2nd-order')
plt.loglog(n_values, errors_4th, 'ro-', linewidth=2, markersize=8, label='4th-order')
plt.loglog(n_values, [errors_2nd[0]*(n_values[0]/n)**2 for n in n_values], 'b--', 
           label='O(1/n²) ref', linewidth=1, alpha=0.5)
plt.loglog(n_values, [errors_4th[0]*(n_values[0]/n)**4 for n in n_values], 'r--', 
           label='O(1/n⁴) ref', linewidth=1, alpha=0.5)
plt.xlabel('Number of Trotter steps (n)')
plt.ylabel('Error')
plt.title('2nd vs. 4th Order Suzuki')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
n_range = range(1, 20)
errors_1st = [trotter_error(H_terms, H_total, 1.0, n, order=1) for n in n_range]
errors_2nd = [trotter_error(H_terms, H_total, 1.0, n, order=2) for n in n_range]
errors_4th = [trotter_error(H_terms, H_total, 1.0, n, order=4) for n in n_range]
plt.loglog(n_range, errors_1st, 'g-', label='1st-order', linewidth=2)
plt.loglog(n_range, errors_2nd, 'b-', label='2nd-order', linewidth=2)
plt.loglog(n_range, errors_4th, 'r-', label='4th-order', linewidth=2)
plt.xlabel('Number of steps (n)')
plt.ylabel('Error')
plt.title('All Orders Comparison')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('suzuki_expansions_comparison.png', dpi=150)
print("\nPlot saved: suzuki_expansions_comparison.png")
