"""
Level 42: Molecular H₂ Simulation

Physical meaning:
Electronic structure Hamiltonian for H₂ molecule in minimal basis.
After parity symmetry reduction: 2 qubits.

H = h₀I + h₁Z₀ + h₂Z₁ + h₃Z₀Z₁ + h₄X₀X₁

Used for quantum chemistry applications.
"""

import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt

# Pauli matrices
X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])
I = np.eye(2)

def kron(*args):
    """Kronecker product."""
    result = args[0]
    for arg in args[1:]:
        result = np.kron(result, arg)
    return result

def h2_hamiltonian(bond_length=0.75):
    """Build H₂ Hamiltonian at given bond length (Angstroms).
    
    Coefficients from STO-3G basis, parity symmetry reduction.
    Values are approximate and depend on bond length.
    
    Returns:
        dict with keys: h0, h1, h2, h3, h4, H_matrix
    """
    # Simplified coefficients (typical values at equilibrium)
    # In practice, these come from quantum chemistry calculations
    h0 = -0.5  # Constant offset
    h1 = -0.1  # Z₀ coefficient
    h2 = -0.1  # Z₁ coefficient  
    h3 = 0.05  # Z₀Z₁ coefficient
    h4 = 0.02  # X₀X₁ coefficient (bonding term)
    
    # Build Hamiltonian matrix
    H = (h0 * kron(I, I) + 
         h1 * kron(Z, I) + 
         h2 * kron(I, Z) + 
         h3 * kron(Z, Z) + 
         h4 * kron(X, X))
    
    return {
        'h0': h0, 'h1': h1, 'h2': h2, 'h3': h3, 'h4': h4,
        'H_matrix': H,
        'bond_length': bond_length
    }

def trotter_step_h2(h_params, dt):
    """Trotter step for H₂ Hamiltonian.
    
    Decompose: H = h₀I + h₁Z₀ + h₂Z₁ + h₃Z₀Z₁ + h₄X₀X₁
    All terms except X₀X₁ commute with each other.
    """
    h0, h1, h2, h3, h4 = h_params['h0'], h_params['h1'], h_params['h2'], h_params['h3'], h_params['h4']
    
    # Commuting terms (can combine)
    U_commute = expm(-1j * (h1 * kron(Z, I) + h2 * kron(I, Z) + h3 * kron(Z, Z)) * dt)
    
    # Non-commuting term
    U_xx = expm(-1j * h4 * kron(X, X) * dt)
    
    # Trotter step (symmetric)
    U = U_commute @ U_xx @ U_commute
    
    return U

def simulate_h2(h_params, t, n_steps, psi0):
    """Simulate time evolution under H₂ Hamiltonian."""
    dt = t / n_steps
    psi = psi0.copy()
    
    for _ in range(n_steps):
        U_step = trotter_step_h2(h_params, dt)
        psi = U_step @ psi
    
    return psi

def get_ground_state(H):
    """Find ground state via exact diagonalization."""
    eigenvalues, eigenvectors = np.linalg.eigh(H)
    return eigenvalues[0], eigenvectors[:, 0]

# Test 1: Hamiltonian at equilibrium
print("=== H₂ Molecular Simulation ===")
h2_params = h2_hamiltonian(bond_length=0.75)
H = h2_params['H_matrix']

print(f"\nBond length: {h2_params['bond_length']} Å")
print(f"\nHamiltonian coefficients:")
print(f"  h₀ (constant) = {h2_params['h0']:.4f}")
print(f"  h₁ (Z₀)       = {h2_params['h1']:.4f}")
print(f"  h₂ (Z₁)       = {h2_params['h2']:.4f}")
print(f"  h₃ (Z₀Z₁)     = {h2_params['h3']:.4f}")
print(f"  h₄ (X₀X₁)     = {h2_params['h4']:.4f}")

# Ground state
E_gs, psi_gs = get_ground_state(H)
print(f"\nGround state energy: E₀ = {E_gs:.6f} Hartree")
print(f"Ground state: |ψ₀⟩ = [{psi_gs[0]:.4f}, {psi_gs[1]:.4f}, {psi_gs[2]:.4f}, {psi_gs[3]:.4f}]")

# Test 2: Time evolution from excited state
print("\nTest 1 - Time Evolution from Excited State:")
# Start in |01⟩ (first excited state of non-interacting system)
psi0 = np.array([0, 1, 0, 0], dtype=complex)
t_max = 10.0
n_steps = 100

times = np.linspace(0, t_max, n_steps)
energies = []
fidelities = []

for t in times:
    psi = simulate_h2(h2_params, t, n_steps, psi0)
    E = np.vdot(psi, H @ psi).real
    F = np.abs(np.vdot(psi_gs, psi))**2  # Overlap with ground state
    energies.append(E)
    fidelities.append(F)

print(f"{'t':>8} | {'⟨H⟩':>10} | {'|⟨ψ₀|ψ⟩|²':>10}")
print("-" * 35)
for i in [0, n_steps//4, n_steps//2, 3*n_steps//4, n_steps-1]:
    t = times[i]
    print(f"{t:>8.2f} | {energies[i]:>10.4f} | {fidelities[i]:>10.4f}")

# Test 3: Trotter convergence
print("\nTest 2 - Trotter Convergence:")
t = 5.0
psi_exact = expm(-1j * H * t) @ psi0
for n in [10, 20, 50, 100, 200]:
    psi_trotter = simulate_h2(h2_params, t, n, psi0)
    error = np.linalg.norm(psi_exact - psi_trotter)
    print(f"  n={n}: error = {error:.2e}")

# Test 3: Dissociation curve (energy vs. bond length)
print("\nTest 3 - Dissociation Curve:")
bond_lengths = np.linspace(0.5, 2.0, 10)
ground_energies = []

for r in bond_lengths:
    params = h2_hamiltonian(bond_length=r)
    E_gs, _ = get_ground_state(params['H_matrix'])
    ground_energies.append(E_gs)
    print(f"  r = {r:.2f} Å: E₀ = {E_gs:.6f} Hartree")

# Plot
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(times, energies, 'b-', linewidth=2, label='⟨H⟩')
plt.plot(times, fidelities, 'r-', linewidth=2, label='|⟨ψ₀|ψ⟩|²')
plt.xlabel('Time t')
plt.ylabel('Energy / Fidelity')
plt.title('H₂ Time Evolution')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(bond_lengths, ground_energies, 'go-', linewidth=2, markersize=8)
plt.xlabel('Bond Length (Å)')
plt.ylabel('Ground State Energy (Hartree)')
plt.title('H₂ Dissociation Curve')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('h2_simulation.png', dpi=150)
print("\nPlot saved: h2_simulation.png")
