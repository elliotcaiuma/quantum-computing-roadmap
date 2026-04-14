# Transformations

Key mathematical transformations used throughout quantum computing and many-body physics.

## Available Transformations

### Jordan-Wigner Transformation

Maps spin-1/2 systems to fermionic systems, enabling simulation of spin chains on quantum computers.

**Documentation:** `jordan-wigner/jordan-wigner.pdf` (25 pages)

**Code:** `jordan-wigner/code/` - 4 Python modules

**Topics Covered:**
- Pauli spin operators and raising/lowering operators
- Jordan-Wigner transformation derivation from first principles
- Fermionic anticommutation relations (verified numerically)
- Inverse transformation: spins in terms of fermions
- Application to transverse Ising model
- Bridge to Fourier transform and Bogoliubov transformation

**Code Modules:**
- `01_pauli_utils.py` - Pauli matrices, Kronecker products, commutators
- `02_jw_operators.py` - Build fermionic operators, verify anticommutation
- `03_inverse_transformation.py` - Construct spin operators from fermions
- `04_jw_hamiltonian.py` - Build Ising, XY, Heisenberg Hamiltonians

### Bogoliubov Transformation

Diagonalizes quadratic fermionic Hamiltonians in momentum space.

**Documentation:** _Coming soon_

### Quantum Fourier Transform

Fundamental transformation for quantum algorithms (Shor's, phase estimation).

**Documentation:** _Coming soon_

---

## Code Structure

Each transformation folder contains:

```
transformation-name/
├── transformation-name.pdf    # Full derivation and theory
├── code/                      # Implementation examples (coming soon)
│   ├── 01_intro.py
│   └── ...
└── README.md                  # This file
```

---

## Prerequisites

- Linear algebra (eigenvalues, eigenvectors, unitary transformations)
- Quantum mechanics basics (operators, commutation relations)
- Second quantization (creation/annihilation operators)

---

## References

**Sachdev, S. (2011)** - *Quantum Phase Transitions* (2nd ed.):
- Chapter 1: Quantum Ising model
- Jordan-Wigner transformation
- Bogoliubov transformation

**Continentino, M. A. (2017)** - *Quantum Scaling in Many-Body Systems* (2nd ed.):
- Chapter 2: Mean-field approximation
- Fermionization of spin chains
