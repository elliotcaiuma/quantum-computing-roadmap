"""
Level 30: Oracle Functions for Quantum Algorithms

Physical meaning:
Oracles are black-box functions used in quantum algorithms.
They encode a function f(x) into a unitary transformation.

Oracle definition:
O_f |x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩

Phase kickback (when target is |->):
O_f |x⟩|-> = (-1)^{f(x)} |x⟩|->
"""

from qiskit import QuantumCircuit

def oracle_constant_0(n):
    """Oracle for f(x) = 0 (constant function).
    
    Args:
        n: int - number of input qubits
    
    Returns:
        QuantumCircuit - oracle that does nothing (f(x) = 0)
    """
    qc = QuantumCircuit(n + 1)
    # No operation - f(x) = 0 for all x
    return qc

def oracle_constant_1(n):
    """Oracle for f(x) = 1 (constant function).
    
    Args:
        n: int - number of input qubits
    
    Returns:
        QuantumCircuit - oracle that flips target (f(x) = 1)
    """
    qc = QuantumCircuit(n + 1)
    qc.X(n)  # Flip target qubit
    return qc

def oracle_balanced_parity(n):
    """Oracle for f(x) = parity of x (balanced function).
    
    Args:
        n: int - number of input qubits
    
    Returns:
        QuantumCircuit - oracle that computes parity
    """
    qc = QuantumCircuit(n + 1)
    for i in range(n):
        qc.cx(i, n)  # CNOT from each input to target
    return qc

def oracle_balanced_first_qubit(n):
    """Oracle for f(x) = first bit of x (balanced function).
    
    Args:
        n: int - number of input qubits
    
    Returns:
        QuantumCircuit - oracle that checks first qubit
    """
    qc = QuantumCircuit(n + 1)
    qc.cx(0, n)  # CNOT from first qubit to target
    return qc

# Test oracle
if __name__ == "__main__":
    n = 3
    oracle = oracle_balanced_parity(n)
    print("Oracle circuit for balanced function (parity):")
    print(oracle.draw())
    print()
    
    oracle_const = oracle_constant_0(n)
    print("Oracle circuit for constant function (f(x) = 0):")
    print(oracle_const.draw())
