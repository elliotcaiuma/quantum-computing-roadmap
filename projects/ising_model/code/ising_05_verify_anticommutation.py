"""
Ising Model - Phase 2: Jordan-Wigner Transformation
Level 2: Verifying Anticommutation Relations

This code numerically verifies that the JW-transformed operators satisfy
the canonical fermionic anticommutation relations:

{c_i, c_j^†} = δ_ij
{c_i, c_j} = 0
{c_i^†, c_j^†} = 0

where {A,B} = AB + BA denotes the anticommutator.
"""

import numpy as np


class MatrixTool:
    """Utility class for matrix operations."""
    
    @staticmethod
    def pauli(label):
        if label == 'I':
            return np.eye(2)
        elif label == 'Z':
            return np.array([[1, 0], [0, -1]])
    
    @staticmethod
    def kron(ops):
        res = ops[0]
        for op in ops[1:]:
            res = np.kron(res, op)
        return res


class JWHamiltonian:
    """Jordan-Wigner transformation for spin-to-fermion mapping."""
    
    @staticmethod
    def build_fermion_ops(n):
        I = MatrixTool.pauli('I')
        sm = np.array([[0, 1], [0, 0]])
        sp = np.array([[0, 0], [1, 0]])
        Z = MatrixTool.pauli('Z')
        
        c, cdag = [], []
        
        for i in range(n):
            ops_c = []
            ops_dag = []
            
            for j in range(i):
                ops_c.append(Z)
                ops_dag.append(Z)
            
            ops_c.append(sm)
            ops_dag.append(sp)
            
            for j in range(i+1, n):
                ops_c.append(I)
                ops_dag.append(I)
            
            c.append(MatrixTool.kron(ops_c))
            cdag.append(MatrixTool.kron(ops_dag))
        
        return c, cdag
    
    @staticmethod
    def verify_anticommutation(n):
        """
        Verify fermionic anticommutation relations.
        
        Parameters
        ----------
        n : int
            Number of sites
            
        Returns
        -------
        bool
            True if all relations satisfied within numerical precision
        """
        c, cdag = JWHamiltonian.build_fermion_ops(n)
        dim = 2**n
        I = np.eye(dim)
        
        print("Verifying fermionic anticommutation relations...")
        print(f"Number of sites: {n}, Hilbert space dimension: {dim}")
        print()
        
        max_violation = 0.0
        
        for i in range(n):
            for j in range(n):
                # {c_i, c_j^†}
                anticomm_cdag = c[i] @ cdag[j] + cdag[j] @ c[i]
                expected = I if i == j else np.zeros((dim, dim))
                violation = np.max(np.abs(anticomm_cdag - expected))
                max_violation = max(max_violation, violation)
                
                if i == j:
                    print(f"{{c_{i}, c_{j}^†}} = I, violation = {violation:.2e}")
                
                # {c_i, c_j}
                anticomm_c = c[i] @ c[j] + c[j] @ c[i]
                violation = np.max(np.abs(anticomm_c))
                max_violation = max(max_violation, violation)
                
                # {c_i^†, c_j^†}
                anticomm_dag = cdag[i] @ cdag[j] + cdag[j] @ cdag[i]
                violation = np.max(np.abs(anticomm_dag))
                max_violation = max(max_violation, violation)
        
        print()
        print(f"Maximum anticommutation violation: {max_violation:.2e}")
        
        success = max_violation < 1e-10
        print(f"Anticommutation relations satisfied: {success}")
        
        return success


if __name__ == "__main__":
    print("="*60)
    print("Ising Model - Phase 2: Jordan-Wigner Transformation")
    print("Level 2: Verifying Anticommutation Relations")
    print("="*60)
    print()
    
    for n in [2, 3, 4]:
        print("="*50)
        JWHamiltonian.verify_anticommutation(n)
        print()
