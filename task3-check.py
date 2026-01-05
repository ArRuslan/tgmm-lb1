import numpy as np

from graphs_data import *
from transpose_this_shi import calc

adj_matrix = [
    [0 for _ in nodes]
    for _ in nodes
]

for (u, v) in all_edges:
    u -= 1
    v -= 1

    adj_matrix[u][v] = 1

print_matrix(adj_matrix, True)

adj = np.asarray(adj_matrix)
adj_tr = adj.transpose()

print("="*32)
print_matrix(adj_tr, True)

inc_matrix = [
    [0 for _ in all_edges]
    for _ in nodes
]

for (u, v) in all_edges:
    edge_idx = edge_index[(u, v)]

    u -= 1
    v -= 1

    inc_matrix[u][edge_idx] = 1
    inc_matrix[v][edge_idx] = -1

print("="*32)
print_matrix(inc_matrix, True)

inc = np.asarray(inc_matrix)
inc_tr = inc.transpose()

print("="*32)
print_matrix(inc_tr, True)

check = np.array([
    [2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
])
calc(adj, inc, check)
