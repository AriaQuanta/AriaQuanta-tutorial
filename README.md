
# Introduction

We introduce AriaQuanta, a powerful and flexible tool for designing, simulating, and implementing quantum circuits. This open-source software is designed to make it easy for users of all experience
levels to learn and use quantum computing. The first version includes a compiler for implementing
various quantum circuits and algorithms. Additionally, parametric circuits allow for the implementation of variational quantum algorithms, and various noise models are available for simulating noisy circuits.


# General Architecture

This architecture includes features such as the ability to integrate various functions, communicate with
external computing systems, manage computing tasks efficiently, and provide a user-friendly interface. In
the general architecture, a quantum circuit or algorithm is first defined, similar to the previous section.
It is then sent to a compiler that integrates a backend and task management and after executing the
program, the results are obtained. It is important to note that the program can be executed using a
CPU, QPU, or HPC. The results include the state vector, density matrix, and probability distribution of
states. 

# Getting Started

### Installation
AriaQuanta is available on both `pip` and `conda`. You can install AriaQuanta  from pip by doing

```ruby
pip install AriaQuanta
```
For verify installation  by loading following command
```ruby
import AriaQuanta
```
If no errors occur, the installation was successful, and you're ready to start!!!

# Quick Start
Here are some examples of how to work with AriaQuanta.


### Example 1: Create a entangled states

```ruby
from AriaQuanta.aqc.gatelibrary import H, CX
from AriaQuanta.aqc.circuit import Circuit
qc = Circuit(2)         # Create a 2-qubit quantum circuit
qc | H(0) | CX(0,1)    # Add Hadamard gate on qubit 1 and  a CX gate between qubits 1 and 2
qc.run()                # run quantum circuit
print("\nstate vector: ", qc.statevector)  
print("\ndensity matrix: ", qc.density_matrix)
```
### Example 2: Teleportation
```ruby

from AriaQuanta.aqc.circuit import Circuit
from AriaQuanta.aqc.gatelibrary import H, CX, Z, X
from AriaQuanta.aqc.measure import MeasureQubit
from AriaQuanta.aqc.operations import If_cbit
from AriaQuanta.aqc.qubit import create_state

#--------------------------------------------------
# define qubits with optional states

alpha = 0.3
# create qubit=0 with state alpha|0>+beta|1>
q0 = create_state(0,alpha) 

# create qubit=1 with state |0>
q1 = create_state(1,1)

# create qubit=2 with state |0>
q2 = create_state(2,1)

print("\nq0 state =\n", q0.state)
print("\nq1 state =\n", q1.state)
print("\nq2 state =\n", q2.state)

#--------------------------------------------------
# add qubits to a circuit
qc = Circuit(3, list_of_qubits=[q0, q1, q2])

print("\ninitial state of the circuit:\n", qc.statevector)

#--------------------------------------------------
# Make the shared entangled state 
qc | H(1)
qc | CX(1, 2)

# Alice applies teleportation gates (or projects to Bell basis)
qc | CX(0, 1)
qc | H(0)

# Alice measures her qubits
qc | MeasureQubit([0,1], ['a','b'])

# Bob applies certain gates based on the outcome of Alice's measurements
qc | If_cbit(['a',1], Z(2))
qc | If_cbit(['b',1], X(2))

#--------------------------------------------------
# simple run and output the statevector
# Bob checks the state of the teleported qubit
qc.run()
print("\nBob's statevector:\n", qc.statevector)
```
### Example 3: Bernestein-Vazirani Algorithm
```ruby
from AriaQuanta.aqc.circuit import Circuit
from AriaQuanta.aqc.gatelibrary import H, CX, Z, I
from AriaQuanta.backend.simulator import Simulator
from AriaQuanta.aqc.measure import MeasureQubit
from AriaQuanta.backend.result import plot_histogram

#-------------------------------------------------------------------
# Bernestein-Vazirani Algorithm for string '10' 

qc = Circuit(3)

qc | H(0) | H(1) | H(2) | Z(2) | CX(0,2) | H(0) | H(1) | MeasureQubit([0,1])

sim = Simulator()
result = sim.simulate(qc, 1000, 1)

counts, probability = result.count()

print('\ncounting measurement on the result:\n', counts)

plot_histogram(counts)

```
# Documentation

You can access the complete documentation online through GitHub Pages. Follow the link below for comprehensive explanations and step-by-step tutorials
[Online Documentation](https://github.com/AriaQuanta/AriaQuanta-tutorial/blob/main/docs/AriaQuanta_tutorials.ipynb).


https://github.com/AriaQuanta/AriaQuanta-tutorial/blob/main/docs/AriaQuanta_tutorials.ipynb

# Paper

Our paper introduces and thoroughly details this quantum software. This paper offers an in-depth overview of the methodology underlying AriaQuanta, encompassing its design principles and implementation details.




