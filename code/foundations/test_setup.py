#!/usr/bin/env python3
"""
Test script to verify quantum computing setup.
Run this after installing requirements.txt.
"""

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector

print("="*60)
print("Testing quantum computing setup...")
print("="*60)

# 1. NumPy test
arr = np.array([1, 2, 3])
print(f"✓ NumPy: {arr}")

# 2. Matplotlib test
plt.figure()
plt.plot([1, 2, 3], [1, 4, 9])
plt.close()
print("✓ Matplotlib: plotting works")

# 3. Qiskit test
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
print("✓ Qiskit: circuit creation works")

# 4. Simulator test
simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(qc, shots=100).result()
counts = result.get_counts()
print(f"✓ Qiskit-Aer: simulation works - {counts}")

# 5. Visualization test
plot_bloch_multivector(qc)
plt.close()
print("✓ Visualization: Bloch sphere works")

print("\n" + "="*60)
print("🎉 All tests passed! Setup complete!")
print("="*60)
