# Topological Sort
## Topological Sort Graph
```
from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def __repr__(self):
        return f"Graph({self.graph})"

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        for v in range(self.V):
            if not visited[v]:
                self.topological_sort_util(v, visited, stack)

        return stack[::-1]


# Example usage:
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(1, 2)
    g.add_edge(1, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 5)
    g.add_edge(2, 3)
    g.add_edge(3, 5)
    """
    1 → 2 → 3
    ↓       ↓
    → → →   ↓
        ↓   ↓
    4 → 0   ↓
    ↓       ↓
    5 ← ← ← ← 
    """

    print(g.topological_sort())  # [5, 4, 2, 3, 1, 0]
```
