# Ising Model Project

Comprehensive study of the transverse Ising model: mean-field theory (Phase 1) and quantum simulation (Phase 2+).

## Project Overview

This project studies the 1D transverse Ising model from two complementary perspectives:

### Phase 1: Mean-Field Theory (Analytical) ✅ COMPLETE
- **Goal:** Understand phase transitions, critical behavior, and order parameters
- **Method:** Mean-field approximation with self-consistent solutions
- **Output:** Analytical formulas for $T_c$, $\Gamma_c$, order parameter $\langle \sigma^z \rangle$
- **Documentation:** `ising_docs/ising-phase1-mean-field.pdf` (27 pages)
- **Code:** 3 educational Python modules

### Phase 2: Exact Diagonalization (Numerical) 🚧 PLANNED
- **Goal:** Benchmark mean-field results against exact solutions
- **Method:** Full diagonalization for small systems (N ≤ 20)
- **Output:** Ground state energy, magnetization, correlation functions

### Phase 3: Quantum Simulation (Trotter-Suzuki) 🚧 PLANNED
- **Goal:** Simulate quantum dynamics on quantum circuits
- **Method:** Trotter-Suzuki decomposition
- **Output:** Time evolution, quench dynamics, thermalization

---

## Hamiltonian

The transverse Ising Hamiltonian is:

$$H = -J_0 \sum_{\langle i,j \rangle} \sigma_i^z \sigma_j^z - \Gamma \sum_i \sigma_i^x$$

Where:
- $J_0$: Exchange coupling constant (energy scale)
- $\Gamma$: Transverse field strength (quantum fluctuations)
- $\sigma_i^{x,z}$: Pauli operators at site $i$ (eigenvalues $\pm 1$)
- $\langle i,j \rangle$: Sum over nearest-neighbor pairs

### Physical Meaning

| Term | Physics | Effect |
|------|---------|--------|
| $-J_0 \sigma_i^z \sigma_j^z$ | Ising interaction | Favors $z$-axis alignment (ferromagnetic for $J_0 > 0$) |
| $-\Gamma \sigma_i^x$ | Transverse field | Quantum fluctuations, favors $x$-axis alignment |

**Competition:** These terms don't commute → quantum phase transition at $\Gamma_c = J_0 z$

---

## Project Structure

```
projects/ising_model/
├── README.md                    # This file (project overview)
├── PHASE1_README.md             # Phase 1 detailed guide
│
├── ising_docs/                  # Documentation (PDFs)
│   └── ising-phase1-mean-field.pdf    # 27-page comprehensive theory + code
│
├── code/                        # Python code modules
│   ├── ising_01_mean_field_core.py    # Core functions (self-consistency, T_c, Γ_c)
│   ├── ising_02_phase_diagram.py      # Phase boundary visualization
│   ├── ising_03_order_parameter.py    # Order parameter plots
│   ├── ising_04_jw_operators.py       # JW fermionic operators
│   ├── ising_05_verify_anticommutation.py  # Verify fermionic statistics
│   ├── ising_06_jw_hamiltonian.py     # Fermionic Hamiltonian
│   └── ising_07_compare_representations.py  # Spin vs. fermion comparison
│
├── scripts/                     # Utility scripts (Phase 2+)
│   └── (to be added)
│
└── results/                     # Generated outputs
    └── (to be added)
```

---

## Phase 1: Mean-Field Theory (Complete)

### Key Results

| Quantity | Formula | Physical Meaning |
|----------|---------|------------------|
| **Molecular field** | $h^z = J_0 z \langle \sigma^z \rangle$ | Effective field from neighbors |
| **Field magnitude** | $h = \sqrt{\Gamma^2 + (J_0 z \langle \sigma^z \rangle)^2}$ | Total effective field |
| **Self-consistency** | $\langle \sigma^z \rangle = \frac{s J_0 z \langle \sigma^z \rangle}{h} \tanh(\beta h s)$ | Order parameter equation |
| **Critical temperature** | $T_c = \frac{\Gamma s}{k_B \, \text{arctanh}(\Gamma/(J_0 z s))}$ | Phase boundary |
| **Quantum critical point** | $\Gamma_c = J_0 z s$ | $T=0$ transition |
| **Ground state** | $\langle \sigma^z \rangle_{T=0} = s\sqrt{1 - (\Gamma/\Gamma_c)^2}$ | Zero-T order parameter |
| **Sum rule** | $\langle \sigma^z \rangle^2 + \langle \sigma^x \rangle^2 = s^2$ | Fixed spin length |

### Code Modules

| File | Lines | Purpose | Key Functions |
|------|-------|---------|---------------|
| `ising_01_mean_field_core.py` | ~400 | Core equations & solvers | `effective_field()`, `solve_self_consistency()`, `critical_temperature()`, `ground_state_order()` |
| `ising_02_phase_diagram.py` | ~230 | Phase boundary plot | `plot_phase_diagram()` |
| `ising_03_order_parameter.py` | ~400 | Order parameter plots | `plot_order_vs_temperature()`, `plot_order_vs_gamma()` |

### Running Phase 1 Code

```bash
# Navigate to code directory
cd projects/ising_model/code

# Run core functions (with test suite)
python ising_01_mean_field_core.py

# Generate phase diagram
python ising_02_phase_diagram.py

# Generate order parameter plots
python ising_03_order_parameter.py
```

**Expected Output:**
```
============================================================
Mean-Field Core Functions - Test Suite
============================================================

Parameters: J0 = 1.0, z = 1

Test Case 1: Pauli Matrix Convention (s = 1)
  Gamma_c = J0*z*s = 1.000
  T_c = 0.9692
  <sigma^z> at T=0: 0.9539
  Sum rule: <sigma^z>^2 + <sigma^x>^2 = 1.0000 ✓
```

### Phase Diagram

The phase boundary in the $(T, \Gamma)$ plane:

- **Ordered phase** ($\langle \sigma^z \rangle \neq 0$): $T < T_c(\Gamma)$ AND $\Gamma < \Gamma_c$
- **Disordered phase** ($\langle \sigma^z \rangle = 0$): $T > T_c(\Gamma)$ OR $\Gamma > \Gamma_c$
- **Quantum critical point**: $(\Gamma_c, T=0)$

---

## Future Phases

### Phase 2: Exact Diagonalization

**Goals:**
- Solve small systems exactly (no mean-field approximation)
- Benchmark mean-field results
- Study finite-size effects

**Planned Code:**
- `ising_04_exact_diagonalization.py`: Full diagonalization for N ≤ 20
- `ising_05_ground_state.py`: Ground state properties
- `ising_06_correlations.py`: Spin-spin correlation functions

### Phase 3: Quantum Simulation

**Goals:**
- Implement Trotter-Suzuki decomposition
- Simulate real-time dynamics
- Study quench dynamics and thermalization

**Planned Code:**
- `ising_07_trotter_circuit.py`: Quantum circuit implementation
- `ising_08_time_evolution.py`: Real-time dynamics
- `ising_09_quench.py`: Quantum quench protocols

---

## Physics Summary

### Mean-Field Approximation

Replace many-body interaction with effective single-particle field:

$$\sigma_i^z \sigma_j^z \approx \langle \sigma^z \rangle(\sigma_i^z + \sigma_j^z) - \langle \sigma^z \rangle^2$$

**Physical meaning:** Each spin feels the average field from all neighbors, not instantaneous interactions.

**Limitations:**
- Neglects fluctuations (critical near $T_c$)
- Overestimates $T_c$ by 10-30%
- Incorrect critical exponents ($\beta = 1/2$ vs. exact $\beta = 1/8$ in 2D)

### Quantum Phase Transition

At $T = 0$, varying $\Gamma$ drives a transition at $\Gamma = \Gamma_c$:

| Region | Physics | Order Parameter |
|--------|---------|-----------------|
| $\Gamma < \Gamma_c$ | Ferromagnetic order | $\langle \sigma^z \rangle \neq 0$ |
| $\Gamma > \Gamma_c$ | Quantum paramagnet | $\langle \sigma^z \rangle = 0$ |

**Key insight:** This transition is driven by **quantum fluctuations** (zero-point motion), not thermal fluctuations.

### Critical Behavior

Near the transition, the order parameter follows:

$$\langle \sigma^z \rangle \propto (T_c - T)^{1/2} \quad \text{(thermal)}$$
$$\langle \sigma^z \rangle \propto (\Gamma_c - \Gamma)^{1/2} \quad \text{(quantum)}$$

The exponent $\beta = 1/2$ is the **mean-field critical exponent**.

---

## Documentation

| Document | Location | Description |
|----------|----------|-------------|
| **Project overview** | `README.md` | This file |
| **Phase 1 guide** | `PHASE1_README.md` | Detailed Phase 1 instructions, exercises, references |
| **Theory + Code PDF** | `ising_docs/ising-phase1-mean-field.pdf` | 27-page comprehensive derivation with integrated code |

---

## References

### Core Materials
1. **Phase 1 PDF:** `ising-phase1-mean-field.pdf` (27 pages, complete mean-field theory)
2. **Reference PDF:** `chapter01-mean-field.pdf`
3. **Reference Code:** `1_ising_mean_field.py`

### Textbooks
4. **Sachdev, S. (2011).** *Quantum Phase Transitions* (2nd ed.). Cambridge University Press.
   - Chapter 1: Quantum Ising model
   - Chapter 4: Mean-field theory
   - Chapter 5: Quantum criticality

5. **Continentino, M. A. (2017).** *Quantum Scaling in Many-Body Systems* (2nd ed.). Cambridge University Press.
   - Chapter 2: Mean-field approximation
   - Chapter 3: Quantum phase transitions

6. **Goldenfeld, N. (1992).** *Lectures on Phase Transitions and the Renormalization Group*. Addison-Wesley.
   - Chapter 2: Landau theory and mean-field
   - Chapter 4: Critical exponents

7. **Altland, A. & Simons, B. D. (2010).** *Condensed Matter Field Theory* (2nd ed.). Cambridge University Press.
   - Chapter 2: Second quantization
   - Chapter 5: Spontaneous symmetry breaking

### Online Resources
8. **Wikipedia:** Transverse-field Ising model - https://en.wikipedia.org/wiki/Transverse-field_Ising_model
9. **Stanford Encyclopedia:** Quantum Phase Transitions - https://plato.stanford.edu/entries/quantum-phase-transitions/

---

## Contributing

This project is part of the larger Quantum Computing Roadmap. For questions or contributions:

- **Repository:** https://github.com/elliotcaiuma/quantum-computing-roadmap
- **Issues:** https://github.com/elliotcaiuma/quantum-computing-roadmap/issues

---

*Phase 1 completed: March 2026*  
*Author: Cai Yundi Elliot*
