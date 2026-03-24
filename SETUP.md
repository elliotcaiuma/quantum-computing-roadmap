# Environment Setup Guide

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/elliotcaiuma/quantum-computing-roadmap.git
cd quantum-computing-roadmap
```

### 2. Create Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python code/foundations/test_setup.py
```

Expected output:
```
✓ Qiskit working!
✓ NumPy imported
✓ Matplotlib ready
✓ Setup complete!
```

---

## Manual Installation

If you prefer individual packages:

```bash
# Core packages
pip install numpy scipy matplotlib

# Quantum computing
pip install qiskit qiskit-aer

# Jupyter (optional)
pip install jupyter notebook
```

---

## Qiskit Version Notes

**Qiskit 1.0+** (2024) introduced breaking changes:
- `qiskit.Aer` → `qiskit_aer.Aer`
- `execute()` → use `Simulator.run()`
- New modular architecture

This roadmap uses Qiskit 2.x syntax.

---

## IDE Setup

### VS Code (Recommended)

**Extensions:**
- Python (Microsoft)
- Jupyter (Microsoft)
- LaTeX Workshop (for documentation)

**Settings:**
```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.terminal.activateEnvironment": true
}
```

### PyCharm

1. Open project
2. Go to Settings → Project → Python Interpreter
3. Add → Existing Environment → Select `venv/bin/python`

---

## Jupyter Notebook Setup

```bash
# Install kernel
python -m ipykernel install --user --name=quantum-roadmap

# Launch Jupyter
jupyter notebook
```

Access at: `http://localhost:8888`

---

## LaTeX Setup (for Documentation)

### Windows

**MiKTeX:**
- Download: https://miktex.org/download
- Install with auto-package installation enabled

### macOS

**MacTeX:**
- Download: https://tug.org/mactex/
- Full installation (~4GB)

### Linux

**TeX Live:**
```bash
sudo apt install texlive-full  # Ubuntu/Debian
sudo dnf install texlive-scheme-full  # Fedora
```

---

## Troubleshooting

### Issue: Matplotlib backend error

```bash
pip install --upgrade matplotlib
```

Or set backend explicitly in code:
```python
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg'
```

### Issue: Qiskit import errors

```bash
pip uninstall qiskit qiskit-aer
pip install qiskit qiskit-aer
```

### Issue: Virtual environment not activating

**Windows:**
```powershell
.\venv\Scripts\Activate.ps1
```

If blocked by execution policy:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Issue: Jupyter kernel not found

```bash
python -m ipykernel install --user --name=quantum-roadmap
jupyter kernelspec list
```

---

## Verify Complete Setup

Run this comprehensive test:

```python
# test_complete.py
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector

print("Testing quantum computing setup...")

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
from qiskit import execute
result = execute(qc, simulator, shots=100).result()
counts = result.get_counts()
print(f"✓ Qiskit-Aer: simulation works - {counts}")

# 5. Visualization test
plot_bloch_multivector(qc)
plt.close()
print("✓ Visualization: Bloch sphere works")

print("\n🎉 All tests passed! Setup complete!")
```

---

## Next Steps

1. ✅ Run `test_complete.py` to verify everything works
2. ✅ Start with `code/foundations/create_state.py`
3. ✅ Follow `ROADMAP.md` week-by-week
4. ✅ Track progress in `progress/template.md`

---

## Getting Help

- **Qiskit Documentation:** https://qiskit.org/documentation
- **Qiskit Textbook:** https://qiskit.org/textbook
- **Quantum Computing Stack Exchange:** https://quantumcomputing.stackexchange.com
- **GitHub Issues:** Report setup issues in this repo

---

*Last Updated: March 2026*
