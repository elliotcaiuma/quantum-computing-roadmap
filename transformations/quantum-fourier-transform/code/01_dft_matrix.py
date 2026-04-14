"""
QFT Code Module 1: DFT and QFT Matrix Construction

What This Code Does:
- Constructs the classical DFT matrix
- Builds the QFT circuit and extracts its matrix
- Verifies that QFT matches DFT
- Checks unitarity

Corresponds to: Section 5 of qft.pdf
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator


def create_dft_matrix(n):
    """
    Create the N x N Discrete Fourier Transform matrix.
    N = 2^n for n qubits.
    
    DFT[k, j] = exp(2*pi*i*j*k / N) / sqrt(N)
    
    Args:
        n (int): Number of qubits
        
    Returns:
        np.ndarray: N x N DFT matrix (complex)
    """
    N = 2**n
    omega = np.exp(2j * np.pi / N)
    DFT = np.zeros((N, N), dtype=complex)
    
    for j in range(N):
        for k in range(N):
            DFT[k, j] = omega**(j * k) / np.sqrt(N)
    
    return DFT


def create_qft_circuit(n, do_swaps=True):
    """
    Build the Quantum Fourier Transform circuit for n qubits.
    Uses Qiskit's QFT synthesis.
    
    Args:
        n (int): Number of qubits
        do_swaps (bool): Include swap gates to reverse qubit order
        
    Returns:
        QuantumCircuit: QFT circuit
    """
    from qiskit.synthesis.qft import synth_qft_full
    
    qft_gate = synth_qft_full(num_qubits=n, do_swaps=do_swaps)
    qc = QuantumCircuit(n)
    qc.append(qft_gate, range(n))
    
    return qc


def create_qft_matrix(n):
    """
    Get the QFT matrix by simulating the circuit.
    
    Args:
        n (int): Number of qubits
        
    Returns:
        np.ndarray: N x N QFT matrix (complex)
    """
    qc = create_qft_circuit(n)
    U = Operator(qc).data
    return U


def verify_qft(n):
    """
    Verify that QFT matches DFT and is unitary.
    
    Args:
        n (int): Number of qubits
        
    Returns:
        tuple: (U_qft, U_dft, unitarity_error)
    """
    print(f"\n=== QFT Verification for {n} qubits ===")
    
    # Get QFT matrix from circuit
    U_qft = create_qft_matrix(n)
    
    # Get DFT matrix
    U_dft = create_dft_matrix(n)
    
    # Check unitarity: U^dag @ U = I
    N = 2**n
    I = np.eye(N, dtype=complex)
    unitarity_error = np.max(np.abs(U_qft.conj().T @ U_qft - I))
    print(f"Unitarity error: {unitarity_error:.2e}")
    
    # Check match with DFT
    match = np.allclose(U_qft, U_dft)
    print(f"QFT matches DFT: {match}")
    
    return U_qft, U_dft, unitarity_error


if __name__ == "__main__":
    print("=" * 60)
    print("QFT CODE MODULE 1: DFT Matrix Construction")
    print("=" * 60)
    
    # Test for 2 qubits
    n = 2
    U_qft, U_dft, error = verify_qft(n)
    
    print("\nDFT matrix (2 qubits):")
    print(np.round(U_dft, 3))
    
    print("\nQFT matrix (2 qubits):")
    print(np.round(U_qft, 3))
    
    # Test for 3 qubits
    n = 3
    U_qft, U_dft, error = verify_qft(n)
    print(f"\n3-qubit QFT verified (unitarity error: {error:.2e})")
    
    print("\n" + "=" * 60)
    print("Code Module 1 complete!")
    print("=" * 60)
