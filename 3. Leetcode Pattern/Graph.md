# Graph
## DFS
```
6 - 4 - 3
    |   |
    5 - 2 - 1
```

```python
visited = set()


def dfs(graph, vertex):
    visited.add(vertex)
    print(vertex, end=" ")  # Process the node

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')
```

## BFS
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")  # Process the node
        
        # Add neighbors to the queue if not visited
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')
```

# Patterns
## DFS
### [All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/)
```python
def allPathsSourceTarget(graph):
    paths = []
    path = []
    visited = set()

    def dfs(atVertex=0):
        if atVertex == len(graph) - 1:
            return paths.append(path + [atVertex])

        path.append(atVertex)
        visited.add(atVertex)

        for vertex in graph[atVertex]:
            if vertex not in visited:
                dfs(vertex)

        visited.remove(atVertex)
        path.pop()

    dfs()
    return paths


print(allPathsSourceTarget([[1, 2], [3], [3], []]))
```
- **TC**: **O(|E| + |V|)**
    - **|E|** denotes the number of edges we have to traverse. We might re-traverse an edge over and over
    - **|V|** denotes the numbers of vertices we have to traverse. Even though if we don't have any edges, we still to travere through all the keys (vertices)
- **SC**: **O(|V|)**
    - **O(|V|)** from longest currentPath.
    - **O(|V|)** from visited set
    - **O(|V|)** from recursion stack trace.
    - Hence **O(3|V|)** > **O(|V|)**
