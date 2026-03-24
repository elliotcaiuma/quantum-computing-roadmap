# Quantum Computing Foundations Roadmap

## 6-Week Study Plan

This focused roadmap covers only **foundations** — single-qubit and multi-qubit systems. Master these before moving to algorithms.

---

## Phase 1: Single-Qubit Foundations (Weeks 1-3)

### Week 1: Quantum Mechanics Basics

**Topics:**
- Dirac notation (bras, kets, outer products)
- State vectors in Hilbert space
- Qubit representation: $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$
- Normalization condition: $|\alpha|^2 + |\beta|^2 = 1$
- Complex probability amplitudes

**Reading:**
- Nielsen & Chuang: Sections 1.1-1.3, 2.1

**Coding:**
```python
# code/foundations/create_state.py
from qiskit.quantum_info import Statevector

# Create custom state
psi = Statevector([1/np.sqrt(2), 1/np.sqrt(2)])  # |+⟩
print(psi)
```

**Milestone:** Can represent any single-qubit state and calculate probabilities

**Check Understanding:**
- [ ] Explain what a qubit is
- [ ] Normalize a state vector
- [ ] Calculate measurement probabilities

---

### Week 2: Bloch Sphere & Visualization

**Topics:**
- Bloch sphere representation
- Bloch vector: $\vec{r} = (\langle X \rangle, \langle Y \rangle, \langle Z \rangle)$
- Pure states on surface, mixed states inside
- Euler angles for rotations
- North pole = $|0\rangle$, South pole = $|1\rangle$

**Reading:**
- Nielsen & Chuang: Section 1.2, 2.4

**Coding:**
```python
# code/foundations/bloch_sphere.py
from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector

qc = QuantumCircuit(1)
qc.h(0)  # Hadamard gate
plot_bloch_multivector(qc)
```

**Milestone:** Visualize any single-qubit state on Bloch sphere

**Check Understanding:**
- [ ] Plot |0⟩, |1⟩, |+⟩, |-⟩ on Bloch sphere
- [ ] Explain what Bloch vector components mean
- [ ] Rotate state with gates

---

### Week 3: Single-Qubit Gates & Measurement

**Topics:**
- Pauli gates: X, Y, Z (and matrices)
- Hadamard gate: H (creates superposition)
- Phase gates: S, T
- Rotation gates: Rx, Ry, Rz
- Measurement postulates
- Born rule: $P(i) = |\langle i|\psi\rangle|^2$
- Expectation values

**Reading:**
- Nielsen & Chuang: Sections 2.2.3, 4.2

**Coding:**
```python
# code/foundations/gates.py
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.x(0)   # X gate (NOT)
qc.h(0)   # Hadamard (superposition)
qc.z(0)   # Z gate (phase flip)
qc.measure_all()
```

**Milestone:** Implement all single-qubit gates and measure in any basis

**Check Understanding:**
- [ ] Write matrix for X, Y, Z, H
- [ ] Explain what H does to |0⟩
- [ ] Measure in X, Y, Z bases

---

## Phase 2: Multi-Qubit Foundations (Weeks 4-6)

### Week 4: Tensor Products

**Topics:**
- Composite systems: $|\psi\rangle = |\psi_1\rangle \otimes |\psi_2\rangle$
- Tensor product notation
- Dimension: $2^n$ for n qubits
- Kronecker product
- Separable vs entangled states

**Reading:**
- Nielsen & Chuang: Section 2.3

**Coding:**
```python
# code/multi_qubit/tensor_products.py
import numpy as np

# Tensor product of two states
psi1 = np.array([1, 0])      # |0⟩
psi2 = np.array([0, 1])      # |1⟩
psi_combined = np.kron(psi1, psi2)  # |01⟩
print(psi_combined)  # [0, 1, 0, 0]
```

**Milestone:** Compute tensor products for multi-qubit states

**Check Understanding:**
- [ ] Compute tensor product of 2 qubits
- [ ] Explain why dimension is 2^n
- [ ] Identify separable states

---

### Week 5: Entanglement & Bell States

**Topics:**
- Bell states (4 maximally entangled states)
- $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$
- $|\Phi^-\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle)$
- $|\Psi^+\rangle = \frac{1}{\sqrt{2}}(|01\rangle + |10\rangle)$
- $|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$
- Schmidt decomposition (intro)
- CHSH inequality (optional)

**Reading:**
- Nielsen & Chuang: Sections 2.3, 4.3

**Coding:**
```python
# code/multi_qubit/bell_states.py
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)        # Create superposition
qc.cx(0, 1)    # CNOT creates Bell state
```

**Milestone:** Create all 4 Bell states and verify entanglement

**Check Understanding:**
- [ ] Create all 4 Bell states
- [ ] Explain why Bell states are entangled
- [ ] Measure correlations

---

### Week 6: Multi-Qubit Gates & Protocols

**Topics:**
- CNOT gate (controlled-NOT)
- Matrix representation
- Truth table
- CZ, SWAP gates
- Quantum teleportation protocol
- Superdense coding (2-bit protocol)

**Reading:**
- Nielsen & Chuang: Sections 4.3-4.4

**Coding:**
```python
# code/multi_qubit/teleportation.py
from qiskit import QuantumCircuit

# Teleportation circuit
qc = QuantumCircuit(3)
# Qubit 0: Alice's state to teleport
# Qubit 1,2: Bell pair (Alice, Bob)
```

**Milestone:** Implement quantum teleportation and superdense coding

**Check Understanding:**
- [ ] Draw CNOT truth table
- [ ] Implement teleportation protocol
- [ ] Explain superdense coding

---

## Assessment: Foundation Mastery

After completing 6 weeks, you should be able to:

### Single-Qubit ✅
- [ ] Represent any single-qubit state as $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$
- [ ] Visualize on Bloch sphere
- [ ] Implement X, Y, Z, H, S, T gates
- [ ] Measure in X, Y, Z bases
- [ ] Calculate probabilities using Born rule

### Multi-Qubit ✅
- [ ] Compute tensor products
- [ ] Create all 4 Bell states
- [ ] Explain entanglement
- [ ] Implement CNOT, CZ, SWAP
- [ ] Run quantum teleportation protocol

---

## Weekly Study Routine

### Session Structure (60-90 minutes)

1. **Reading (20-30 min):** Read assigned Nielsen & Chuang sections
2. **Theory (20 min):** Work through derivations by hand
3. **Coding (30-40 min):** Implement concepts in Qiskit
4. **Review (10 min):** Update progress tracker, note questions

### Weekly Review (Sunday)

- Review all code written during the week
- Re-read difficult sections
- Update `progress/template.md`
- Plan next week's topics

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

## What's Next?

After mastering foundations, you're ready for:

### Phase 3: Quantum Algorithms
- Quantum Fourier Transform (QFT)
- Grover's search algorithm
- Shor's factoring algorithm

### Phase 4: Quantum Information
- Density matrices
- Quantum noise
- Error correction

But first, **master these foundations**. Don't rush!

---

## Common Questions

### Q: How long should I spend on foundations?

**A:** 6 weeks with consistent daily study (1-2 hours). Don't rush—these concepts are used throughout quantum computing.

### Q: Should I memorize gate matrices?

**A:** Understand them, don't just memorize. Know what X, H, CNOT do intuitively.

### Q: What if I get stuck?

**A:** Normal! Quantum is counterintuitive. Code everything, visualize on Bloch sphere, ask on Quantum Computing Stack Exchange.

---

*Based on Nielsen & Chuang "Quantum Computation and Quantum Information"*  
*Last Updated: March 2026*
