"""
Level 34: Quantum Phase Estimation

Physical meaning:
Estimates the eigenvalue phase φ of a unitary operator U.
Given: U|ψ> = e^{2πiφ}|ψ>
Find: φ to n bits of precision

Key subroutine in Shor's algorithm and quantum simulation.
"""

from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit.library import QFT
import numpy as np

def phase_estimation(unitary, eigenstate_prep, n_count):
    """Estimate eigenvalue phase of unitary operator.
    
    Args:
        unitary: QuantumCircuit - the unitary U
        eigenstate_prep: QuantumCircuit - prepares |ψ> where U|ψ> = e^{2πiφ}|ψ>
        n_count: int - number of counting qubits (precision)
    
    Returns:
        float: estimated phase φ
    """
    n_target = unitary.num_qubits
    qc = QuantumCircuit(n_count + n_target, n_count)
    
    # Step 1: Prepare eigenstate on target qubits
    qc.compose(eigenstate_prep, qubits=range(n_count, n_count + n_target), inplace=True)
    
    # Step 2: Hadamard on counting qubits
    qc.h(range(n_count))
    
    # Step 3: Controlled-U^{2^j}
    for j in range(n_count):
        # Apply U^{2^j} controlled by qubit j
        power = 2 ** j
        for _ in range(power):
            qc.compose(unitary.control(), qubits=[j] + list(range(n_count, n_count + n_target)), inplace=True)
    
    # Step 4: Inverse QFT on counting qubits
    qc.append(QFT(n_count, inverse=True).to_gate(), range(n_count))
    
    # Step 5: Measure counting qubits
    qc.measure(range(n_count), range(n_count))
    
    # Execute
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1024).result()
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
    eigenstate = QuantumCircuit(1)
    eigenstate.x(0)  # |1> is eigenstate of T
    unitary = QuantumCircuit(1)
    unitary.t(0)
    
    phi_est = phase_estimation(unitary, eigenstate, 3)
    print(f"Estimated phase: {phi_est:.4f}")
    print(f"Expected phase: 0.1250")
    print(f"Error: {abs(phi_est - 0.125):.4f}\n")
    
    # Test 2: S gate (φ = 1/4 = 0.25)
    print("Test 2 - S gate (expected φ = 0.25):")
    eigenstate = QuantumCircuit(1)
    eigenstate.x(0)  # |1> is eigenstate of S
    unitary = QuantumCircuit(1)
    unitary.s(0)
    
    phi_est = phase_estimation(unitary, eigenstate, 3)
    print(f"Estimated phase: {phi_est:.4f}")
    print(f"Expected phase: 0.2500")
    print(f"Error: {abs(phi_est - 0.25):.4f}\n")
    
    # Test 3: Z gate (φ = 1/2 = 0.5)
    print("Test 3 - Z gate (expected φ = 0.5):")
    eigenstate = QuantumCircuit(1)
    eigenstate.x(0)  # |1> is eigenstate of Z
    unitary = QuantumCircuit(1)
    unitary.z(0)
    
    phi_est = phase_estimation(unitary, eigenstate, 3)
    print(f"Estimated phase: {phi_est:.4f}")
    print(f"Expected phase: 0.5000")
    print(f"Error: {abs(phi_est - 0.5):.4f}")
