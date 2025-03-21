
from AriaQuanta.aqc.gatelibrary import H, RX, RZ, CX
from AriaQuanta.aqc import Circuit, MeasureQubit
from AriaQuanta.backend import Simulator, plot_histogram
import random

def generate_random_circuit(n_qubits, depth):
    """
    Generates a random quantum circuit.
    - n_qubits: Number of qubits in the circuit.
    - depth: Number of layers (depth) in the circuit.
    """
    qc = Circuit(n_qubits)  # Define circuit with the correct number of qubits
    for _ in range(depth):
        for qubit in range(n_qubits):
            # Apply a random single-qubit gate (Hadamard, RX, or RZ)
            gate = random.choice([H, RX, RZ])
            if gate in [RX, RZ]:
                angle = random.uniform(0, 2 * 3.14159)  # Random rotation angle
                qc | gate(qubit, angle)
            else:
                qc | gate(qubit)  # Gates like H don't require parameters
        
        # Add a random CX gate ensuring valid qubit IDs
        control = random.randint(0, n_qubits - 1)
        target = random.randint(0, n_qubits - 1)
        while target == control:  # Ensure control and target are not the same
            target = random.randint(0, n_qubits - 1)
        qc | CX(control, target)
    
    return qc

# Define circuit parameters
n_qubits = 3  # Number of qubits
depth = 3  # Depth of the circuit

# Generate a random circuit
random_qc = generate_random_circuit(n_qubits, depth)

# Add measurement for all valid qubits
random_qc | MeasureQubit([i for i in range(n_qubits)])

# Simulate the circuit
sim = Simulator()
result = sim.simulate(random_qc, 1000)  # Run simulation with 1000 shots

# Retrieve and display results
counts = result.count()
print("Measurement Results:", counts)

# Plot the histogram of results
plot_histogram(counts)
