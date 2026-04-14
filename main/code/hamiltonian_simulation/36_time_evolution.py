"""
Level 36: Time Evolution Operator e^{-iHt}

Physical meaning:
Time evolution operator U(t) = e^{-iHt} evolves quantum states.
For Hermitian H, U(t) is unitary and preserves state norm.
"""

import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt

# Pauli matrices
X = np.array([[0, 1], [1, 0]])
Y = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]])
I = np.eye(2)

def time_evolution(H, t):
    """Compute time evolution operator U(t) = e^{-iHt}.
    
    Args:
        H: np.ndarray - Hamiltonian (2x2 Hermitian matrix)
        t: float - evolution time
    
    Returns:
        np.ndarray - unitary evolution operator
    """
    return expm(-1j * H * t)

def verify_unitarity(U):
    """Check if U is unitary: U†U = I."""
    return np.allclose(U.conj().T @ U, I)

def evolve_state(H, psi0, t):
    """Evolve initial state psi0 under Hamiltonian H for time t."""
    U = time_evolution(H, t)
    return U @ psi0

# Test 1: Z Hamiltonian (rotation)
theta = 1.0
H_z = (theta/2) * Z
print("Test 1 - Z Hamiltonian:")
for t in [0, np.pi/4, np.pi/2, np.pi]:
    U = time_evolution(H_z, t)
    print(f"  t={t:.3f}: U = [[{U[0,0]:.3f}, {U[0,1]:.3f}], [{U[1,0]:.3f}, {U[1,1]:.3f}]]")
    print(f"    Unitary: {verify_unitarity(U)}")

# Test 2: X Hamiltonian (Rabi oscillations)
H_x = (theta/2) * X
psi0 = np.array([1, 0])  # |0>
print("\nTest 2 - Rabi Oscillations (H = ωX, initial |0>):")
times = np.linspace(0, np.pi, 100)
probabilities = []
for t in times:
    psi = evolve_state(H_x, psi0, t)
    prob_1 = np.abs(psi[1])**2  # Probability of |1>
    probabilities.append(prob_1)
    if t in [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]:
        print(f"  t={t:.3f}: P(|1>) = {prob_1:.4f}")

# Plot Rabi oscillations
plt.figure(figsize=(8, 4))
plt.plot(times, probabilities, 'b-', linewidth=2)
plt.xlabel('Time t')
plt.ylabel('P(|1>)')
plt.title('Rabi Oscillations: H = ωX, |ψ(0)⟩ = |0⟩')
plt.grid(True, alpha=0.3)
plt.savefig('rabi_oscillations.png', dpi=150)
print("\nPlot saved: rabi_oscillations.png")

# Test 3: Verify analytical formula
print("\nTest 3 - Verify analytical formula:")
t = np.pi/3
U_numerical = time_evolution(H_z, t)
U_analytical = np.array([[np.exp(-1j*theta*t/2), 0], [0, np.exp(1j*theta*t/2)]])
print(f"  Numerical:  [[{U_numerical[0,0]:.4f}, {U_numerical[0,1]:.4f}], [{U_numerical[1,0]:.4f}, {U_numerical[1,1]:.4f}]]")
print(f"  Analytical: [[{U_analytical[0,0]:.4f}, {U_analytical[0,1]:.4f}], [{U_analytical[1,0]:.4f}, {U_analytical[1,1]:.4f}]]")
print(f"  Match: {np.allclose(U_numerical, U_analytical)}")
