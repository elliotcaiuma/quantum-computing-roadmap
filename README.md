# Quantum Computing Roadmap

A beginner-friendly learning path for mastering quantum computing fundamentals with hands-on Qiskit implementations.

![Quantum Computing](https://img.shields.io/badge/Quantum-Roadmap-blue)
![Qiskit](https://img.shields.io/badge/Qiskit-2.x-purple)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Overview

This repository focuses on **quantum computing foundations** — single-qubit and multi-qubit systems. Based on Nielsen & Chuang's textbook with practical Qiskit code.

## 📚 What's Covered

### Phase 1: Single-Qubit (Weeks 1-3)
- Dirac notation and bra-ket formalism
- Qubit representation
- Bloch sphere visualization
- Single-qubit gates (X, Y, Z, H, S, T)
- Quantum measurement

### Phase 2: Multi-Qubit (Weeks 4-6)
- Tensor products
- Entanglement and Bell states
- Multi-qubit gates (CNOT, CZ, SWAP)
- Quantum teleportation
- Superdense coding

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/elliotcaiuma/quantum-computing-roadmap.git
cd quantum-computing-roadmap

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
│   ├── foundations/     # Levels 1-9: Single-qubit
│   │   ├── 01_hello_qubit.py
│   │   ├── 02_create_basis.py
│   │   ├── 03_create_superposition.py
│   │   ├── 04_custom_state.py
│   │   ├── 05_measure_z.py
│   │   ├── 06_measure_any_basis.py
│   │   ├── 07_apply_x_gate.py
│   │   ├── 08_apply_all_single_gates.py
│   │   └── 09_gate_transformer.py
│   └── multi_qubit/     # Levels 10-17: Multi-qubit
│       ├── 10_hello_2qubit.py
│       ├── 11_tensor_product.py
│       ├── 12_tensor_product_calculator.py
│       ├── 13_create_bell_phi_plus.py
│       ├── 14_all_bell_states.py
│       ├── 15_bell_factory.py
│       ├── 16_measure_bell.py
│       └── 17_bell_analyzer.py
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
| 10-12 | Tensor products | Multi-qubit intro |
| 13-15 | Bell states | Entanglement |
| 16-17 | Analysis | Complete tools |

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

**Elliot Cai**  
GitHub: [@elliotcaiuma](https://github.com/elliotcaiuma)

---

*Last Updated: March 2026*
