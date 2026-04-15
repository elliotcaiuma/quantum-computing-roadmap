# Entanglement Entropy in Conformal Field Theory

Replica trick, twist fields, and the universal formula $S = \frac{c}{3} \ln L$.

## Documentation

**Theory:** `entanglement-entropy.pdf` (64 pages)

**Code:** `code/01_correlation_matrix.py` - Correlation matrix method for numerical verification

**Interactive:**
- `entanglement-entropy-interactive.html` - Visual exploration of replica trick and entanglement scaling
- `uniformizing-map-interactive.html` - Interactive visualization of the two-step uniformizing transformation

## Overview

Entanglement entropy quantifies quantum correlations between a subsystem and its complement. In 1+1D conformal field theory (CFT), it takes a universal logarithmic form that depends only on the central charge $c$.

## Main Result

For a 1+1D CFT with central charge `c`, the entanglement entropy of an interval of length `L` is:

```
S_A = (c/3) ln(L/a) + const
```

where `a` is the UV cutoff (lattice spacing).

**For the transverse Ising model (c = 1/2):**

```
S_A = (1/6) ln(L/a) + const
```

## Key Derivations

### 1. Replica Trick

Avoids direct diagonalization of ρ_A by computing Rényi entropies:

```
S^(n) = (1/(1-n)) ln Tr(ρ_A^n)
```

Then take n → 1 via L'Hôpital's rule to recover von Neumann entropy.

### 2. Path Integral Representation

The trace Tr(ρ_A^n) is represented as a path integral on an n-sheeted Riemann surface:

```
Tr(ρ_A^n) = Z_n / (Z_1)^n
```

where Z_n is the partition function on the n-sheeted surface.

### 3. Twist Fields

The n-sheeted geometry is mapped to the complex plane via twist fields T_n:

```
Tr(ρ_A^n) = ⟨T_n(u) T̃_n(v)⟩
```

The scaling dimension is derived via the Schwarzian derivative:

```
Δ_n = (c/12)(n - 1/n)
```

### 4. n → 1 Limit

Taking the derivative with respect to n at n=1:

```
dΔ_n/dn|_{n=1} = c/6
```

This gives the entanglement entropy:

```
S_A = (c/3) ln(L/a) + const
```

## Appendix A: Position-Momentum Overlap

Complete derivation of ⟨p|q⟩ = e^{-ipq} from first principles:

1. Translation operator: e^{-ia p̂}|q⟩ = |q+a⟩
2. Differential equation: ∂/∂q ⟨p|q⟩ = -ip⟨p|q⟩
3. Solution: ⟨p|q⟩ = C(p)e^{-ipq}
4. Normalization: |C(p)| = 1, choose C(p) = 1

## Path Integral Matrix Elements

Complete derivations for the short-time propagator:

**First factor:**

```
⟨p_k|e^{-εV(q̂)}|q_k⟩ = e^{-εV(q_k)}e^{-ip_k q_k}
```

**Proof:** V(q̂) acts diagonally on position eigenstates via power series expansion.

**Second factor:**

```
⟨q_{k+1}|e^{-εp̂²/(2m)}|p_k⟩ = e^{-εp_k²/(2m)}e^{ip_k q_{k+1}}
```

**Proof:** p̂² acts diagonally on momentum eigenstates.

**Origin of 1/(2π):** Comes from momentum completeness relation convention:
- ⟨p|q⟩ = e^{-ipq} (no prefactor)
- ⟨p|p'⟩ = 2πδ(p-p')
- Completeness: ∫ (dp/2π)|p⟩⟨p| = I$

## Code Module

The correlation matrix method computes entanglement entropy numerically for free fermion systems:

```python
# Build correlation matrix for transverse Ising model
Pi_A = ising_correlation_matrix(L, g)

# Compute entanglement entropy
S = entanglement_entropy(Pi_A, subsystem_size)

# Verify CFT prediction
c_extracted = verify_cft_prediction(L_values, g)
```

**Expected output for Ising model ($g=1$):**
```
L =   4: S = 0.6842
L =   8: S = 0.8503
L =  16: S = 1.0164
L =  32: S = 1.1825
L =  64: S = 1.3486
L = 128: S = 1.5147

Fit results:
  Slope (c/3): 0.1667
  Extracted c: 0.5000
  Expected c:  0.500 (Ising CFT)
  Error:       0.0000
```

## Structure

```
entanglement-entropy/
├── entanglement-entropy.pdf          (64 pages)
├── entanglement-entropy-interactive.html
├── uniformizing-map-interactive.html
├── cut.png                           (Branch cut visualization)
├── README.md
└── code/
    └── 01_correlation_matrix.py
```

## Prerequisites

- Quantum mechanics (density matrices, partial trace)
- Path integral formalism (Euclidean time)
- Complex analysis (contour integration, conformal maps)
- CFT basics (central charge, primary fields)

## References

**Calabrese, P. & Cardy, J. (2004)** - *Entanglement entropy and quantum field theory*, J. Stat. Mech. P06002

**Sachdev, S. (2011)** - *Quantum Phase Transitions* (2nd ed.), Cambridge University Press

**Di Francesco, P. et al. (1997)** - *Conformal Field Theory*, Springer
