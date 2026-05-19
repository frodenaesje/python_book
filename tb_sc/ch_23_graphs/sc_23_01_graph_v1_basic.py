# file: sc_23_01_graph_v1_basic.py
from collections import deque

class GraphV1Basic:
    """Basic adjacency-list graph with BFS/DFS traversal order."""

    def __init__(self, directed: bool = False) -> None:
        self._adj: dict[str, list[str]] = {}
        self._directed = directed

    def add_vertex(self, v: str) -> None:
        """Add vertex if it does not exist."""
        if v not in self._adj:
            self._adj[v] = []

    def add_edge(self, u: str, v: str) -> None:
        """Add edge u->v (and v->u when undirected)."""
        if u not in self._adj:
            self.add_vertex(u)
        if v not in self._adj:
            self.add_vertex(v)

        if v not in self._adj[u]:
            self._adj[u].append(v)

        if not self._directed and u not in self._adj[v]:
            self._adj[v].append(u)

    def neighbors(self, v: str) -> list[str]:
        """Return neighbors for vertex v, or empty list if missing."""
        return self._adj.get(v, [])

    def vertices(self) -> list[str]:
        """Return all vertices in insertion order."""
        return list(self._adj.keys())

    def has_vertex(self, v: str) -> bool:
        """Return True when vertex v exists."""
        return v in self._adj

    def has_edge(self, u: str, v: str) -> bool:
        """Return True when edge u->v exists."""
        return u in self._adj and v in self._adj[u]

    def edge_count(self) -> int:
        """Return number of edges (logical edge count for graph type)."""
        total = sum(len(neigh) for neigh in self._adj.values())
        if self._directed:
            return total
        return total // 2

    @classmethod
    def from_file(
        cls,
        filename: str,
        directed: bool = False
    ) -> "GraphV1Basic":
        """Load graph from edge-list file.
        One edge 'u v' per line."""
        graph = cls(directed)

        with open(filename, encoding="utf-8") as file:
            for line_no, line in enumerate(file, start=1):
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                parts = stripped.split()
                if len(parts) != 2:
                    msg = (
                        f"Invalid edge at line {line_no}: "
                        f"expected 'u v'"
                    )
                    raise ValueError(msg)
                u, v = parts
                graph.add_edge(u, v)

        return graph
    
    def is_connected(self) -> bool:
        """Return True if all vertices are
        reachable from one start vertex."""
        verts = self.vertices()
        if not verts:
            return True

        start = verts[0]
        visited = set(self.bfs(start))
        return len(visited) == len(verts)
    
    def bfs(self, start: str) -> list[str]:
        """Return breadth-first traversal order from start vertex."""
        if start not in self._adj:
            return []

        visited = {start}
        queue = deque([start])
        order = []

        while queue:
            node = queue.popleft() # dequeue
            order.append(node)

            for neighbor in self.neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def dfs(self, start: str) -> list[str]:
        """Iterative DFS that goes depth-first before backtracking."""
        if start not in self._adj:
            return []

        visited = {start}
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            order.append(node)

            # Reverse push for left-to-right
            # traversal when nodes are popped.
            for neighbor in reversed(self.neighbors(node)):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        return order

    def __str__(self) -> str:
        """Pretty adjacency-list string for
        demos and debugging."""
        lines = []
        for vertex in self.vertices():
            neigh = ", ".join(self._adj[vertex])
            lines.append(f"{vertex}: [{neigh}]")
        return "\n".join(lines)
