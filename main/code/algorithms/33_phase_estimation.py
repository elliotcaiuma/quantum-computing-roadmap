"""
Level 34: Quantum Phase Estimation

Physical meaning:
Estimates the eigenvalue phase φ of a unitary operator U.
Given: U|ψ> = e^{2πiφ}|ψ>
Find: φ to n bits of precision

Key subroutine in Shor's algorithm and quantum simulation.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def qft_manual(n, inverse=False):
    """Manual QFT implementation to avoid deprecated library.
    
    Args:
        n: int - number of qubits
        inverse: bool - if True, return inverse QFT
    """
    qc = QuantumCircuit(n)
    
    if inverse:
        # Reverse SWAPs first
        for i in range(n // 2):
            qc.swap(i, n - 1 - i)
        # Then reverse the rotations and Hadamards
        for j in range(n - 1, -1, -1):
            for k in range(n - 1, j, -1):
                angle = -2 * np.pi / (2 ** (k - j + 1))
                qc.cp(angle, k, j)
            qc.h(j)
    else:
        for j in range(n):
            qc.h(j)
            for k in range(j + 1, n):
                angle = 2 * np.pi / (2 ** (k - j + 1))
                qc.cp(angle, k, j)
        for i in range(n // 2):
            qc.swap(i, n - 1 - i)
    
    return qc

def phase_estimation(gate_name, n_count):
    """Estimate eigenvalue phase for T, S, or Z gate.
    
    Args:
        gate_name: str - 'T', 'S', or 'Z'
        n_count: int - number of counting qubits (precision)
    
    Returns:
        float: estimated phase φ
    """
    # Create circuit: n_count counting qubits + 1 target qubit
    qc = QuantumCircuit(n_count + 1, n_count)
    
    # Step 1: Prepare |1> on target (eigenstate of T, S, Z)
    qc.x(n_count)
    
    # Step 2: Hadamard on counting qubits
    qc.h(range(n_count))
    
    # Step 3: Controlled-U^{2^j} using controlled gates directly
    for j in range(n_count):
        power = 2 ** j
        for _ in range(power):
            if gate_name == 'T':
                qc.cp(np.pi / 4, j, n_count)  # Controlled-T
            elif gate_name == 'S':
                qc.cp(np.pi / 2, j, n_count)  # Controlled-S
            elif gate_name == 'Z':
                qc.cp(np.pi, j, n_count)  # Controlled-Z
    
    # Step 4: Inverse QFT on counting qubits
    qc.compose(qft_manual(n_count, inverse=True), qubits=range(n_count), inplace=True)
    
    # Step 5: Measure counting qubits
    qc.measure(range(n_count), range(n_count))
    
    # Execute
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1024)
    result = job.result()
    counts = result.get_counts()
    
    # Get most likely outcome
    outcome = max(counts, key=counts.get)
    phase = int(outcome, 2) / (2 ** n_count)
    
    return phase

# Test phase estimation
if __name__ == "__main__":
    print("=== Quantum Phase Estimation ===\n")
    
    # Test 1: T gate (φ = 1/8 = 0.125)
    print("Test 1 - T gate (expected φ = 0.125):")
    phi_est = phase_estimation('T', 3)
    print(f"Estimated phase: {phi_est:.4f}")
    print(f"Expected phase: 0.1250")
    print(f"Error: {abs(phi_est - 0.125):.4f}\n")
    
    # Test 2: S gate (φ = 1/4 = 0.25)
    print("Test 2 - S gate (expected φ = 0.25):")
    phi_est = phase_estimation('S', 3)
    print(f"Estimated phase: {phi_est:.4f}")
    print(f"Expected phase: 0.2500")
    print(f"Error: {abs(phi_est - 0.25):.4f}\n")
    
    # Test 3: Z gate (φ = 1/2 = 0.5)
    print("Test 3 - Z gate (expected φ = 0.5):")
    phi_est = phase_estimation('Z', 3)
    print(f"Estimated phase: {phi_est:.4f}")
    print(f"Expected phase: 0.5000")
    print(f"Error: {abs(phi_est - 0.5):.4f}")
