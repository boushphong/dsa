# Graph
## DFS
```
6 - 4 - 3
    |   |
    5 - 2 - 1
```

```python
from collections import defaultdict


def allPaths(graph, fromNode, toNode):
    currentPath = []
    paths = []
    visited = set()

    def dfs(vertex=fromNode, destination=toNode):
        if vertex == destination:
            return paths.append(currentPath + [destination])

        currentPath.append(vertex)
        visited.add(vertex)
        for v in graph[vertex]:
            if v not in visited:
                dfs(v, destination)
        visited.remove(vertex)
        currentPath.pop()

    dfs()
    return paths


adj = defaultdict(list)
adj[1] = [2, 5]
adj[2] = [1, 3, 5]
adj[3] = [2, 4]
adj[4] = [3, 5, 6]
adj[5] = [1, 2, 4]
adj[6] = [4]
print(allPaths(adj, 1, 6))
# [[1, 2, 3, 4, 6], [1, 2, 5, 4, 6], [1, 5, 2, 3, 4, 6], [1, 5, 4, 6]]
```

- **TC**: **O(|E| + |V|)**
    - **|E|** denotes the number of edges we have to traverse.
    - **|V|** denotes the numbers of vertices we have to traverse. Even though if we don't have any edges, we still to travere through all the keys (vertices)
- **SC**: **O(|V|)**
    - **O(|V|)** from longest currentPath.
    - **O(|V|)** from visited set
    - **O(|V|)** from recursion stack trace.
    - Hence **O(3|V|)** > **O(|V|)**

## BFS
