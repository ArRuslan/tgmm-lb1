from graphs_data import *

inc_matrix = [
    [0 for _ in all_edges]
    for _ in nodes
]

for (u, v) in all_edges:
    edge_idx = edge_index[(u, v)]

    u -= 1
    v -= 1

    inc_matrix[u][edge_idx] = inc_matrix[v][edge_idx] = 1

print_matrix(inc_matrix, True)