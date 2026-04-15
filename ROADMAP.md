# Quantum Computing Foundations Roadmap

## Study Plan

This roadmap covers **foundations** - single-qubit and multi-qubit systems.

---

## Phase 1: Single-Qubit

### Topics

- Dirac notation (bras, kets, outer products)
- Qubit representation: $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$
- Bloch sphere visualization
- Single-qubit gates: X, Y, Z, H, S, T
- Measurement theory and Born rule

### Code Progression

```
01_hello_qubit.py      → Create |0⟩
02_create_basis.py     → Create |0⟩, |1⟩
03_create_superposition.py → Create |+⟩, |-⟩
04_custom_state.py     → Create ANY state (function)
05_measure_z.py        → Measure in Z basis
06_measure_any_basis.py → Measure in X/Y/Z
07_apply_x_gate.py     → Apply X gate
08_apply_all_single_gates.py → All gates
09_gate_transformer.py → Apply ANY sequence
```

### Milestone

✅ Represent any single-qubit state
✅ Visualize on Bloch sphere
✅ Implement all single-qubit gates
✅ Measure in any basis

---

## Phase 2: Multi-Qubit [COMPLETE]

### Topics

- Tensor products and composite systems
- Entanglement and Bell states (all 4 Bell states)
- Multi-qubit gates: CNOT, CZ, SWAP (with matrix representations)
- Rotation gates (R_x, R_y, R_z) and Z-Y-Z decomposition
- A-X-B-X-C decomposition for controlled-U gates
- Quantum teleportation protocol
- Superdense coding

### Code Progression

```
11_hello_2qubit.py          → Create |00⟩
12_tensor_product.py        → |0⟩ ⊗ |1⟩
13_tensor_product_calculator.py → ANY tensor product
14_create_bell_phi_plus.py  → Create |Φ⁺⟩
15_all_bell_states.py       → All 4 Bell states
16_bell_factory.py          → Create ANY Bell state
17_measure_bell.py          → Measure Bell state
18_bell_analyzer.py         → Analyze ANY Bell state
19_ancilla_measurement.py   → Ancilla-assisted measurement
20_controlled_u_decomposition.py → Universal controlled-U gate
```

### Milestone

✅ Compute tensor products
✅ Create all 4 Bell states
✅ Understand entanglement
✅ Implement CNOT, CZ, SWAP gates
✅ Run teleportation protocol
✅ Run superdense coding protocol  

---

## Phase 3: Density Matrix & Decomposition [COMPLETE]

### Topics

- Density matrix formalism (pure vs mixed states)
- Bloch sphere for mixed states (inside the sphere)
- Purification (mixed states as parts of larger pure states)
- Schmidt decomposition via SVD (complete derivation from Axler)
- Reduced density matrices and partial trace
- Entanglement detection (Schmidt rank test)
- Von Neumann entropy and purity measures

### Code Progression

```
21_create_density_matrix.py     → ρ = |ψ⟩⟨ψ| from state vector
22_mixed_state_ensemble.py      → ρ = Σ p_i |ψ_i⟩⟨ψ_i|
23_check_valid_density_matrix.py → Verify Hermitian, trace=1, PSD
24_bloch_vector.py              → Extract Bloch vector from ρ
25_purification.py              → Construct pure state from ρ
26_schmidt_decomposition.py     → Compute Schmidt coefficients
27_reduced_density_matrix.py    → Partial trace over subsystem
28_entanglement_check.py        → Check Schmidt rank
29_complete_analyzer.py         → Full density matrix analysis
```

### Milestone

✅ Distinguish pure vs mixed states  
✅ Compute Bloch vectors for mixed states  
✅ Construct purification of any mixed state  
✅ Perform Schmidt decomposition via SVD  
✅ Compute reduced density matrices  
✅ Detect entanglement via Schmidt rank  
✅ Compute von Neumann entropy  

---

## Code Philosophy

Code follows **easy → hard, specific → general**:

| Level Range | Focus | Style |
|-------------|-------|-------|
| 1-3 | Copy-paste examples | No functions |
| 4-6 | First functions | Single purpose |
| 7-9 | Gate operations | Reusable tools |
| 11-13 | Tensor products | Multi-qubit intro |
| 14-18 | Bell states | Entanglement |
| 19 | Ancilla measurement | Physical process |
| 20 | Controlled-U decomposition | Universal gate construction |
| 21-23 | Density matrix basics | Pure vs mixed states |
| 24 | Bloch vector | Mixed state visualization |
| 25 | Purification | Larger Hilbert space |
| 26-27 | Schmidt & reduced density | Entanglement analysis |
| 28-29 | Entanglement detection | Complete tools |

See `code/README.md` for details.

---

## Textbook Reference

**Quantum Computing:**
- **Nielsen & Chuang**: Chapters 1-2 (fundamental concepts), Chapter 4 (quantum circuits)

**Mathematical Reference:**
- **Linear Algebra Done Right** (Axler, 3rd ed.): Chapter 7, Section 7.C (SVD for Schmidt decomposition)

---

## Progress Tracker

| Phase | Topic | PDF | Code Levels | Status |
|-------|-------|-----|-------------|--------|
| Phase 1 | Single-Qubit Foundations | 40 pages | 1-9 | ✅ COMPLETE |
| Phase 2 | Multi-Qubit Systems | 44 pages | 11-20 | ✅ COMPLETE |
| Phase 3 | Density Matrix & Decomposition | 31 pages | 21-29 | ✅ COMPLETE |
| Phase 4 | Quantum Algorithms | 29 pages | 30-35 | ✅ COMPLETE |
| Phase 5 | Hamiltonian Simulation | 22 pages | 36-43 | ✅ COMPLETE |

**Total:** 166 pages of theory + 43 code levels

---

## Phase 4: Quantum Algorithms [COMPLETE]

### Topics

- Oracle model and phase kickback
- Deutsch-Jozsa algorithm (exponential speedup)
- Grover's search algorithm (quadratic speedup)
- Quantum phase estimation (eigenvalue extraction)
- Shor's factoring algorithm (cryptanalysis)
- Quantum Fourier Transform (complete derivation from Nielsen & Chuang)

### Code Progression

```
30_oracle_functions.py        → Construct constant/balanced oracles
31_deutsch_jozsa.py           → Distinguish constant vs balanced
32_grover_search.py           → Unstructured search with √N speedup
33_phase_estimation.py        → Extract eigenvalue phases
34_shor_factoring.py          → Factor integers via order finding
35_quantum_fourier_transform.py → QFT with O(n²) gates
```

### Milestone

✅ Implement Deutsch-Jozsa with single query  
✅ Implement Grover's with optimal iterations  
✅ Perform phase estimation on unitaries  
✅ Factor integers using Shor's algorithm  
✅ Derive and implement QFT from first principles  
✅ Analyze quantum vs classical complexity  

---

## Phase 5: Hamiltonian Simulation [COMPLETE]

### Topics

- Time evolution operator $e^{-iHt}$ and matrix exponential
- Lie-Trotter product formula and intuition
- First-order Trotterization (error scaling O(t²/n))
- Second-order symmetric Trotter / Strang splitting (error scaling O(t³/n²))
- Higher-order Suzuki expansions (4th-order: O(t⁵/n⁴))
- Heisenberg model simulation (spin-spin correlations)
- Molecular H₂ simulation (electronic structure, dissociation curve)
- Error analysis and resource estimation

### Code Progression

```
36_time_evolution.py      → U(t) = e^{-iHt}
37_trotter_introduction.py → Commuting vs. non-commuting
38_first_order_trotter.py  → O(t²/n) scaling
39_second_order_trotter.py → O(t³/n²) scaling (50-500× better)
40_suzuki_expansions.py   → 4th-order: O(t⁵/n⁴)
41_heisenberg_model.py    → Spin correlations ⟨XX⟩, ⟨YY⟩, ⟨ZZ⟩
42_molecular_h2.py        → H₂ dissociation curve
43_error_analysis.py      → Resource estimation
```

### Milestone

✅ Implement time evolution operator
✅ Understand Trotter-Suzuki decomposition
✅ Simulate Heisenberg spin model
✅ Calculate molecular H₂ ground state
✅ Estimate resources for chemical accuracy
✅ Know when quantum has advantage (~8 qubits)

---

## Transformations [NEW]

### Jordan-Wigner Transformation

Maps spin-1/2 systems to fermionic systems, enabling simulation of spin chains on quantum computers.

### Topics

- Spin operators in terms of Pauli matrices
- Fermionic creation/annihilation operators
- String operator: $S_i = \prod_{j<i} Z_j$
- Jordan-Wigner mapping:
  - $c_i = S_i \sigma_i^-$
  - $c_i^\dagger = S_i \sigma_i^+$
- Proof of fermionic anticommutation relations
- Inverse transformation: $\sigma_i^x, \sigma_i^z$ in terms of fermions
- Critical identity: $(c_i^\dagger + c_i) Z_i = c_i^\dagger - c_i$
- Application to transverse Ising model
- Bogoliubov transformation (momentum space diagonalization)

### Milestone

✅ Understand why we need fermionization  
✅ Derive JW transformation from first principles  
✅ Prove anticommutation relations  
✅ Transform Ising Hamiltonian to fermionic form  
✅ Diagonalize via Bogoliubov transform  
✅ Extract dispersion relation  

---

## Conformal Field Theory [NEW]

### Entanglement Entropy in 1+1D CFT

Universal formula for entanglement entropy using replica trick and twist fields.

### Topics

- Reduced density matrix and partial trace
- Von Neumann entropy vs. Rényi entropies
- Replica trick: $S_A = -\lim_{n \to 1} \frac{\partial}{\partial n} \text{Tr}(\rho_A^n)$
- Path integral representation on $n$-sheeted Riemann surface
- Twist fields as boundary condition changing operators
- Uniformizing map: Möbius transformation + power map
- Stress tensor transformation and Schwarzian derivative
- Scaling dimension: $\Delta_n = \frac{c}{12}(n - 1/n)$
- Virasoro generators and orbifold CFT
- Partition function ratio: $Z_n/(Z_1)^n = \langle \mathcal{T}_n(u) \tilde{\mathcal{T}}_n(v) \rangle$
- Main result: $S_A = \frac{c}{3} \ln(L/a) + \text{const}$
- Numerical verification via correlation matrix method

### Milestone

✅ Understand replica trick and why it works  
✅ Derive path integral representation of Tr(ρ_A^n)  
✅ Explain twist fields and their role  
✅ Compute scaling dimension via Schwarzian  
✅ Derive uniformizing map construction  
✅ Verify CFT prediction numerically for Ising model  

---

## Next Steps

After completing all 5 phases:
- **Phase 6: Quantum Error Correction** (planned)
  - Bit-flip and phase-flip codes
  - Shor code (9-qubit)
  - Steane code (7-qubit)
  - Surface codes and fault tolerance
  
- **Variational methods** (VQE, QAOA) for NISQ devices
- **Advanced quantum simulation** (chemistry, materials science)
- **Quantum machine learning** (QML algorithms)

---

*Last Updated: March 2026*
