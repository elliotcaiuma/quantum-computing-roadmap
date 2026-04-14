# Jordan-Wigner Transformation - Code

This folder contains Python code implementing the Jordan-Wigner transformation.

## Files

| File | Description |
|------|-------------|
| `01_pauli_utils.py` | Pauli matrix utilities (σ^x, σ^y, σ^z, σ^±) |
| `02_jw_operators.py` | Build fermionic operators c_i, c_i^† using JW transformation |
| `03_inverse_transformation.py` | Construct spin operators from fermions |
| `04_jw_hamiltonian.py` | Build Ising, XY, Heisenberg Hamiltonians |

## Usage

```bash
# Test Pauli algebra
python 01_pauli_utils.py

# Build JW operators and verify anticommutation
python 02_jw_operators.py

# Test inverse transformation
python 03_inverse_transformation.py

# Build and diagonalize Hamiltonians
python 04_jw_hamiltonian.py
```

## Requirements

```bash
pip install numpy
```

## Code Progression

The code follows a logical progression:

1. **Utilities** (`01_pauli_utils.py`): Basic building blocks
2. **JW Operators** (`02_jw_operators.py`): Core transformation
3. **Inverse** (`03_inverse_transformation.py`): Verify consistency
4. **Applications** (`04_jw_hamiltonian.py`): Build physical models

Each module is self-contained and can be imported independently.

## Physical Significance

- **01_pauli_utils.py**: Pauli matrices form the basis for spin operators
- **02_jw_operators.py**: JW string ensures fermionic anticommutation
- **03_inverse_transformation.py**: Confirms spin-fermion equivalence
- **04_jw_hamiltonian.py**: Quadratic fermionic Hamiltonians (exactly solvable)

## Next Steps

After building the Hamiltonian:
1. Diagonalize using `np.linalg.eigvalsh(H)`
2. Extract ground state energy and gap
3. Compute correlation functions
4. (Optional) Fourier transform + Bogoliubov diagonalization
