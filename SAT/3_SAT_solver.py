# import Qiskit quantum libraries
from qiskit.visualization import plot_histogram
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Grover
from qiskit.circuit.library import PhaseOracle
from qiskit import Aer
from qiskit.algorithms import AmplificationProblem
import numpy as np
import os
import matplotlib.pyplot as plt

with open('3sat3-5.cnf', 'r') as f:
    sat_cnf = f.read()
    oracle = PhaseOracle.from_dimacs_file("3sat3-5.cnf")
print(sat_cnf)

backend = Aer.get_backend('qasm_simulator')
grover = Grover(quantum_instance=backend)
problem = AmplificationProblem(oracle)
result = grover.amplify(problem)
histogram = plot_histogram(result.circuit_results)
print(result.circuit_results)

print("Result assignment:", result.assignment)
print("Iterations performed:", result.iterations)

results = result.circuit_results[0]

counts = np.array(list(results.values()))

mean = np.mean(counts)
std_dev = np.std(counts)

threshold = mean + std_dev

high_values = {state: count for state, count in results.items() if count > threshold}
print("High-value states:", high_values)


print(f"Total qubits used: {oracle.num_qubits}")
oracle.draw(output="mpl")
plt.show()