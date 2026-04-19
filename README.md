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

**Theory:** Read `docs/quantum-computing-phase1.pdf` (36 pages)

**Code:** Levels 1-9 in `code/foundations/`

### Phase 2: Multi-Qubit Systems
- Tensor products and composite systems
- Entanglement and Bell states (all 4 Bell states)
- Multi-qubit gates (CNOT, CZ, SWAP) with matrix representations
- Rotation gates (R_x, R_y, R_z) and Z-Y-Z decomposition
- A-X-B-X-C decomposition for controlled-U gates
- Quantum teleportation
- Superdense coding

**Theory:** Read `docs/quantum-computing-phase2.pdf` (42 pages)

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

**Theory:** Read `docs/quantum-computing-phase4.pdf` (27 pages)

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

**Theory:** Read `docs/quantum-computing-phase5.pdf` (23 pages)

**Code:** Levels 36-43 in `code/hamiltonian_simulation/`

**Key Results:**
- 2nd-order Trotter: 50-500× better accuracy than 1st-order
- 4th-order Suzuki: Optimal for chemical accuracy (ε ~ 10⁻³)
- Quantum advantage: Emerges at ~8 qubits for simulation tasks

---

## Transformations

Key mathematical transformations used throughout quantum computing and many-body physics.

### Jordan-Wigner Transformation

Maps spin systems to fermionic systems, enabling simulation of spin chains on quantum computers.

**Theory:** Read `transformations/jordan-wigner/jordan-wigner.pdf` (25 pages)

**Code:** See `transformations/jordan-wigner/code/` for Python implementations

**Key Topics:**
- Pauli spin operators and raising/lowering operators
- Jordan-Wigner transformation derivation from first principles
- Fermionic anticommutation relations (verified numerically)
- Inverse transformation: spins in terms of fermions
- Application to transverse Ising model
- Bridge to Fourier transform and Bogoliubov transformation

### Quantum Fourier Transform

Quantum algorithm for Fourier transform with exponential speedup over classical FFT.

**Theory:** Read `transformations/quantum-fourier-transform/qft.pdf` (14 pages) and `fqft.pdf` (14 pages)

**Code:** See `transformations/quantum-fourier-transform/code/` for Python implementations

**Key Topics:**
- Classical DFT definition and properties
- QFT mathematical formulation
- Circuit decomposition (Hadamard + controlled phase gates)
- Gate complexity: O(n²) vs classical O(2ⁿ n)
- Fermionic QFT via determinant lifting
- Block-diagonal structure by particle number

---

## Conformal Field Theory

Universal results for entanglement and critical phenomena in 1+1D quantum systems.

### Entanglement Entropy

Derivation of universal entanglement entropy formula in 1+1D CFT using replica trick and twist fields.

**Theory:** Read `conformal_field_theory/entanglement-entropy/entanglement-entropy.pdf` (64 pages)

**Code:** See `conformal_field_theory/entanglement-entropy/code/` for correlation matrix method

**Interactive Visualizations:**
- `entanglement-entropy-interactive.html` - 3D replica trick visualizer with ground/global/local quench scenarios
- `uniformizing-map-interactive.html` - Interactive two-step uniformizing transformation (Möbius + power map)

**Main result:** For 1+1D CFT with central charge \(c\):
\[
S_A = \frac{c}{3} \ln\left(\frac{L}{a}\right) + \text{const}
\]

**For Ising model (\(c = 1/2\)):**
\[
S_A = \frac{1}{6} \ln\left(\frac{L}{a}\right) + \text{const}
\]

**Key derivations:**
- Replica trick: avoiding direct diagonalization via Rényi entropies
- Path integral representation on \(n\)-sheeted Riemann surface
- Twist fields and their scaling dimension \(\Delta_n = \frac{c}{12}(n - 1/n)\)
- Complete derivation via Schwarzian derivative
- Position-momentum overlap \(\langle p | q \rangle = e^{-ipq}\) from first principles
- Matrix element derivations for path integral propagator
- Numerical verification using correlation matrix method

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

# Run transformation examples (coming soon)
# python transformations/jordan-wigner/code/jw_01_demo.py
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
├── main/                                # Main content
│   ├── code/                            # Quantum Basics code
│   │   ├── foundations/                 # Levels 1-9: Single-qubit
│   │   ├── multi_qubit/                 # Levels 11-20: Multi-qubit
│   │   ├── density_matrix/              # Levels 21-29: Density matrix
│   │   ├── algorithms/                  # Levels 30-35: Quantum algorithms
│   │   └── hamiltonian_simulation/      # Levels 36-43: Hamiltonian sim
│   │
│   └── docs/                            # Quantum Basics PDFs
│       ├── quantum-computing-phase1.pdf   (36 pages)
│       ├── quantum-computing-phase2.pdf   (42 pages)
│       ├── quantum-computing-phase3.pdf   (32 pages)
│       ├── quantum-computing-phase4.pdf   (27 pages)
│       └── quantum-computing-phase5.pdf   (23 pages)
│
├── transformations/                   # Key transformations
│   ├── README.md
│   ├── jordan-wigner/                 # Spin ↔ Fermion mapping
│   │   ├── jordan-wigner.pdf          (25 pages)
│   │   ├── README.md
│   │   └── code/                      # Python implementations (4 modules)
│   └── quantum-fourier-transform/     # QFT for algorithms
│       ├── qft.pdf                    (14 pages)
│       ├── fqft.pdf                   (14 pages)
│       ├── README.md
│       └── code/                      # Python implementations (3 modules)
│
├── conformal_field_theory/            # CFT and entanglement
│   ├── entanglement-entropy/          # Replica trick derivation
│   │   ├── entanglement-entropy.pdf   (64 pages)
│   │   ├── entanglement-entropy-interactive.html
│   │   ├── uniformizing-map-interactive.html
│   │   ├── README.md
│   │   └── code/                      # Correlation matrix method
│   └── bogoliubov-transform/          # Coming soon
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
| **PDF Pages** | 260 (160 Basics + 52 Transformations + 64 CFT) |
| **Code Files** | 48 |
| **Interactive Visualizations** | 2 (Entanglement Entropy replica trick + Uniformizing map) |
| **Code Levels** | 43 |
| **Algorithms** | 7 (Deutsch-Jozsa, Grover, QFT, Phase Estimation, Shor, Trotter, Suzuki) |
| **Physical Models** | 2 (Heisenberg, H₂) |
| **Transformations** | 2 (Jordan-Wigner + QFT/FQFT with code) |
| **CFT** | 1 (Entanglement Entropy with replica trick, 64 pages, 2 interactive visualizations) |
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

### Transformations & Many-Body Physics

**Sachdev, S. (2011)** - *Quantum Phase Transitions* (2nd ed.), Cambridge University Press:
- Chapter 1: Quantum Ising model
- Chapter 4: Mean-field theory
- Chapter 5: Quantum criticality
- Jordan-Wigner transformation
- Bogoliubov transformation

**Continentino, M. A. (2017)** - *Quantum Scaling in Many-Body Systems* (2nd ed.), Cambridge University Press:
- Chapter 2: Mean-field approximation
- Chapter 3: Quantum phase transitions
- Fermionization of spin chains

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
