from qiskit_algorithms import Grover
from qiskit.circuit.library import PhaseOracle
from qiskit_aer import Aer
from qiskit_algorithms import AmplificationProblem

import os
with open('3sat3-5.cnf', 'r') as f:
    sat_cnf = f.read()
    oracle = PhaseOracle.from_dimacs_file("3sat3-5.cnf")
print(sat_cnf)

backend = Aer.get_backend('qasm_simulator')
grover = Grover(quantum_instance=backend)
problem = AmplificationProblem(oracle)
result = grover.amplify(problem)
print(result.assignment)