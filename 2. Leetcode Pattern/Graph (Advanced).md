# Graph (Advanced)
# Patterns
## Union-Find
### [Similar String Groups](https://leetcode.com/problems/similar-string-groups)
```python
def numSimilarGroups(strs):
    n = len(strs)
    parent = list(range(n))

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX

    def isSimilar(str1, str2):
        count = 0
        for s1, s2 in zip(str1, str2):
            if s1 != s2:
                count += 1
                if count > 2:
                    return False
        return True
            
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            sml = isSimilar(strs[j], strs[i])
            if sml:
                union(j, i)

    ans = 0
    for idx, val in enumerate(parent):
        if idx == val:
            ans += 1

    return ans


print(numSimilarGroups(["tars", "rats", "arts", "star"]))  # 2
```

### [The Earliest Moment When Everyone Become Friends](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends)
```python
def earliestAcq(logs, n):
    logs.sort(key=lambda l: l[0])
    parent = list(range(n))
    count = n

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        nonlocal count
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX
            count -= 1

    for ts, x, y in logs:
        union(x, y)
        if count == 1:
            return ts
    return -1


print(earliestAcq(
    [[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3],
     [20190312, 1, 2], [20190322, 4, 5]], 6))  # 20190301

print(earliestAcq([[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]], 4))  # 3

print(earliestAcq([[9, 3, 0], [0, 2, 1], [8, 0, 1], [1, 3, 2], [2, 2, 0], [3, 3, 1]], 4))  # 2
```

### [Accounts Merge](https://leetcode.com/problems/accounts-merge)
```python
def accountsMerge(accounts):
    visited = {}
    parent = list(range(len(accounts)))

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)

        if rootX != rootY:
            parent[rootY] = rootX

    for i, account in enumerate(accounts):
        emails = account[1:]
        for email in emails:
            if email not in visited:
                visited[email] = i
            else:
                union(visited.get(email), i)

    tmp = defaultdict(list)
    for email, index in visited.items():
        tmp[find(index)].append(email)

    return [[accounts[idx][0]] + sorted(emails) for idx, emails in tmp.items()]


print(accountsMerge(
    [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
     ["John", "johnsmith@mail.com", "john00@mail.com"],
     ["Mary", "mary@mail.com"],
     ["John", "johnnybravo@mail.com"]]))
#
print(accountsMerge([["David", "David0@m.co", "David1@m.co"],
                     ["David", "David3@m.co", "David4@m.co"],
                     ["David", "David4@m.co", "David5@m.co"],
                     ["David", "David2@m.co", "David3@m.co"],
                     ["David", "David1@m.co", "David2@m.co"],
                     ["David", "hello@m.co"]]
                    ))
```

## Union-Find (Graph)
### [Number of Islands II](https://leetcode.com/problems/number-of-islands-ii)
```python
def numIslands2(m, n, positions):
    parent = [-1] * (m * n)
    count = 0

    def find(x):
        nonlocal count
        if parent[x] == -1:
            parent[x] = x
            count += 1
        elif parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        nonlocal count
        rootX, rootY = find(x), find(y)
        if rootX != rootY:
            parent[rootY] = rootX
            count -= 1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    result = []

    for idx, (row, col) in enumerate(positions):
        visited.add((row, col))
        current_index = row * n + col
        find(current_index)

        all_points = [(row + x, col + y) for x, y in directions if row + x not in {-1, m} and col + y not in {-1, n}]
        for nx, ny in all_points:
            neighbor_index = nx * n + ny

            if (nx, ny) in visited:
                union(current_index, neighbor_index)
        result.append(count)
        
    return result


print(numIslands2(1, 2, [[0, 1], [0, 0]]))  # [1, 1]
print(numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 2], [1, 1]]))  # [1, 1, 2, 2, 1]
```

#### Using HashMap as `Parent`
### [Making A Large Island](https://leetcode.com/problems/making-a-large-island/)
```python
def largestIsland(grid):
    n = len(grid)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    parent = {}

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                parent[(i, j)] = (i, j)

    def find(row, col):
        if (row, col) != parent.get((row, col)):
            parent[(row, col)] = find(*parent.get((row, col)))
        return parent[(row, col)]

    def union(rowX, colX, rowY, colY):
        parent[find(rowY, colY)] = find(rowX, colX)

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                for movedByRow, movedByCol in directions:
                    tmpRow, tmpCol = i + movedByRow, j + movedByCol
                    if tmpCol in {-1, n} or tmpRow in {-1, n} or not grid[tmpRow][tmpCol]:
                        continue
                    union(i, j, tmpRow, tmpCol)

    res = 0
    islandSize = defaultdict(int)
    for _, v in parent.items():
        rowKey, colKey = find(*v)
        islandSize[(rowKey, colKey)] += 1
        res = max(res, islandSize[(rowKey, colKey)])

    for i in range(n):
        for j in range(n):
            if not grid[i][j]:
                up = parent.get((i + 1, j))
                down = parent.get((i - 1, j))
                right = parent.get((i, j + 1))
                left = parent.get((i, j - 1))
                neighbors = {find(*_) for _ in [up, down, right, left] if _}
                res = max(res, sum(islandSize.get(_, 0) for _ in neighbors) + 1)

    return res


print(largestIsland([
    [0, 1, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0]
]))  # 24
```

## Topological Sort
### [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
```python
def findOrder(numCourses, prerequisites):
    if not prerequisites:
        return list(range(numCourses - 1, -1, -1))

    graph = defaultdict(list)

    for toNode, fromNode in prerequisites:
        graph[fromNode].append(toNode)

    visited = [False] * numCourses
    recStack = [False] * numCourses
    res = []

    def toposortUtil(node):
        visited[node] = True
        recStack[node] = True

        for childNode in graph.get(node, []):
            if not visited[childNode]:
                if toposortUtil(childNode):
                    return True
            elif recStack[childNode]:
                return True

        recStack[node] = False
        res.append(node)
        return False

    for curNode in graph.keys():
        if not visited[curNode]:
            if toposortUtil(curNode):
                return []

    unlistedCourse = [i for i, haveSeen in enumerate(visited) if not haveSeen]
    return unlistedCourse + res[::-1]


print(findOrder(6, [[5, 4], [1, 2], [2, 4], [2, 3], [4, 0], [3, 0], [0, 2]]))  # []
print(findOrder(6, [[5, 4], [1, 2], [2, 4], [2, 3], [4, 0], [3, 0]]))  # [0, 4, 3, 2, 1, 5]
print(findOrder(8, [[5, 4], [1, 2], [2, 4], [4, 0]]))  # [3, 6, 7, 0, 4, 2, 1, 5]
```


### [All Ancestors of a Node in a Directed Acyclic Graph](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/)
```python
def getAncestors(n, edges):
    graph = defaultdict(set)

    for fromNode, toNode in edges:
        graph[fromNode].add(toNode)

    visited = [False] * n
    stack = []

    def toposortUtil(node):
        visited[node] = True
        for childNode in graph.get(node, []):
            if not visited[childNode]:
                toposortUtil(childNode)

        stack.append(node)

    for curNode in graph.keys():
        if not visited[curNode]:
            toposortUtil(curNode)

    stack = stack[::-1]
    res = [set() for _ in range(n)]
    for i, node in enumerate(stack):
        for j in range(i - 1, -1, -1):
            if node in graph[stack[j]]:
                res[node].add(stack[j])
                res[node].update(res[stack[j]])
    return [sorted(_) for _ in res]


print(getAncestors(8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]))
# [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]
```

### [Course Schedule IV](https://leetcode.com/problems/course-schedule-iv/)
```python
def checkIfPrerequisite(numCourses, prerequisites, queries):
    graph = defaultdict(set)

    for fromNode, toNode in prerequisites:
        graph[fromNode].add(toNode)

    visited = set()
    stack = []

    def toposortUtil(node):
        visited.add(node)

        for childNode in graph.get(node, []):
            if childNode not in visited:
                toposortUtil(childNode)

        stack.append(node)

    for curNode in graph.keys():
        if curNode not in visited:
            toposortUtil(curNode)

    stack = stack[::-1]
    query = [set() for _ in range(numCourses)]
    for i, node in enumerate(stack):
        for j in range(i - 1, -1, -1):
            if node in graph[stack[j]]:
                query[node].add(stack[j])
                query[node].update(query[stack[j]])

    return [preNode in query[node] for preNode, node in queries]


print(checkIfPrerequisite(5, [[1, 0], [2, 3], [3, 4]], [[0, 1], [1, 0]]))
# [False, True]
```

## Minimum Spanning Tree
### [Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)
```python
def minimumCost(n, connections):
    parent = list(range(n))

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX

    connections.sort(key=lambda x: x[2])

    cost = edgeCnt = 0
    for fromVertex, toVertex, weight in connections:
        if find(fromVertex - 1) != find(toVertex - 1):
            union(fromVertex - 1, toVertex - 1)
            edgeCnt += 1
            cost += weight

    return cost if edgeCnt == n - 1 else -1


print(minimumCost(3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]))  # 6
print(minimumCost(4, [[1, 2, 3], [3, 4, 4]]))
```
