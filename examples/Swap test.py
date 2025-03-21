from AriaQuanta.aqc import Circuit, MeasureQubit
from AriaQuanta.aqc.gatelibrary import H, SWAP, X

# Create a circuit with 3 qubits (2 target qubits and 1 ancillary qubit)
qc = Circuit(3, 1)  # 3 quantum bits, 1 classical bit

# Initialize the target qubits with test states
# For example, set qubit 1 to |1⟩ using an X gate
qc | X(1)

# Apply a Hadamard gate to the ancillary qubit
qc | H(0)

# Apply the SWAP gate between the two target qubits
qc | SWAP(1, 2)

# Apply another Hadamard gate to the ancillary qubit
qc | H(0)

# Measure the ancillary qubit
qc | MeasureQubit([0], ['ancilla'])

# Execute the circuit
qc.run()

# Get the measurement result of the ancillary qubit
result = qc.measurequbit_values
print("\nAncillary qubit measurement result:", result)
