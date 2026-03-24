# Quantum Computing Foundations Roadmap

## Study Plan

This roadmap covers **foundations** — single-qubit and multi-qubit systems.

---

## Phase 1: Single-Qubit

### Topics

- Dirac notation (bras, kets, outer products)
- Qubit representation: $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$
- Bloch sphere visualization
- Single-qubit gates: X, Y, Z, H, S, T
- Measurement theory and Born rule

### Code Progression

```
01_hello_qubit.py      → Create |0⟩
02_create_basis.py     → Create |0⟩, |1⟩
03_create_superposition.py → Create |+⟩, |-⟩
04_custom_state.py     → Create ANY state (function)
05_measure_z.py        → Measure in Z basis
06_measure_any_basis.py → Measure in X/Y/Z
07_apply_x_gate.py     → Apply X gate
08_apply_all_single_gates.py → All gates
09_gate_transformer.py → Apply ANY sequence
```

### Milestone

✅ Represent any single-qubit state  
✅ Visualize on Bloch sphere  
✅ Implement all single-qubit gates  
✅ Measure in any basis  

---

## Phase 2: Multi-Qubit

### Topics

- Tensor products and composite systems
- Entanglement and Bell states
- Multi-qubit gates: CNOT, CZ, SWAP
- Quantum teleportation protocol
- Superdense coding

### Code Progression

```
10_hello_2qubit.py     → Create |00⟩
11_tensor_product.py   → |0⟩ ⊗ |1⟩
12_tensor_product_calculator.py → ANY tensor product
13_create_bell_phi_plus.py → Create |Φ⁺⟩
14_all_bell_states.py  → All 4 Bell states
15_bell_factory.py     → Create ANY Bell state
16_measure_bell.py     → Measure Bell state
17_bell_analyzer.py    → Analyze ANY Bell state
```

### Milestone

✅ Compute tensor products  
✅ Create all 4 Bell states  
✅ Understand entanglement  
✅ Implement CNOT gate  
✅ Run teleportation protocol  

---

## Code Philosophy

Code follows **easy → hard, specific → general**:

1. **Levels 1-3:** Copy-paste examples (no functions)
2. **Levels 4-6:** First functions (single purpose)
3. **Levels 7-9:** Gate operations (reusable)
4. **Levels 10-12:** Tensor products (multi-qubit)
5. **Levels 13-15:** Bell states (entanglement)
6. **Levels 16-17:** Analysis (complete tools)

See `code/README.md` for details.

---

## Textbook Reference

Follows **Nielsen & Chuang**:
- Chapters 1-2: Fundamental concepts
- Chapter 4: Quantum circuits

---

## Next Steps

After mastering foundations:
- Quantum algorithms (QFT, Grover's, Shor's)
- Variational methods (VQE, QAOA)
- Quantum information (error correction)

---

*Last Updated: March 2026*
