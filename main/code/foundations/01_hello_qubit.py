#!/usr/bin/env python3
"""
Level 1: Hello Qubit - Task Specific

This is the simplest quantum code. Just creates |0⟩ state and prints it.
No functions, no parameters, just one specific task.

Perfect for absolute beginners - run this first!
"""

from qiskit.quantum_info import Statevector

# Create the |0⟩ state (ground state)
zero_state = Statevector.from_label('0')

# Print it
print("My first quantum state:")
print(zero_state)

# That's it! You just created a qubit!
