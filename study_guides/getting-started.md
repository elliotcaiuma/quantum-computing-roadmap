# Getting Started with Quantum Foundations

## Focus: Weeks 1-6 Only

This guide covers **only foundations** — single-qubit and multi-qubit systems. Master these before touching algorithms.

---

## Prerequisites Checklist

Before starting, ensure you have:

### Mathematics
- [ ] **Linear Algebra:** Vectors, matrices, matrix multiplication
- [ ] **Complex Numbers:** $i = \sqrt{-1}$, complex conjugate, $|z|^2$
- [ ] **Probability:** Basic probability (optional but helpful)

### Programming
- [ ] **Python Basics:** Variables, functions, loops
- [ ] **NumPy:** Arrays, `np.kron()` for tensor products

### Physics
- [ ] **Not Required!** We teach the math you need

---

## Week 1: Your First Qubit

### Install & Test

```bash
# Clone the repository
git clone https://github.com/elliotcaiuma/quantum-computing-roadmap.git
cd quantum-roadmap

# Set up environment
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Test setup
python code/foundations/test_setup.py
```

### Create Your First State

```python
# Run the state creator
python code/foundations/create_state.py
```

**Learn:**
- What is a qubit? $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$
- Normalization: $|\alpha|^2 + |\beta|^2 = 1$
- Probability: $P(0) = |\alpha|^2$, $P(1) = |\beta|^2$

### Practice States

**Exercises:**
1. Create $|0\rangle$, $|1\rangle$
2. Create $|+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}$
3. Create $|-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}$
4. Calculate measurement probabilities for each

---

## Week 2: Bloch Sphere

### Key Concepts

- **Bloch sphere:** Visual representation of single-qubit states
- **North pole:** $|0\rangle$
- **South pole:** $|1\rangle$
- **Equator:** Superposition states ($|+\rangle$, $|-\rangle$, $|+i\rangle$, $|-i\rangle$)

### Code Practice

```python
from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector

qc = QuantumCircuit(1)
qc.h(0)  # Creates |+⟩
plot_bloch_multivector(qc)  # Shows on Bloch sphere
```

### Exercises

1. Plot |0⟩, |1⟩ — should be at poles
2. Plot |+⟩, |-⟩ — should be on equator
3. Apply X gate to |0⟩ — where does it move?
4. Apply H gate to |0⟩ — where does it move?

---

## Week 3: Gates & Measurement

### Gates to Master

| Gate | Effect | Matrix |
|------|--------|--------|
| **X** | Bit flip (NOT) | $\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$ |
| **Y** | Bit + phase flip | $\begin{pmatrix}0 & -i\\ i & 0\end{pmatrix}$ |
| **Z** | Phase flip | $\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}$ |
| **H** | Creates superposition | $\frac{1}{\sqrt{2}}\begin{pmatrix}1 & 1\\ 1 & -1\end{pmatrix}$ |

### Measurement

**Born Rule:**
$$P(i) = |\langle i|\psi\rangle|^2$$

**Code:**
```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1, 1)
qc.h(0)  # Superposition
qc.measure(0, 0)  # Measure
```

**Expected:** 50% |0⟩, 50% |1⟩

### Exercises

1. Apply X to |0⟩ — what do you get?
2. Apply H to |0⟩ — measure 100 times, what %?
3. Apply H then Z — what happens?

---

## Week 4: Tensor Products

### Key Concept

For 2 qubits:
$$|\psi\rangle = |\psi_1\rangle \otimes |\psi_2\rangle$$

Dimension: $2^n$ for n qubits (2 qubits = 4 dimensions)

### Code Practice

```python
# code/multi_qubit/tensor_products.py
import numpy as np

psi1 = np.array([1, 0])  # |0⟩
psi2 = np.array([0, 1])  # |1⟩
psi_combined = np.kron(psi1, psi2)  # |01⟩
print(psi_combined)  # [0, 1, 0, 0]
```

### Exercises

1. Compute $|0\rangle \otimes |0\rangle$
2. Compute $|0\rangle \otimes |1\rangle$
3. Compute $|1\rangle \otimes |0\rangle$
4. Compute $|1\rangle \otimes |1\rangle$

---

## Week 5: Entanglement & Bell States

### Bell States

4 maximally entangled states:

$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$
$$|\Phi^-\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle)$$
$$|\Psi^+\rangle = \frac{1}{\sqrt{2}}(|01\rangle + |10\rangle)$$
$$|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$$

### Circuit to Create $|\Phi^+\rangle$

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)     # Hadamard on qubit 0
qc.cx(0, 1) # CNOT with control=0, target=1
```

### Exercises

1. Create all 4 Bell states
2. Measure both qubits — what correlations do you see?
3. Why can't Bell states be written as tensor product?

---

## Week 6: Teleportation & Superdense Coding

### Quantum Teleportation

**Protocol:**
1. Alice and Bob share Bell pair
2. Alice has qubit |ψ⟩ to teleport
3. Alice measures her qubits
4. Alice sends classical bits to Bob
5. Bob applies correction gates

**Circuit:**
```python
# code/multi_qubit/teleportation.py
from qiskit import QuantumCircuit

qc = QuantumCircuit(3)
# Qubit 0: State to teleport
# Qubit 1,2: Bell pair (Alice, Bob)
```

### Superdense Coding

Send 2 classical bits using 1 qubit:
1. Alice and Bob share Bell pair
2. Alice applies gates based on 2 bits
3. Alice sends qubit to Bob
4. Bob measures and decodes 2 bits

### Exercises

1. Implement full teleportation circuit
2. Verify teleported state matches original
3. Implement superdense coding protocol

---

## Common Questions

### Q: Do I need physics background?

**A:** No! Linear algebra and complex numbers are enough.

### Q: How much time per week?

**A:** 5-8 hours (1 hour daily + weekend review).

### Q: What if I don't understand entanglement?

**A:** Normal! It's counterintuitive. Focus on the math: Bell states can't be written as $|\psi_1\rangle \otimes |\psi_2\rangle$.

### Q: Should I memorize matrices?

**A:** Understand them. Know what H does (creates superposition), what CNOT does (flips target when control is |1⟩).

---

## Tips for Success

### 1. Code Every Concept

Don't just read—implement:
```python
# Even simple exercises help
qc = QuantumCircuit(1)
qc.h(0)
```

### 2. Visualize Constantly

Use Bloch sphere:
```python
plot_bloch_multivector(qc)
```

### 3. Track Progress

Update `progress/template.md` weekly.

### 4. Ask Questions

- Quantum Computing Stack Exchange
- Qiskit Slack: https://qiskit.slack.com

---

## Mastery Checklist

After 6 weeks, you should be able to:

### Single-Qubit ✅
- [ ] Represent any state as $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$
- [ ] Normalize states
- [ ] Visualize on Bloch sphere
- [ ] Implement X, Y, Z, H, S, T gates
- [ ] Measure in X, Y, Z bases
- [ ] Calculate probabilities

### Multi-Qubit ✅
- [ ] Compute tensor products
- [ ] Create all 4 Bell states
- [ ] Explain entanglement
- [ ] Implement CNOT, CZ, SWAP
- [ ] Run teleportation protocol
- [ ] Run superdense coding

---

## What's Next?

After mastering foundations:
- **Quantum Algorithms:** QFT, Grover's, Shor's
- **Variational Methods:** VQE, QAOA
- **Quantum Information:** Density matrices, error correction

But first, **master these 6 weeks**. Don't rush!

---

*Last Updated: March 2026*
