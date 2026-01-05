import numpy as np

from graphs_data import *
from matrix_power import calc

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

calc(adj, 13)
