"""
Pauli Matrix Utilities

This module provides fundamental tools for working with Pauli matrices
and tensor products. These are the building blocks for all Jordan-Wigner
transformation code.

Key Functions:
- pauli(label): Return Pauli matrix by label (I, X, Y, Z, +, -)
- kron(ops): Kronecker product of multiple matrices
- commutator(A, B): Compute [A, B] = AB - BA
- anticommutator(A, B): Compute {A, B} = AB + BA

Physical Significance:
- Pauli matrices form the basis for single-qubit operators
- Raising/lowering operators (σ⁺, σ⁻) connect to fermionic creation/annihilation
- Kronecker products build multi-site operators
- Commutators/anticommutators verify algebraic relations
"""

import numpy as np


class PauliTool:
    """Utility class for Pauli matrices and tensor products."""
    
    @staticmethod
    def pauli(label):
        """
        Return Pauli matrix by label.
        
        Args:
            label: 'I', 'X', 'Y', 'Z', '+', or '-'
            
        Returns:
            2x2 numpy array
            
        Examples:
            >>> PauliTool.pauli('X')
            array([[0, 1],
                   [1, 0]])
            >>> PauliTool.pauli('+')  # sigma^+ (raising)
            array([[0, 1],
                   [0, 0]])
        """
        if label == 'I':
            return np.eye(2, dtype=complex)
        elif label == 'X':
            return np.array([[0, 1], [1, 0]], dtype=complex)
        elif label == 'Y':
            return np.array([[0, -1j], [1j, 0]], dtype=complex)
        elif label == 'Z':
            return np.array([[1, 0], [0, -1]], dtype=complex)
        elif label == '+':
            return np.array([[0, 1], [0, 0]], dtype=complex)  # sigma^+
        elif label == '-':
            return np.array([[0, 0], [1, 0]], dtype=complex)  # sigma^-
        else:
            raise ValueError(f"Unknown Pauli label: {label}")
    
    @staticmethod
    def kron(ops):
        """
        Kronecker product of a list of matrices.
        
        Args:
            ops: List of 2x2 matrices
            
        Returns:
            2^n x 2^n matrix (n = len(ops))
            
        Example:
            For 2 sites: kron([Z, I]) = Z ⊗ I (4x4 matrix)
        """
        res = ops[0]
        for op in ops[1:]:
            res = np.kron(res, op)
        return res
    
    @staticmethod
    def commutator(A, B):
        """Compute [A, B] = AB - BA."""
        return A @ B - B @ A
    
    @staticmethod
    def anticommutator(A, B):
        """Compute {A, B} = AB + BA."""
        return A @ B + B @ A


def test_pauli_algebra():
    """Test Pauli matrix algebra relations."""
    X, Y, Z = PauliTool.pauli('X'), PauliTool.pauli('Y'), PauliTool.pauli('Z')
    sp, sm = PauliTool.pauli('+'), PauliTool.pauli('-')
    
    print("Testing Pauli algebra:")
    print("="*50)
    
    # Test [X, Y] = 2iZ
    comm_XY = PauliTool.commutator(X, Y)
    expected = 2j * Z
    print(f"[X, Y] = {comm_XY}")
    print(f"2iZ   = {expected}")
    print(f"Match: {np.allclose(comm_XY, expected)}")
    print()
    
    # Test {σ⁺, σ⁻} = I
    anticomm = PauliTool.anticommutator(sp, sm)
    print(f"{{sigma^+, sigma^-}} = {anticomm}")
    print(f"Should be: I = {np.eye(2)}")
    print(f"Match: {np.allclose(anticomm, np.eye(2))}")
    print()
    
    # Test tensor product
    Z0 = PauliTool.kron([Z, PauliTool.pauli('I')])
    Z1 = PauliTool.kron([PauliTool.pauli('I'), Z])
    print(f"Z ⊗ I (4x4):")
    print(Z0)
    print()
    print(f"I ⊗ Z (4x4):")
    print(Z1)


if __name__ == "__main__":
    test_pauli_algebra()
