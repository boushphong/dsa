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


def numSimilarGroups(self, strs: List[str]) -> int:
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


def numIslands2(m: int, n: int, positions):
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
