# Quantum Computing Learning Roadmap

## Detailed Study Plan

This roadmap provides a week-by-week guide for mastering quantum computing based on Nielsen & Chuang's textbook with practical Qiskit implementations.

---

## Phase 1: Foundations (Weeks 1-3)

### Week 1: Quantum Mechanics Basics

**Topics:**
- Dirac notation (bras, kets, outer products)
- State vectors in Hilbert space
- Qubit representation: $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$
- Normalization condition: $|\alpha|^2 + |\beta|^2 = 1$

**Reading:**
- Nielsen & Chuang: Sections 1.1-1.3, 2.1-2.2

**Coding:**
```python
# code/foundations/create_state.py
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create custom state
psi = Statevector.from_label('0')
print(psi)
```

**Milestone:** Can represent any single-qubit state and calculate probabilities

---

### Week 2: Bloch Sphere & Visualization

**Topics:**
- Bloch sphere representation
- Bloch vector: $\vec{r} = (\langle X \rangle, \langle Y \rangle, \langle Z \rangle)$
- Pure states on surface, mixed states inside
- Euler angles for rotations

**Reading:**
- Nielsen & Chuang: Section 1.2, 2.4

**Coding:**
```python
# code/foundations/bloch_sphere.py
from qiskit.visualization import plot_bloch_multivector
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.h(0)  # Hadamard gate
plot_bloch_multivector(qc)
```

**Milestone:** Visualize any single-qubit state on Bloch sphere

---

### Week 3: Single-Qubit Gates & Measurement

**Topics:**
- Pauli gates: X, Y, Z
- Hadamard gate: H
- Phase gates: S, T
- Rotation gates: Rx, Ry, Rz
- Measurement postulates
- Born rule: $P(i) = |\langle i|\psi\rangle|^2$

**Reading:**
- Nielsen & Chuang: Sections 2.2.3, 4.2

**Coding:**
```python
# code/foundations/gates.py
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.x(0)  # X gate
qc.h(0)  # Hadamard
qc.measure_all()
```

**Milestone:** Implement all single-qubit gates and measure in any basis

---

## Phase 2: Multi-Qubit Systems (Weeks 4-6)

### Week 4: Tensor Products

**Topics:**
- Composite systems: $|\psi\rangle = |\psi_1\rangle \otimes |\psi_2\rangle$
- Tensor product notation
- Dimension: $2^n$ for n qubits
- Separable vs entangled states

**Reading:**
- Nielsen & Chuang: Section 2.3

**Coding:**
```python
# code/multi_qubit/tensor_products.py
import numpy as np

# Tensor product of two states
psi1 = np.array([1, 0])
psi2 = np.array([0, 1])
psi_combined = np.kron(psi1, psi2)
print(psi_combined)  # [0, 1, 0, 0]
```

**Milestone:** Compute tensor products for multi-qubit states

---

### Week 5: Entanglement & Bell States

**Topics:**
- Bell states (4 maximally entangled states)
- $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$
- Schmidt decomposition
- CHSH inequality

**Reading:**
- Nielsen & Chuang: Sections 2.3, 4.3

**Coding:**
```python
# code/multi_qubit/bell_states.py
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)  # Create Bell state
```

**Milestone:** Create all 4 Bell states and verify entanglement

---

### Week 6: Multi-Qubit Gates & Teleportation

**Topics:**
- CNOT gate (controlled-NOT)
- CZ, SWAP gates
- Quantum teleportation protocol
- Superdense coding

**Reading:**
- Nielsen & Chuang: Sections 4.3-4.4

**Coding:**
```python
# code/multi_qubit/teleportation.py
from qiskit import QuantumCircuit

# Teleportation circuit
qc = QuantumCircuit(3)
# Alice's qubit, Bell pair, Bob's qubit
```

**Milestone:** Implement quantum teleportation protocol

---

## Phase 3: Quantum Circuits (Weeks 7-9)

### Week 7: Circuit Construction

**Topics:**
- Quantum circuit notation
- Gate sequences
- Circuit diagrams
- Reversible computation

**Reading:**
- Nielsen & Chuang: Sections 4.1-4.2

**Coding:**
```python
# code/circuits/builder.py
from qiskit import QuantumCircuit

qc = QuantumCircuit(4, 4)
qc.h(range(4))
qc.cx(0, 1)
qc.cx(1, 2)
```

**Milestone:** Build complex multi-gate circuits

---

### Week 8: Controlled Operations

**Topics:**
- Controlled-U gates
- Decomposition: 2 CNOTs + 3 single-qubit
- Toffoli gate (controlled-controlled-NOT)
- Multi-controlled gates

**Reading:**
- Nielsen & Chuang: Sections 4.3

**Coding:**
```python
# code/circuits/controlled_u.py
from qiskit import QuantumCircuit

qc = QuantumCircuit(3)
qc.cu(theta, phi, lam, 0, 1, 2)  # Controlled-U
```

**Milestone:** Decompose controlled-unitary gates

---

### Week 9: Universality & Synthesis

**Topics:**
- Universal gate sets
- Two-level unitaries
- Approximating arbitrary unitaries
- Gate count optimization

**Reading:**
- Nielsen & Chuang: Sections 4.7-4.8

**Coding:**
```python
# code/circuits/synthesis.py
from qiskit.synthesis import synth_qubit_unitary
```

**Milestone:** Synthesize arbitrary single-qubit unitaries

---

## Phase 4: Quantum Algorithms (Weeks 10-15)

### Week 10-11: Quantum Fourier Transform

**Topics:**
- QFT definition
- Circuit implementation
- Complexity: O(n²) vs classical O(n2^n)
- Applications

**Reading:**
- Nielsen & Chuang: Section 5.1

**Coding:**
```python
# code/algorithms/qft.py
from qiskit.circuit.library import QFT

qft = QFT(num_qubits=4)
```

**Milestone:** Implement QFT for n qubits

---

### Week 12-13: Grover's Algorithm

**Topics:**
- Unstructured search
- Oracle construction
- Amplitude amplification
- O(√N) speedup

**Reading:**
- Nielsen & Chuang: Section 6.1

**Coding:**
```python
# code/algorithms/grover.py
from qiskit.circuit.library import GroverOperator
```

**Milestone:** Implement Grover's search for database

---

### Week 14-15: Shor's Algorithm

**Topics:**
- Integer factorization
- Period finding
- Modular exponentiation
- Continued fractions

**Reading:**
- Nielsen & Chuang: Section 6.2

**Coding:**
```python
# code/algorithms/shor.py
# Implement period finding for factoring 15
```

**Milestone:** Factor small integers (15, 21)

---

## Phase 5: Quantum Information (Weeks 16-21)

### Week 16-17: Density Matrices

**Topics:**
- Mixed states
- Density operator: $\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|$
- Partial trace
- Purification

**Reading:**
- Nielsen & Chuang: Sections 2.4, 8.2

**Coding:**
```python
# code/advanced/density_matrix.py
from qiskit.quantum_info import DensityMatrix
```

**Milestone:** Work with mixed states and partial trace

---

### Week 18-19: Quantum Noise

**Topics:**
- Quantum channels
- Kraus representation
- Noise models: depolarizing, dephasing, amplitude damping
- Master equation

**Reading:**
- Nielsen & Chuang: Sections 8.3-8.5

**Coding:**
```python
# code/advanced/noise.py
from qiskit_aer.noise import NoiseModel
```

**Milestone:** Simulate noise channels

---

### Week 20-21: Error Correction

**Topics:**
- 3-qubit bit-flip code
- Phase-flip code
- Shor's 9-qubit code
- Stabilizer formalism

**Reading:**
- Nielsen & Chuang: Sections 10.1-10.6

**Coding:**
```python
# code/advanced/error_correction.py
# Implement 3-qubit code
```

**Milestone:** Implement basic error correction codes

---

## Phase 6: Advanced Topics (Weeks 22+)

### Week 22-23: VQE

**Topics:**
- Variational Quantum Eigensolver
- Ansatz construction
- Classical optimization
- Quantum chemistry applications

**Coding:**
```python
# code/advanced/vqe.py
from qiskit.algorithms import VQE
```

**Milestone:** Calculate ground state energy of H₂

---

### Week 24-25: QAOA

**Topics:**
- Quantum Approximate Optimization Algorithm
- Combinatorial optimization
- MaxCut problem
- Ansatz: alternating operators

**Coding:**
```python
# code/advanced/qaoa.py
from qiskit.algorithms import QAOA
```

**Milestone:** Solve MaxCut with QAOA

---

### Week 26+: Hamiltonian Simulation

**Topics:**
- Trotterization
- Product formulas
- Error analysis
- Ising model

**Coding:**
```python
# code/advanced/trotter.py
# Implement first and second-order Trotter
```

**Milestone:** Simulate time evolution of Hamiltonian

---

## Progress Tracking

Use `progress/template.md` to track weekly progress:

```markdown
## Week X: [Topic]

### Completed
- [ ] Reading: Sections X.X
- [ ] Coding: file.py
- [ ] Understanding: Key concept

### Challenges
- What was difficult
- How I overcame it

### Next Week
- Upcoming topics
- Goals
```

---

## Assessment Checkpoints

### After Phase 1
- ✅ Can represent any single-qubit state
- ✅ Visualize on Bloch sphere
- ✅ Implement all single-qubit gates

### After Phase 2
- ✅ Create Bell states
- ✅ Implement teleportation
- ✅ Understand entanglement

### After Phase 3
- ✅ Build complex circuits
- ✅ Decompose controlled gates
- ✅ Synthesize unitaries

### After Phase 4
- ✅ Implement QFT
- ✅ Run Grover's search
- ✅ Factor integers with Shor's

### After Phase 5
- ✅ Work with density matrices
- ✅ Simulate noise
- ✅ Implement error correction

### After Phase 6
- ✅ Run VQE for molecules
- ✅ Solve optimization with QAOA
- ✅ Simulate Hamiltonian dynamics

---

*Based on Nielsen & Chuang "Quantum Computation and Quantum Information"*  
*Last Updated: March 2026*
