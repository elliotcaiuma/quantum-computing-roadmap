# Ising Model Project

Comprehensive study of the transverse Ising model: mean-field theory (Phase 1) and quantum simulation (Phase 2+).

## Overview

This project studies the 1D transverse Ising model from two complementary perspectives:

### Phase 1: Mean-Field Theory (Analytical)
- **Goal:** Understand phase transitions, critical behavior, and order parameters
- **Method:** Mean-field approximation with self-consistent solutions
- **Output:** Analytical formulas for $T_c$, $\Gamma_c$, order parameter $\langle \sigma^z \rangle$
- **Documentation:** `ising_docs/ising-phase1-mean-field.pdf` (27 pages)

### Phase 2+: Quantum Simulation (Numerical)
- **Goal:** Simulate quantum dynamics and benchmark against mean-field theory
- **Method:** Trotter-Suzuki decomposition with quantum circuits
- **Output:** Time evolution, ground state energy, correlation functions
- **Code:** `code/02_exact_diagonalization.py` and beyond

### Hamiltonian

The transverse Ising Hamiltonian is:

$$H = -J_0 \sum_{\langle i,j \rangle} \sigma_i^z \sigma_j^z - \Gamma \sum_i \sigma_i^x$$

Where:
- $J_0$: Exchange coupling constant (energy scale)
- $\Gamma$: Transverse field strength (quantum fluctuations)
- $\sigma_i^{x,z}$: Pauli operators at site $i$ (eigenvalues $\pm 1$)
- $\langle i,j \rangle$: Sum over nearest-neighbor pairs

## Structure

```
ising_model/
├── README.md
├── docs/
│   ├── ising-theory.pdf          → Mathematical derivation
│   ├── trotter-decomposition.pdf → Simulation method
│   └── results.pdf               → Simulation results
├── code/
│   ├── 01_ising_hamiltonian.py   → Hamiltonian construction
│   ├── 02_exact_diagonalization.py → Classical baseline
│   ├── 03_trotter_circuit.py     → Quantum circuit
│   ├── 04_ground_state.py        → Variational preparation
│   └── 05_correlations.py        → Measure ⟨ZZ⟩, ⟨XX⟩
├── scripts/
│   ├── run_all.py                → Run all simulations
│   └── plot_results.py           → Generate figures
└── results/
    └── (generated outputs)
```

## Physics Background

### Transverse Ising Model

The Hamiltonian exhibits a quantum phase transition at $h/J = 1$:

- **$h \ll J$ (ordered phase):** Spins align (ferromagnetic) or anti-align (antiferromagnetic)
- **$h \gg J$ (disordered phase):** Spins polarized along $x$-direction
- **$h = J$ (critical point):** Quantum phase transition, gap closes

### Key Observables

1. **Magnetization:** $\langle X \rangle = \frac{1}{N}\sum_i \langle X_i \rangle$
2. **Spin correlations:** $\langle Z_i Z_{i+1} \rangle$
3. **Energy:** $\langle H \rangle$ (ground state energy)
4. **Gap:** Energy difference between ground and first excited state

## Simulation Method

### Trotter-Suzuki Decomposition

Time evolution operator:
$$U(t) = e^{-iHt} \approx \left(e^{-iH_Z \delta t} e^{-iH_X \delta t}\right)^n$$

Where:
- $H_Z = -J \sum_i Z_i Z_{i+1}$ (commuting terms)
- $H_X = -h \sum_i X_i$ (commuting terms)
- $\delta t = t/n$ (time step)

### Circuit Implementation

**ZZ interaction:**
```
e^{-iθ Z₁Z₂} = CNOT(1,2) · R_z(2θ) on qubit 2 · CNOT(1,2)
```

**X rotation:**
```
e^{-iθ X} = R_x(2θ)
```

## Getting Started

### Prerequisites

```bash
cd quantum-roadmap-repo
source venv/bin/activate  # or .\venv\Scripts\Activate.ps1
```

### Run Simulations

```bash
# Run all simulations
python scripts/run_all.py

# Generate plots
python scripts/plot_results.py
```

### Individual Code Files

```bash
# Build Hamiltonian
python code/01_ising_hamiltonian.py

# Classical exact diagonalization (small N)
python code/02_exact_diagonalization.py

# Quantum Trotter circuit
python code/03_trotter_circuit.py

# Ground state preparation
python code/04_ground_state.py

# Measure correlations
python code/05_correlations.py
```

## Expected Results

### Ground State Energy

| N | J | h | E₀ (exact) | E₀ (Trotter) | Error |
|---|---|---|------------|--------------|-------|
| 2 | 1 | 0.5 | -2.236 | -2.230 | 0.3% |
| 3 | 1 | 0.5 | -3.354 | -3.340 | 0.4% |
| 4 | 1 | 0.5 | -4.472 | -4.450 | 0.5% |

### Phase Transition

At $N \to \infty$:
- **Ordered phase** ($h/J < 1$): $\langle Z \rangle \neq 0$
- **Disordered phase** ($h/J > 1$): $\langle Z \rangle = 0$
- **Critical point** ($h/J = 1$): Gap closes as $1/N$

## Extensions

1. **2D Ising model:** Add $Z_i Z_j$ terms for 2D lattice
2. **Long-range interactions:** Power-law decay $1/r^\alpha$
3. **Disorder:** Random $J_i$ or $h_i$ (many-body localization)
4. **Dynamics:** Quench dynamics, thermalization
5. **VQE:** Variational ground state search

## References

- Sachdev, S. (2011). *Quantum Phase Transitions* (2nd ed.)
- Nielsen & Chuang (2010). *Quantum Computation and Quantum Information*
- Preskill (2018). "Quantum Computing in the NISQ Era"

---

*Project created: March 2026*
