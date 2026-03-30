"""
Level 1a: Mean-Field Core Functions
====================================

This module implements the core equations of mean-field theory for the
transverse Ising model with general spin magnitude s.

Physical System
---------------
The transverse Ising model describes spins on a lattice with:
- Ferromagnetic coupling J₀ along the z-direction
- Transverse field Γ along the x-direction (creates quantum fluctuations)

The Hamiltonian is:
    H = -J₀ Σ⟨i,j⟩ σᵢᶻ σⱼᶻ - Γ Σᵢ σᵢˣ

where σ are spin operators with eigenvalues ±s.

Spin Factor s
-------------
The spin factor s determines the magnitude of the spin:
- s = 1/2: Spin-1/2 systems (quantum bits, electrons)
- s = 1: Spin-1 systems (some magnetic materials)
- s = 1: Pauli matrix convention (eigenvalues ±1)

For spin-1/2 with Pauli matrices, we typically use s = 1 (not 1/2) because
Pauli matrices σᶻ have eigenvalues ±1, not ±1/2.

The relationship is:
    Sᶻ = (ℏ/2) σᶻ  →  In units where ℏ=1: Sᶻ = σᶻ/2

So for true spin-1/2: s = 1/2
For Pauli matrices: s = 1

Mean-Field Theory
-----------------
The key idea: replace the many-body interaction with an effective field.
Each spin feels an average field from all other spins:
    h_eff = (Γ, 0, J₀z⟨σᶻ⟩)

where z is the coordination number (number of nearest neighbors).

Key Equations (with spin factor s)
----------------------------------
1. Effective field magnitude:
   h = √(Γ² + (J₀z⟨σᶻ⟩)²)

2. Self-consistency equation:
   ⟨σᶻ⟩ = s × tanh(βhs) × (J₀z⟨σᶻ⟩ / h)
   
   Note: The factor s appears in two places:
   - Overall prefactor (maximum possible magnetization)
   - Inside tanh (thermal energy scale)

3. Critical temperature:
   T_c = (Γs) / [k_B arctanh(Γ/(J₀zs))]
   
   For s = 1 (Pauli): T_c = Γ / [k_B arctanh(Γ/(J₀z))]
   For s = 1/2: T_c = Γ / [2k_B arctanh(Γ/(J₀z))]

4. Quantum critical point:
   Γ_c = J₀zs
   
   For s = 1 (Pauli): Γ_c = J₀z
   For s = 1/2: Γ_c = J₀z/2

5. Ground state (T = 0):
   ⟨σᶻ⟩ = s × √(1 - (Γ/Γ_c)²)

Reference
---------
Based on: 1_ising_mean_field.py
"""

import numpy as np
from scipy.optimize import brentq

# Physical constants
kB = 1.0  # Boltzmann constant (set to 1 for convenience)


def effective_field(sigma_z, gamma, J0, z=1):
    """
    Calculate the magnitude of the effective field.
    
    The effective field has two components:
    - x-component: Γ (transverse field)
    - z-component: J₀z⟨σᶻ⟩ (molecular field from neighbors)
    
    The magnitude is:
        h = √(Γ² + (J₀z⟨σᶻ⟩)²)
    
    Note: This does NOT depend on the spin factor s.
    
    Parameters
    ----------
    sigma_z : float
        Order parameter ⟨σᶻ⟩ (trial value)
    gamma : float
        Transverse field strength Γ
    J0 : float
        Ferromagnetic coupling constant
    z : int, optional
        Coordination number (default: 1)
        - z = 1: 1D chain (mean-field approx)
        - z = 2: 2D square lattice
        - z = 4: 2D square lattice (actual)
        - z = 6: 3D cubic lattice
    
    Returns
    -------
    h_mag : float
        Magnitude of the effective field
    
    Examples
    --------
    >>> effective_field(0.5, 0.3, 1.0, z=1)
    0.583...
    """
    return np.sqrt(gamma**2 + (sigma_z * J0 * z)**2)


def self_consistency_eq(sigma_z, gamma, J0, beta, z=1, s=1.0):
    """
    Self-consistency equation for the order parameter.
    
    We want to find ⟨σᶻ⟩ such that:
        ⟨σᶻ⟩ = ⟨σᶻ⟩_thermal
    
    The thermal average is:
        ⟨σᶻ⟩_thermal = s × tanh(βhs) × (J₀z⟨σᶻ⟩ / h)
    
    This function computes:
        f(⟨σᶻ⟩) = ⟨σᶻ⟩ - ⟨σᶻ⟩_thermal
    
    We find the root f(⟨σᶻ⟩) = 0 using numerical methods.
    
    Parameters
    ----------
    sigma_z : float
        Trial value of order parameter ⟨σᶻ⟩
    gamma : float
        Transverse field Γ
    J0 : float
        Coupling constant
    beta : float
        Inverse temperature β = 1/(k_B T)
    z : int, optional
        Coordination number (default: 1)
    s : float, optional
        Spin magnitude (default: 1.0 for Pauli matrices)
        - s = 1.0: Pauli matrix convention (eigenvalues ±1)
        - s = 0.5: True spin-1/2 systems
    
    Returns
    -------
    f : float
        Value of self-consistency function f(⟨σᶻ⟩)
    
    Notes
    -----
    There are always two solutions:
    1. Trivial: ⟨σᶻ⟩ = 0 (paramagnetic phase)
    2. Non-trivial: ⟨σᶻ⟩ ≠ 0 (ferromagnetic phase, exists only for T < T_c)
    
    The maximum possible value of ⟨σᶻ⟩ is s (not 1).
    """
    # Calculate effective field magnitude
    h_mag = effective_field(sigma_z, gamma, J0, z)
    
    # Thermal average of σᶻ
    # Formula: ⟨σᶻ⟩ = s × tanh(βhs) × (J₀z⟨σᶻ⟩ / h)
    if h_mag < 1e-10:
        # Avoid division by zero when h → 0
        sigma_z_ave = 0.0
    else:
        sigma_z_ave = s * np.tanh(beta * h_mag * s) * (J0 * z * sigma_z / h_mag)
    
    # Return f(σᶻ) = σᶻ - ⟨σᶻ⟩_thermal
    return sigma_z - sigma_z_ave


def find_critical_temperature(gamma, J0, z=1, s=1.0, kB=1.0):
    """
    Calculate the critical temperature T_c.
    
    At T = T_c, the order parameter ⟨σᶻ⟩ → 0, so h → Γ.
    The self-consistency equation becomes:
        1 = (J₀zs/Γ) × tanh(Γs/(k_B T_c))
    
    Solving for T_c:
        T_c = (Γs) / [k_B arctanh(Γ/(J₀zs))]
    
    Parameters
    ----------
    gamma : float
        Transverse field Γ
    J0 : float
        Coupling constant
    z : int, optional
        Coordination number (default: 1)
    s : float, optional
        Spin magnitude (default: 1.0)
    kB : float, optional
        Boltzmann constant (default: 1)
    
    Returns
    -------
    Tc : float
        Critical temperature
        
        - Tc > 0: Ordered phase exists for T < Tc
        - Tc = 0: Quantum disordered phase (no order at any T)
    
    Special Cases
    -------------
    1. Classical limit (Γ → 0):
       T_c = J₀zs / k_B
       
       For s = 1: T_c = J₀z / k_B
       For s = 1/2: T_c = J₀z / (2k_B)
       
    2. Quantum critical point (Γ ≥ J₀zs):
       T_c = 0 (no finite-temperature phase transition)
       
       For s = 1: Γ_c = J₀z
       For s = 1/2: Γ_c = J₀z/2
    
    Examples
    --------
    >>> find_critical_temperature(0.0, 1.0, z=1, s=1.0)  # Classical limit, s=1
    1.0
    >>> find_critical_temperature(0.0, 1.0, z=1, s=0.5)  # Classical limit, s=1/2
    0.5
    >>> find_critical_temperature(1.0, 1.0, z=1, s=1.0)  # Quantum critical point, s=1
    0.0
    """
    # Quantum critical point (depends on s!)
    gamma_c = J0 * z * s
    
    if gamma == 0:
        # Classical limit: use L'Hôpital's rule
        # lim_{Γ→0} (Γs)/arctanh(Γ/Γ_c) = Γ_c s = J₀zs²
        # But actually: T_c = J₀zs / k_B
        return (J0 * z * s) / kB
    
    elif gamma >= gamma_c:
        # Quantum disordered phase
        # No solution to the self-consistency equation
        return 0.0
    
    else:
        # General formula: T_c = (Γs) / [k_B arctanh(Γ/Γ_c)]
        return (gamma * s / kB) / np.arctanh(gamma / gamma_c)


def solve_self_consistency(gamma, J0, T, z=1, s=1.0, kB=1.0):
    """
    Solve for the order parameter ⟨σᶻ⟩ at temperature T.
    
    This is the main solver function. It handles three cases:
    
    1. T = 0: Use analytical ground state formula
    2. T ≥ T_c: Return 0 (disordered phase)
    3. 0 < T < T_c: Solve numerically using Brent's method
    
    Parameters
    ----------
    gamma : float
        Transverse field Γ
    J0 : float
        Coupling constant
    T : float
        Temperature
    z : int, optional
        Coordination number (default: 1)
    s : float, optional
        Spin magnitude (default: 1.0)
    kB : float, optional
        Boltzmann constant (default: 1)
    
    Returns
    -------
    sigma_z : float
        Order parameter ⟨σᶻ⟩
        
        - 0 ≤ ⟨σᶻ⟩ ≤ s
        - ⟨σᶻ⟩ = s: Perfect order (all spins aligned)
        - ⟨σᶻ⟩ = 0: Disordered (random spins)
    
    Algorithm
    ---------
    1. Check if in quantum disordered phase (Γ ≥ Γ_c)
    2. Check if at zero temperature (use analytical formula)
    3. Check if above T_c (return 0)
    4. Use Brent's method to find non-trivial root in [ε, s]
    
    Ground State Formula (T = 0)
    ----------------------------
    ⟨σᶻ⟩ = s × √(1 - (Γ/Γ_c)²)
    
    where Γ_c = J₀zs
    
    Examples
    --------
    >>> solve_self_consistency(0.3, 1.0, T=0, z=1, s=1.0)  # Ground state, s=1
    0.9539...
    >>> solve_self_consistency(0.3, 1.0, T=0, z=1, s=0.5)  # Ground state, s=1/2
    0.4769...
    >>> solve_self_consistency(0.3, 1.0, T=2.0, z=1, s=1.0)  # Above T_c
    0.0
    """
    # Quantum critical point (depends on s!)
    gamma_c = J0 * z * s
    
    # Case 1: Quantum disordered phase
    if gamma >= gamma_c:
        return 0.0
    
    # Case 2: Zero temperature (analytical solution)
    # Ground state: ⟨σᶻ⟩ = s × √(1 - (Γ/Γ_c)²)
    if T < 1e-10:
        return s * np.sqrt(1 - (gamma / gamma_c)**2)
    
    # Case 3: Calculate T_c and check if above it
    Tc = find_critical_temperature(gamma, J0, z, s, kB)
    if T >= Tc:
        return 0.0  # Disordered phase
    
    # Case 4: Solve numerically for 0 < T < T_c
    beta = 1.0 / (kB * T)
    
    try:
        # Brent's method finds root in interval [1e-6, s]
        # Lower bound > 0 to avoid trivial solution ⟨σᶻ⟩ = 0
        # Upper bound = s (maximum possible magnetization)
        sigma_z_solution = brentq(
            self_consistency_eq, 
            1e-6, s, 
            args=(gamma, J0, beta, z, s)
        )
        return sigma_z_solution
    
    except ValueError:
        # No non-trivial solution found
        return 0.0


def solve_sx_component(gamma, J0, T, z=1, s=1.0, kB=1.0):
    """
    Calculate the transverse component ⟨σˣ⟩.
    
    Once ⟨σᶻ⟩ is known, ⟨σˣ⟩ is given by:
        ⟨σˣ⟩ = s × tanh(βhs) × (Γ / h)
    
    Parameters
    ----------
    gamma : float
        Transverse field Γ
    J0 : float
        Coupling constant
    T : float
        Temperature
    z : int, optional
        Coordination number (default: 1)
    s : float, optional
        Spin magnitude (default: 1.0)
    kB : float, optional
        Boltzmann constant (default: 1)
    
    Returns
    -------
    sigma_x : float
        Transverse spin component ⟨σˣ⟩
    
    Physical Interpretation
    -----------------------
    - At T = 0, Γ = 0: ⟨σˣ⟩ = 0 (all spins along z)
    - At T = 0, Γ = Γ_c: ⟨σˣ⟩ = s (all spins along x)
    - At high T: ⟨σˣ⟩ → 0 (thermal fluctuations)
    
    Notes
    -----
    Unlike ⟨σᶻ⟩, the transverse component ⟨σˣ⟩ is always non-zero
    when Γ > 0 (even in the ordered phase).
    
    At T = 0, the sum rule holds:
        ⟨σᶻ⟩² + ⟨σˣ⟩² = s²
    """
    # First solve for ⟨σᶻ⟩
    sigma_z = solve_self_consistency(gamma, J0, T, z, s, kB)
    
    # Calculate effective field magnitude
    h_mag = effective_field(sigma_z, gamma, J0, z)
    
    # Avoid division by zero
    if h_mag < 1e-10:
        return 0.0
    
    # Thermal average: ⟨σˣ⟩ = s × tanh(βhs) × (Γ / h)
    beta = 1.0 / (kB * T) if T > 1e-10 else 1e10
    sigma_x = s * np.tanh(beta * h_mag * s) * (gamma / h_mag)
    
    return sigma_x


# ============================================================================
# Main: Test the core functions
# ============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Mean-Field Core Functions - Test Suite")
    print("=" * 60)
    
    # Test parameters
    J0 = 1.0
    z = 1
    
    print(f"\nParameters: J0 = {J0}, z = {z}")
    
    # ========================================================================
    # Test Case 1: Pauli matrix convention (s = 1)
    # ========================================================================
    
    print("\n" + "=" * 60)
    print("Test Case 1: Pauli Matrix Convention (s = 1)")
    print("=" * 60)
    
    s = 1.0
    gamma_c = J0 * z * s
    gamma = 0.3 * gamma_c
    
    print(f"\nSpin: s = {s}")
    print(f"Gamma_c = J0*z*s = {gamma_c:.3f}")
    print(f"Gamma = 0.3 * Gamma_c = {gamma:.3f}")
    
    # Test 1.1: Critical temperature
    Tc = find_critical_temperature(gamma, J0, z, s)
    print(f"\nT_c = {Tc:.4f}")
    print(f"Expected: T_c > 0 (ordered phase exists)")
    
    # Test 1.2: Ground state order parameter
    sigma_z_0 = solve_self_consistency(gamma, J0, T=0, z=z, s=s)
    expected = s * np.sqrt(1 - (gamma/gamma_c)**2)
    print(f"\n<sigma^z> at T=0: {sigma_z_0:.4f}")
    print(f"Expected:         {expected:.4f}")
    print(f"Formula:          s * sqrt(1 - (Gamma/Gamma_c)^2) = {expected:.4f}")
    
    # Test 1.3: Order parameter at T = T_c/2
    sigma_z_half = solve_self_consistency(gamma, J0, T=Tc/2, z=z, s=s)
    print(f"\n<sigma^z> at T=T_c/2: {sigma_z_half:.4f}")
    print(f"Expected: 0 < <sigma^z> < s = {s}")
    
    # Test 1.4: Transverse component
    sigma_x_0 = solve_sx_component(gamma, J0, T=0, z=z, s=s)
    expected_x = gamma / (J0 * z)
    print(f"\n<sigma^x> at T=0: {sigma_x_0:.4f}")
    print(f"Expected:         {expected_x:.4f}")
    print(f"Formula:          Gamma/(J0*z) = {expected_x:.4f}")
    
    # Verify sum rule at T=0
    sum_rule = sigma_z_0**2 + sigma_x_0**2
    print(f"\nSum rule: <sigma^z>^2 + <sigma^x>^2 = {sum_rule:.4f} (should equal s^2 = {s**2:.4f})")
    
    # ========================================================================
    # Test Case 2: True spin-1/2 (s = 0.5)
    # ========================================================================
    
    print("\n" + "=" * 60)
    print("Test Case 2: True Spin-1/2 (s = 0.5)")
    print("=" * 60)
    
    s = 0.5
    gamma_c = J0 * z * s
    gamma = 0.3 * gamma_c
    
    print(f"\nSpin: s = {s}")
    print(f"Gamma_c = J0*z*s = {gamma_c:.3f}")
    print(f"Gamma = 0.3 * Gamma_c = {gamma:.3f}")
    
    # Test 2.1: Critical temperature
    Tc = find_critical_temperature(gamma, J0, z, s)
    print(f"\nT_c = {Tc:.4f}")
    print(f"Note: T_c is smaller than for s=1 (reduced energy scale)")
    
    # Test 2.2: Ground state order parameter
    sigma_z_0 = solve_self_consistency(gamma, J0, T=0, z=z, s=s)
    expected = s * np.sqrt(1 - (gamma/gamma_c)**2)
    print(f"\n<sigma^z> at T=0: {sigma_z_0:.4f}")
    print(f"Expected:         {expected:.4f}")
    print(f"Formula:          s * sqrt(1 - (Gamma/Gamma_c)^2) = {expected:.4f}")
    
    # Test 2.3: Transverse component
    sigma_x_0 = solve_sx_component(gamma, J0, T=0, z=z, s=s)
    expected_x = s * gamma / (J0 * z * s)  # = gamma/(J0*z) but scaled by s
    print(f"\n<sigma^x> at T=0: {sigma_x_0:.4f}")
    
    # Verify sum rule at T=0
    sum_rule = sigma_z_0**2 + sigma_x_0**2
    print(f"\nSum rule: <sigma^z>^2 + <sigma^x>^2 = {sum_rule:.4f} (should equal s^2 = {s**2:.4f})")
    
    # ========================================================================
    # Test Case 3: Quantum critical point
    # ========================================================================
    
    print("\n" + "=" * 60)
    print("Test Case 3: Quantum Critical Point (s = 1)")
    print("=" * 60)
    
    s = 1.0
    gamma_c = J0 * z * s
    gamma = gamma_c  # Exactly at quantum critical point
    
    Tc_c = find_critical_temperature(gamma, J0, z, s)
    sigma_z_c = solve_self_consistency(gamma, J0, T=0, z=z, s=s)
    
    print(f"\nGamma = Gamma_c = {gamma_c}")
    print(f"T_c = {Tc_c:.4f} (should be 0)")
    print(f"<sigma^z> at T=0: {sigma_z_c:.4f} (should be 0)")
    print(f"Physics: Quantum fluctuations destroy order")
    
    # ========================================================================
    # Summary
    # ========================================================================
    
    print("\n" + "=" * 60)
    print("All tests complete!")
    print("=" * 60)
    
    print("\nKey Observations:")
    print("  1. Spin factor s sets the energy scale and maximum magnetization")
    print("  2. For s=1 (Pauli): Gamma_c = J0*z, max <sigma^z> = 1")
    print("  3. For s=0.5: Gamma_c = J0*z/2, max <sigma^z> = 0.5")
    print("  4. Sum rule <sigma^z>^2 + <sigma^x>^2 = s^2 holds at T=0")
    print("  5. At Gamma = Gamma_c: quantum phase transition (<sigma^z> = 0)")
