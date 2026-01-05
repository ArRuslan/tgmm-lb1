import numpy as np

from graphs_data import *

kirghoph_matrix = [
    [0 for _ in nodes]
    for _ in nodes
]

for (u, v) in all_edges:
    u -= 1
    v -= 1

    kirghoph_matrix[u][v] = kirghoph_matrix[v][u] = -1

    kirghoph_matrix[u][u] += 1
    kirghoph_matrix[v][v] += 1

print_matrix(kirghoph_matrix, True)

mat = np.asarray(kirghoph_matrix)

mat = np.delete(mat, 0, 0)
mat = np.delete(mat, 0, 1)

print("="*32)

print_matrix(mat, True)

print(np.linalg.det(mat))
