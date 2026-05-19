from pprint import pprint
from sc_23_01_graph_v1_basic import GraphV1Basic

def print_adjacency(graph):
    adj_view = {v: list(graph.neighbors(v)) for v in graph.vertices()}
    pprint(adj_view, sort_dicts=False)

def main():
    graph = GraphV1Basic.from_file("graph.txt")

    print("Graph V1 (basic):")
    print_adjacency(graph)

    print("\nBFS order from A:")
    print(graph.bfs("A"))

    print("\nDFS order from A:")
    print(graph.dfs("A"))

    print("\nConnected:")
    print(graph.is_connected())


if __name__ == "__main__":
    main()