import cirq

# Deux qubits
q0, q1 = cirq.LineQubit.range(2)

circuit = cirq.Circuit()

# Superposition
circuit.append([cirq.H(q0), cirq.H(q1)])

# Oracle : marque |11>
circuit.append(cirq.CZ(q0, q1))

# Diffusion operator
circuit.append([cirq.H(q0), cirq.H(q1)])
circuit.append([cirq.X(q0), cirq.X(q1)])
circuit.append(cirq.H(q1))
circuit.append(cirq.CNOT(q0, q1))
circuit.append(cirq.H(q1))
circuit.append([cirq.X(q0), cirq.X(q1)])
circuit.append([cirq.H(q0), cirq.H(q1)])

# Mesure
circuit.append(cirq.measure(q0, q1, key='result'))

print(circuit)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=100)

print(result.histogram(key='result'))