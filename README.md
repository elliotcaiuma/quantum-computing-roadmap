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
- Lie-Trotter product formula and intuition
- First-order Trotterization (O(t²/n) error)
- Second-order symmetric Trotter / Strang splitting (O(t³/n²) error)
- Higher-order Suzuki expansions (4th-order: O(t⁵/n⁴))
- Heisenberg model simulation (spin-spin correlations)
- Molecular H₂ simulation (electronic structure, dissociation curve)
- Error analysis and resource estimation (chemical accuracy)

**Theory:** Read `docs/quantum-computing-phase5.pdf` (22 pages)

**Code:** Levels 36-43 in `code/hamiltonian_simulation/`

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
│   └── quantum-computing-phase5.pdf    (22 pages, Hamiltonian simulation) [COMPLETE]
│
├── study_guides/
│   └── getting-started.md
│
└── progress/
    └── template.md
```

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

## Resources

- Qiskit Textbook: https://qiskit.org/textbook
- Qiskit Docs: https://qiskit.org/documentation
- IBM Quantum: https://quantum.ibm.com

## 📄 License

MIT License

## 👨‍💻 Author

**Cai Yundi Elliot**  
GitHub: [@elliotcaiuma](https://github.com/elliotcaiuma)
