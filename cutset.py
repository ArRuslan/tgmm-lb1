import numpy as np

from graphs_data import *

cutset_matrix = []

for (u, v) in spanning_edges:
    T_tmp = T.copy()
    T_tmp.remove_edge(u, v)

    comps = list(nx.connected_components(T_tmp))
    assert len(comps) == 2, "T is not a valid spanning tree"

    compA, compB = comps

    row = [0] * len(all_edges)

    for (x, y) in all_edges:
        inA_x = x in compA
        inA_y = y in compA

        if inA_x != inA_y:
            if inA_x and (y in compB):
                row[edge_index[(x, y)]] = +1
            else:
                row[edge_index[(x, y)]] = -1

    cutset_matrix.append(row)

cutset_matrix_frfr = reorder_matrix(cutset_matrix)
print_matrix(cutset_matrix_frfr, True)

np_cutset = np.asarray(cutset_matrix_frfr, dtype=np.int8)
np_cutset = np_cutset[:, len(spanning_idxs):]
print(np_cutset)
print(np_cutset.transpose())
