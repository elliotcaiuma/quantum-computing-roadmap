"""
Jordan-Wigner Fermionic Operators

This module implements the Jordan-Wigner transformation to construct
fermionic creation (c†) and annihilation (c) operators as 2^n × 2^n matrices.

The JW transformation:
    c_i     = (Z_0 ⊗ Z_1 ⊗ ... ⊗ Z_{i-1}) ⊗ σ⁻_i ⊗ I_{i+1} ⊗ ... ⊗ I_{n-1}
    c_i^†   = (Z_0 ⊗ Z_1 ⊗ ... ⊗ Z_{i-1}) ⊗ σ⁺_i ⊗ I_{i+1} ⊗ ... ⊗ I_{n-1}

Key Insight:
The Jordan-Wigner string (product of Z operators) ensures that fermionic
operators on different sites anticommute, even though spin operators commute.

Physical Significance:
- Each c_i is a 2^n × 2^n matrix acting on the full Fock space
- The JW string "counts" the parity of occupied sites before site i
- For site i=0, there is no JW string (just σ⁻ on site 0)
- For site i>0, the string of Z's ensures correct fermionic statistics
"""

import numpy as np
from pauli_utils import PauliTool


class JWTransformation:
    """Jordan-Wigner transformation utilities."""
    
    @staticmethod
    def build_fermion_ops(n):
        """
        Construct fermionic annihilation (c_i) and creation (c_i^†) matrices.
        
        The JW mapping ensures fermionic anticommutation relations:
            {c_i, c_j^†} = δ_ij
            {c_i, c_j} = 0
            {c_i^†, c_j^†} = 0
        
        Args:
            n: Number of sites
            
        Returns:
            Tuple (c, cdag) of lists of 2^n × 2^n matrices
            where c[i] is the annihilation operator for site i
            
        Example:
            For n=2:
            c_0 = σ⁻ ⊗ I
            c_1 = Z ⊗ σ⁻
            
            c_0^† = σ⁺ ⊗ I
            c_1^† = Z ⊗ σ⁺
        """
        I = PauliTool.pauli('I')
        sm = PauliTool.pauli('-')  # sigma^- (annihilation)
        sp = PauliTool.pauli('+')  # sigma^+ (creation)
        Z = PauliTool.pauli('Z')
        
        c, cdag = [], []
        
        for i in range(n):
            ops_c = []
            ops_dag = []
            
            # Jordan-Wigner string: Z operators on all sites before i
            # This is the product ∏_{j=0}^{i-1} Z_j
            for j in range(i):
                ops_c.append(Z)
                ops_dag.append(Z)
            
            # Annihilation/creation on site i (σ⁻_i or σ⁺_i)
            ops_c.append(sm)
            ops_dag.append(sp)
            
            # Identity on all sites after i (I_{i+1} ⊗ ... ⊗ I_{n-1})
            for j in range(i+1, n):
                ops_c.append(I)
                ops_dag.append(I)
            
            c.append(PauliTool.kron(ops_c))
            cdag.append(PauliTool.kron(ops_dag))
        
        return c, cdag
    
    @staticmethod
    def verify_anticommutation(n, tol=1e-10):
        """
        Verify that JW operators satisfy fermionic anticommutation relations.
        
        This is a critical sanity check - if the relations are violated,
        the transformation is incorrect.
        
        Checks:
            {c_i, c_j^†} = δ_ij (should be I if i==j, else 0)
            {c_i, c_j} = 0
            {c_i^†, c_j^†} = 0
        
        Args:
            n: Number of sites
            tol: Tolerance for numerical comparison
            
        Returns:
            True if all relations satisfied within tolerance
        """
        c, cdag = JWTransformation.build_fermion_ops(n)
        dim = 2**n
        I = np.eye(dim, dtype=complex)
        
        print(f"Verifying fermionic anticommutation (n={n})...")
        
        max_violation = 0.0
        
        for i in range(n):
            for j in range(n):
                # {c_i, c_j^†}
                anticomm_cdag = PauliTool.anticommutator(c[i], cdag[j])
                expected = I if i == j else np.zeros((dim, dim), dtype=complex)
                violation = np.max(np.abs(anticomm_cdag - expected))
                max_violation = max(max_violation, violation)
                
                # {c_i, c_j}
                anticomm_c = PauliTool.anticommutator(c[i], c[j])
                violation = np.max(np.abs(anticomm_c))
                max_violation = max(max_violation, violation)
                
                # {c_i^†, c_j^†}
                anticomm_dag = PauliTool.anticommutator(cdag[i], cdag[j])
                violation = np.max(np.abs(anticomm_dag))
                max_violation = max(max_violation, violation)
        
        print(f"  Maximum violation: {max_violation:.2e}")
        success = max_violation < tol
        print(f"  Anticommutation satisfied: {success}")
        
        return success


def test_jw_operators():
    """Test JW operator construction and verification."""
    print("="*60)
    print("Jordan-Wigner Transformation: Building Fermionic Operators")
    print("="*60)
    print()
    
    for n in [2, 3, 4]:
        c, cdag = JWTransformation.build_fermion_ops(n)
        
        print(f"Number of sites: {n}")
        print(f"Hilbert space dimension: {2**n}")
        print(f"Fermionic operators constructed:")
        for i in range(n):
            print(f"  c_{i}: shape = {c[i].shape}, dtype = {c[i].dtype}")
            print(f"  c_{i}^†: shape = {cdag[i].shape}, dtype = {cdag[i].dtype}")
        print()
    
    print("="*60)
    print("Verifying Anticommutation Relations")
    print("="*60)
    print()
    
    all_pass = True
    for n in [2, 3, 4]:
        passed = JWTransformation.verify_anticommutation(n)
        all_pass = all_pass and passed
        print()
    
    print(f"All tests passed: {all_pass}")


if __name__ == "__main__":
    test_jw_operators()
