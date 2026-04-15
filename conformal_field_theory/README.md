# Conformal Field Theory

Universal results for entanglement and critical phenomena in 1+1D quantum systems.

## Available Documentation

### Entanglement Entropy

Derivation of universal entanglement entropy formula in 1+1D CFT using replica trick and twist fields.

**Documentation:** `entanglement-entropy/entanglement-entropy.pdf` (64 pages)

**Code:** `entanglement-entropy/code/` - Correlation matrix method for numerical verification

**Interactive Visualizations:**
- `entanglement-entropy-interactive.html` - 3D replica trick visualizer
- `uniformizing-map-interactive.html` - Uniformizing transformation explorer

**Topics Covered:**
- Entanglement entropy definition and physical interpretation
- Replica trick: avoiding direct diagonalization via Rényi entropies
- Path integral representation of Tr(ρ_A^n) on n-sheeted Riemann surface
- Twist fields: mapping curved geometry to flat plane correlation functions
- Scaling dimension: Δ_n = (c/12)(n - 1/n) via Schwarzian derivative
- n → 1 limit using L'Hôpital's rule
- Main result: S = (c/3) ln(L/a) + const
- Numerical verification via correlation matrix method
- Connection to Kibble-Zurek mechanism after quantum quench

**Key Derivations:**
- Position-momentum overlap: ⟨p\|q⟩ = e^{-ipq} from first principles (Appendix A)
- Matrix elements for path integral propagator:
  - ⟨p_k\|e^{-εV(q̂)}\|q_k⟩ = e^{-εV(q_k)}e^{-ip_k q_k}
  - ⟨q_{k+1}\|e^{-εp̂²/(2m)}\|p_k⟩ = e^{-εp_k²/(2m)}e^{ip_k q_{k+1}}
- Origin of 1/(2π) factor in momentum completeness relation
- Euclidean path integral for ground state preparation
- Reduced density matrix via partial trace over region B
- Replica construction with cyclic boundary conditions
- Detailed gluing procedure: from Eq. 154 to Z_n/(Z_1)^n with delta functionals
- Replica sheet distinction: what's identical vs. what differs
- Uniformizing map derivation: Möbius + power map construction
- Stress tensor OPE and Virasoro algebra
- Anomalous transformation law from first principles (OPE → infinitesimal → finite → cocycle)
- Virasoro generators L_n mode expansion and physical interpretation
- Twist fields as local operators in n-copy CFT
- Orbifold CFT and Fourier diagonalization
- Partition function factorization into k-modes

**Code Module:**
- `01_correlation_matrix.py` - Compute S for transverse Ising model, verify c = 1/2

### Bogoliubov Transformation

Diagonalizes quadratic fermionic Hamiltonians in momentum space.

**Documentation:** _Coming soon_

---

## Code Structure

Each CFT topic folder contains:

```
topic-name/
├── topic-name.pdf           # Full derivation and theory
├── code/                    # Implementation examples
│   ├── 01_intro.py
│   └── ...
└── README.md                # This file
```

---

## Prerequisites

- Quantum mechanics basics (operators, commutation relations)
- Path integral formalism (Euclidean time, ground state projection)
- Complex analysis (contour integration, conformal maps)
- Second quantization (creation/annihilation operators)

---

## References

**Calabrese, P. & Cardy, J. (2004)** - *Entanglement entropy and quantum field theory*:
- Replica trick formulation
- Twist field correlation functions
- Universal logarithmic term

**Sachdev, S. (2011)** - *Quantum Phase Transitions* (2nd ed.):
- Chapter 1: Quantum Ising model
- Chapter 5: Quantum criticality and CFT

**Di Francesco, P. et al. (1997)** - *Conformal Field Theory*:
- Stress tensor and Schwarzian derivative
- Primary fields and scaling dimensions
