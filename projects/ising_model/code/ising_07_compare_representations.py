"""
Ising Model - Phase 2: Jordan-Wigner Transformation
Level 4: Comparison with Spin Representation

This code builds the Ising Hamiltonian both in the original spin 
representation and via JW transformation, then verifies they give 
identical spectra. This confirms the equivalence of the two representations.
"""

import numpy as np


class MatrixTool:
    """Utility class for matrix operations."""
    
    @staticmethod
    def pauli(label):
        if label == 'I':
            return np.eye(2)
        elif label == 'X':
            return np.array([[0, 1], [1, 0]])
        elif label == 'Z':
            return np.array([[1, 0], [0, -1]])
    
    @staticmethod
    def kron(ops):
        res = ops[0]
        for op in ops[1:]:
            res = np.kron(res, op)
        return res
    
    @staticmethod
    def eigenvalue(H):
        """Return sorted eigenvalues of Hermitian matrix."""
        return np.sort(np.linalg.eigvalsh(H))


class IsingHamiltonian:
    """Ising Hamiltonian in spin representation."""
    
    @staticmethod
    def build_spin_H(n, J, h):
        """
        Build Ising Hamiltonian in spin representation.
        
        H = -J Σ X_i X_{i+1} - h Σ Z_i
        
        Parameters
        ----------
        n : int
            Number of sites
        J : float
            Exchange coupling constant
        h : float
            Transverse field strength
            
        Returns
        -------
        H : ndarray
            2^n × 2^n Hamiltonian matrix
        """
        dim = 2**n
        H = np.zeros((dim, dim), dtype=complex)
        
        # Interaction terms: -J X_i X_{i+1}
        for i in range(n-1):
            ops = [MatrixTool.pauli('I')] * n
            ops[i] = MatrixTool.pauli('X')
            ops[i+1] = MatrixTool.pauli('X')
            H += -J * MatrixTool.kron(ops)
    
        # Transverse field terms: -h Z_i
        for i in range(n):
            ops = [MatrixTool.pauli('I')] * n
            ops[i] = MatrixTool.pauli('Z')
            H += -h * MatrixTool.kron(ops)
        
        return H


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
    def build_H_jw(n, J, h):
        """
        Build the fermionic Hamiltonian using Jordan-Wigner mapping.
        
        Parameters
        ----------
        n : int
            Number of sites
        J : float
            Exchange coupling constant
        h : float
            Transverse field strength
            
        Returns
        -------
        H : ndarray
            2^n × 2^n Hamiltonian matrix
        """
        dim = 2**n
        c, cdag = JWHamiltonian.build_fermion_ops(n)
        
        n_ops = [cdag[i] @ c[i] for i in range(n)]
        Z_ops = [np.eye(dim) - 2*n_ops[i] for i in range(n)]
        X_plus = [cdag[i] + c[i] for i in range(n)]
        X_minus = [cdag[i] - c[i] for i in range(n)]
        
        H = np.zeros((dim, dim), dtype=complex)
        
        for i in range(n-1):
            H += -J * (X_minus[i] @ X_plus[i+1])
        
        for i in range(n):
            H += -h * Z_ops[i]
        
        return H


if __name__ == "__main__":
    print("="*60)
    print("Ising Model - Phase 2: Jordan-Wigner Transformation")
    print("Level 4: Comparison with Spin Representation")
    print("="*60)
    print()
    print("Comparison: Spin vs. Jordan-Wigner Fermionic Representation")
    print()
    
    for n in [2, 3, 4]:
        J, h = 1.0, 1.5
        
        H_spin = IsingHamiltonian.build_spin_H(n, J, h)
        H_jw = JWHamiltonian.build_H_jw(n, J, h)
        
        E_spin = MatrixTool.eigenvalue(H_spin)
        E_jw = MatrixTool.eigenvalue(H_jw)
        
        max_diff = np.max(np.abs(E_spin - E_jw))
        
        print(f"n = {n} sites:")
        print(f"  Ground state (spin):  {E_spin[0]:.10f}")
        print(f"  Ground state (JW):    {E_jw[0]:.10f}")
        print(f"  Maximum difference:   {max_diff:.2e}")
        print(f"  Representations match: {max_diff < 1e-10}")
        print()
