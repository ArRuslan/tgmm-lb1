from graphs_data import *

adj_matrix = [
    [0 for _ in nodes]
    for _ in nodes
]

for (u, v) in all_edges:
    u -= 1
    v -= 1

    adj_matrix[u][v] = adj_matrix[v][u] = 1

print_matrix(adj_matrix, True)