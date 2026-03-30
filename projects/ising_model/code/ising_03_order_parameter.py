"""
Level 1c: Order Parameter Plots
================================

This module visualizes the behavior of the order parameter <sigma^z> and the
transverse component <sigma^x> as functions of temperature and transverse field,
including the spin factor s.

Physical Background
-------------------
The order parameter <sigma^z> characterizes the phase of the system:

1. Ordered Phase (T < T_c, Gamma < Gamma_c):
   - <sigma^z> != 0: Spontaneous symmetry breaking
   - Spins preferentially align along +z or -z direction
   - Long-range ferromagnetic order

2. Disordered Phase (T > T_c or Gamma > Gamma_c):
   - <sigma^z> = 0: Symmetry restored
   - Spins randomly oriented
   - No net magnetization

The transverse component <sigma^x> is always non-zero when Gamma > 0:
- It represents quantum fluctuations induced by the transverse field
- Even in the ordered phase, spins have some x-component

Spin Factor s
-------------
The spin magnitude s affects:
- Maximum possible order: <sigma^z>_max = s
- Quantum critical point: Gamma_c = J0*z*s
- Critical temperature: T_c(0) = J0*z*s/k_B
- Ground state: <sigma^z>_(T=0) = s * sqrt(1 - (Gamma/Gamma_c)^2)

Common values:
- s = 1.0: Pauli matrix convention (eigenvalues +/-1)
- s = 0.5: True spin-1/2 systems (eigenvalues +/-1/2)

Key Behaviors
-------------
1. Temperature dependence:
   - At T = 0: Maximum order (<sigma^z> largest)
   - As T increases: Thermal fluctuations reduce order
   - At T = T_c: Phase transition (<sigma^z> -> 0 continuously)

2. Field dependence:
   - At Gamma = 0: Maximum order (classical Ising model)
   - As Gamma increases: Quantum fluctuations reduce order
   - At Gamma = Gamma_c: Quantum phase transition (<sigma^z> = 0)

3. Critical behavior:
   - Near T_c: <sigma^z> proportional to (T_c - T)^beta with beta = 1/2 (mean-field)
   - Near Gamma_c: <sigma^z> proportional to (Gamma_c - Gamma)^beta with beta = 1/2 (mean-field)

Usage
-----
Run this script to display all three plots:
    python ising_03_order_parameter.py

Reference
---------
Based on: 1_ising_mean_field.py - plot_order_parameter(), plot_spin()
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Import core functions from module 01
from ising_01_mean_field_core import (
    find_critical_temperature,
    solve_self_consistency,
    solve_sx_component
)

# ============================================================================
# Plot Configuration
# ============================================================================

# Set matplotlib parameters for consistent appearance
rcParams['font.size'] = 11
rcParams['figure.figsize'] = (10, 6)
rcParams['axes.linewidth'] = 1.2
rcParams['grid.linewidth'] = 0.8


def plot_order_parameter(J0=1.0, z=1, s=1.0, kB=1.0, show=True):
    """
    Plot the order parameter <sigma^z> vs temperature for various Gamma values.
    
    This shows how thermal fluctuations destroy ferromagnetic order.
    
    Parameters
    ----------
    J0 : float, optional
        Coupling constant (default: 1.0)
    z : int, optional
        Coordination number (default: 1)
    s : float, optional
        Spin magnitude (default: 1.0)
    kB : float, optional
        Boltzmann constant (default: 1.0)
    show : bool, optional
        Whether to display the plot (default: True)
    
    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes
    
    Plot Features
    -------------
    - Each curve: Fixed Gamma value, varying T
    - X-axis: Normalized temperature T/T_c(0)
    - Y-axis: Order parameter <sigma^z>
    - Markers: Critical temperature T_c for each Gamma
    
    Physical Interpretation
    -----------------------
    - At T = 0: <sigma^z> is maximum (ground state order = s)
    - As T -> T_c: <sigma^z> -> 0 continuously (second-order transition)
    - For T > T_c: <sigma^z> = 0 (disordered phase)
    - Higher Gamma -> Lower T_c -> Order destroyed at lower temperature
    
    Effect of Spin Factor s
    -----------------------
    - Maximum <sigma^z> = s (at T=0, Gamma=0)
    - Shape of curves is independent of s (when normalized)
    """
    fig, ax = plt.subplots()
    
    # ========================================================================
    # Calculate Reference Temperature
    # ========================================================================
    
    Tc_0 = find_critical_temperature(0, J0, z, s, kB)
    
    # Temperature range: 0 to 1.5 x T_c(0)
    T_vals = np.linspace(0, 1.5 * Tc_0, 500)
    
    # ========================================================================
    # Calculate Order Parameter for Different Gamma Values
    # ========================================================================
    
    # Representative Gamma values (normalized by Gamma_c)
    gamma_fractions = [0.0, 0.3, 0.6, 0.9, 1.0]
    
    for gamma_frac in gamma_fractions:
        # Actual Gamma value
        gamma = gamma_frac * J0 * z * s
        
        # Calculate <sigma^z> for each temperature
        sigma_z_vals = [
            solve_self_consistency(gamma, J0, T, z, s, kB) 
            for T in T_vals
        ]
        
        # Calculate T_c for this Gamma
        Tc = find_critical_temperature(gamma, J0, z, s, kB)
        
        # Create label with Gamma and T_c information
        label = f'$\\Gamma/\\Gamma_c = {gamma_frac:.1f}$'
        if Tc > 0:
            label += f' ($T_c/T_c(0) = {Tc/Tc_0:.2f}$)'
        
        # Plot the curve
        line = ax.plot(T_vals / Tc_0, sigma_z_vals, linewidth=2.5, label=label)[0]
        
        # Mark the critical temperature with a circle
        if Tc > 0:
            ax.plot(Tc / Tc_0, 0, 'o', markersize=8, color=line.get_color(),
                   label=f'$T_c$ for $\\Gamma/\\Gamma_c={gamma_frac:.1f}$')
    
    # ========================================================================
    # Labels and Formatting
    # ========================================================================
    
    ax.set_xlabel(r'$T / T_c(\Gamma=0)$', fontsize=13, fontweight='bold')
    ax.set_ylabel(r'$\langle \sigma^z \rangle$', fontsize=13, fontweight='bold')
    ax.set_title('Order Parameter vs Temperature\nMean-Field Theory', 
                 fontsize=13, fontweight='bold')
    
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Horizontal line at <sigma^z> = 0
    ax.axhline(y=0, color='k', linestyle='--', linewidth=1, alpha=0.5)
    
    # Axis limits
    ax.set_xlim(0, 1.5)
    ax.set_ylim(-0.05, s*1.05)
    
    # Key ticks
    ax.set_xticks([0, 0.5, 1.0, 1.5])
    ax.set_yticks([0, s*0.5, s])
    
    plt.tight_layout()
    
    if show:
        plt.show()
    
    return fig, ax


def plot_spin_components(gamma, J0=1.0, z=1, s=1.0, kB=1.0, show=True):
    """
    Plot both <sigma^z> and <sigma^x> vs temperature for a fixed Gamma.
    
    This shows the competition between ordering (<sigma^z>) and quantum
    fluctuations (<sigma^x>).
    
    Parameters
    ----------
    gamma : float
        Transverse field Gamma (in units of J0*z*s)
    J0 : float, optional
        Coupling constant (default: 1.0)
    z : int, optional
        Coordination number (default: 1)
    s : float, optional
        Spin magnitude (default: 1.0)
    kB : float, optional
        Boltzmann constant (default: 1.0)
    show : bool, optional
        Whether to display the plot (default: True)
    
    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes
    
    Physical Interpretation
    -----------------------
    - <sigma^z> (solid): Order parameter, non-zero only for T < T_c
    - <sigma^x> (dashed): Transverse component, always non-zero for Gamma > 0
    - At T = 0: <sigma^z>^2 + <sigma^x>^2 = s^2 (spins lie on "Bloch sphere" of radius s)
    - At T -> infinity: Both -> 0 (complete disorder)
    
    Notes
    -----
    The sum rule <sigma^z>^2 + <sigma^x>^2 <= s^2 reflects that spins have fixed length s.
    At finite temperature, thermal fluctuations reduce the total magnitude.
    """
    # Check if ordered phase exists
    Tc = find_critical_temperature(gamma, J0, z, s, kB)
    
    if Tc == 0:
        print(f"No ordered phase for Gamma/Gamma_c = {gamma/(J0*z*s):.2f}")
        print("(System is in quantum disordered phase)")
        return None, None
    
    # ========================================================================
    # Temperature Range
    # ========================================================================
    
    # From near-zero to 3 x T_c
    T_vals = np.linspace(1e-5, 3 * Tc, 300)
    
    fig, ax = plt.subplots()
    
    # ========================================================================
    # Calculate Both Components
    # ========================================================================
    
    sigma_z_vals = []
    sigma_x_vals = []
    
    for T in T_vals:
        # Longitudinal component (order parameter)
        sigma_z = solve_self_consistency(gamma, J0, T, z, s, kB)
        
        # Transverse component (quantum fluctuations)
        sigma_x = solve_sx_component(gamma, J0, T, z, s, kB)
        
        sigma_z_vals.append(sigma_z)
        sigma_x_vals.append(sigma_x)
    
    # ========================================================================
    # Plot Both Components
    # ========================================================================
    
    # <sigma^z>: Solid line
    ax.plot(T_vals / Tc, sigma_z_vals, 'b-', linewidth=2.5, 
            label=r'$\langle \sigma^z \rangle$ (order)')
    
    # <sigma^x>: Dashed line
    ax.plot(T_vals / Tc, sigma_x_vals, 'r--', linewidth=2.5, 
            label=r'$\langle \sigma^x \rangle$ (fluctuations)')
    
    # Mark critical temperature
    ax.axvline(1.0, color='k', linestyle='--', alpha=0.6, linewidth=1.5, 
               label=r'$T_c$ (phase transition)')
    
    # ========================================================================
    # Labels and Formatting
    # ========================================================================
    
    ax.set_xlabel(r'$T / T_c$', fontsize=13, fontweight='bold')
    ax.set_ylabel(r'Pauli Expectation Values', fontsize=13, fontweight='bold')
    ax.set_title(f'Spin Components vs Temperature\n($\Gamma/\Gamma_c = {gamma/(J0*z*s):.2f}$)', 
                 fontsize=13, fontweight='bold')
    
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3, linestyle='--')
    
    ax.set_xlim(0, 3)
    ax.set_ylim(-0.05, s*1.05)
    
    ax.set_xticks([0, 1.0, 2.0, 3.0])
    ax.set_yticks([0, s*0.5, s])
    
    plt.tight_layout()
    
    if show:
        plt.show()
    
    return fig, ax


def plot_ground_state(J0=1.0, z=1, s=1.0, kB=1.0, show=True):
    """
    Plot the ground state order parameter <sigma^z> at T = 0 vs Gamma.
    
    This shows the QUANTUM phase transition at Gamma = Gamma_c.
    
    Parameters
    ----------
    J0 : float, optional
        Coupling constant (default: 1.0)
    z : int, optional
        Coordination number (default: 1)
    s : float, optional
        Spin magnitude (default: 1.0)
    kB : float, optional
        Boltzmann constant (default: 1.0)
    show : bool, optional
        Whether to display the plot (default: True)
    
    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes
    
    Physical Interpretation
    -----------------------
    - For Gamma < Gamma_c: <sigma^z> = s * sqrt(1 - (Gamma/Gamma_c)^2) (ordered phase)
    - For Gamma >= Gamma_c: <sigma^z> = 0 (quantum disordered phase)
    - The transition at Gamma = Gamma_c is driven by QUANTUM fluctuations
      (zero-point motion), not thermal fluctuations
    
    Key Difference from Thermal Transition
    ---------------------------------------
    - Thermal transition: Vary T at fixed Gamma < Gamma_c
    - Quantum transition: Vary Gamma at T = 0
    - Both are second-order phase transitions with same critical exponent
    
    Effect of Spin Factor s
    -----------------------
    - Maximum <sigma^z> = s (at Gamma = 0)
    - Gamma_c = J0*z*s (quantum critical point scales with s)
    - Shape of curve is independent of s (when normalized)
    """
    fig, ax = plt.subplots()
    
    # ========================================================================
    # Calculate Ground State for Different Gamma
    # ========================================================================
    
    gamma_c = J0 * z * s
    
    # Gamma values from 0 to 1.5 x Gamma_c
    gamma_vals = np.linspace(0, 1.5 * gamma_c, 500)
    
    # Calculate <sigma^z> at T = 0 for each Gamma
    sigma_z_vals = []
    for gamma in gamma_vals:
        sigma_z = solve_self_consistency(gamma, J0, T=0, z=z, s=s, kB=kB)
        sigma_z_vals.append(sigma_z)
    
    # ========================================================================
    # Plot Ground State Order Parameter
    # ========================================================================
    
    ax.plot(gamma_vals / gamma_c, sigma_z_vals, 'b-', linewidth=2.5)
    
    # Fill the ordered region
    ax.fill_between(gamma_vals / gamma_c, 0, sigma_z_vals, 
                    alpha=0.3, color='blue', label='Ordered (<sigma^z> != 0)')
    
    # Mark quantum critical point
    ax.axvline(1.0, color='k', linestyle='--', alpha=0.6, linewidth=1.5, 
               label=r'$\Gamma_c$ (quantum critical point)')
    
    # ========================================================================
    # Labels and Formatting
    # ========================================================================
    
    ax.set_xlabel(r'$\Gamma / \Gamma_c$', fontsize=13, fontweight='bold')
    ax.set_ylabel(r'$\langle \sigma^z \rangle_{T=0}$', fontsize=13, fontweight='bold')
    ax.set_title('Ground State Order Parameter\nQuantum Phase Transition at T = 0', 
                 fontsize=13, fontweight='bold')
    
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3, linestyle='--')
    
    ax.set_xlim(0, 1.5)
    ax.set_ylim(-0.05, s*1.05)
    
    ax.set_xticks([0, 0.5, 1.0, 1.5])
    ax.set_yticks([0, s*0.5, s])
    
    plt.tight_layout()
    
    if show:
        plt.show()
    
    return fig, ax


# ============================================================================
# Main: Generate all three plots
# ============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Order Parameter Plots")
    print("=" * 60)
    
    # Physical parameters
    J0 = 1.0  # Coupling constant
    z = 1     # Coordination number
    kB = 1.0  # Boltzmann constant
    
    print("\n" + "=" * 60)
    print("Case 1: Pauli Matrix Convention (s = 1.0)")
    print("=" * 60)
    
    s = 1.0
    
    # Calculate critical parameters
    gamma_c = J0 * z * s
    
    print(f"\nPhysical Parameters:")
    print(f"  J0 = {J0}")
    print(f"  z  = {z}")
    print(f"  s  = {s}")
    print(f"  Gamma_c = J0*z*s = {gamma_c:.3f}")
    
    print("\nGenerating plots...")
    
    # ========================================================================
    # Plot 1: Order Parameter vs Temperature
    # ========================================================================
    
    print("\n" + "-" * 60)
    print("Plot 1: Order Parameter vs Temperature")
    print("-" * 60)
    print("Shows: How <sigma^z> decreases with T for different Gamma values")
    print("Key feature: Each curve ends at its T_c (marked with circle)")
    print("Note: Maximum <sigma^z> = s = 1.0")
    print("(Close the plot window to continue)")
    
    plot_order_parameter(J0, z, s, kB)
    
    # ========================================================================
    # Plot 2: Spin Components vs Temperature
    # ========================================================================
    
    print("\n" + "-" * 60)
    print("Plot 2: Spin Components (<sigma^z> and <sigma^x>) vs Temperature")
    print("-" * 60)
    print("Shows: Competition between order and quantum fluctuations")
    print("Key feature: <sigma^z> drops to 0 at T_c, while <sigma^x> persists")
    print("Note: At T=0, <sigma^z>^2 + <sigma^x>^2 = s^2 = 1")
    print("(Close the plot window to continue)")
    
    plot_spin_components(0.5 * gamma_c, J0, z, s, kB)
    
    # ========================================================================
    # Plot 3: Ground State vs Transverse Field
    # ========================================================================
    
    print("\n" + "-" * 60)
    print("Plot 3: Ground State Order Parameter vs Gamma")
    print("-" * 60)
    print("Shows: Quantum phase transition at T = 0")
    print("Key feature: <sigma^z> drops to 0 at Gamma = Gamma_c (quantum critical point)")
    print("Note: Maximum <sigma^z> = s = 1.0 at Gamma = 0")
    print("(Close the plot window to continue)")
    
    plot_ground_state(J0, z, s, kB)
    
    # ========================================================================
    # Case 2: True Spin-1/2
    # ========================================================================
    
    print("\n" + "=" * 60)
    print("Case 2: True Spin-1/2 (s = 0.5)")
    print("=" * 60)
    
    s = 0.5
    gamma_c = J0 * z * s
    
    print(f"\nPhysical Parameters:")
    print(f"  J0 = {J0}")
    print(f"  z  = {z}")
    print(f"  s  = {s}")
    print(f"  Gamma_c = J0*z*s = {gamma_c:.3f}")
    
    print("\nNote: Both Gamma_c and maximum <sigma^z> are reduced by factor of 2")
    
    print("\nGenerating ground state plot...")
    print("(Close the plot window to continue)")
    
    plot_ground_state(J0, z, s, kB)
    
    # ========================================================================
    # Summary
    # ========================================================================
    
    print("\n" + "=" * 60)
    print("All plots complete!")
    print("=" * 60)
    
    print("\nKey Physics Summary:")
    print("  1. Order parameter <sigma^z> measures ferromagnetic order")
    print("  2. Thermal fluctuations destroy order (<sigma^z> -> 0 as T -> T_c)")
    print("  3. Quantum fluctuations also destroy order (<sigma^z> -> 0 as Gamma -> Gamma_c)")
    print("  4. Two types of phase transitions:")
    print("     - Thermal: Vary T at fixed Gamma < Gamma_c")
    print("     - Quantum: Vary Gamma at T = 0")
    print("  5. Transverse component <sigma^x> represents quantum fluctuations")
    print("\nEffect of Spin Factor s:")
    print("  - Maximum <sigma^z> = s")
    print("  - Gamma_c = J0*z*s (quantum critical point)")
    print("  - T_c(0) = J0*z*s/k_B (classical critical temperature)")
    print("  - Shape of curves independent of s (when properly normalized)")
