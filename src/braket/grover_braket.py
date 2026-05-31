from braket.circuits import Circuit
from braket.devices import LocalSimulator

circuit = Circuit()

# Superposition
circuit.h(0)
circuit.h(1)

# Oracle
circuit.cz(0, 1)

# Diffusion
circuit.h(0)
circuit.h(1)

circuit.x(0)
circuit.x(1)

circuit.h(1)
circuit.cnot(0, 1)
circuit.h(1)

circuit.x(0)
circuit.x(1)

circuit.h(0)
circuit.h(1)

# Mesure
device = LocalSimulator()
result = device.run(circuit, shots=100).result()

print(result.measurement_counts)