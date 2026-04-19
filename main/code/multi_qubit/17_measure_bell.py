#!/usr/bin/env python3
"""
Level 17: Measure Bell State - Task Specific

Measures |Φ⁺⟩ Bell state and shows perfect correlations.
"""

from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector


# Create Bell state |Φ⁺⟩
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)

# Measure
qc.measure_all()

# Run simulation
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1000).result()
counts = result.get_counts()

print("Measuring |Φ⁺⟩ (1000 shots):")
print("="*50)

for outcome, count in sorted(counts.items()):
    percentage = count / 1000 * 100
    print(f"   |{outcome}⟩: {count} ({percentage:.1f}%)")

print("="*50)

# Perfect correlation: only |00⟩ and |11⟩!
# When you measure one qubit, the other is instantly determined
# This is ENTANGLEMENT!
