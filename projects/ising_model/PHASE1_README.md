# Phase 1: Mean-Field Theory

## Overview

Mean-field theory for the transverse Ising model using Pauli matrix notation.

**Reference materials:**
- PDF: `chapter01-mean-field.pdf`
- Code: `1_ising_mean_field.py`

## Hamiltonian

$$H = -J_0 \sum_{\langle i,j \rangle} \sigma_i^z \sigma_j^z - \Gamma \sum_i \sigma_i^x$$

where $\sigma^{x,z}$ are Pauli matrices with eigenvalues $\pm 1$.

## Key Equations

| Quantity | Formula |
|----------|---------|
| Effective field | $h = \sqrt{\Gamma^2 + (J_0 z \langle \sigma^z \rangle)^2}$ |
| Self-consistency | $\langle \sigma^z \rangle = \frac{J_0 z \langle \sigma^z \rangle}{h} \tanh\left(\beta h\right)$ |
| Critical temperature | $T_c = \frac{\Gamma}{k_B \, \text{arctanh}(\Gamma/J_0 z)}$ |
| Quantum critical point | $\Gamma_c = J_0 z$ |
| Ground state | $\langle \sigma^z \rangle_{T=0} = \sqrt{1 - (\Gamma/J_0 z)^2}$ |

## Code Structure

Phase 1 consists of 3 educational modules:

| File | Purpose | Lines | Educational Focus |
|------|---------|-------|-------------------|
| `01_mean_field_core.py` | Core equations & solvers | ~300 | Functions with detailed docstrings, physical interpretation, test suite |
| `02_phase_diagram.py` | Phase boundary plot | ~230 | Visualization of phase transition, annotated plots |
| `03_order_parameter.py` | Order parameter plots | ~400 | Temperature/field dependence, quantum vs thermal transitions |

## Running the Code

### Prerequisites
```bash
pip install numpy matplotlib scipy
```

### Step 1: Core Functions (with tests)
```bash
python code/01_mean_field_core.py
```

**What it does:**
- Tests all core functions
- Verifies analytical formulas
- Shows expected vs actual values

**Output:**
```
Test 1: Critical Temperature
  Γ/Γ_c = 0.3
  T_c = 0.9539
  Expected: T_c > 0 (ordered phase exists)

Test 2: Ground State (T = 0)
  ⟨σᶻ⟩ at T=0: 0.9539
  Expected:   0.9539
  Analytical: √(1 - (Γ/Γ_c)²) = 0.9539
```

### Step 2: Phase Diagram
```bash
python code/02_phase_diagram.py
```

**What it does:**
- Plots phase boundary in (T, Γ) plane
- Shows ordered vs disordered regions
- Marks quantum critical point

**Learning points:**
- How T_c depends on Γ
- Meaning of quantum critical point
- Difference between thermal and quantum transitions

### Step 3: Order Parameter Plots
```bash
python code/03_order_parameter.py
```

**What it does:**
- Plot 1: ⟨σᶻ⟩ vs T for various Γ
- Plot 2: ⟨σᶻ⟩ and ⟨σˣ⟩ vs T (competition)
- Plot 3: ⟨σᶻ⟩ at T=0 vs Γ (quantum transition)

**Learning points:**
- How thermal fluctuations destroy order
- Role of quantum fluctuations
- Critical behavior near T_c and Γ_c

## Physics Summary

### Mean-Field Approximation

Replace many-body interaction with effective single-particle field:

$$\sigma_i^z \sigma_j^z \approx \langle \sigma^z \rangle(\sigma_i^z + \sigma_j^z) - \langle \sigma^z \rangle^2$$

**Physical meaning:** Each spin feels the average field from all neighbors, not instantaneous interactions.

### Phases

| Phase | Condition | Order Parameter |
|-------|-----------|-----------------|
| **Ordered** | $\Gamma < \Gamma_c$ AND $T < T_c$ | $\langle \sigma^z \rangle \neq 0$ |
| **Disordered** | $\Gamma \geq \Gamma_c$ OR $T \geq T_c$ | $\langle \sigma^z \rangle = 0$ |

### Quantum Phase Transition

At $T = 0$, varying $\Gamma$ drives a transition at $\Gamma = \Gamma_c$:

| Region | Physics |
|--------|---------|
| $\Gamma < \Gamma_c$ | Ferromagnetic order (spins align along z) |
| $\Gamma > \Gamma_c$ | Quantum paramagnet (spins align along x) |

**Key insight:** This transition is driven by **quantum fluctuations** (zero-point motion), not thermal fluctuations.

### Critical Behavior

Near the transition, the order parameter follows:

$$\langle \sigma^z \rangle \propto (T_c - T)^{1/2} \quad \text{(thermal)}$$
$$\langle \sigma^z \rangle \propto (\Gamma_c - \Gamma)^{1/2} \quad \text{(quantum)}$$

The exponent $\beta = 1/2$ is the **mean-field critical exponent**.

## Exercises

### Exercise 1: Classical Limit
**Task:** Show $T_c(\Gamma \to 0) = J_0 z / k_B$.

**Hint:** Use $\text{arctanh}(x) \approx x$ for small $x$.

### Exercise 2: Ground State
**Task:** Verify $\langle \sigma^x \rangle_{T=0} = \Gamma / (J_0 z)$.

**Hint:** Use $\langle \sigma^x \rangle = \tanh(\beta h) \cdot (\Gamma/h)$ and take $T \to 0$.

### Exercise 3: Critical Exponent
**Task:** Near $T_c$, show $\langle \sigma^z \rangle \propto (T_c - T)^{1/2}$.

**Hint:** Expand the self-consistency equation for small $\langle \sigma^z \rangle$ and $T \approx T_c$.

### Exercise 4: Coordination Number
**Task:** Modify the code to test different $z$ values (1, 2, 4, 6).

**Question:** How does $\Gamma_c$ scale with $z$?

**Answer:** $\Gamma_c = J_0 z$ (linear scaling).

## Code Documentation Guide

Each module is designed for learning:

### 1. Module Docstring
- Physical background
- Key equations
- Usage examples

### 2. Function Docstrings
- Purpose and physics
- Parameter descriptions
- Return value explanation
- Special cases and limits
- Example calculations

### 3. Inline Comments
- Explain non-obvious steps
- Connect code to equations
- Highlight physical interpretation

### 4. Test Suite (in `01_mean_field_core.py`)
- Verify analytical limits
- Check edge cases
- Show expected outputs

## Common Questions

**Q: Why use Pauli matrices (σ) instead of spin operators (S)?**

A: Pauli matrices have eigenvalues $\pm 1$, which simplifies the equations (no factors of 1/2). This is standard in quantum information and condensed matter.

**Q: What is the coordination number z?**

A: Number of nearest neighbors. For mean-field theory, we typically use $z = 1$ as an effective parameter. Real lattices: 1D chain ($z=2$), square lattice ($z=4$), cubic lattice ($z=6$).

**Q: Why is there no PNG output?**

A: The plots are for interactive learning. Run the scripts to see them displayed. You can modify the code to save figures if needed.

**Q: What happens if I change J₀ or k_B?**

A: These are scale factors. The physics depends only on dimensionless ratios: $T/T_c$ and $\Gamma/\Gamma_c$.

## Next Steps

After mastering Phase 1:

**Phase 2: Exact Diagonalization**
- Solve small systems exactly (no mean-field approximation)
- Benchmark mean-field results
- See where mean-field theory breaks down

**Phase 3: Larger Systems**
- Use numerical methods (Lanczos, DMRG)
- Study finite-size effects
- Compare with mean-field predictions

## Documentation

- **LaTeX source:** `../../report-latex/ising/ising-phase1-mean-field.tex` (outside repo)
- **PDF:** `ising_docs/ising-phase1-mean-field.pdf` (27 pages, comprehensive theory + code)
- **This guide:** `PHASE1_README.md`

## References

### Core Materials
1. **PDF Notes:** `ising-phase1-mean-field.pdf` (27 pages, complete mean-field theory derivation)
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
