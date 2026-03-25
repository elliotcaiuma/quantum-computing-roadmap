"""
Level 26: Complete Density Matrix Analyzer

Comprehensive analysis tool for density matrices.
"""

import numpy as np


def is_valid_density_matrix(rho, tol=1e-10):
    """Check if matrix is valid density matrix."""
    if not np.allclose(rho, rho.conj().T):
        return False, "Not Hermitian"
    if not np.abs(np.trace(rho) - 1) < tol:
        return False, "Trace != 1"
    eigenvalues = np.linalg.eigvalsh(rho)
    if np.any(eigenvalues < -tol):
        return False, "Not positive semi-definite"
    return True, "Valid density matrix"


def bloch_vector(rho):
    """Extract Bloch vector components from density matrix."""
    X = np.array([[0, 1], [1, 0]])
    Y = np.array([[0, -1j], [1j, 0]])
    Z = np.array([[1, 0], [0, -1]])
    rx = np.trace(rho @ X).real
    ry = np.trace(rho @ Y).real
    rz = np.trace(rho @ Z).real
    return np.array([rx, ry, rz])


class DensityMatrixAnalyzer:
    """Complete analysis of density matrices."""
    
    def __init__(self, rho):
        """Initialize with density matrix."""
        self.rho = rho
        self.valid, self.msg = is_valid_density_matrix(rho)
    
    def eigenvalues(self):
        """Get eigenvalues."""
        return np.linalg.eigvalsh(self.rho)
    
    def von_neumann_entropy(self):
        """Calculate von Neumann entropy: S(rho) = -Tr(rho log_2 rho)"""
        eigenvalues = self.eigenvalues()
        eigenvalues = eigenvalues[eigenvalues > 1e-10]
        return -np.sum(eigenvalues * np.log2(eigenvalues))
    
    def purity(self):
        """Calculate purity: Pur(rho) = Tr(rho^2)"""
        return np.trace(self.rho @ self.rho).real
    
    def bloch_vector(self):
        """Get Bloch vector."""
        return bloch_vector(self.rho)
    
    def report(self):
        """Print complete analysis report."""
        print(f"Valid: {self.valid} ({self.msg})")
        print(f"Eigenvalues: {self.eigenvalues()}")
        print(f"Purity: {self.purity():.4f}")
        print(f"Von Neumann entropy: {self.von_neumann_entropy():.4f}")
        print(f"Bloch vector: {self.bloch_vector()}")
        print()
        
        if np.isclose(self.purity(), 1.0):
            print("Interpretation: Pure state")
        else:
            print(f"Interpretation: Mixed state (purity < 1)")


if __name__ == "__main__":
    psi_plus = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
    rho_plus = np.outer(psi_plus, psi_plus.conj())
    
    print("=== Pure State |+> ===")
    analyzer = DensityMatrixAnalyzer(rho_plus)
    analyzer.report()
    
    rho_mix = np.eye(2) / 2
    
    print("=== Maximally Mixed State ===")
    analyzer = DensityMatrixAnalyzer(rho_mix)
    analyzer.report()
    
    rho_partial = np.array([[0.7, 0], [0, 0.3]])
    
    print("=== Partially Mixed State ===")
    analyzer = DensityMatrixAnalyzer(rho_partial)
    analyzer.report()
