import sys
import networkx as nx
from qiskit_optimization.applications import Clique
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_optimization.converters import QuadraticProgramToQubo
from qiskit.algorithms import QAOA
from qiskit import Aer

def read_input(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        n, m = map(int, lines[0].split())
    
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(1, m + 1):
        u, v = map(int, lines[i].split())
        G.add_edge(u, v)
    
    return G

def read_answer(answer_file):
    with open(answer_file, 'r') as file:
        lines = file.readlines()
    n = int(lines[0])
    cliques = [set(map(int, lines[i].split())) for i in range(1, n + 1)]
    max_size = max(len(clique) for clique in cliques)
    largest_cliques = [clique for clique in cliques if len(clique) == max_size]
    return largest_cliques


if len(sys.argv) != 4:
    print("Usage: python3 clique_QUBO.py [input_file] [answer_file] [reps]")
    exit(1)
input_file = sys.argv[1]
answer_file = sys.argv[2]
reps = int(sys.argv[3])

G = read_input(input_file)
G = nx.relabel_nodes(G, {old_label: new_label for new_label, old_label in enumerate(G.nodes())})

# Convert the graph into a Clique problem
clique = Clique(graph=G)
qp = clique.to_quadratic_program()
# print(qp)
qubo = QuadraticProgramToQubo().convert(qp)
# print(qubo)
# ising_model, offset = qubo.to_ising()
# print(ising_model)
# print("Offset:", offset)

# Solve using QAOA
quantum_instance = Aer.get_backend('aer_simulator')
quantum_instance.set_options(shots=1024)
qaoa = QAOA(reps=reps, quantum_instance=quantum_instance)

quantum_optimizer = MinimumEigenOptimizer(qaoa)
quantum_result = quantum_optimizer.solve(qubo)
quantum_found_clique = set(clique.interpret(quantum_result))
print("Quantum result: ", quantum_found_clique)

networkx_cliques = list(nx.find_cliques(G))
max_clique = max(networkx_cliques, key=len)
print("NetworkX result:", max_clique)

expected_clique = read_answer(answer_file)
is_correct = quantum_found_clique in expected_clique
print("Found Clique Nodes:", " ".join(map(str, quantum_found_clique)))
if is_correct:
    print("Result: Correct")
else:
    print("Result: Incorrect")
    exit(1)
