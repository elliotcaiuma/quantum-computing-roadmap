"""
Ising Model - Phase 2: Jordan-Wigner Transformation
Level 1: Building Fermionic Operators

This code constructs fermionic creation (c_i^†) and annihilation (c_i) 
operators as 2^n × 2^n matrices using the Jordan-Wigner transformation.

JW mapping:
c_i     = (Z_0 ⊗ Z_1 ⊗ ... ⊗ Z_{i-1}) ⊗ σ⁻_i ⊗ I_{i+1} ⊗ ... ⊗ I_{n-1}
c_i^†   = (Z_0 ⊗ Z_1 ⊗ ... ⊗ Z_{i-1}) ⊗ σ⁺_i ⊗ I_{i+1} ⊗ ... ⊗ I_{n-1}

where σ⁻ = |0⟩⟨1| and σ⁺ = |1⟩⟨0|
"""

import numpy as np


class MatrixTool:
    """Utility class for matrix operations."""
    
    @staticmethod
    def pauli(label):
        """Return Pauli matrix by label."""
        if label == 'I':
            return np.eye(2)
        elif label == 'X':
            return np.array([[0, 1], [1, 0]])
        elif label == 'Y':
            return np.array([[0, -1j], [1j, 0]])
        elif label == 'Z':
            return np.array([[1, 0], [0, -1]])
    
    @staticmethod
    def kron(ops):
        """Kronecker product of a list of matrices."""
        res = ops[0]
        for op in ops[1:]:
            res = np.kron(res, op)
        return res


class JWHamiltonian:
    """Jordan-Wigner transformation for spin-to-fermion mapping."""
    
    @staticmethod
    def build_fermion_ops(n):
        """
        Construct fermionic annihilation (c_i) and creation (c_i^†) 
        matrices using the Jordan-Wigner transformation.
        
        Parameters
        ----------
        n : int
            Number of spin sites
            
        Returns
        -------
        c : list of ndarray
            Annihilation operators [c_0, c_1, ..., c_{n-1}]
        cdag : list of ndarray
            Creation operators [c_0^†, c_1^†, ..., c_{n-1}^†]
        """
        I = MatrixTool.pauli('I')
        sm = np.array([[0, 1], [0, 0]])   # σ⁻ (annihilation)
        sp = np.array([[0, 0], [1, 0]])   # σ⁺ (creation)
        Z = MatrixTool.pauli('Z')
        
        c, cdag = [], []
        
        for i in range(n):
            # Build the operator string for site i
            ops_c = []
            ops_dag = []
            
            # Jordan-Wigner string: Z operators on all sites before i
            for j in range(i):
                ops_c.append(Z)
                ops_dag.append(Z)
            
            # Annihilation/creation on site i
            ops_c.append(sm)
            ops_dag.append(sp)
            
            # Identity on all sites after i
            for j in range(i+1, n):
                ops_c.append(I)
                ops_dag.append(I)
            
            c.append(MatrixTool.kron(ops_c))
            cdag.append(MatrixTool.kron(ops_dag))
        
        return c, cdag


if __name__ == "__main__":
    print("="*60)
    print("Ising Model - Phase 2: Jordan-Wigner Transformation")
    print("Level 1: Building Fermionic Operators")
    print("="*60)
    print()
    
    for n in [2, 3, 4]:
        c, cdag = JWHamiltonian.build_fermion_ops(n)
        
        print(f"Number of sites: {n}")
        print(f"Hilbert space dimension: {2**n}")
        print(f"Fermionic operators constructed:")
        for i in range(n):
            print(f"  c_{i}: shape = {c[i].shape}, dtype = {c[i].dtype}")
            print(f"  c_{i}^†: shape = {cdag[i].shape}, dtype = {cdag[i].dtype}")
        print()
