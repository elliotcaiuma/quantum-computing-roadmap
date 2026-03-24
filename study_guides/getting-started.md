# Getting Started with Quantum Computing

## Prerequisites Checklist

Before diving into quantum computing, ensure you have:

### Mathematics
- [ ] **Linear Algebra:** Vectors, matrices, eigenvalues, eigenvectors
- [ ] **Complex Numbers:** Euler's formula, polar form, complex conjugate
- [ ] **Probability:** Basic probability, expectation values
- [ ] **Calculus:** Derivatives, integrals (helpful but not essential)

### Programming
- [ ] **Python Basics:** Variables, functions, loops, classes
- [ ] **NumPy:** Array operations, linear algebra
- [ ] **Matplotlib:** Basic plotting (optional but helpful)

### Physics (Optional)
- [ ] **Basic Quantum Mechanics:** Wave functions, Schrödinger equation (helpful but not required)

---

## Week 1: Your First Quantum Circuit

### Day 1-2: Install & Test

```bash
# Clone the repository
git clone https://github.com/elliotcaiuma/quantum-computing-roadmap.git
cd quantum-computing-roadmap

# Set up environment
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Test setup
python code/foundations/test_setup.py
```

### Day 3-4: Create Your First State

```python
# Run the state creator
python code/foundations/create_state.py
```

**Learn:**
- What is a qubit?
- How to represent $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$
- Normalization: $|\alpha|^2 + |\beta|^2 = 1$

### Day 5-7: Visualize on Bloch Sphere

**Key Concepts:**
- Bloch sphere representation
- North pole = $|0\rangle$, South pole = $|1\rangle$
- Equator = superposition states

---

## Week 2: Single-Qubit Gates

### Gates to Master

| Gate | Matrix | Effect |
|------|--------|--------|
| **X** | $\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$ | Bit flip (NOT) |
| **Y** | $\begin{pmatrix}0 & -i\\ i & 0\end{pmatrix}$ | Bit + phase flip |
| **Z** | $\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}$ | Phase flip |
| **H** | $\frac{1}{\sqrt{2}}\begin{pmatrix}1 & 1\\ 1 & -1\end{pmatrix}$ | Creates superposition |
| **S** | $\begin{pmatrix}1 & 0\\ 0 & i\end{pmatrix}$ | Phase gate (π/2) |
| **T** | $\begin{pmatrix}1 & 0\\ 0 & e^{i\pi/4}\end{pmatrix}$ | Phase gate (π/4) |

### Practice Code

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.x(0)   # X gate
qc.h(0)   # Hadamard
qc.z(0)   # Z gate
```

---

## Week 3: Measurement

### Born Rule

Probability of measuring outcome $i$:
$$P(i) = |\langle i|\psi\rangle|^2$$

### Practice

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1, 1)
qc.h(0)  # Create superposition
qc.measure(0, 0)  # Measure
```

**Expected:** 50% |0⟩, 50% |1⟩

---

## Common Questions

### Q: Do I need a physics background?

**A:** No! Many successful quantum programmers come from CS/math backgrounds. The math is more important than physics intuition.

### Q: How much math do I need?

**A:** Comfort with linear algebra (vectors, matrices) is essential. Complex numbers are used throughout. Calculus is helpful but not required for basics.

### Q: Should I use Qiskit or another framework?

**A:** Qiskit is recommended because:
- Excellent documentation
- Large community
- Runs on real IBM hardware
- Python-based (accessible)

Alternatives: Cirq (Google), Pennylane (Xanadu), Q# (Microsoft)

### Q: How long until I understand quantum algorithms?

**A:** With consistent study (1-2 hours daily):
- 2-3 weeks: Comfortable with single-qubit
- 4-6 weeks: Multi-qubit and entanglement
- 8-10 weeks: First algorithms (QFT, Grover's)

---

## Tips for Success

### 1. Code Every Day

Don't just read—implement everything:
```python
# Even simple exercises help
qc = QuantumCircuit(1)
qc.h(0)
```

### 2. Visualize States

Use Bloch sphere constantly:
```python
from qiskit.visualization import plot_bloch_multivector
plot_bloch_multivector(qc)
```

### 3. Join Communities

- Qiskit Slack: https://qiskit.slack.com
- Quantum Computing Stack Exchange
- r/QuantumComputing (Reddit)

### 4. Be Patient

Quantum computing is counterintuitive. It's normal to feel confused initially. Keep coding!

---

## Next Steps

After Week 3:
1. Move to **multi-qubit systems** (Week 4-6)
2. Learn **entanglement** and Bell states
3. Implement **quantum teleportation**

Follow `ROADMAP.md` for the complete study plan.

---

*Last Updated: March 2026*
