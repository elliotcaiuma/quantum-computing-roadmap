# Quantum Fourier Transform (QFT)

The Quantum Fourier Transform is one of the most important quantum algorithms, providing exponential speedup over the classical FFT and serving as the key subroutine in Shor's algorithm and quantum phase estimation.

## Documentation

**QFT (Standard):** [qft.pdf](./qft.pdf) (14 pages)

**FQFT (Fermionic):** [fqft.pdf](./fqft.pdf) (14 pages)

**Code:** `code/` folder - 3 Python implementations

## Key Results

### Standard QFT

For $n$ qubits with $N = 2^n$:

\[
\text{QFT} \ket{j} = \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} e^{2\pi i j k / N} \ket{k}
\]

**Complete derivations included:**
- Proof of DFT unitarity (geometric series)
- Product state representation derivation
- Step-by-step 2-qubit circuit construction
- Numerical examples for all 2-qubit basis states

**Circuit decomposition:**
- $n$ Hadamard gates
- $n(n-1)/2$ controlled phase gates
- $n/2$ swap gates
- **Total:** $O(n^2)$ gates vs classical $O(2^n n)$

### Fermionic QFT (FQFT)

Transforms fermionic creation operators:

\[
c_j^\dagger \to \tilde{c}_k^\dagger = \frac{1}{\sqrt{n}} \sum_{j=0}^{n-1} e^{2\pi i j k / n} c_j^\dagger
\]

**Many-body action:** Via determinant lifting

\[
\ket{j_1, \dots, j_p} \to \sum_{k_1,\dots,k_p} \det(u_{k_1\dots k_p, j_1\dots j_p}) \ket{k_1, \dots, k_p}
\]

**Block structure:** Diagonal by particle number, blocks are $\Lambda^p(u)$

**Complete derivations included:**
- Bitstring to occupied sites mapping
- Determinant formula for many-body states
- Block-diagonal structure proof
- Numerical examples for 3-mode FQFT

## Code Modules

### QFT (Standard)

- **Module 1:** `01_dft_matrix.py` - DFT matrix construction, QFT circuit simulation, unitarity verification
- **Module 2:** `02_circuit_builder.py` - Manual QFT circuit construction from H + controlled phase gates

### FQFT (Fermionic)

- **Module 3:** `03_fqft_matrix.py` - FQFT matrix via determinant lifting, block-diagonal structure analysis

## Prerequisites

- Complex numbers and exponentials
- Matrix operations (unitarity, determinants)
- Basic quantum circuits (Hadamard, controlled gates)
- For FQFT: Second quantization, fermionic operators

## Applications

### Standard QFT
- Shor's factoring algorithm
- Quantum phase estimation
- Hidden subgroup problems
- Quantum simulation

### FQFT
- Quantum chemistry (molecular orbitals)
- Condensed matter (momentum space)
- Electronic structure calculations
- Fermionic simulation

## Next Steps

1. Study Shor's algorithm (uses QFT for period finding)
2. Explore quantum phase estimation
3. Implement FQFT for fermionic systems
4. Connect to Jordan-Wigner transformation

---

**Related:** See `../jordan-wigner/` for fermion-to-qubit mapping.
