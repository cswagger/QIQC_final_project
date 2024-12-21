import networkx as nx
import sys

def all_maximal_cliques(graph):
    cliques = list(nx.find_cliques(graph))
    return cliques


def max_clique_solver(graph):
    cliques = all_maximal_cliques(graph)

    sorted_cliques = [sorted(sublist) for sublist in cliques]
    sorted_cliques = sorted(sorted_cliques)
    print(len(sorted_cliques))
    for clique in sorted_cliques:
        print(" ".join(map(str, clique)))
    
    return


G = nx.erdos_renyi_graph(n=int(sys.argv[1]), p=float(sys.argv[2]))

print(int(sys.argv[1]), len(G.edges))

for u, v in G.edges:
    print(u, v)

ans_vertex = max_clique_solver(G)




