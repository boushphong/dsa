# Graph
# Tables of Contents
* [Graph](#graph)
   * [Graph Operations](#graph-operations)
   * [DFS](#dfs)
   * [BFS](#bfs)
* [Patterns](#patterns)
   * [DFS (Adjacency list)](#dfs-adjacency-list)
   * [BFS (Adjacency list)](#bfs-adjacency-list)
   * [DFS (Adjacency matrix)](#dfs-adjacency-matrix)
   * [BFS (Adjacency matrix)](#bfs-adjacency-matrix)

## Graph Operations
| Node / Edge Management | Storage          | Add Vertex       | Add Edge         | Remove Vertex    | Remove Edge | Query    |
|------------------------|------------------|------------------|------------------|------------------|-------------|----------|
| Adjacency list         | O(\|V\|+\|E\|)   | O(1)             | O(1)             | O(\|V\|+\|E\|)   | O(\|E\|)    | O(\|V\|) |
| Incidence list         | O(\|V\|+\|E\|)   | O(1)             | O(1)             | O(\|E\|)         | O(\|E\|)    | O(\|E\|) |
| Adjacency matrix       | O(\|V\|^2)       | O(\|V\|^2)       | O(1)             | O(\|V\|^2)       | O(1)        | O(1)     |
| Incidence matrix       | O(\|V\| * \|E\|) | O(\|V\| * \|E\|) | O(\|V\| * \|E\|) | O(\|V\| * \|E\|) | O(\|E\|)    | O(\|E\|) |
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
## DFS (Adjacency list)
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

### [Course Schedule](https://leetcode.com/problems/course-schedule)
```python
from collections import defaultdict


def canFinish(numCourses, prerequisites):
    if not prerequisites:
        return True

    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)

    visited = [False] * numCourses
    visitedSet = set()

    def dfs(i):
        if visited[i]:
            return False

        visited[i] = True

        noCycle = True
        for v in graph[i]:
            if v not in graph or v in visitedSet:
                continue
            noCycle = dfs(v) and noCycle

        visited[i] = False
        visitedSet.add(i)

        return noCycle

    for a in graph:
        val = dfs(a)
        if not val:
            return val

    return True


print(canFinish(20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]))  # False
print(canFinish(4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]))  # False
print(canFinish(4, [[1, 0], [1, 2], [2, 0]]))  # False
```
 
## BFS (Adjacency list)
### [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite)
```python
def isBipartite(graph):
    colors = [None] * len(graph)
    queue = deque()

    def coloring(start):
        queue.append(start)
        colors[start] = 1
        while queue:
            vertex = queue.popleft()

            for neighbor in graph[vertex]:
                if not colors[neighbor]:
                    queue.append(neighbor)
                tmp_color = colors[neighbor]
                colors[neighbor] = colors[vertex] * -1
                if tmp_color and tmp_color != colors[neighbor]:
                    return False

    for i in range(len(graph)):
        if not colors[i]:
            val = coloring(i)
            if val is False:
                return False

    return True


print(isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
```

## DFS (Adjacency matrix)
### [Number of Islands](https://leetcode.com/problems/number-of-islands/)
```python
def numIslands(grid):
    lengthRow, lengthCol = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    ans = 0

    def dfs(row, col):
        visited.add((row, col))

        for (moveByRow, moveByCol) in directions:
            r, c = row + moveByRow, col + moveByCol
            if r in {-1, lengthRow} or c in {-1, lengthCol} or (r, c) in visited or grid[r][c] == 0:
                continue

            if grid[r][c] == "1":
                dfs(r, c)

    for i in range(lengthRow):
        for j in range(lengthCol):
            if grid[i][j] == "1" and (i, j) not in visited:
                dfs(i, j)
                ans += 1

    return ans


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslands(grid))
```

### [Surrounded Regions](https://leetcode.com/problems/surrounded-regions)
```python
def solve(board):
    lengthRow, lengthCol = len(board), len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()

    def dfs(row, col):
        visited.add((row, col))

        for (moveByRow, moveByCol) in directions:
            r, c = row + moveByRow, col + moveByCol
            if r in {-1, lengthRow} or c in {-1, lengthCol} or (r, c) in visited or board[r][c] == "X":
                continue

            if board[r][c] == "O":
                dfs(r, c)

    for i in range(lengthRow):
        for j in range(lengthCol):
            if (i in {0, lengthRow - 1} or j in {0, lengthCol - 1}) and board[i][j] == "O":
                dfs(i, j)

    for i in range(lengthRow):
        for j in range(lengthCol):
            if (i, j) not in visited:
                board[i][j] = "X"


grid = [
    ["X", "X", "X", "X"],
    ["X", "X", "O", "X"],
    ["X", "X", "X", "X"],
    ["O", "O", "X", "X"],
    ["X", "O", "X", "X"]
]

print(solve(grid))
```
 
## BFS (Adjacency matrix)
### [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix)
```python
from collections import deque


def shortestPathBinaryMatrix(grid):
    if grid[0][0] == 1:
        return -1
    elif len(grid) == 1:
        return 1
    size = len(grid)
    visited = {(0, 0)}
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    queue = deque([(0, 0, 1)])

    while queue:
        row, col, dist = queue.popleft()

        for (moveByRow, moveByCol) in directions:
            newRow, newCol = row + moveByRow, col + moveByCol
            if newRow in {-1, size} or newCol in {-1, size} or grid[newRow][newCol] == 1 or (newRow, newCol) in visited:
                continue
            if (newRow, newCol) == (size - 1, size - 1):
                return dist + 1

            queue.append((newRow, newCol, dist + 1))
            visited.add((newRow, newCol))
    return -1


grid = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
]

print(shortestPathBinaryMatrix(grid))
```
