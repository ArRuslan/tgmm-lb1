import networkx as nx

_all_edges_my0 = [
    (1, 2),
    (2, 3),
    (3, 5),
    (5, 6),
    (6, 9),
    (9, 8),
    (8, 7),
    (7, 4),
    (4, 1),
    (4, 2),
    (2, 5),
    (5, 4),
    (7, 5),
    (6, 7),
]

_all_edges_my1 = [
    (1, 2),
    (2, 3),
    (3, 5),
    (5, 6),
    (6, 9),
    (9, 8),
    (8, 7),
    (7, 4),
    (4, 1),
    (4, 2),
    (2, 5),
    (5, 4),
    (7, 5),
    (6, 7),
]
_all_edges_my2 = [
    (1, 2),
    (2, 3),
    (3, 5),
    (5, 6),
    (6, 9),
    (8, 9),
    (7, 8),
    (4, 7),
    (1, 4),
    (4, 2),
    (2, 5),
    (4, 5),
    (7, 5),
    (7, 6),
]
_spanning_remove_edges_my = [6, 10, 11, 12, 13, 14]

_all_edges_i0 = [
    (1, 2),
    (2, 3),
    (1, 6),
    (2, 6),
    (2, 5),
    (2, 4),
    (3, 4),
    (4, 5),
    (6, 7),
    (5, 8),
    (4, 9),
    (7, 8),
    (8, 9),
]
_all_edges_i1_cont = [
    (1, 2),
    (2, 3),
    (6, 1),
    (6, 2),
    (2, 5),
    (4, 2),
    (3, 4),
    (5, 4),
    (7, 6),
    (5, 8),
    (4, 9),
    (8, 7),
    (9, 8),
]
_all_edges_i2_nocont = [
    (1, 2),
    (2, 3),
    (1, 6),
    (6, 2),
    (2, 5),
    (2, 4),
    (3, 4),
    (5, 4),
    (6, 7),
    (5, 8),
    (4, 9),
    (7, 8),
    (8, 9),
]
_spanning_remove_edges_i = [4, 6, 8, 12, 13]

nodes = range(1, 9 + 1)
all_edges = _all_edges_i1_cont
spanning_remove_edges = _spanning_remove_edges_i

spanning_remove_idxs = [edge - 1 for edge in spanning_remove_edges]
spanning_nodes = [node for node in nodes if node not in spanning_remove_edges]
spanning_idxs = [idx for idx in range(len(all_edges)) if idx not in spanning_remove_idxs]

edge_index = {edge: idx for idx, edge in enumerate(all_edges)}
spanning_edges = [
    edge
    for idx, edge in enumerate(all_edges)
    if idx not in spanning_remove_idxs
]
chords = [edge for edge in all_edges if edge not in spanning_edges]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(all_edges)

GD = nx.DiGraph()
GD.add_nodes_from(nodes)
GD.add_edges_from(all_edges)

T = nx.Graph()
T.add_nodes_from(nodes)
T.add_edges_from(spanning_edges)


def reorder_matrix(mat: list[list[int]]) -> list[list[int]]:
    return [
        [
            *(row[idx] for idx, _ in enumerate(all_edges) if idx not in spanning_remove_idxs),
            *(row[idx] for idx in spanning_remove_idxs),
        ]
        for row in mat
    ]


def print_matrix(mat: list[list[int]], tabs: bool = False) -> None:
    for row in mat:
        for col in row:
            if tabs:
                print(col, end="\t")
            else:
                print(f"{col:>3}", end=" ")
        print()
