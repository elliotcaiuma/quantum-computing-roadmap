"""
Ising Model - Phase 2: Jordan-Wigner Transformation
Level 3: Building the Fermionic Hamiltonian

This code constructs the transverse-field Ising Hamiltonian in fermionic
form using the Jordan-Wigner transformation.

Spin operators in terms of fermions:
X_i = c_i^† + c_i
Z_i = I - 2 n_i = I - 2 c_i^† c_i

Hamiltonian:
H = -J Σ X_i X_{i+1} - h Σ Z_i
  = -J Σ (c_i^† - c_i)(c_{i+1}^† + c_{i+1}) - h Σ (I - 2 n_i)
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
        
        # Number operators n_i = c_i^† c_i
        n_ops = [cdag[i] @ c[i] for i in range(n)]
        
        # Z_i = I - 2 n_i
        Z_ops = [np.eye(dim) - 2*n_ops[i] for i in range(n)]
        
        # X_i = c_i^† + c_i
        X_plus = [cdag[i] + c[i] for i in range(n)]
        
        # (c_i^† - c_i) for XX interaction
        X_minus = [cdag[i] - c[i] for i in range(n)]
        
        H = np.zeros((dim, dim), dtype=complex)
        
        # Interaction term: -J X_i X_{i+1}
        for i in range(n-1):
            H += -J * (X_minus[i] @ X_plus[i+1])
        
        # Transverse field term: -h Z_i
        for i in range(n):
            H += -h * Z_ops[i]
        
        return H


if __name__ == "__main__":
    print("="*60)
    print("Ising Model - Phase 2: Jordan-Wigner Transformation")
    print("Level 3: Building the Fermionic Hamiltonian")
    print("="*60)
    print()
    
    # Parameters
    n = 4
    J = 1.0
    h = 1.5
    
    H_jw = JWHamiltonian.build_H_jw(n, J, h)
    energies = MatrixTool.eigenvalue(H_jw)
    
    print(f"Ising Model: n={n} sites, J={J}, h={h}")
    print(f"Hilbert space dimension: {2**n}")
    print()
    print("Energy spectrum (sorted):")
    for i, E in enumerate(energies):
        print(f"  E_{i:2d} = {E.real:12.6f}")
    
    print()
    print(f"Ground state energy: E_0 = {energies[0].real:.6f}")
    print(f"Energy gap: ΔE = {energies[1].real - energies[0].real:.6f}")
