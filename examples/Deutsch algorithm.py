from AriaQuanta.aqc import Circuit, MeasureQubit
from AriaQuanta.aqc.gatelibrary import H, X, CX

# Define the Deutsch Oracle (general structure for f(x))
def deutsch_oracle(circuit, control, target, function_type="balanced"):
    """
    This function implements the oracle for the Deutsch algorithm.
    - `function_type="constant"` for constant functions (e.g., f(x) = 0 or f(x) = 1).
    - `function_type="balanced"` for balanced functions (e.g., f(x) = x).
    """
    if function_type == "constant":
        # Oracle for a constant function: Do nothing or apply an X gate (f(x) = 1 for all x)
        pass  # No operation needed for f(x) = 0
    elif function_type == "balanced":
        # Oracle for a balanced function (example: f(x) = x)
        circuit | CX(control, target)
    return circuit

# Step 1: Create a circuit with 2 qubits (1 for input, 1 for output)
qc = Circuit(2)

# Step 2: Initialize the second qubit in state |1>
qc | X(1)

# Step 3: Apply Hadamard gates to create superposition
qc | H(0) | H(1)

# Step 4: Apply the Deutsch Oracle
# Choose the type of function: "constant" or "balanced"
qc = deutsch_oracle(qc, control=0, target=1, function_type="balanced")

# Step 5: Apply Hadamard gate to the first qubit
qc | H(0)

# Step 6: Measure the first qubit
qc | MeasureQubit([0], ['result'])

# Execute the circuit
qc.run()

# Retrieve and display the result
result = qc.measurequbit_values  # List of measured values
if result:
    print("Result of Deutsch Algorithm (0: constant, 1: balanced):", result)
else:
    print("Error: No measurement results found.")
