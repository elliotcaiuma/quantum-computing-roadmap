"""
Level 31: Deutsch-Jozsa Algorithm

Physical meaning:
Determines whether a function is constant or balanced in ONE query.
Classical computer needs 2^{n-1} + 1 queries in worst case.
Quantum computer needs only 1 query - exponential speedup.

Key technique: Phase kickback + interference
"""

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import execute

def deutsch_jozsa(oracle, n):
    """Implement Deutsch-Jozsa algorithm.
    
    Args:
        oracle: QuantumCircuit - the oracle O_f
        n: int - number of input qubits
    
    Returns:
        str: 'constant' or 'balanced'
    """
    # Step 1: Initialize n input qubits + 1 output qubit
    qc = QuantumCircuit(n + 1, n)
    
    # Step 2: Hadamard on all qubits
    qc.h(range(n))
    qc.x(n)  # Prepare |1> for output qubit
    qc.h(n)  # Create |->
    
    # Step 3: Apply oracle
    qc.compose(oracle, inplace=True)
    
    # Step 4: Hadamard on input register only
    qc.h(range(n))
    
    # Step 5: Measure input register
    qc.measure(range(n), range(n))
    
    # Execute
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1).result()
    counts = result.get_counts()
    outcome = list(counts.keys())[0]
    
    # Interpret: all zeros = constant, otherwise = balanced
    if outcome == '0' * n:
        return 'constant'
    else:
        return 'balanced'

# Test with constant oracle
if __name__ == "__main__":
    print("=== Deutsch-Jozsa Algorithm ===\n")
    
    # Test 1: Constant function f(x) = 0
    n = 3
    oracle_const = QuantumCircuit(n + 1)  # No operation
    result = deutsch_jozsa(oracle_const, n)
    print(f"Test 1 - Constant function (f(x) = 0):")
    print(f"Result: {result}")
    print(f"Expected: constant\n")
    
    # Test 2: Constant function f(x) = 1
    oracle_const1 = QuantumCircuit(n + 1)
    oracle_const1.x(n)  # Flip target
    result = deutsch_jozsa(oracle_const1, n)
    print(f"Test 2 - Constant function (f(x) = 1):")
    print(f"Result: {result}")
    print(f"Expected: constant\n")
    
    # Test 3: Balanced function (parity)
    oracle_bal = QuantumCircuit(n + 1)
    for i in range(n):
        oracle_bal.cx(i, n)
    result = deutsch_jozsa(oracle_bal, n)
    print(f"Test 3 - Balanced function (parity):")
    print(f"Result: {result}")
    print(f"Expected: balanced\n")
    
    # Test 4: Balanced function (first qubit)
    oracle_bal2 = QuantumCircuit(n + 1)
    oracle_bal2.cx(0, n)
    result = deutsch_jozsa(oracle_bal2, n)
    print(f"Test 4 - Balanced function (first bit):")
    print(f"Result: {result}")
    print(f"Expected: balanced")
