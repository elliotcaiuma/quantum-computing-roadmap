"""
Jordan-Wigner Hamiltonian Builder

This module builds arbitrary 1D spin Hamiltonians in fermionic form
using the Jordan-Wigner transformation.

Supported Models:
1. Transverse-Field Ising Model
   H = -J Σ σ^x_i σ^x_{i+1} - h Σ σ^z_i

2. XY Model (Anisotropic)
   H = -Σ (J_x σ^x_i σ^x_{i+1} + J_y σ^y_i σ^y_{i+1}) - h Σ σ^z_i

3. General Nearest-Neighbor Interactions
   H = -Σ (J_x σ^x_i σ^x_{i+1} + J_y σ^y_i σ^y_{i+1} + J_z σ^z_i σ^z_{i+1}) - h Σ σ^z_i

Key Operator Mappings:
    σ^x_i σ^x_{i+1} → (c^†_i - c_i)(c^†_{i+1} + c_{i+1})
    σ^y_i σ^y_{i+1} → -(c^†_i + c_i)(c^†_{i+1} - c_{i+1})
    σ^z_i           → I - 2 c^†_i c_i

Physical Significance:
- The fermionic Hamiltonian is quadratic (can be diagonalized exactly)
- Ground state energy and gap determine phase behavior
- At critical point (h = J for Ising), gap closes in thermodynamic limit
- Code scales as O(2^n) — limited to n ≲ 20 on classical computers
"""

import numpy as np
from pauli_utils import PauliTool
from jw_operators import JWTransformation


class JWHamiltonian:
    """Build spin Hamiltonians in fermionic form."""
    
    @staticmethod
    def transverse_ising(n, J, h):
        """
        Transverse-field Ising model in fermionic form.
        
        Original spin Hamiltonian:
            H = -J Σ σ^x_i σ^x_{i+1} - h Σ σ^z_i
        
        After JW transformation:
            H = -J Σ (c^†_i - c_i)(c^†_{i+1} + c_{i+1}) + 2h Σ c^†_i c_i - nh
        
        Args:
            n: Number of sites
            J: Coupling strength (interaction)
            h: Transverse field strength
            
        Returns:
            2^n × 2^n Hamiltonian matrix (Hermitian)
            
        Physics:
            - Quantum phase transition at h = J
            - Ordered (ferromagnetic) phase for h < J
            - Disordered (paramagnetic) phase for h > J
            - Critical exponents: ν = 1, z = 1
        """
        c, cdag = JWTransformation.build_fermion_ops(n)
        dim = 2**n
        H = np.zeros((dim, dim), dtype=complex)
        
        # Interaction term: σ^x_i σ^x_{i+1} = (c^†_i - c_i)(c^†_{i+1} + c_{i+1})
        for i in range(n-1):
            X_minus = cdag[i] - c[i]
            X_plus = cdag[i+1] + c[i+1]
            H += -J * (X_minus @ X_plus)
        
        # Field term: σ^z_i = I - 2 c^†_i c_i
        for i in range(n):
            H += -h * (np.eye(dim, dtype=complex) - 2 * cdag[i] @ c[i])
        
        return H
    
    @staticmethod
    def xy_model(n, Jx, Jy, h):
        """
        XY model with anisotropic interactions.
        
        Original spin Hamiltonian:
            H = -Σ (J_x σ^x_i σ^x_{i+1} + J_y σ^y_i σ^y_{i+1}) - h Σ σ^z_i
        
        After JW transformation:
            H = -Σ [J_x (c^†_i - c_i)(c^†_{i+1} + c_{i+1})
                   - J_y (c^†_i + c_i)(c^†_{i+1} - c_{i+1})] + 2h Σ c^†_i c_i
        
        Args:
            n: Number of sites
            Jx: X-coupling strength
            Jy: Y-coupling strength
            h: Transverse field strength
            
        Returns:
            2^n × 2^n Hamiltonian matrix (Hermitian)
            
        Special Cases:
            - Ising limit (Jy = 0): Reduces to transverse-field Ising model
            - XX model (Jx = Jy): Becomes free fermions with hopping only
            - XY anisotropy (γ = (Jx-Jy)/(Jx+Jy)): Controls critical behavior
        """
        c, cdag = JWTransformation.build_fermion_ops(n)
        dim = 2**n
        H = np.zeros((dim, dim), dtype=complex)
        
        for i in range(n-1):
            # σ^x_i σ^x_{i+1}
            X_minus = cdag[i] - c[i]
            X_plus = cdag[i+1] + c[i+1]
            H += -Jx * (X_minus @ X_plus)
            
            # σ^y_i σ^y_{i+1} = -(c^†_i + c_i)(c^†_{i+1} - c_{i+1})
            Y_plus = cdag[i] + c[i]
            Y_minus = cdag[i+1] - c[i+1]
            H += Jy * (Y_plus @ Y_minus)
        
        # Field term
        for i in range(n):
            H += -h * (np.eye(dim, dtype=complex) - 2 * cdag[i] @ c[i])
        
        return H
    
    @staticmethod
    def heisenberg(n, J, h=0, delta=0):
        """
        Heisenberg model with anisotropy.
        
        Original spin Hamiltonian:
            H = J Σ (σ^x_i σ^x_{i+1} + σ^y_i σ^y_{i+1} + Δ σ^z_i σ^z_{i+1}) - h Σ σ^z_i
        
        Args:
            n: Number of sites
            J: Exchange coupling (J > 0: antiferromagnetic, J < 0: ferromagnetic)
            h: Magnetic field (optional)
            delta: Anisotropy parameter (Δ = 0: XY, Δ = 1: isotropic Heisenberg)
            
        Returns:
            2^n × 2^n Hamiltonian matrix (Hermitian)
        """
        c, cdag = JWTransformation.build_fermion_ops(n)
        dim = 2**n
        H = np.zeros((dim, dim), dtype=complex)
        
        for i in range(n-1):
            # σ^x_i σ^x_{i+1}
            X_minus = cdag[i] - c[i]
            X_plus = cdag[i+1] + c[i+1]
            H += J * (X_minus @ X_plus)
            
            # σ^y_i σ^y_{i+1}
            Y_plus = cdag[i] + c[i]
            Y_minus = cdag[i+1] - c[i+1]
            H += J * (Y_plus @ Y_minus)
            
            # Δ σ^z_i σ^z_{i+1}
            if delta != 0:
                n_i = cdag[i] @ c[i]
                n_ip1 = cdag[i+1] @ c[i+1]
                H += J * delta * (np.eye(dim) - 2*n_i) @ (np.eye(dim) - 2*n_ip1)
        
        # Field term
        if h != 0:
            for i in range(n):
                H += -h * (np.eye(dim, dtype=complex) - 2 * cdag[i] @ c[i])
        
        return H


def test_hamiltonians():
    """Test Hamiltonian construction and diagonalization."""
    print("="*60)
    print("JW Hamiltonians: Building and Diagonalizing")
    print("="*60)
    print()
    
    # Parameters
    n = 4
    
    # Transverse-field Ising
    print("1. Transverse-Field Ising Model")
    print("-" * 40)
    J, h = 1.0, 1.5
    H_ising = JWHamiltonian.transverse_ising(n, J, h)
    energies_ising = np.linalg.eigvalsh(H_ising)
    
    print(f"Parameters: n={n}, J={J}, h={h}")
    print(f"Ground state energy: E_0 = {energies_ising[0]:.6f}")
    print(f"Energy gap: ΔE = {energies_ising[1] - energies_ising[0]:.6f}")
    print(f"Full spectrum: {np.sort(energies_ising)}")
    print()
    
    # XY model
    print("2. XY Model (Anisotropic)")
    print("-" * 40)
    H_xy = JWHamiltonian.xy_model(n, Jx=1.0, Jy=0.5, h=1.0)
    energies_xy = np.linalg.eigvalsh(H_xy)
    
    print(f"Parameters: n={n}, Jx=1.0, Jy=0.5, h=1.0")
    print(f"Ground state energy: E_0 = {energies_xy[0]:.6f}")
    print(f"Energy gap: ΔE = {energies_xy[1] - energies_xy[0]:.6f}")
    print()
    
    # Heisenberg model
    print("3. Heisenberg Model (Isotropic)")
    print("-" * 40)
    H_heis = JWHamiltonian.heisenberg(n, J=1.0, h=0, delta=1.0)
    energies_heis = np.linalg.eigvalsh(H_heis)
    
    print(f"Parameters: n={n}, J=1.0, Δ=1.0, h=0")
    print(f"Ground state energy: E_0 = {energies_heis[0]:.6f}")
    print(f"Energy gap: ΔE = {energies_heis[1] - energies_heis[0]:.6f}")
    print()


if __name__ == "__main__":
    test_hamiltonians()
