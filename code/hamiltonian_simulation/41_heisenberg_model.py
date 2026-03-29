"""
Level 41: Heisenberg Model Simulation

Physical meaning:
Heisenberg Hamiltonian describes spin-spin interactions:
H = J Σ (XᵢXⱼ + YᵢYⱼ + ZᵢZⱼ)

Used to model magnetic materials and quantum magnetism.
Demonstrates Trotterization for multi-qubit systems.
"""

import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt

# Pauli matrices
X = np.array([[0, 1], [1, 0]])
Y = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]])
I = np.eye(2)

def kron(*args):
    """Kronecker product."""
    result = args[0]
    for arg in args[1:]:
        result = np.kron(result, arg)
    return result

def heisenberg_hamiltonian(J=1.0):
    """Build 2-qubit Heisenberg Hamiltonian.
    
    H = J(X₁X₂ + Y₁Y₂ + Z₁Z₂)
    """
    H_xx = kron(X, X)
    H_yy = kron(Y, Y)
    H_zz = kron(Z, Z)
    return J * (H_xx + H_yy + H_zz)

def trotter_step_heisenberg(J, dt):
    """Trotter step for Heisenberg model.
    
    Decompose: H = J·X₁X₂ + J·Y₁Y₂ + J·Z₁Z₂
    U_step = e^{-iJ·X₁X₂ dt} e^{-iJ·Y₁Y₂ dt} e^{-iJ·Z₁Z₂ dt}
    """
    U_xx = expm(-1j * J * kron(X, X) * dt)
    U_yy = expm(-1j * J * kron(Y, Y) * dt)
    U_zz = expm(-1j * J * kron(Z, Z) * dt)
    return U_zz @ U_yy @ U_xx  # Apply in reverse order

def simulate_heisenberg(J, t, n_steps, psi0):
    """Simulate time evolution under Heisenberg Hamiltonian."""
    dt = t / n_steps
    psi = psi0.copy()
    
    for _ in range(n_steps):
        U_step = trotter_step_heisenberg(J, dt)
        psi = U_step @ psi
    
    return psi

def measure_correlation(psi):
    """Measure spin-spin correlations ⟨Z₁Z₂⟩, ⟨X₁X₂⟩, ⟨Y₁Y₂⟩."""
    # Reshape to 2x2 for easier calculation
    psi_2d = psi.reshape(2, 2)
    
    # ⟨Z₁Z₂⟩
    ZZ = kron(Z, Z)
    corr_zz = np.vdot(psi, ZZ @ psi)
    
    # ⟨X₁X₂⟩
    XX = kron(X, X)
    corr_xx = np.vdot(psi, XX @ psi)
    
    # ⟨Y₁Y₂⟩
    YY = kron(Y, Y)
    corr_yy = np.vdot(psi, YY @ psi)
    
    return corr_zz.real, corr_xx.real, corr_yy.real

# Parameters
J = 1.0
t_max = 4.0
n_steps = 100

# Initial state: |↑↓⟩ (antiparallel spins)
psi0 = np.array([0, 1, 0, 0], dtype=complex)  # |01⟩

print("=== Heisenberg Model Simulation ===")
print(f"Hamiltonian: H = J(X₁X₂ + Y₁Y₂ + Z₁Z₂), J = {J}")
print(f"Initial state: |↑↓⟩ = |01⟩")
print(f"Simulation time: t = 0 to {t_max}")
print()

# Time evolution
times = np.linspace(0, t_max, n_steps)
correlations = []

for t in times:
    psi = simulate_heisenberg(J, t, max(1, int(t/dt)), psi0)
    corr = measure_correlation(psi)
    correlations.append(corr)

# Convert to array for plotting
correlations = np.array(correlations)

# Test 1: Print key time points
print("Test 1 - Spin Correlations vs. Time:")
print(f"{'t':>8} | {'⟨Z₁Z₂⟩':>10} | {'⟨X₁X₂⟩':>10} | {'⟨Y₁Y₂⟩':>10}")
print("-" * 45)
for i in [0, n_steps//4, n_steps//2, 3*n_steps//4, n_steps-1]:
    t = times[i]
    cz, cx, cy = correlations[i]
    print(f"{t:>8.3f} | {cz:>10.4f} | {cx:>10.4f} | {cy:>10.4f}")

# Test 2: Verify conservation laws
print("\nTest 2 - Conservation Laws:")
# Total spin S² should be conserved for Heisenberg model
# For 2 qubits: S² = (σ₁ + σ₂)²/4 = 3/2 + (σ₁·σ₂)/2
# Eigenvalues: 0 (singlet) or 2 (triplet)

# Initial state |01⟩ = (|↑↓⟩ + |↓↑⟩)/√2 + (|↑↓⟩ - |↓↑⟩)/√2
# = triplet + singlet mixture

# Compute ⟨H⟩ (should be constant)
H = heisenberg_hamiltonian(J)
energies = []
for t in times:
    psi = simulate_heisenberg(J, t, max(1, int(t/dt)), psi0)
    E = np.vdot(psi, H @ psi).real
    energies.append(E)

print(f"  Initial energy: ⟨H⟩ = {energies[0]:.6f}")
print(f"  Final energy: ⟨H⟩ = {energies[-1]:.6f}")
print(f"  Energy drift: {abs(energies[-1] - energies[0]):.2e}")

# Plot
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(times, correlations[:, 0], 'r-', linewidth=2, label='⟨Z₁Z₂⟩')
plt.plot(times, correlations[:, 1], 'g-', linewidth=2, label='⟨X₁X₂⟩')
plt.plot(times, correlations[:, 2], 'b-', linewidth=2, label='⟨Y₁Y₂⟩')
plt.xlabel('Time t')
plt.ylabel('Correlation')
plt.title('Spin-Spin Correlations vs. Time')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(times, energies, 'k-', linewidth=2)
plt.xlabel('Time t')
plt.ylabel('⟨H⟩')
plt.title('Energy Conservation')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('heisenberg_simulation.png', dpi=150)
print("\nPlot saved: heisenberg_simulation.png")

# Test 3: Trotter convergence
print("\nTest 3 - Trotter Convergence:")
t = 2.0
psi_exact = expm(-1j * H * t) @ psi0
for n in [10, 20, 50, 100]:
    psi_trotter = simulate_heisenberg(J, t, n, psi0)
    error = np.linalg.norm(psi_exact - psi_trotter)
    print(f"  n={n}: error = {error:.2e}")
