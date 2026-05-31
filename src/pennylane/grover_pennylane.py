import pennylane as qml
from pennylane import numpy as np

# Simulateur
DEV = qml.device("default.qubit", wires=2, shots=100)

@qml.qnode(DEV)
def grover():
    # Superposition
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)

    # Oracle
    qml.CZ(wires=[0, 1])

    # Diffusion
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)

    qml.PauliX(wires=0)
    qml.PauliX(wires=1)

    qml.Hadamard(wires=1)
    qml.CNOT(wires=[0, 1])
    qml.Hadamard(wires=1)

    qml.PauliX(wires=0)
    qml.PauliX(wires=1)

    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)

    return qml.sample()

print(grover()) 