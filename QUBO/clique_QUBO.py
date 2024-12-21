import networkx as nx
from qiskit_optimization.applications import Clique
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms import QAOA
from qiskit import Aer

# 創建帶權圖
G = nx.Graph()
G.add_weighted_edges_from([
    (0, 1, 3), (1, 2, 5), (2, 3, 2), (0, 3, 4), (1, 3, 1)
])

# 定義加權團問題
clique = Clique(graph=G)
qubo = clique.to_qubo()

# 使用 QAOA 求解
quantum_instance = Aer.get_backend('aer_simulator')
qaoa = QAOA(quantum_instance=quantum_instance)
optimizer = MinimumEigenOptimizer(qaoa)
result = optimizer.solve(qubo)

# 輸出結果
print("找到的團：", result.x)
print("目標值（總權重）：", result.fval)
