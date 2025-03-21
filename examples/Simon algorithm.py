from AriaQuanta.aqc import Circuit, MeasureQubit
from AriaQuanta.aqc.gatelibrary import H, CX

# Define Simon's Oracle (Generalized)
def simon_oracle(circuit, n_qubits, s):
    """
    Simon's oracle applies the quantum operation based on the hidden string s.
    - circuit: the quantum circuit.
    - n_qubits: the number of input/output qubits.
    - s: the hidden binary string (as a string, e.g., "110").
    """
    for i in range(n_qubits):
        if s[i] == "1":
            circuit | CX(i, n_qubits + i)  # Apply CNOT gate between input/output qubits
    return circuit

# Step 1: Number of qubits and the hidden string
n_qubits = 3  # Number of input/output qubits
s = "101"     # The hidden string (binary representation)

# Step 2: Create a quantum circuit with 2n qubits (n for input, n for output)
qc = Circuit(2 * n_qubits)

# Step 3: Apply Hadamard gates to all input qubits
for i in range(n_qubits):
    qc | H(i)

# Step 4: Apply Simon's Oracle
qc = simon_oracle(qc, n_qubits, s)

# Step 5: Apply Hadamard gates again to all input qubits
for i in range(n_qubits):
    qc | H(i)

# Step 6: Measure the input qubits to generate linear equations
qc | MeasureQubit(list(range(n_qubits)), [f"q{i}" for i in range(n_qubits)])

# Execute the circuit
qc.run()

# Retrieve and display the results
results = qc.measurequbit_values
print("Measured results:", results)

