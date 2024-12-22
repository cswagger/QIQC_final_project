import networkx as nx
from qiskit_optimization.applications import Clique
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms import QAOA
from qiskit import Aer
from sys import argv

def read_input(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        n, m = map(int, lines[0].split())
    
    G = nx.Graph()
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


if len(argv) != 4:
    print("Usage: python3 clique_QUBO.py [input_file] [answer_file] [reps]")
    exit(1)
input_file = argv[1]
answer_file = argv[2]
reps = int(argv[3])

G = read_input(input_file)
G = nx.relabel_nodes(G, {old_label: new_label for new_label, old_label in enumerate(G.nodes())})

# Convert the graph into a Clique problem
clique = Clique(graph=G)
qubo = clique.to_quadratic_program()
# print(qubo)

# Solve using QAOA
quantum_instance = Aer.get_backend('aer_simulator')
qaoa = QAOA(reps=reps, quantum_instance=quantum_instance)
optimizer = MinimumEigenOptimizer(qaoa)
result = optimizer.solve(qubo)
found_clique = set(clique.interpret(result))

expected_clique = read_answer(answer_file)
is_correct = found_clique in expected_clique
print("Found Clique Nodes:", " ".join(map(str, found_clique)))
if is_correct:
    print("Result: Correct")
else:
    print("Result: Incorrect")
    exit(1)
