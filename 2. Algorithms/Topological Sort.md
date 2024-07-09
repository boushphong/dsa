# Topological Sort
## Topological Sort Graph (with DFS)
```python
from collections import defaultdict


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

## Topological Sort Graph (with BFS)
```python
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    def __repr__(self):
        return f"Graph({self.graph})"

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_bfs(self):
        # Step 1: Calculate in-degrees of all vertices
        in_degree = [0] * self.V
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1

        # Step 2: Initialize the queue with all vertices having in-degree 0
        queue = deque([i for i in range(self.V) if in_degree[i] == 0])

        # Step 3: Process the vertices
        top_order = []
        while queue:
            u = queue.popleft()
            top_order.append(u)

            # Decrease the in-degree of all adjacent vertices
            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        # Step 4: Check if there was a cycle
        if len(top_order) != self.V:
            raise ValueError("There exists a cycle in the graph")

        return top_order

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
