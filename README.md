# Quantum Computing Roadmap

A comprehensive learning path for mastering quantum computing, based on Nielsen & Chuang's textbook with hands-on Qiskit implementations.

![Quantum Computing](https://img.shields.io/badge/Quantum-Computing-blue)
![Qiskit](https://img.shields.io/badge/Qiskit-2.x-purple)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Overview

This repository provides a structured roadmap for learning quantum computing from foundations to advanced topics. Whether you're a physics student, software engineer, or researcher, this guide will help you navigate the quantum landscape systematically.

## 📚 Learning Path

### Phase 1: Foundations (2-3 weeks)
- Dirac notation and bra-ket formalism
- Qubit representation and Bloch sphere
- Single-qubit gates (X, Y, Z, H, S, T)
- Quantum measurement theory

### Phase 2: Multi-Qubit Systems (2-3 weeks)
- Tensor products and composite systems
- Entanglement and Bell states
- Multi-qubit gates (CNOT, CZ, SWAP)
- Quantum teleportation protocol

### Phase 3: Quantum Circuits (2-3 weeks)
- Circuit construction and notation
- Controlled operations
- Superdense coding
- Universality of quantum gates

### Phase 4: Quantum Algorithms (4-6 weeks)
- Quantum Fourier Transform (QFT)
- Phase estimation algorithm
- Grover's search algorithm
- Shor's factoring algorithm

### Phase 5: Quantum Information (4-6 weeks)
- Density matrices and mixed states
- Quantum noise and decoherence
- Quantum error correction
- Entropy and information theory

### Phase 6: Advanced Topics (Ongoing)
- Variational algorithms (VQE, QAOA)
- Hamiltonian simulation
- Quantum machine learning
- Real hardware execution (IBM Quantum)

## 🛠️ Prerequisites

- **Mathematics:** Linear algebra, complex numbers, probability
- **Programming:** Python basics
- **Physics:** Basic quantum mechanics (helpful but not required)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/elliotcaiuma/quantum-computing-roadmap.git
cd quantum-computing-roadmap
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

## 📁 Repository Structure

```
quantum-computing-roadmap/
├── README.md                    # This file
├── ROADMAP.md                   # Detailed learning path
├── requirements.txt             # Python dependencies
├── SETUP.md                     # Environment setup guide
│
├── code/                        # Qiskit implementations
│   ├── foundations/             # Phase 1-2 code
│   │   ├── create_state.py
│   │   ├── bloch_sphere.py
│   │   └── measurement.py
│   ├── multi_qubit/            # Phase 2-3 code
│   │   ├── bell_states.py
│   │   ├── teleportation.py
│   │   └── superdense.py
│   ├── algorithms/             # Phase 4 code
│   │   ├── qft.py
│   │   ├── grover.py
│   │   └── shor.py
│   └── advanced/               # Phase 5-6 code
│       ├── vqe.py
│       ├── qaoa.py
│       └── trotterization.py
│
├── study_guides/               # Topic-specific guides
│   ├── dirac-notation.md
│   ├── bloch-sphere.md
│   ├── entanglement.md
│   └── error-correction.md
│
├── projects/                   # Project ideas & templates
│   ├── beginner/
│   ├── intermediate/
│   └── advanced/
│
├── resources/                  # External resources
│   ├── textbooks.md
│   ├── video-lectures.md
│   └── online-tools.md
│
└── progress/                   # Learning tracking
    └── template.md             # Progress tracking template
```

## 📖 Textbook Reference

This roadmap follows **Nielsen & Chuang's** "Quantum Computation and Quantum Information" (10th Anniversary Edition):

- **Chapters 1-4:** Fundamental Concepts (Phases 1-3)
- **Chapters 5-7:** Quantum Computation (Phase 4)
- **Chapters 8-12:** Quantum Information (Phases 5-6)

## 🎓 Project Ideas

### Beginner
- State creator and Bloch sphere visualizer
- Measurement simulator with arbitrary bases
- Single-qubit gate library

### Intermediate
- Bell state generator and correlator
- Quantum teleportation protocol
- Superdense coding implementation

### Advanced
- Grover's search algorithm
- Shor's factoring algorithm
- VQE for molecular ground states

## 🔗 External Resources

- **Qiskit Textbook:** https://qiskit.org/textbook
- **Qiskit Documentation:** https://qiskit.org/documentation
- **IBM Quantum:** https://quantum.ibm.com
- **Quantum Computing Stack Exchange:** https://quantumcomputing.stackexchange.com

## 📊 Progress Tracking

Track your learning journey using the template in `progress/template.md`. Update weekly with:
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
