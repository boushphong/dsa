# Graph (Advanced)
# Patterns
## Union-Find
### [Similar String Groups](https://leetcode.com/problems/similar-string-groups)
```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        stack = []
        while self.parent[x] != x:
            stack.append(x)
            x = self.parent[x]

        for idx in stack:
            self.parent[idx] = x

        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parent[rootY] = rootX


def numSimilarGroups(strs):
    n = len(strs)
    uf = UnionFind(n)

    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            sml = self.isSimilar(strs[j], strs[i])
            if sml:
                uf.union(j, i)

    ans = 0
    for idx, val in enumerate(uf.parent):
        if idx == val:
            ans += 1

    return ans

def isSimilar(str1, str2):
    count = 0
    for s1, s2 in zip(str1, str2):
        if s1 != s2:
            count += 1
            if count > 2:
                return False
    return True


print(numSimilarGroups(["tars", "rats", "arts", "star"]))  # 2
```

### [The Earliest Moment When Everyone Become Friends](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends)
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        stack = []
        while self.parent[x] != x:
            stack.append(x)
            x = self.parent[x]

        for idx in stack:
            self.parent[idx] = x

        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parent[rootY] = rootX
            self.count -= 1

    def get_count(self):
        return self.count


def earliestAcq(logs, n):
    logs.sort(key=lambda l: l[0])
    uf = UnionFind(n)
    for ts, x, y in logs:
        uf.union(x, y)
        count = uf.get_count()
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
import collections


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def __repr__(self):
        return str(self.parent)

    def find(self, x):
        stack = []
        while self.parent[x] != x:
            stack.append(x)
            x = self.parent[x]

        for idx in stack:
            self.parent[idx] = x

        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parent[rootY] = rootX


def accountsMerge(accounts):
    uf = UnionFind(len(accounts))
    visited = {}

    for i, account in enumerate(accounts):
        emails = account[1:]
        for email in emails:
            if email not in visited:
                visited[email] = i
            else:
                uf.union(visited.get(email), i)

    tmp = collections.defaultdict(list)
    for email, index in visited.items():
        tmp[uf.find(index)].append(email)

    ans = [[accounts[idx][0]] + sorted(emails) for idx, emails in tmp.items()]

    return ans


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
class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.count = 0

    def find(self, x):
        if self.parent[x] == -1:
            self.parent[x] = x
            self.count += 1
        elif self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parent[rootY] = rootX
            self.count -= 1

    def get_count(self):
        return self.count


def numIslands2(m, n, positions):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    uf = UnionFind(m * n)
    result = []

    for idx, (row, col) in enumerate(positions):
        visited.add((row, col))
        current_index = row * n + col
        uf.find(current_index)

        all_points = [(row + x, col + y) for x, y in directions if row + x not in {-1, m} and col + y not in {-1, n}]
        for nx, ny in all_points:
            neighbor_index = nx * n + ny

            if (nx, ny) in visited:
                uf.union(current_index, neighbor_index)

        result.append(uf.get_count())

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
            row, col = parent[(row, col)]
        return row, col

    def union(rowX, colX, rowY, colY):
        rootX = find(rowX, colX)
        rootY = find(rowY, colY)
        if rootX != rootY:
            parent[rootY] = rootX

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
from collections import defaultdict


def findOrder(numCourses, prerequisites):
    if not prerequisites:
        return list(range(numCourses - 1, -1, -1))

    ans = []
    graph = defaultdict(list)
    visited = set()

    truth = [False] * numCourses

    for a, b in prerequisites:
        graph[a].append(b)

    def dfs(v):
        if v in visited and truth[v]:
            return False
        if v in visited:
            return True

        visited.add(v)
        if truth[v]:
            return False
        truth[v] = True

        noCycle = True
        for adj in graph.get(v, []):
            noCycle = noCycle and dfs(adj)

        truth[v] = False
        ans.append(v)

        return noCycle

    for i in range(numCourses):
        if i not in graph:
            continue
        if i not in visited:
            if not dfs(i):
                return []

    tmp = [i for i in range(numCourses) if i not in visited]
    return tmp + ans


print(findOrder(6, [[5, 4], [1, 2], [2, 4], [2, 3], [4, 0], [3, 0], [0, 2]]))  # []
print(findOrder(6, [[5, 4], [1, 2], [2, 4], [2, 3], [4, 0], [3, 0]]))  # [0, 4, 3, 2, 1, 5]
print(findOrder(8, [[5, 4], [1, 2], [2, 4], [4, 0]]))  # [3, 6, 7, 0, 4, 2, 1, 5]
```