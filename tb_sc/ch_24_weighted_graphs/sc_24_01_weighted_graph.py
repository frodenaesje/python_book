# file: sc_24_01_weighted_graph.py
from heapq import heappop, heappush
import random

class WeightedGraph:
    """Weighted graph with adjacency list and Dijkstra/Prim."""

    def __init__(self, directed=False):
        self._adj: dict[str, list[tuple[str, float]]] = {}
        self._directed = directed

    def add_vertex(self, v: str) -> None:
        if v not in self._adj:
            self._adj[v] = []

    def add_edge(self, u: str, v: str, w: float) -> None:
        if u not in self._adj:
            self.add_vertex(u)
        if v not in self._adj:
            self.add_vertex(v)
        self._adj[u].append((v, w))
        if not self._directed:
            self._adj[v].append((u, w))

    def neighbors(self, v: str) -> list[tuple[str, float]]:
        return self._adj.get(v, [])

    def vertices(self) -> list[str]:
        return list(self._adj.keys())

    @classmethod
    def from_file(cls, filename: str, directed: bool = False) -> "WeightedGraph":
        graph = cls(directed)
        with open(filename, encoding="utf-8") as file:
            for line_no, line in enumerate(file, start=1):
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                parts = stripped.split()
                if len(parts) != 3:
                    raise ValueError(f"Line {line_no}: expected 'u v w'")
                u, v, w = parts
                graph.add_edge(u, v, float(w))
        return graph

    def dijkstra(self, start: str) -> tuple[dict[str, float], dict[str, str | None]]:
        if start not in self._adj:
            raise ValueError(f"Unknown start node: {start}")

        # Best known distance from start to each node
        distance = {v: float("inf") for v in self._adj}
        distance[start] = 0.0

        # predecessor[v] stores the previous node on the best known path to v
        predecessor = {v: None for v in self._adj}

        # Nodes whose shortest distance is now final
        finalized = set()

        # Priority queue entries are (distance, node)
        priority_queue: list[tuple[float, str]] = []
        heappush(priority_queue, (0.0, start))

        while priority_queue:
            current_distance, u = heappop(priority_queue)

            # Ignore nodes already finalized
            if u in finalized:
                continue

            finalized.add(u)
            
            for v, weight in self._adj[u]:
                if v in finalized:
                    continue

                new_distance = current_distance + weight

                if new_distance < distance[v]:
                    distance[v] = new_distance
                    predecessor[v] = u
                    heappush(priority_queue, (new_distance, v))

        return distance, predecessor

    def prim(self, start: str = None) -> list[tuple[str, str, float]]:
        # Empty graph -> empty MST
        if not self._adj:
            return []

        # Choose arbitrary start node if none is given
        if start is None:
            start = random.choice(list(self._adj))

        in_mst = {start}
        mst = []

        # Candidate edges: (weight, from, to)
        priority_queue = []

        # Initialize with edges from start node
        for neighbor, weight in self._adj[start]:
            heappush(priority_queue, (weight, start, neighbor))

        # Grow the tree
        while priority_queue and len(in_mst) < len(self._adj):
            weight, u, v = heappop(priority_queue)

            # Skip edges leading to already visited nodes
            if v in in_mst:
                continue

            # Add edge to MST
            in_mst.add(v)
            mst.append((u, v, weight))

            # Add new candidate edges from v
            for neighbor, next_weight in self._adj[v]:
                if neighbor not in in_mst:
                    heappush(priority_queue, (next_weight, v, neighbor))

        return mst
