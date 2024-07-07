# Graph (Advanced)
# Patterns
## Union-Find
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
```

### [Similar String Groups](https://leetcode.com/problems/similar-string-groups)
```python
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

