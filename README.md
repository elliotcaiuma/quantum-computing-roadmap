# Quantum Computing Roadmap

A beginner-friendly learning path for mastering quantum computing fundamentals with hands-on Qiskit implementations.

![Quantum Computing](https://img.shields.io/badge/Quantum-Roadmap-blue)
![Qiskit](https://img.shields.io/badge/Qiskit-2.x-purple)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Overview

This repository focuses on **quantum computing foundations** — single-qubit and multi-qubit systems. Based on Nielsen & Chuang's textbook with practical Qiskit code.

## 📚 What's Covered

### Phase 1: Single-Qubit Foundations ✅
- Dirac notation and bra-ket formalism
- Qubit representation
- Bloch sphere visualization
- Single-qubit gates (X, Y, Z, H, S, T) with geometric interpretations
- Quantum measurement (complete mathematical treatment)

**Theory:** Read `docs/quantum-computing-phase1.pdf` (40 pages)

**Code:** Levels 1-9 in `code/foundations/`

### Phase 2: Multi-Qubit Systems ✅
- Tensor products and composite systems
- Entanglement and Bell states (all 4 Bell states)
- Multi-qubit gates (CNOT, CZ, SWAP) with matrix representations
- Rotation gates (R_x, R_y, R_z) and Z-Y-Z decomposition
- A-X-B-X-C decomposition for controlled-U gates
- Quantum teleportation
- Superdense coding

**Theory:** Read `docs/quantum-computing-phase2.pdf` (44 pages)

**Code:** Levels 11-20 in `code/multi_qubit/`

### Phase 3: Density Matrix & Decomposition 🚧
- Density matrix formalism (pure vs mixed states)
- Bloch sphere for mixed states
- Purification
- Schmidt decomposition
- Reduced density matrices
- Entanglement detection

**Theory:** Read `docs/quantum-computing-phase3.pdf` (12 pages)

**Code:** Levels 21-29 in `code/density_matrix/`

## 🚀 Quick Start

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

## 📁 Structure

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
│
├── docs/
│   ├── quantum-computing-phase1.pdf    (40 pages, single-qubit foundations) ✅
│   ├── quantum-computing-phase2.pdf    (44 pages, multi-qubit systems) ✅
│   └── quantum-computing-phase3.pdf    (12 pages, density matrix) 🚧
│
├── study_guides/
│   └── getting-started.md
│
└── progress/
    └── template.md
```

## 🎓 Code Progression

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

See `code/README.md` for details.

## 📖 Textbook

Follows **Nielsen & Chuang**:
- Chapters 1-2: Fundamental concepts
- Chapter 4: Quantum circuits

## 🔗 Resources

- Qiskit Textbook: https://qiskit.org/textbook
- Qiskit Docs: https://qiskit.org/documentation
- IBM Quantum: https://quantum.ibm.com

## 📄 License

MIT License

## 👨‍💻 Author

**Cai Yundi Elliot**  
GitHub: [@elliotcaiuma](https://github.com/elliotcaiuma)
