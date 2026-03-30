"""
Level 1b: Phase Diagram Plotter
================================

This module visualizes the phase boundary between ordered and disordered
phases in the (T, Γ) plane, including the spin factor s.

Physical Background
-------------------
The transverse Ising model with spin factor s has two phases:

1. Ordered Phase (Ferromagnetic):
   - ⟨σᶻ⟩ ≠ 0 (spontaneous magnetization along z)
   - Exists for T < T_c(Γ) and Γ < Γ_c

2. Disordered Phase (Paramagnetic):
   - ⟨σᶻ⟩ = 0 (no net magnetization)
   - Exists for T > T_c(Γ) or Γ > Γ_c

The phase boundary is given by:
    T_c(Γ) = (Γs) / [k_B arctanh(Γ/(J₀zs))]

Spin Factor s
-------------
The spin factor affects the critical parameters:
- Quantum critical point: Γ_c = J₀zs
- Classical critical temperature: T_c(0) = J₀zs/k_B
- Maximum magnetization: ⟨σᶻ⟩_max = s

Common values:
- s = 1.0: Pauli matrix convention (eigenvalues ±1)
- s = 0.5: True spin-1/2 systems (eigenvalues ±1/2)

Key Features
------------
- Classical limit (Γ → 0): T_c = J₀zs/k_B
- Quantum critical point (Γ = Γ_c): T_c = 0
- The transition at T = 0, Γ = Γ_c is a QUANTUM phase transition
  (driven by quantum fluctuations, not thermal fluctuations)

Usage
-----
Run this script to display the phase diagram:
    python 02_phase_diagram.py

Reference
---------
Based on: 1_ising_mean_field.py - plot_phase_diagram()
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Import core functions from module 01
from ising_01_mean_field_core import find_critical_temperature

# ============================================================================
# Plot Configuration
# ============================================================================

# Set matplotlib parameters for consistent appearance
rcParams['font.size'] = 12
rcParams['figure.figsize'] = (8, 6)
rcParams['axes.linewidth'] = 1.2
rcParams['grid.linewidth'] = 0.8


def plot_phase_diagram(J0=1.0, z=1, s=1.0, kB=1.0, show=True):
    """
    Plot the phase diagram in the (T, Γ) plane.
    
    This function calculates and displays the phase boundary between
    the ordered (ferromagnetic) and disordered (paramagnetic) phases.
    
    Parameters
    ----------
    J0 : float, optional
        Ferromagnetic coupling constant (default: 1.0)
    z : int, optional
        Coordination number (default: 1)
    s : float, optional
        Spin magnitude (default: 1.0)
        - s = 1.0: Pauli matrix convention
        - s = 0.5: True spin-1/2
    kB : float, optional
        Boltzmann constant (default: 1.0)
    show : bool, optional
        Whether to display the plot (default: True)
    
    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure object
    ax : matplotlib.axes.Axes
        The axes object
    
    Plot Features
    -------------
    - Blue curve: Phase boundary T_c(Γ)
    - Blue shaded region: Ordered phase (⟨σᶻ⟩ ≠ 0)
    - White region: Disordered phase (⟨σᶻ⟩ = 0)
    - Axes normalized by T_c(0) and Γ_c
    
    Interpretation
    --------------
    - For any point (T, Γ) below the curve: system is ordered
    - For any point (T, Γ) above the curve: system is disordered
    - The curve ends at (0, 1): the quantum critical point
    
    Effect of Spin Factor s
    -----------------------
    - s affects Γ_c = J₀zs (quantum critical point)
    - s affects T_c(0) = J₀zs/k_B (classical critical temperature)
    - But the SHAPE of the phase boundary is independent of s
      (when axes are properly normalized)
    """
    # Create figure and axes
    fig, ax = plt.subplots()
    
    # ========================================================================
    # Calculate Phase Boundary
    # ========================================================================
    
    # Quantum critical point (depends on s!)
    gamma_c = J0 * z * s
    
    # Generate Γ values from 0 to 1.5 × Γ_c
    gamma_vals = np.linspace(0, 1.5 * gamma_c, 500)
    
    # Calculate T_c for each Γ value
    Tc_vals = np.array([
        find_critical_temperature(g, J0, z, s, kB) 
        for g in gamma_vals
    ])
    
    # ========================================================================
    # Normalize Axes
    # ========================================================================
    
    # Reference temperature: T_c at Γ = 0 (classical limit)
    Tc_0 = find_critical_temperature(0, J0, z, s, kB)
    
    # Normalized coordinates
    x_vals = Tc_vals / Tc_0  # T / T_c(0)
    y_vals = gamma_vals / gamma_c  # Γ / Γ_c
    
    # ========================================================================
    # Plot Phase Boundary
    # ========================================================================
    
    # Draw the phase boundary curve
    ax.plot(x_vals, y_vals, 'b-', linewidth=2.5, label='Phase boundary')
    
    # Fill the ordered region (below the curve)
    ax.fill_betweenx(y_vals, 0, x_vals, alpha=0.3, color='blue',
                     label='Ordered phase (⟨σᶻ⟩ ≠ 0)')
    
    # ========================================================================
    # Add Region Labels
    # ========================================================================
    
    # Label for ordered phase
    ax.text(0.5, 0.3, 'Ordered Phase\\n(⟨σᶻ⟩ ≠ 0)',
            fontsize=11, ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    
    # Label for disordered phase
    ax.text(0.8, 1.1, 'Disordered Phase\\n(⟨σᶻ⟩ = 0)',
            fontsize=11, ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    
    # ========================================================================
    # Labels and Title
    # ========================================================================
    
    ax.set_xlabel(r'$T / T_c(\\Gamma=0)$', fontsize=13, fontweight='bold')
    ax.set_ylabel(r'$\\Gamma / \\Gamma_c$', fontsize=13, fontweight='bold')
    ax.set_title('Mean-Field Phase Diagram\\nTransverse Ising Model', 
                 fontsize=13, fontweight='bold')
    
    # Legend
    ax.legend(loc='upper right', fontsize=10, framealpha=0.9)
    
    # Grid
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # ========================================================================
    # Set Axis Limits
    # ========================================================================
    
    ax.set_xlim(0, 1.2)
    ax.set_ylim(0, 1.5)
    
    # Add ticks at key points
    ax.set_xticks([0, 0.5, 1.0])
    ax.set_yticks([0, 0.5, 1.0, 1.5])
    
    plt.tight_layout()
    
    # ========================================================================
    # Display or Save
    # ========================================================================
    
    if show:
        plt.show()
    
    return fig, ax


def plot_phase_boundary_scaled(gamma_c, Tc_0, show=True):
    """
    Alternative plot: Phase boundary with explicit Γ_c and T_c values.
    
    This version shows the actual (not normalized) values.
    
    Parameters
    ----------
    gamma_c : float
        Quantum critical point Γ_c
    Tc_0 : float
        Classical critical temperature T_c(Γ=0)
    show : bool, optional
        Whether to display the plot (default: True)
    
    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes
    """
    fig, ax = plt.subplots()
    
    # Calculate phase boundary
    gamma_vals = np.linspace(0, 1.5 * gamma_c, 500)
    Tc_vals = np.array([
        find_critical_temperature(g, 1.0, 1, kB=gamma_c) 
        for g in gamma_vals
    ])
    
    # Plot
    ax.plot(gamma_vals / gamma_c, Tc_vals / Tc_0, 'b-', linewidth=2.5)
    ax.fill_between(gamma_vals / gamma_c, 0, Tc_vals / Tc_0, 
                    alpha=0.3, color='blue')
    
    # Labels
    ax.set_xlabel(r'$\\Gamma / \\Gamma_c$', fontsize=13, fontweight='bold')
    ax.set_ylabel(r'$T_c / T_c(0)$', fontsize=13, fontweight='bold')
    ax.set_title('Phase Boundary', fontsize=13, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(0, 1.5)
    ax.set_ylim(0, 1.2)
    
    plt.tight_layout()
    
    if show:
        plt.show()
    
    return fig, ax


# ============================================================================
# Main: Generate phase diagram
# ============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Phase Diagram Plotter")
    print("=" * 60)
    
    # Physical parameters
    J0 = 1.0  # Coupling constant
    z = 1     # Coordination number
    kB = 1.0  # Boltzmann constant
    
    print("\n" + "-" * 60)
    print("Case 1: Pauli Matrix Convention (s = 1.0)")
    print("-" * 60)
    
    s = 1.0
    
    # Calculate critical parameters
    gamma_c = J0 * z * s
    Tc_0 = find_critical_temperature(0, J0, z, s, kB)
    
    print(f"\nPhysical Parameters:")
    print(f"  J0 = {J0}")
    print(f"  z  = {z}")
    print(f"  s  = {s}")
    print(f"  Gamma_c = J0*z*s = {gamma_c:.3f}")
    print(f"  T_c(Gamma=0) = J0*z*s/k_B = {Tc_0:.3f}")
    
    print("\nPhase Diagram Features:")
    print("  - Ordered phase: T < T_c(Gamma) and Gamma < Gamma_c")
    print("  - Disordered phase: T > T_c(Gamma) or Gamma >= Gamma_c")
    print("  - Quantum critical point: (T=0, Gamma=Gamma_c)")
    
    print("\nGenerating phase diagram...")
    print("(Close the plot window to continue)")
    
    # Generate and display the plot
    fig, ax = plot_phase_diagram(J0, z, s, kB)
    
    print("\n" + "-" * 60)
    print("Case 2: True Spin-1/2 (s = 0.5)")
    print("-" * 60)
    
    s = 0.5
    
    # Calculate critical parameters
    gamma_c = J0 * z * s
    Tc_0 = find_critical_temperature(0, J0, z, s, kB)
    
    print(f"\nPhysical Parameters:")
    print(f"  J0 = {J0}")
    print(f"  z  = {z}")
    print(f"  s  = {s}")
    print(f"  Gamma_c = J0*z*s = {gamma_c:.3f}")
    print(f"  T_c(Gamma=0) = J0*z*s/k_B = {Tc_0:.3f}")
    
    print("\nNote: Both Gamma_c and T_c are reduced by factor of 2")
    print("      (compared to s = 1.0)")
    
    print("\nGenerating phase diagram...")
    print("(Close the plot window to continue)")
    
    # Generate and display the plot
    fig, ax = plot_phase_diagram(J0, z, s, kB)
    
    print("\n" + "=" * 60)
    print("Phase diagrams complete!")
    print("=" * 60)
    print("\nKey observations:")
    print("  1. T_c decreases as Gamma increases")
    print("  2. T_c -> 0 as Gamma -> Gamma_c (quantum critical point)")
    print("  3. At Gamma = 0, we recover the classical Ising model")
    print("  4. The SHAPE of the phase boundary is independent of s")
    print("     (when axes are normalized by Gamma_c and T_c(0))")
    print("  5. Spin factor s sets the energy scale:")
    print("     - s = 1: Gamma_c = J0*z, T_c(0) = J0*z/k_B")
    print("     - s = 0.5: Gamma_c = J0*z/2, T_c(0) = J0*z/(2k_B)")
