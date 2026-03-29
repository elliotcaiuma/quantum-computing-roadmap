"""
Level 33: Quantum Fourier Transform (QFT)

Physical meaning:
QFT is the quantum analog of discrete Fourier transform.
It transforms computational basis to Fourier basis.
Key subroutine in Shor's algorithm and phase estimation.

Complexity: O(n²) gates (exponential speedup over classical FFT)
"""

from qiskit import QuantumCircuit
import numpy as np

def qft(n):
    """Create QFT circuit on n qubits.
    
    Args:
        n: int - number of qubits
    
    Returns:
        QuantumCircuit - QFT circuit
    """
    qc = QuantumCircuit(n)
    
    for j in range(n):
        # Hadamard on qubit j
        qc.h(j)
        
        # Controlled phase rotations
        for k in range(j + 1, n):
            # Rotation angle: 2π / 2^(k-j+1)
            angle = 2 * np.pi / (2 ** (k - j + 1))
            qc.cp(angle, k, j)
    
    # Swap qubits to reverse order
    for i in range(n // 2):
        qc.swap(i, n - 1 - i)
    
    return qc

def qft_inverse(n):
    """Create inverse QFT circuit.
    
    Args:
        n: int - number of qubits
    
    Returns:
        QuantumCircuit - inverse QFT circuit
    """
    qc = qft(n)
    return qc.inverse()

# Test QFT
if __name__ == "__main__":
    print("=== Quantum Fourier Transform ===\n")
    
    # Test 1: 2-qubit QFT circuit
    n = 2
    qft_circuit = qft(n)
    print(f"Test 1 - QFT circuit for {n} qubits:")
    print(qft_circuit.draw())
    print()
    
    # Test 2: 3-qubit QFT circuit
    n = 3
    qft_circuit = qft(n)
    print(f"Test 2 - QFT circuit for {n} qubits:")
    print(qft_circuit.draw())
    print()
    
    # Test 3: Verify QFT + QFT† = I
    n = 2
    qc = QuantumCircuit(n)
    qc.compose(qft(n), inplace=True)
    qc.compose(qft_inverse(n), inplace=True)
    print(f"Test 3 - QFT followed by inverse QFT (should be identity):")
    print(qc.draw())
    print()
    
    # Test 4: Count gates
    for n in [2, 3, 4]:
        qc = qft(n)
        print(f"QFT({n} qubits) - Gates: {qc.size()}, Depth: {qc.depth()}")
