# Jordan-Wigner Transformation

The Jordan-Wigner transformation maps spin-1/2 operators to fermionic creation and annihilation operators, enabling the simulation of spin chains using fermionic systems.

## Documentation

**Full Derivation:** [jordan-wigner.pdf](./jordan-wigner.pdf) (30 pages)

## Key Results

### The Transformation

For a 1D spin chain, the Jordan-Wigner transformation is:

\[
c_i = \left(\prod_{j<i} Z_j\right) \sigma_i^-
\]

\[
c_i^\dagger = \left(\prod_{j<i} Z_j\right) \sigma_i^+
\]

where:
- $c_i, c_i^\dagger$ are fermionic annihilation/creation operators
- $\sigma_i^\pm = \frac{1}{2}(\sigma_i^x \pm i\sigma_i^y)$ are spin raising/lowering operators
- $Z_j$ is the Pauli-Z operator on site $j$
- The string operator $S_i = \prod_{j<i} Z_j$ ensures fermionic anticommutation

### Inverse Transformation

Spins in terms of fermions:

\[
\sigma_i^x = (c_i^\dagger + c_i) S_i
\]

\[
\sigma_i^z = I - 2c_i^\dagger c_i
\]

### Critical Identity

\[
(c_i^\dagger + c_i) Z_i = c_i^\dagger - c_i
\]

This identity is essential for transforming the transverse field term.

### Application: Transverse Ising Model

The transverse Ising Hamiltonian:

\[
H = -J \sum_i \sigma_i^x \sigma_{i+1}^x - \Gamma \sum_i \sigma_i^z
\]

becomes (after JW transformation):

\[
H = -J \sum_i (c_i^\dagger - c_i)(c_{i+1}^\dagger + c_{i+1}) - \Gamma \sum_i (I - 2c_i^\dagger c_i)
\]

This quadratic fermionic Hamiltonian can be diagonalized via:
1. Fourier transform to momentum space
2. Bogoliubov transformation

Result: free fermions with dispersion $\epsilon_k = 2\sqrt{(\Gamma - J\cos k)^2 + (J\sin k)^2}$

## Code Modules

Located in `code/` folder:

- `01_pauli_utils.py` - Pauli matrices, Kronecker products, commutators
- `02_jw_operators.py` - Build JW fermionic operators, verify anticommutation
- `03_inverse_transformation.py` - Construct spin operators from fermions
- `04_jw_hamiltonian.py` - Build Ising, XY, Heisenberg Hamiltonians

See [code/README.md](./code/README.md) for usage instructions.

## Prerequisites

- Pauli matrices and spin algebra
- Fermionic operators and anticommutation relations
- Tensor products for multi-site operators

## Next Steps

After understanding JW:
1. Study Bogoliubov transformation for diagonalization
2. Explore applications to other spin models (XY, Heisenberg)
3. Implement quantum simulation of spin chains

---

**Related:** See `../bogoliubov-transform/` for momentum space diagonalization.
