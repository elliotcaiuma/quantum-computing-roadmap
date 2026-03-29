# Getting Started with Quantum Computing

## Complete Learning Path (Phases 1-5)

This guide covers the **complete roadmap** — from single-qubit basics through Hamiltonian simulation for quantum chemistry.

---

## Quick Start

```bash
# Clone
git clone https://github.com/elliotcaiuma/quantum-computing-roadmap.git
cd quantum-computing-roadmap

# Setup
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt

# Test
python code/foundations/01_hello_qubit.py
```

---

## Phase Overview

| Phase | Topic | PDF | Code | Prerequisites |
|-------|-------|-----|------|---------------|
| **1** | Single-Qubit | 40 pages | 9 files | Linear algebra basics |
| **2** | Multi-Qubit | 44 pages | 10 files | Phase 1 complete |
| **3** | Density Matrix | 31 pages | 9 files | Phase 2 complete |
| **4** | Algorithms | 29 pages | 6 files | Phases 1-3 complete |
| **5** | Hamiltonian Simulation | 30 pages | 8 files | Phase 4 complete |

**Total:** 174 pages + 42 code files

---

## Phase 1: Single-Qubit Foundations

**Duration:** 2-3 weeks  
**PDF:** `docs/quantum-computing-phase1.pdf`  
**Code:** `code/foundations/` (Levels 1-9)

### What You'll Learn

- Dirac notation (bras, kets, outer products)
- Qubit representation: $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$
- Bloch sphere visualization
- Single-qubit gates (X, Y, Z, H, S, T)
- Quantum measurement (Born rule)

### Code Progression

```
01_hello_qubit.py          → Create |0⟩
02_create_basis.py         → Create |0⟩, |1⟩
03_create_superposition.py → Create |+⟩, |-⟩
04_custom_state.py         → Create ANY state
05_measure_z.py            → Measure in Z basis
06_measure_any_basis.py    → Measure in X/Y/Z
07_apply_x_gate.py         → Apply X gate
08_apply_all_single_gates.py → All single gates
09_gate_transformer.py     → Apply ANY sequence
```

### Milestones

- [ ] Represent any single-qubit state
- [ ] Visualize states on Bloch sphere
- [ ] Implement all single-qubit gates
- [ ] Measure in any basis (X, Y, Z)
- [ ] Calculate measurement probabilities

### Key Equations

**Qubit state:**
$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \quad |\alpha|^2 + |\beta|^2 = 1$$

**Measurement probability:**
$$P(0) = |\alpha|^2, \quad P(1) = |\beta|^2$$

**Bloch sphere:**
$$|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$$

---

## Phase 2: Multi-Qubit Systems

**Duration:** 3-4 weeks  
**PDF:** `docs/quantum-computing-phase2.pdf`  
**Code:** `code/multi_qubit/` (Levels 11-20)

### What You'll Learn

- Tensor products and composite systems
- Entanglement and Bell states
- Multi-qubit gates (CNOT, CZ, SWAP)
- Quantum teleportation
- Superdense coding

### Code Progression

```
11_hello_2qubit.py           → Create |00⟩
12_tensor_product.py         → |0⟩ ⊗ |1⟩
13_tensor_product_calculator.py → ANY tensor product
14_create_bell_phi_plus.py   → Create |Φ⁺⟩
15_all_bell_states.py        → All 4 Bell states
16_bell_factory.py           → Create ANY Bell state
17_measure_bell.py           → Measure Bell state
18_bell_analyzer.py          → Analyze ANY Bell state
19_ancilla_measurement.py    → Ancilla-assisted measurement
20_controlled_u_decomposition.py → Universal controlled-U gate
```

### Milestones

- [ ] Compute tensor products
- [ ] Create all 4 Bell states
- [ ] Understand entanglement (non-separable states)
- [ ] Implement CNOT, CZ, SWAP gates
- [ ] Run quantum teleportation protocol
- [ ] Run superdense coding protocol

### Key Equations

**Tensor product:**
$$|0\rangle \otimes |1\rangle = |01\rangle = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}$$

**Bell state:**
$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

**CNOT gate:**
$$\text{CNOT}|00\rangle = |00\rangle, \quad \text{CNOT}|10\rangle = |11\rangle$$

---

## Phase 3: Density Matrix & Decomposition

**Duration:** 3-4 weeks  
**PDF:** `docs/quantum-computing-phase3.pdf`  
**Code:** `code/density_matrix/` (Levels 21-29)

### What You'll Learn

- Density matrix formalism (pure vs. mixed states)
- Bloch sphere for mixed states
- Purification
- Schmidt decomposition
- Entanglement detection

### Code Progression

```
21_create_density_matrix.py     → ρ = |ψ⟩⟨ψ|
22_mixed_state_ensemble.py      → ρ = Σ pᵢ|ψᵢ⟩⟨ψᵢ|
23_check_valid_density_matrix.py → Verify valid ρ
24_bloch_vector.py              → Extract Bloch vector
25_purification.py              → Construct pure state from ρ
26_schmidt_decomposition.py     → Schmidt coefficients
27_reduced_density_matrix.py    → Partial trace
28_entanglement_check.py        → Schmidt rank test
29_complete_analyzer.py         → Complete analysis
```

### Milestones

- [ ] Create density matrix from state vector
- [ ] Create density matrix from ensemble
- [ ] Verify valid density matrix (Hermitian, trace=1, PSD)
- [ ] Extract Bloch vector for mixed states
- [ ] Perform Schmidt decomposition
- [ ] Detect entanglement (Schmidt rank > 1)

### Key Equations

**Density matrix (pure):**
$$\rho = |\psi\rangle\langle\psi|$$

**Density matrix (mixed):**
$$\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|$$

**Schmidt decomposition:**
$$|\psi\rangle = \sum_i \lambda_i |u_i\rangle \otimes |v_i\rangle$$

---

## Phase 4: Quantum Algorithms

**Duration:** 4-5 weeks  
**PDF:** `docs/quantum-computing-phase4.pdf`  
**Code:** `code/algorithms/` (Levels 30-35)

### What You'll Learn

- Deutsch-Jozsa algorithm (exponential speedup)
- Grover's search (quadratic speedup)
- Quantum Fourier Transform
- Phase estimation
- Shor's factoring algorithm

### Code Progression

```
30_oracle_functions.py        → Oracle construction
31_deutsch_jozsa.py           → Constant vs. balanced
32_grover_search.py           → Unstructured search
33_phase_estimation.py        → Eigenvalue extraction
34_shor_factoring.py          → Integer factorization
35_quantum_fourier_transform.py → QFT implementation
```

### Milestones

- [ ] Implement Deutsch-Jozsa with single query
- [ ] Implement Grover's with optimal iterations
- [ ] Derive and implement QFT from scratch
- [ ] Perform phase estimation
- [ ] Factor integers using Shor's algorithm

### Key Algorithms

**Deutsch-Jozsa:** 1 query vs. $2^{n-1}+1$ classical queries

**Grover's:** $O(\sqrt{N})$ vs. $O(N)$ classical search

**QFT:** $O(n^2)$ gates vs. $O(n 2^n)$ classical FFT

---

## Phase 5: Hamiltonian Simulation

**Duration:** 4-5 weeks  
**PDF:** `docs/quantum-computing-phase5.pdf`  
**Code:** `code/hamiltonian_simulation/` (Levels 36-43)

### What You'll Learn

- Time evolution operator $e^{-iHt}$
- Lie-Trotter product formula
- First-order Trotterization
- Second-order (symmetric) Trotter
- Higher-order Suzuki expansions
- Heisenberg model simulation
- Molecular H₂ simulation

### Code Progression

```
36_time_evolution.py      → U(t) = e^{-iHt}
37_trotter_introduction.py → Commuting vs. non-commuting
38_first_order_trotter.py  → O(t²/n) scaling
39_second_order_trotter.py → O(t³/n²) scaling
40_suzuki_expansions.py   → 4th-order: O(t⁵/n⁴)
41_heisenberg_model.py    → Spin correlations
42_molecular_h2.py        → H₂ dissociation curve
43_error_analysis.py      → Resource estimation
```

### Milestones

- [ ] Implement time evolution operator
- [ ] Understand Trotter-Suzuki decomposition
- [ ] Simulate Heisenberg spin model
- [ ] Calculate molecular H₂ ground state
- [ ] Estimate resources for chemical accuracy
- [ ] Know when quantum has advantage (~8 qubits)

### Key Formulas

**Lie-Trotter:**
$$e^{-i(A+B)t} = \lim_{n\to\infty} \left(e^{-iAt/n} e^{-iBt/n}\right)^n$$

**First-order error:**
$$\text{Error} \leq \frac{t^2}{2n}\|[A,B]\|$$

**Second-order error:**
$$\text{Error} \leq \frac{t^3}{12n^2}\left(\|[A,[A,B]]\| + \|[B,[B,A]]\|\right)$$

---

## Study Tips

### 1. Read Theory First

Before running code, read the corresponding PDF section. Understand:
- What problem does this solve?
- What are the key equations?
- What is the physical meaning?

### 2. Run Code Step-by-Step

Don't just execute — modify and experiment:
- Change input states
- Vary parameters
- Break things intentionally to understand

### 3. Do the Exercises

Each PDF section has exercises. Complete them before moving on.

### 4. Build Intuition

Use the Bloch sphere visualization. Ask:
- Where is this state on the sphere?
- How does this gate move the state?
- What does measurement do?

### 5. Connect to Physics

Remember what the math represents:
- Qubits → spin-1/2 particles, photon polarization
- Gates → magnetic fields, optical elements
- Measurement → Stern-Gerlach, polarizers

---

## Common Pitfalls

### ❌ Rushing Through Foundations

**Problem:** Jumping to algorithms without mastering basics.

**Solution:** Spend adequate time on Phases 1-2. Everything builds on tensor products and entanglement.

### ❌ Not Doing Exercises

**Problem:** Passive reading without active problem-solving.

**Solution:** Complete ALL exercises. They reinforce understanding.

### ❌ Ignoring the Math

**Problem:** Treating quantum computing as just programming.

**Solution:** Work through derivations. The math IS the physics.

### ❌ Not Visualizing

**Problem:** Abstract states without geometric intuition.

**Solution:** Use Bloch sphere for every single-qubit state.

---

## Next Steps After Phase 5

After completing all 5 phases:

### Phase 6: Quantum Error Correction (Planned)
- Bit-flip and phase-flip codes
- Shor code (9-qubit)
- Steane code (7-qubit)
- Surface codes

### Advanced Topics
- Variational algorithms (VQE, QAOA)
- Quantum machine learning
- Advanced quantum simulation
- Quantum communication protocols

---

## Resources

### Textbooks
- **Nielsen & Chuang:** "Quantum Computation and Quantum Information" (standard reference)
- **Preskill's Lecture Notes:** Caltech PH219/CS219 (free online)

### Online Tools
- **IBM Quantum Experience:** Run circuits on real quantum computers
- **QuTiP:** Quantum toolbox in Python
- **Qiskit Textbook:** Interactive tutorials

### Communities
- **Qiskit Slack:** Active community
- **Quantum Computing Stack Exchange:** Q&A
- **Discord servers:** Quantum computing channels

---

## Getting Help

1. **Check the PDF:** Most answers are in the theory sections
2. **Review code comments:** Each file explains what it does
3. **Run tests:** Verify your setup works
4. **Ask questions:** Use GitHub Issues or Quantum Stack Exchange

---

*Last Updated: March 2026*
