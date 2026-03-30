# Quantum Computing Roadmap

A beginner-friendly learning path for mastering quantum computing fundamentals with hands-on Qiskit implementations.

![Quantum Computing](https://img.shields.io/badge/Quantum-Roadmap-blue)
![Qiskit](https://img.shields.io/badge/Qiskit-2.x-purple)
![License](https://img.shields.io/badge/License-MIT-green)
![Lint](https://github.com/elliotcaiuma/quantum-computing-roadmap/actions/workflows/lint.yml/badge.svg)
![Tests](https://github.com/elliotcaiuma/quantum-computing-roadmap/actions/workflows/test.yml/badge.svg)

## Overview

This repository contains **quantum computing projects** — from foundational learning paths to specialized physics simulations. Based on Nielsen & Chuang's textbook with practical Qiskit code.

---

## Quantum Basics

A structured learning path through quantum computing fundamentals with theory (PDFs) and code (Qiskit).

### Phase 1: Single-Qubit Foundations
- Dirac notation and bra-ket formalism
- Qubit representation
- Bloch sphere visualization
- Single-qubit gates (X, Y, Z, H, S, T) with geometric interpretations
- Quantum measurement (complete mathematical treatment)

**Theory:** Read `docs/quantum-computing-phase1.pdf` (40 pages)

**Code:** Levels 1-9 in `code/foundations/`

### Phase 2: Multi-Qubit Systems
- Tensor products and composite systems
- Entanglement and Bell states (all 4 Bell states)
- Multi-qubit gates (CNOT, CZ, SWAP) with matrix representations
- Rotation gates (R_x, R_y, R_z) and Z-Y-Z decomposition
- A-X-B-X-C decomposition for controlled-U gates
- Quantum teleportation
- Superdense coding

**Theory:** Read `docs/quantum-computing-phase2.pdf` (44 pages)

**Code:** Levels 11-20 in `code/multi_qubit/`

### Phase 3: Density Matrix & Decomposition
- Density matrix formalism (pure vs mixed states)
- Bloch sphere for mixed states
- Purification (mixed states as parts of larger pure states)
- Schmidt decomposition via SVD (complete derivation)
- Reduced density matrices and partial trace
- Entanglement detection (Schmidt rank test)
- Von Neumann entropy and purity measures

**Theory:** Read `docs/quantum-computing-phase3.pdf` (31 pages)

**Code:** Levels 21-29 in `code/density_matrix/`

### Phase 4: Quantum Algorithms
- Deutsch-Jozsa algorithm (exponential speedup demonstration)
- Grover's search algorithm (quadratic speedup, amplitude amplification)
- Quantum phase estimation (eigenvalue extraction)
- Shor's factoring algorithm (cryptanalysis application)
- Quantum Fourier Transform (QFT) with complete derivation

**Theory:** Read `docs/quantum-computing-phase4.pdf` (29 pages)

**Code:** Levels 30-35 in `code/algorithms/`

### Phase 5: Hamiltonian Simulation
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

---

## Projects

### Project 1: Ising Model Simulation

Study of the transverse Ising model using mean-field theory and quantum simulation techniques.

#### Phase 1: Mean-Field Theory
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

#### Phase 2: Exact Diagonalization (Planned)
- Full diagonalization for small systems (N ≤ 20)
- Benchmark mean-field results
- Finite-size effects analysis

#### Phase 3: Quantum Simulation (Planned)
- Trotter-Suzuki decomposition
- Real-time dynamics
- Quench dynamics and thermalization

---

## Quick Start

```bash
# Clone
git clone https://github.com/elliotcaiuma/quantum-computing-roadmap.git
cd quantum-roadmap

# Setup
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt

# Run Quantum Basics code (start here for learning)
python code/foundations/01_hello_qubit.py

# Run Ising Model code (Project 1)
python projects/ising_model/code/ising_01_mean_field_core.py
```

---

## Structure

```
quantum-computing-roadmap/
├── README.md
├── ROADMAP.md
├── SETUP.md
├── requirements.txt
│
├── code/                              # Quantum Basics code
│   ├── foundations/                   # Levels 1-9: Single-qubit
│   ├── multi_qubit/                   # Levels 11-20: Multi-qubit
│   ├── density_matrix/                # Levels 21-29: Density matrix
│   ├── algorithms/                    # Levels 30-35: Quantum algorithms
│   └── hamiltonian_simulation/        # Levels 36-43: Hamiltonian sim
│
├── docs/                              # Quantum Basics PDFs
│   ├── quantum-computing-phase1.pdf   (40 pages)
│   ├── quantum-computing-phase2.pdf   (44 pages)
│   ├── quantum-computing-phase3.pdf   (31 pages)
│   ├── quantum-computing-phase4.pdf   (29 pages)
│   └── quantum-computing-phase5.pdf   (30 pages)
│
├── projects/                          # Research projects
│   └── ising_model/                   # Project 1: Ising Model
│       ├── README.md
│       ├── ising_docs/
│       │   └── ising-phase1-mean-field.pdf  (27 pages)
│       └── code/
│           ├── ising_01_mean_field_core.py
│           ├── ising_02_phase_diagram.py
│           └── ising_03_order_parameter.py
│
├── study_guides/
│   └── getting-started.md
│
└── progress/
    └── tracker.md
```

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| **PDF Pages** | 201 (174 Basics + 27 Ising) |
| **Code Files** | 45 (42 Basics + 3 Ising) |
| **Code Levels** | 43 + 3 (Ising modules) |
| **Algorithms** | 7 (Deutsch-Jozsa, Grover, QFT, Phase Estimation, Shor, Trotter, Suzuki) |
| **Physical Models** | 3 (Heisenberg, H₂, Transverse Ising) |
| **Projects** | 1 (Ising Model) + Quantum Basics learning path |
| **Estimated Study Time** | 16-21 weeks |

---

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

---

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

---

## Resources

- Qiskit Textbook: https://qiskit.org/textbook
- Qiskit Docs: https://qiskit.org/documentation
- IBM Quantum: https://quantum.ibm.com

---

## 📄 License

MIT License

## 👨‍💻 Author

**Cai Yundi Elliot**  
GitHub: [@elliotcaiuma](https://github.com/elliotcaiuma)
