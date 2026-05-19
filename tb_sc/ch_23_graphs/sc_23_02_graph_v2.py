from collections import deque


class GraphV2:
    """Transition version from basic traversal to richer graph API."""

    def __init__(self, directed=False):
        self._adj: dict[str, list[str]] = {}
        self._directed = directed

    def add_vertex(self, v):
        if v not in self._adj:
            self._adj[v] = []

    def add_edge(self, u, v):
        if u not in self._adj:
            self.add_vertex(u)
        if v not in self._adj:
            self.add_vertex(v)

        if v not in self._adj[u]:
            self._adj[u].append(v)

        if not self._directed and u not in self._adj[v]:
            self._adj[v].append(u)

    def neighbors(self, v):
        return self._adj.get(v, [])

    def vertices(self):
        return list(self._adj.keys())

    @classmethod
    def from_file(cls, filename, directed=False):
        graph = cls(directed)

        with open(filename) as file:
            for line in file:
                if not line.strip():
                    continue
                u, v = line.strip().split()
                graph.add_edge(u, v)

        return graph

    def _bfs_data(self, start):
        if start not in self._adj:
            return set(), [], {}, {}

        visited = {start}
        parent = {start: None}
        distance = {start: 0}
        queue = deque([start])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in self.neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)

        return visited, order, parent, distance

    def bfs(self, start, return_data=False):
        visited, order, parent, distance = self._bfs_data(start)

        if return_data:
            return {
                "visited": visited,
                "order": order,
                "parent": parent,
                "distance": distance,
            }

        return order

    def bfs_parent(self, start):
        _, _, parent, _ = self._bfs_data(start)
        return parent

    def _dfs_data(self, start):
        if start not in self._adj:
            return set(), [], {}

        visited = set()
        parent = {start: None}
        stack = [start]
        order = []

        while stack:
            node = stack.pop()

            if node in visited:
                continue

            visited.add(node)
            order.append(node)

            for neighbor in reversed(self.neighbors(node)):
                if neighbor not in visited:
                    if neighbor not in parent:
                        parent[neighbor] = node
                    stack.append(neighbor)

        return visited, order, parent

    def dfs(self, start, return_data=False):
        visited, order, parent = self._dfs_data(start)

        if return_data:
            return {
                "visited": visited,
                "order": order,
                "parent": parent,
            }

        return order

    def dfs_parent(self, start):
        _, _, parent = self._dfs_data(start)
        return parent

    def connected_components(self):
        visited = set()
        components = []

        for node in self.vertices():
            if node not in visited:
                component_order = self.bfs(node)
                visited.update(component_order)
                components.append(component_order)

        return components
