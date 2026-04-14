"""
Inverse Jordan-Wigner Transformation

This module constructs spin operators (σ^x, σ^y, σ^z) from fermionic
operators using the inverse JW transformation.

Inverse Relations:
    σ_i^x = (c_i^† + c_i) S_i
    σ_i^y = -i(c_i^† - c_i) S_i
    σ_i^z = I - 2 c_i^† c_i

where S_i = Z_0 ⊗ Z_1 ⊗ ... ⊗ Z_{i-1} is the JW string.

Key Identity:
    (c_i^† + c_i) σ_i^z = c_i^† - c_i

This identity is crucial for transforming σ^x_i σ^x_{i+1} terms correctly.
It encodes the fermionic sign structure that makes the JW transformation work.

Physical Significance:
- Allows reconstruction of spin operators from fermionic representation
- Useful for computing spin correlation functions after solving fermionic model
- Verifies the equivalence between spin and fermionic descriptions
"""

import numpy as np
from pauli_utils import PauliTool
from jw_operators import JWTransformation


class InverseJW:
    """Construct spin operators from fermions."""
    
    @staticmethod
    def build_spin_ops(n):
        """
        Build spin operators from fermionic operators.
        
        Uses the inverse JW transformation:
            σ^x = (c^† + c) S
            σ^y = -i(c^† - c) S
            σ^z = I - 2 c^† c
        
        Args:
            n: Number of sites
            
        Returns:
            Tuple (X, Y, Z) of lists of 2^n × 2^n matrices
            where X[i] is σ^x_i, etc.
        """
        c, cdag = JWTransformation.build_fermion_ops(n)
        dim = 2**n
        
        # Build JW strings: S_i = Z_0 ⊗ Z_1 ⊗ ... ⊗ Z_{i-1}
        strings = []
        for i in range(n):
            ops = [PauliTool.pauli('Z')] * i + [PauliTool.pauli('I')] * (n - i)
            strings.append(PauliTool.kron(ops))
        
        # Construct spin operators
        X, Y, Z = [], [], []
        
        for i in range(n):
            # σ^x = (c^† + c) S_i
            X.append((cdag[i] + c[i]) @ strings[i])
            
            # σ^y = -i(c^† - c) S_i
            Y.append(-1j * (cdag[i] - c[i]) @ strings[i])
            
            # σ^z = I - 2 c^† c
            Z.append(np.eye(dim, dtype=complex) - 2 * cdag[i] @ c[i])
        
        return X, Y, Z
    
    @staticmethod
    def verify_equivalence(n, tol=1e-10):
        """
        Verify that inverse-transformed spins match original Pauli matrices.
        
        This confirms the JW transformation is invertible and consistent.
        
        Args:
            n: Number of sites
            tol: Tolerance for numerical comparison
            
        Returns:
            True if all operators match within tolerance
        """
        X, Y, Z = InverseJW.build_spin_ops(n)
        
        # Build original Pauli matrices for comparison
        orig_X, orig_Y, orig_Z = [], [], []
        for i in range(n):
            ops_x = [PauliTool.pauli('I')] * n
            ops_y = [PauliTool.pauli('I')] * n
            ops_z = [PauliTool.pauli('I')] * n
            
            ops_x[i] = PauliTool.pauli('X')
            ops_y[i] = PauliTool.pauli('Y')
            ops_z[i] = PauliTool.pauli('Z')
            
            orig_X.append(PauliTool.kron(ops_x))
            orig_Y.append(PauliTool.kron(ops_y))
            orig_Z.append(PauliTool.kron(ops_z))
        
        # Compare
        max_diff = 0.0
        for i in range(n):
            max_diff = max(max_diff, np.max(np.abs(X[i] - orig_X[i])))
            max_diff = max(max_diff, np.max(np.abs(Y[i] - orig_Y[i])))
            max_diff = max(max_diff, np.max(np.abs(Z[i] - orig_Z[i])))
        
        print(f"Verifying spin-fermion equivalence (n={n})...")
        print(f"  Maximum difference: {max_diff:.2e}")
        success = max_diff < tol
        print(f"  Equivalence verified: {success}")
        
        return success


def test_inverse_jw():
    """Test inverse JW transformation."""
    print("="*60)
    print("Inverse JW: Building Spin Operators from Fermions")
    print("="*60)
    print()
    
    for n in [2, 3]:
        X, Y, Z = InverseJW.build_spin_ops(n)
        
        print(f"Number of sites: {n}")
        print(f"Operators constructed: X, Y, Z (each {n} operators)")
        print()
        
        # Verify σ^z eigenvalues (should be ±1)
        eig_z0 = np.linalg.eigvalsh(Z[0])
        print(f"σ^z_0 eigenvalues (should be ±1):")
        print(f"  {np.sort(eig_z0)}")
        print()
        
        # Verify equivalence with original Pauli matrices
        InverseJW.verify_equivalence(n)
        print()


if __name__ == "__main__":
    test_inverse_jw()
