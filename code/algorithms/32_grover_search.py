"""
Level 32: Grover's Search Algorithm

Physical meaning:
Searches an unstructured database of N items with O(√N) queries.
Classical computer needs O(N) queries on average.
Quantum computer achieves quadratic speedup.

Key technique: Amplitude amplification (oracle + diffusion)
"""

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import execute
import numpy as np

def grover_oracle(winner):
    """Create oracle that marks the winner state.
    
    Args:
        winner: str - binary string of winner (e.g., '11')
    
    Returns:
        QuantumCircuit - oracle that flips phase of |winner>
    """
    n = len(winner)
    qc = QuantumCircuit(n)
    
    # Apply X gates to flip |1> qubits to |0>
    for i, bit in enumerate(winner):
        if bit == '0':
            qc.x(i)
    
    # Multi-controlled Z (marks |00...0>)
    qc.h(n-1)
    qc.mcx(list(range(n-1)), n-1)
    qc.h(n-1)
    
    # Undo X gates
    for i, bit in enumerate(winner):
        if bit == '0':
            qc.x(i)
    
    return qc

def grover_diffusion(n):
    """Create diffusion operator (inversion about mean).
    
    Args:
        n: int - number of qubits
    
    Returns:
        QuantumCircuit - diffusion operator D = 2|s><s| - I
    """
    qc = QuantumCircuit(n)
    
    # Hadamard
    qc.h(range(n))
    
    # X gates
    qc.x(range(n))
    
    # Multi-controlled Z
    qc.h(n-1)
    qc.mcx(list(range(n-1)), n-1)
    qc.h(n-1)
    
    # X gates
    qc.x(range(n))
    
    # Hadamard
    qc.h(range(n))
    
    return qc

def grover_search(winner, n):
    """Run Grover's algorithm to find the winner.
    
    Args:
        winner: str - binary string of winner
        n: int - number of qubits
    
    Returns:
        dict: measurement counts
    """
    # Calculate optimal iterations
    N = 2**n
    k_opt = int(np.pi / 4 * np.sqrt(N))
    
    # Initialize
    qc = QuantumCircuit(n, n)
    qc.h(range(n))  # Create uniform superposition
    
    # Apply Grover iterations
    for _ in range(k_opt):
        qc.compose(grover_oracle(winner), inplace=True)
        qc.compose(grover_diffusion(n), inplace=True)
    
    # Measure
    qc.measure(range(n), range(n))
    
    # Execute
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1024).result()
    counts = result.get_counts()
    
    return counts

# Test Grover's algorithm
if __name__ == "__main__":
    print("=== Grover's Search Algorithm ===\n")
    
    # Test 1: 2 qubits, winner = |11>
    n = 2
    winner = '11'
    counts = grover_search(winner, n)
    print(f"Test 1 - {n} qubits, winner = |{winner}>:")
    print(f"Results: {counts}")
    print(f"Expected: High probability of measuring |{winner}>\n")
    
    # Test 2: 3 qubits, winner = |101>
    n = 3
    winner = '101'
    counts = grover_search(winner, n)
    print(f"Test 2 - {n} qubits, winner = |{winner}>:")
    print(f"Results: {counts}")
    print(f"Expected: High probability of measuring |{winner}>\n")
    
    # Test 3: 2 qubits, winner = |00>
    n = 2
    winner = '00'
    counts = grover_search(winner, n)
    print(f"Test 3 - {n} qubits, winner = |{winner}>:")
    print(f"Results: {counts}")
    print(f"Expected: High probability of measuring |{winner}>")
