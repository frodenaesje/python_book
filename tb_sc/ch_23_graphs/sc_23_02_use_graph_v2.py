from pprint import pprint

from sc_23_02_graph_v2 import GraphV2


def print_adjacency(graph):
    adj_view = {v: list(graph.neighbors(v)) for v in graph.vertices()}
    pprint(adj_view, sort_dicts=False)


def reconstruct_path(parent, target):
    if target not in parent:
        return None

    path = []
    while target is not None:
        path.append(target)
        target = parent[target]

    return list(reversed(path))


def main():
    graph = GraphV2.from_file("graph.txt")

    print("Graph V2 (transition):")
    print_adjacency(graph)

    print("\nBFS order-only from A:")
    print(graph.bfs("A"))

    print("\nBFS full data from A:")
    bfs_data = graph.bfs("A", return_data=True)
    for key, value in bfs_data.items():
        print(f"{key}:", value)

    print("\nDFS order-only from A:")
    print(graph.dfs("A"))

    print("\nDFS full data from A:")
    dfs_data = graph.dfs("A", return_data=True)
    for key, value in dfs_data.items():
        print(f"{key}:", value)

    print("\nConnected components:")
    print(graph.connected_components())

    print("\nShortest path from A to E (via BFS parent):")
    path = reconstruct_path(graph.bfs_parent("A"), "E")
    print(path)


if __name__ == "__main__":
    main()
