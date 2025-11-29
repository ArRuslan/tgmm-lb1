import networkx as nx

_all_edges1 = [
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
    (6, 1),
]
_all_edges2 = [
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

nodes = range(1, 9 + 1)
spanning_remove_nodes = [6, 10, 11, 12, 13, 14]
spanning_remove_idxs = [node - 1 for node in spanning_remove_nodes]
spanning_nodes = [node for node in nodes if node not in spanning_remove_nodes]
spanning_idxs = [node - 1 for node in spanning_nodes]

all_edges = _all_edges2
edge_index = {edge: idx for idx, edge in enumerate(all_edges)}
spanning_edges = [
    edge
    for idx, edge in enumerate(all_edges)
    if idx not in spanning_remove_idxs
]
chords = [edge for edge in all_edges if edge not in spanning_edges]

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(all_edges)

T = nx.Graph()
T.add_nodes_from(nodes)
T.add_edges_from(spanning_edges)


def reorder_matrix(mat: list[list[int]]) -> list[list[int]]:
    return [
        [
            *(row[idx] for idx in spanning_idxs),
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
