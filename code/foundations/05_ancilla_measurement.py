"""
Ancilla-Based Measurement Implementation
Demonstrates Nielsen & Chuang Eq 2.122-2.125

Measurement as unitary evolution: U|psi>|0> = Sum M_m|psi>|m>
"""
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
import numpy as np

sim = AerSimulator()

print("=" * 60)
print("ANCIlla-BASED MEASUREMENT (Nielsen & Chuang 2.122)")
print("=" * 60)

# Create |psi>|0> where |psi> = 0.6|0> + 0.8|1>
# Qiskit ordering: |q1 q0>, so we want 0.6|00> + 0.8|01>
qc = QuantumCircuit(2, 1)

# Method: Start with |00>, apply rotation to qubit 0
alpha, beta = 0.6, 0.8
theta = 2 * np.arccos(alpha)  # cos(theta/2) = alpha

qc.ry(theta, 0)  # Rotate qubit 0 to alpha|0> + beta|1>

print("\n1. Initial state |psi>|0>:")
sv_initial = Statevector(qc)
print(f"   Statevector: {[f'{x:.2f}' for x in sv_initial.data]}")
print(f"   = 0.60|00> + 0.80|01> = (0.6|0> + 0.8|1>) tensor |0>")
print(f"   (qubit 0 is in superposition, qubit 1 is |0>)")

# Apply CNOT: control=qubit 0, target=qubit 1
# This entangles the system: |00> -> |00>, |01> -> |11>
qc.cx(0, 1)

print("\n2. After unitary U (CNOT with control=0, target=1):")
sv_entangled = Statevector(qc)
print(f"   Statevector: {[f'{x:.2f}' for x in sv_entangled.data]}")
print(f"   = 0.60|00> + 0.80|11>  [ENTANGLED!]")
print(f"   = M0|psi>|0> + M1|psi>|1>")
print(f"   where M0=|0><0|, M1=|1><1| (projective measurement)")

# Measure ancilla (qubit 1)
qc.measure(1, 0)

print("\n3. Measurement statistics (1000 shots):")
job = sim.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()
print(f"   Counts: {counts}")

# Calculate expected probabilities
p0 = abs(0.6)**2  # 0.36
p1 = abs(0.8)**2  # 0.64

print(f"\n4. Comparison with theory (Born rule):")
print(f"   P(0) = |0.6|^2 = {p0:.4f} (expected ~{int(p0*1000)} counts)")
print(f"   P(1) = |0.8|^2 = {p1:.4f} (expected ~{int(p1*1000)} counts)")

# Show post-measurement states
print(f"\n5. Post-measurement states (collapse):")
print(f"   If outcome '0': system collapses to |0>")
print(f"      (normalized M0|psi> = |0><0|psi>/sqrt(p0) = 0.6|0>/0.6 = |0>)")
print(f"   If outcome '1': system collapses to |1>")
print(f"      (normalized M1|psi> = |1><1|psi>/sqrt(p1) = 0.8|1>/0.8 = |1>)")

print("\n" + "=" * 60)
print("POST-MEASUREMENT STATE DEMONSTRATION")
print("=" * 60)

# Demonstrate state collapse by measuring multiple times
print("\nRunning 10 individual measurements to show collapse:")
print("-" * 60)

for i in range(10):
    # Reset and prepare same initial state
    qc_test = QuantumCircuit(2, 1)
    qc_test.ry(theta, 0)
    qc_test.cx(0, 1)
    qc_test.measure(1, 0)
    
    result = sim.run(qc_test, shots=1).result()
    counts = result.get_counts()
    outcome = list(counts.keys())[0]
    
    # Post-measurement state
    if outcome == '0':
        post_state = "|0> (system collapsed to |0>)"
    else:
        post_state = "|1> (system collapsed to |1>)"
    
    print(f"  Shot {i+1:2d}: outcome='{outcome}' -> {post_state}")

print("\n" + "=" * 60)
print("KEY INSIGHT: Measurement = Unitary + Ancilla Readout")
print("This proves N&C Eq 2.122-2.125: any measurement can be")
print("implemented as unitary evolution on a larger system!")
print("=" * 60)

print("\nFORMULA SUMMARY:")
print("  Probability:      p(m) = <psi|M_m^dag M_m|psi>")
print("  Post-measurement: |psi'> = M_m|psi> / sqrt(p(m))")
print("  For projective Z: M_0=|0><0|, M_1=|1><1|")

