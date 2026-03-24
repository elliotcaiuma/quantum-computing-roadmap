# Quantum Computing Foundations

A beginner-friendly learning path for mastering quantum computing fundamentals with hands-on Qiskit implementations.

![Quantum Computing](https://img.shields.io/badge/Quantum-Foundations-blue)
![Qiskit](https://img.shields.io/badge/Qiskit-2.x-purple)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Overview

This repository focuses on **quantum computing foundations** — everything you need to master single-qubit and multi-qubit systems before moving to algorithms. Based on Nielsen & Chuang's textbook with practical Qiskit code.

## 📚 What's Covered

### Phase 1: Single-Qubit Foundations (Weeks 1-3)
- Dirac notation and bra-ket formalism
- Qubit representation: $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$
- Bloch sphere visualization
- Single-qubit gates (X, Y, Z, H, S, T)
- Quantum measurement theory

### Phase 2: Multi-Qubit Foundations (Weeks 4-6)
- Tensor products and composite systems
- Entanglement and Bell states
- Multi-qubit gates (CNOT, CZ, SWAP)
- Quantum teleportation protocol
- Superdense coding

## 🛠️ Prerequisites

- **Mathematics:** Linear algebra (vectors, matrices), complex numbers
- **Programming:** Python basics
- **Physics:** Not required (we teach the math you need)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/elliotcaiuma/quantum-foundations.git
cd quantum-foundations
```

### 2. Set Up Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\Activate.ps1

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Test Your Setup

```bash
python code/foundations/test_setup.py
```

Expected output:
```
✓ Qiskit working!
✓ NumPy imported
✓ Matplotlib ready
🎉 All tests passed! Setup complete!
```

### 4. Run Your First Code

```bash
# Create and visualize quantum states
python code/foundations/create_state.py

# Explore multi-qubit systems
python code/multi_qubit/bell_states.py
```

## 📁 Repository Structure

```
quantum-foundations/
├── README.md                    # This file
├── ROADMAP.md                   # Week-by-week study plan
├── requirements.txt             # Python dependencies
├── SETUP.md                     # Environment setup guide
│
├── code/                        # Qiskit implementations
│   ├── foundations/             # Phase 1: Single-qubit
│   │   ├── test_setup.py        # Verify installation
│   │   ├── create_state.py      # State creator
│   │   ├── bloch_sphere.py      # Bloch visualization
│   │   └── measurement.py       # Measurement simulator
│   └── multi_qubit/             # Phase 2: Multi-qubit
│       ├── tensor_products.py   # Tensor product calculator
│       ├── bell_states.py       # Bell state generator
│       ├── teleportation.py     # Teleportation protocol
│       └── superdense.py        # Superdense coding
│
├── study_guides/                # Beginner guides
│   ├── getting-started.md       # Week 1-3 guide
│   ├── dirac-notation.md        # Bra-ket formalism
│   └── bloch-sphere.md          # Visualization guide
│
└── progress/                    # Learning tracking
    └── template.md              # Weekly progress tracker
```

## 📖 Textbook Reference

This roadmap follows **Nielsen & Chuang's** "Quantum Computation and Quantum Information":

- **Chapters 1-2:** Fundamental concepts (Phase 1)
- **Chapter 4:** Quantum circuits (Phase 2)

## 🎓 Learning Outcomes

After completing this foundation course, you will be able to:

✅ Represent any single-qubit state  
✅ Visualize states on Bloch sphere  
✅ Implement all single-qubit gates  
✅ Measure in arbitrary bases (X, Y, Z)  
✅ Create Bell states and verify entanglement  
✅ Implement quantum teleportation  
✅ Build multi-qubit circuits  

## 🔗 Next Steps

After mastering foundations, continue to:
- **Quantum Algorithms:** QFT, Grover's, Shor's
- **Variational Methods:** VQE, QAOA
- **Quantum Information:** Error correction, noise

## 🔗 External Resources

- **Qiskit Textbook:** https://qiskit.org/textbook
- **Qiskit Documentation:** https://qiskit.org/documentation
- **IBM Quantum:** https://quantum.ibm.com
- **Quantum Computing Stack Exchange:** https://quantumcomputing.stackexchange.com

## 📊 Progress Tracking

Track your learning journey using `progress/template.md`. Update weekly with:
- Topics covered
- Code completed
- Challenges faced
- Next goals

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 👨‍💻 Author

**Elliot Cai**  
GitHub: [@elliotcaiuma](https://github.com/elliotcaiuma)

---

*Last Updated: March 2026*
