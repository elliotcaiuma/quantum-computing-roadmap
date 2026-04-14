"""
QFT Code Module 2: Manual QFT Circuit Construction

What This Code Does:
- Builds QFT circuit from scratch using H and controlled phase gates
- No reliance on Qiskit's built-in synthesis
- Shows the theoretical decomposition explicitly

Corresponds to: Section 6 of qft.pdf
"""

from qiskit import QuantumCircuit
import numpy as np


def create_qft_circuit_manual(n):
    """
    Build QFT circuit manually using H and controlled phase gates.
    
    Pattern:
    - For each qubit m (0 to n-1):
      - Apply H to qubit m
      - Apply controlled phase R_k from qubits m+1 to n-1
    - Swap qubits to reverse order
    
    Args:
        n (int): Number of qubits
        
    Returns:
        QuantumCircuit: QFT circuit
    """
    qc = QuantumCircuit(n)
    
    for m in range(n):
        # Apply Hadamard to qubit m
        qc.h(m)
        
        # Apply controlled phase gates
        for k in range(2, n - m + 1):
            control = m + k - 1
            if control < n:
                theta = 2 * np.pi / (2**k)
                qc.cp(theta, control, m)
    
    # Swap qubits to reverse order
    for i in range(n // 2):
        qc.swap(i, n - 1 - i)
    
    return qc


def count_gates(n):
    """
    Count gates in QFT circuit.
    
    Args:
        n (int): Number of qubits
        
    Returns:
        dict: Gate counts
    """
    qc = create_qft_circuit_manual(n)
    
    gate_counts = {}
    for instruction in qc.data:
        gate_name = instruction.operation.name
        gate_counts[gate_name] = gate_counts.get(gate_name, 0) + 1
    
    return gate_counts, qc.size(), qc.depth()


if __name__ == "__main__":
    print("=" * 60)
    print("QFT CODE MODULE 2: Manual Circuit Construction")
    print("=" * 60)
    
    # Test for 3 qubits
    n = 3
    qc = create_qft_circuit_manual(n)
    
    print(f"\nQFT Circuit for {n} qubits:")
    print(qc.draw())
    
    gate_counts, total, depth = count_gates(n)
    print(f"\nGate counts:")
    for gate, count in gate_counts.items():
        print(f"  {gate}: {count}")
    print(f"Total gates: {total}")
    print(f"Depth: {depth}")
    
    # Test scaling
    print("\n" + "=" * 60)
    print("Gate count scaling:")
    print(f"{'n':<5} {'Total':<8} {'Depth':<8} {'O(n²)':<8}")
    print("-" * 35)
    for n_test in range(2, 6):
        _, total, depth = count_gates(n_test)
        print(f"{n_test:<5} {total:<8} {depth:<8} {n_test**2:<8}")
    
    print("\n" + "=" * 60)
    print("Code Module 2 complete!")
    print("=" * 60)
