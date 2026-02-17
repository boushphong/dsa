# Topological Sort
Topological Sorting (Toposort) is an algorithm for ordering the vertices of a **directed acyclic graph** (**DAG**) such that:
- For every directed edge ( `u → v` ), vertex ( `u` ) comes before vertex ( `v` ) in the ordering.

**NOTE:** A Directed Acyclic Graph (DAG) cannot have cycles hence the algorithm will not work on graphs that have cycles.

## Analyzing Complexity
- **Time:** `O(|V| + |E|)`
- **Space:** `O(|V|)`

## Graph Representation
```mermaid
graph TD
    1 --> 2
    1 --> 0
    4 --> 0
    4 --> 5
    2 --> 3
    3 --> 5
```

## Topological Sort Graph (with DFS)
```python
def toposort(n, edges):
    graph = defaultdict(list)

    for fromNode, toNode in edges:
        graph[fromNode].append(toNode)

    visited = set()
    res = []

    def toposortUtil(node, visitedPath=set()):
        visited.add(node)
        visitedPath.add(node)

        for childNode in graph.get(node, []):
            if childNode not in visited:
                if toposortUtil(childNode, visitedPath):
                    return True
            if childNode in visitedPath:
                return True

        visitedPath.remove(node)
        res.append(node)
        return False

    for curNode in graph.keys():
        if curNode not in visited:
            if toposortUtil(curNode):
                return []

    return res[::-1]


# Example usage:
print(toposort(6, [(1, 2), (1, 0), (4, 0), (4, 5), (2, 3), (3, 5)]))
# [4, 1, 0, 2, 3, 5]
```

| Direction | What it means      | Valid in `[4, 1, 0, 2, 3, 5]`? |
|:----------|:-------------------|:-------------------------------|
| **1 → 0** | 1 must be before 0 | ✅ **Yes** (1 is 2nd, 0 is 3rd) |
| **4 → 0** | 4 must be before 0 | ✅ **Yes** (4 is 1st, 0 is 3rd) |
| **1 → 2** | 1 must be before 2 | ✅ **Yes** (1 is 2nd, 2 is 4th) |
| **2 → 3** | 2 must be before 3 | ✅ **Yes** (2 is 4th, 3 is 5th) |
| **3 → 5** | 3 must be before 5 | ✅ **Yes** (3 is 5th, 5 is 6th) |
| **4 → 5** | 4 must be before 5 | ✅ **Yes** (4 is 1st, 5 is 6th) |

```python
print(toposort(6, [(1, 2), (1, 0), (4, 0), (4, 5), (2, 3), (3, 5), (5, 1)]))
# [] Has Cycle
```

### DFS Underlying Logic and Cycle Detection
1. Run `toposort` on every node.
2. Skip node that has been visited.
3. Append the furthest (then closest) node into the output `res` array. This is handled by recursion.
4. We want to keep visited node `visited` and visited path `visitedPath` separately to handle cycle detection because:
    - Different paths might lead to the same node (`1 --> 0` and `4 --> 0`), hence we don't want to incorrectly detect a cyclic graph when it is not.
    - `visited` usage is to skip reprocessing identical nodes and populate the output `res` array in the correct order. Without this, we must always process nodes that have no indegree nodes to guarantee correct order.
5. Reverse the output `res` array.
    - This is needed since we append the furthest node first then closest. Hence, the reverse guarantees that the closest node would come before the furthest node so that this condition would stay true.
      - For every directed edge ( `u → v` ), vertex ( `u` ) comes before vertex ( `v` ) in the ordering.

**NOTE**: `visitedPath` array is usually used in DFS approach to detect cycle in the DAG. 
The DFS method would still work without the `visitedPath` array, but cycles must not be present else the algorithm would no work.

## Topological Sort Graph (with BFS)
Topological sorting using a **BFS** approach is often referred to as Kahn's Algorithm

```python
from collections import defaultdict, deque

def toposort(n, edges):
    graph = defaultdict(list)
    inDegree = [0] * n

    for fromNode, toNode in edges:
        graph[fromNode].append(toNode)
        inDegree[toNode] += 1

    queue = deque([node for node in range(n) if inDegree[node] == 0])
    res = []

    while queue:
        node = queue.popleft()
        res.append(node)

        for childNode in graph[node]:
            inDegree[childNode] -= 1
            if inDegree[childNode] == 0:
                queue.append(childNode)

    return res if len(res) == n else []


print(toposort(6, [(1, 2), (1, 0), (4, 0), (4, 5), (2, 3), (3, 5)]))
# [1, 4, 2, 0, 3, 5]
print(toposort(6, [(1, 2), (1, 0), (4, 0), (4, 5), (2, 3), (3, 5), (5, 1)]))
# []
```
