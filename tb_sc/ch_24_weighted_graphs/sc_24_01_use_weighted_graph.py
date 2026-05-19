from sc_24_01_weighted_graph import WeightedGraph

def main():
    graph = WeightedGraph.from_file("weighted_graph.txt")
    print("Weighted graph (adjacency):")
    for v in graph.vertices():
        print(f"{v}: {graph.neighbors(v)}")

        distance, predecessor = graph.dijkstra("A")

    print("Korteste avstander fra A:")
    for node in sorted(distance):
        print(f"{node}: {distance[node]}")

    print("\nPredecessor:")
    for node in sorted(predecessor):
        print(f"{node}: {predecessor[node]}")

    print("\nPrim's minimum spanning tree (start A):")
    mst = graph.prim("A")
    for u, v, w in mst:
        print(f"{u} - {v}: {w}")

if __name__ == "__main__":
    main()
