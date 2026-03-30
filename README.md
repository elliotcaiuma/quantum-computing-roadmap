# Quantum Computing Roadmap

A beginner-friendly learning path for mastering quantum computing fundamentals with hands-on Qiskit implementations.

![Quantum Computing](https://img.shields.io/badge/Quantum-Roadmap-blue)
![Qiskit](https://img.shields.io/badge/Qiskit-2.x-purple)
![License](https://img.shields.io/badge/License-MIT-green)
![Lint](https://github.com/elliotcaiuma/quantum-computing-roadmap/actions/workflows/lint.yml/badge.svg)
![Tests](https://github.com/elliotcaiuma/quantum-computing-roadmap/actions/workflows/test.yml/badge.svg)

## Overview

This repository focuses on **quantum computing foundations** — single-qubit and multi-qubit systems. Based on Nielsen & Chuang's textbook with practical Qiskit code.

## What's Covered

### Phase 1: Single-Qubit Foundations [COMPLETE]
- Dirac notation and bra-ket formalism
- Qubit representation
- Bloch sphere visualization
- Single-qubit gates (X, Y, Z, H, S, T) with geometric interpretations
- Quantum measurement (complete mathematical treatment)

**Theory:** Read `docs/quantum-computing-phase1.pdf` (40 pages)

**Code:** Levels 1-9 in `code/foundations/`

### Phase 2: Multi-Qubit Systems [COMPLETE]
- Tensor products and composite systems
- Entanglement and Bell states (all 4 Bell states)
- Multi-qubit gates (CNOT, CZ, SWAP) with matrix representations
- Rotation gates (R_x, R_y, R_z) and Z-Y-Z decomposition
- A-X-B-X-C decomposition for controlled-U gates
- Quantum teleportation
- Superdense coding

**Theory:** Read `docs/quantum-computing-phase2.pdf` (44 pages)

**Code:** Levels 11-20 in `code/multi_qubit/`

### Phase 3: Density Matrix & Decomposition [COMPLETE]
- Density matrix formalism (pure vs mixed states)
- Bloch sphere for mixed states
- Purification (mixed states as parts of larger pure states)
- Schmidt decomposition via SVD (complete derivation)
- Reduced density matrices and partial trace
- Entanglement detection (Schmidt rank test)
- Von Neumann entropy and purity measures

**Theory:** Read `docs/quantum-computing-phase3.pdf` (31 pages)

**Code:** Levels 21-29 in `code/density_matrix/`

### Phase 4: Quantum Algorithms [COMPLETE]
- Deutsch-Jozsa algorithm (exponential speedup demonstration)
- Grover's search algorithm (quadratic speedup, amplitude amplification)
- Quantum phase estimation (eigenvalue extraction)
- Shor's factoring algorithm (cryptanalysis application)
- Quantum Fourier Transform (QFT) with complete derivation

**Theory:** Read `docs/quantum-computing-phase4.pdf` (29 pages)

**Code:** Levels 30-35 in `code/algorithms/`

### Phase 5: Hamiltonian Simulation [COMPLETE]
- Time evolution operator $e^{-iHt}$ and matrix exponential
- Lie-Trotter product formula (complete derivation)
- First-order Trotterization (error bound: $O(t^2/n)$)
- Second-order symmetric Trotter / Strang splitting (error bound: $O(t^3/n^2)$)
- Higher-order Suzuki expansions (4th-order: $O(t^5/n^4)$)
- Heisenberg model simulation (spin-spin correlations ⟨XX⟩, ⟨YY⟩, ⟨ZZ⟩)
- Molecular H₂ simulation (electronic structure, dissociation curve)
- Error analysis and resource estimation (chemical accuracy, quantum advantage)

**Theory:** Read `docs/quantum-computing-phase5.pdf` (30 pages)

**Code:** Levels 36-43 in `code/hamiltonian_simulation/`

**Key Results:**
- 2nd-order Trotter: 50-500× better accuracy than 1st-order
- 4th-order Suzuki: Optimal for chemical accuracy (ε ~ 10⁻³)
- Quantum advantage: Emerges at ~8 qubits for simulation tasks

### Ising Model Project: Mean-Field Theory [COMPLETE]
- Transverse Ising model Hamiltonian
- Mean-field approximation and self-consistency
- Quantum phase transitions and critical phenomena
- Order parameter, critical temperature, quantum critical point
- Spin factor $s$ for generality (Pauli vs. true spin-1/2)

**Theory:** Read `projects/ising_model/ising_docs/ising-phase1-mean-field.pdf` (27 pages)

**Code:** `projects/ising_model/code/` (3 educational modules)

**Key Results:**
- Analytical $T_c(\Gamma)$ formula with full derivation
- Quantum critical point $\Gamma_c = J_0 z s$
- Sum rule verification: $\langle \sigma^z \rangle^2 + \langle \sigma^x \rangle^2 = s^2$

## Quick Start

```bash
# Clone
git clone https://github.com/elliotcaiuma/quantum-computing-roadmap.git
cd quantum-roadmap

# Setup
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt

# Run first code
python code/foundations/01_hello_qubit.py
```

## Structure

```
quantum-computing-roadmap/
├── README.md
├── ROADMAP.md
├── SETUP.md
├── requirements.txt
│
├── code/
│   ├── foundations/     # Levels 1-9: Single-qubit foundations
│   │   ├── 01_hello_qubit.py
│   │   ├── 02_create_basis.py
│   │   ├── 03_create_superposition.py
│   │   ├── 04_custom_state.py
│   │   ├── 05_measure_z.py
│   │   ├── 06_measure_any_basis.py
│   │   ├── 07_apply_x_gate.py
│   │   ├── 08_apply_all_single_gates.py
│   │   └── 09_gate_transformer.py
│   ├── multi_qubit/     # Levels 11-20: Multi-qubit systems
│   │   ├── 11_hello_2qubit.py
│   │   ├── 12_tensor_product.py
│   │   ├── 13_tensor_product_calculator.py
│   │   ├── 14_create_bell_phi_plus.py
│   │   ├── 15_all_bell_states.py
│   │   ├── 16_bell_factory.py
│   │   ├── 17_measure_bell.py
│   │   ├── 18_bell_analyzer.py
│   │   ├── 19_ancilla_measurement.py
│   │   └── 20_controlled_u_decomposition.py
│   └── density_matrix/  # Levels 21-29: Density matrix & decomposition
│       ├── 21_create_density_matrix.py
│       ├── 22_mixed_state_ensemble.py
│       ├── 23_check_valid_density_matrix.py
│       ├── 24_bloch_vector.py
│       ├── 25_purification.py
│       ├── 26_schmidt_decomposition.py
│       ├── 27_reduced_density_matrix.py
│       ├── 28_entanglement_check.py
│       └── 29_complete_analyzer.py
│   ├── algorithms/      # Levels 30-35: Quantum algorithms
│   │   ├── 30_oracle_functions.py
│   │   ├── 31_deutsch_jozsa.py
│   │   ├── 32_grover_search.py
│   │   ├── 33_phase_estimation.py
│   │   ├── 34_shor_factoring.py
│   │   └── 35_quantum_fourier_transform.py
│   └── hamiltonian_simulation/  # Levels 36-43: Hamiltonian simulation
│       ├── 36_time_evolution.py
│       ├── 37_trotter_introduction.py
│       ├── 38_first_order_trotter.py
│       ├── 39_second_order_trotter.py
│       ├── 40_suzuki_expansions.py
│       ├── 41_heisenberg_model.py
│       ├── 42_molecular_h2.py
│       └── 43_error_analysis.py
│
├── docs/
│   ├── quantum-computing-phase1.pdf    (40 pages, single-qubit foundations) [COMPLETE]
│   ├── quantum-computing-phase2.pdf    (44 pages, multi-qubit systems) [COMPLETE]
│   ├── quantum-computing-phase3.pdf    (31 pages, density matrix & decomposition) [COMPLETE]
│   ├── quantum-computing-phase4.pdf    (29 pages, quantum algorithms) [COMPLETE]
│   └── quantum-computing-phase5.pdf    (30 pages, Hamiltonian simulation) [COMPLETE]
│
│   **Total:** 174 pages of theory covering complete foundations through quantum simulation
│
├── study_guides/
│   └── getting-started.md            → Complete learning guide for Phases 1-5
│
└── progress/
    └── tracker.md                    → Progress tracking and statistics
```

## Summary Statistics

| Metric | Count |
|--------|-------|
| **PDF Pages** | 201 (174 roadmap + 27 Ising) |
| **Code Files** | 45 (42 roadmap + 3 Ising) |
| **Code Levels** | 43 + 3 (Ising modules) |
| **Algorithms** | 7 (Deutsch-Jozsa, Grover, QFT, Phase Estimation, Shor, Trotter, Suzuki) |
| **Physical Models** | 3 (Heisenberg, H₂, Transverse Ising) |
| **Projects** | 2 (Quantum Roadmap, Ising Model) |
| **Estimated Study Time** | 16-21 weeks |

## Code Progression

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
| 21-29 | Density matrix | Mixed state analysis |
| 30 | Oracle functions | Black-box abstraction |
| 31 | Deutsch-Jozsa | Exponential speedup |
| 32 | Grover's search | Amplitude amplification |
| 33 | Phase estimation | Eigenvalue extraction |
| 34 | Shor's algorithm | Order finding |
| 35 | QFT | Fourier analysis |
| 36 | Time evolution | Matrix exponential |
| 37 | Trotter intro | Product formulas |
| 38 | 1st-order Trotter | O(t²/n) scaling |
| 39 | 2nd-order Trotter | O(t³/n²) scaling |
| 40 | Suzuki expansions | Higher-order formulas |
| 41 | Heisenberg model | Spin correlations |
| 42 | Molecular H₂ | Quantum chemistry |
| 43 | Error analysis | Resource estimation |

See `code/README.md` for details.

## References

### Quantum Computing

**Nielsen & Chuang** - *Quantum Computation and Quantum Information*:
- Chapters 1-2: Fundamental concepts
- Chapter 4: Quantum circuits

### Mathematics

**Linear Algebra Done Right** (Axler, 3rd ed.):
- Chapter 7: Singular Value Decomposition (Section 7.C)
- Used for Schmidt decomposition derivation (Phase 3)

### Ising Model & Many-Body Physics

**Quantum Ising Phases** - Reference PDF:
- Location: `C:\Users\Elliot Cai\.openclaw\workspace-learning-agent\quantum-computing\references\ising\Quantum Ising Phases.pdf`
- Content: Complete derivation of transverse Ising model phase diagram
- Used for: Mean-field theory, quantum critical point, order parameter analysis

**Sachdev, S. (2011)** - *Quantum Phase Transitions* (2nd ed.), Cambridge University Press:
- Chapter 1: Quantum Ising model
- Chapter 4: Mean-field theory
- Chapter 5: Quantum criticality

**Continentino, M. A. (2017)** - *Quantum Scaling in Many-Body Systems* (2nd ed.), Cambridge University Press:
- Chapter 2: Mean-field approximation
- Chapter 3: Quantum phase transitions

## Resources

- Qiskit Textbook: https://qiskit.org/textbook
- Qiskit Docs: https://qiskit.org/documentation
- IBM Quantum: https://quantum.ibm.com

## 📄 License

MIT License

## 👨‍💻 Author

**Cai Yundi Elliot**  
GitHub: [@elliotcaiuma](https://github.com/elliotcaiuma)
