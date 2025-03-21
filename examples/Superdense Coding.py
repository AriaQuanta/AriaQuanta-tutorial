import random
from AriaQuanta.aqc import Circuit, create_state, MeasureQubit
from AriaQuanta.aqc.gatelibrary import H, CX, X, Z

# Create an entangled state (Bell pair)
qc = Circuit(2, 2)  # Two quantum qubits and two classical bits
qc | H(0) | CX(0, 1)

# Generate a random 2-bit classical message (0 or 1 for each bit)
message = [random.randint(0, 1), random.randint(0, 1)]
print("Random classical message:", message)

# Apply the necessary gates to encode the classical message
if message[0] == 1:
    qc | Z(0)  # Apply Z gate if the first bit is 1
if message[1] == 1:
    qc | X(0)  # Apply X gate if the second bit is 1

# Alice sends her qubit (qubit 0) to Bob

# Bob applies gates (H and CX) to decode the message
qc | CX(0, 1) | H(0)

# Measure qubits to retrieve the classical message
qc | MeasureQubit([0, 1], ['m0', 'm1'])

# Execute the circuit
qc.run()

# Retrieve measurement results
measured_values = qc.measurequbit_values
print("\nDecoded classical message:", measured_values)
