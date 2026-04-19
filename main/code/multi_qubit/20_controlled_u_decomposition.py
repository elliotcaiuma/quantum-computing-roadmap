#!/usr/bin/env python3
"""
Level 20: Controlled-U Decomposition - A-X-B-X-C Method

Builds any controlled-U gate using CNOT + single-qubit rotations.
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
import numpy as np


def zyz_decomposition(U):
    """
    Extract angles gamma, beta, delta from unitary matrix U.
    
    U = R_z(beta) R_y(gamma) R_z(delta)
    """
    a, b = U[0, 0], U[0, 1]
    
    # gamma from |a| = |cos(gamma/2)|
    gamma = 2 * np.arccos(np.abs(a))
    
    # beta, delta from phases
    if np.abs(gamma) < 1e-10:
        # Diagonal case (Z, S, T)
        beta = 0
        delta = np.angle(U[1, 1]) - np.angle(a)
    elif np.abs(gamma - np.pi) < 1e-10:
        # Off-diagonal case (X, Y)
        beta = np.angle(U[1, 0])
        delta = np.angle(b)
    else:
        # General case (H)
        beta = np.angle(a) - np.angle(b)
        delta = np.angle(a) + np.angle(b)
    
    return gamma, beta, delta


def build_controlled_u(U_target):
    """
    Build controlled-U using A-X-B-X-C decomposition.
    
    Returns: 2-qubit circuit (qubit 0 = control, qubit 1 = target)
    """
    # Extract angles
    gamma, beta, delta = zyz_decomposition(U_target)
    
    # Build A, B, C circuits
    A = QuantumCircuit(1)
    A.rz(beta, 0)
    A.ry(gamma / 2, 0)
    
    B = QuantumCircuit(1)
    B.ry(-gamma / 2, 0)
    B.rz(-(beta + delta) / 2, 0)
    
    C = QuantumCircuit(1)
    C.rz((delta - beta) / 2, 0)
    
    # Build controlled-U circuit
    qc = QuantumCircuit(2)
    qc.compose(A, [1], inplace=True)  # A on target
    qc.cx(0, 1)                        # CNOT
    qc.compose(B, [1], inplace=True)  # B on target
    qc.cx(0, 1)                        # CNOT
    qc.compose(C, [1], inplace=True)  # C on target
    
    return qc


# Example 1: Controlled-Hadamard
print("=" * 60)
print("CONTROLLED-HADAMARD")
print("=" * 60)

H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
print("\nTarget Hadamard matrix:")
print(H)

gamma, beta, delta = zyz_decomposition(H)
print(f"\nExtracted angles:")
print(f"  gamma = {gamma:.4f} rad ({gamma/np.pi:.2f}π)")
print(f"  beta  = {beta:.4f} rad ({beta/np.pi:.2f}π)")
print(f"  delta = {delta:.4f} rad ({delta/np.pi:.2f}π)")

qc_ch = build_controlled_u(H)
print("\nControlled-Hadamard circuit:")
print(qc_ch.draw())

# Verify
op = Operator(qc_ch)
U_built = op.data
print("\nBuilt unitary (4x4 matrix):")
print(np.round(U_built, 3))

# Example 2: Controlled-Z rotation
print("\n" + "=" * 60)
print("CONTROLLED-Z ROTATION (R_z(π/3))")
print("=" * 60)

theta = np.pi / 3
Rz = np.array([[1, 0], [0, np.exp(1j * theta)]])
print(f"\nTarget R_z({theta:.4f}):")
print(Rz)

qc_cz = build_controlled_u(Rz)
print("\nControlled-R_z circuit:")
print(qc_cz.draw())
