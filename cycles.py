from graphs_data import *

cycle_matrix = []

for (u, v) in chords:
    path_nodes = nx.shortest_path(T, u, v)

    path_edges = []
    for i in range(len(path_nodes) - 1):
        a, b = path_nodes[i], path_nodes[i + 1]
        if (a, b) in edge_index:
            path_edges.append((a, b))
        elif (b, a) in edge_index:
            path_edges.append((b, a))
        else:
            raise ValueError("Edge not found in all_edges list!")

    row = [0] * len(all_edges)

    row[edge_index[(u, v)]] = +1

    for (a, b) in path_edges:
        if (a, b) in edge_index:
            row[edge_index[(a, b)]] = +1
        else:
            row[edge_index[(b, a)]] = -1

    cycle_matrix.append(row)

print_matrix(reorder_matrix(cycle_matrix), True)
