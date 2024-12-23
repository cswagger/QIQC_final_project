import networkx as nx
import sys

def has_k_clique(graph, k):
    cliques = nx.find_cliques(graph)
    
    for clique in cliques:
        if len(clique) >= k:
            print(1)
            return

    print(0)
    return

G = nx.erdos_renyi_graph(n=int(sys.argv[1]), p=float(sys.argv[2]))

print(int(sys.argv[1]), len(G.edges), int(sys.argv[3]))

for u, v in G.edges:
    print(u, v)

has_k_clique(G, int(sys.argv[3]))