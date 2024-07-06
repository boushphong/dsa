# Graph (Advanced)
## Union-Find / Disjoint Set Union Data Structure
```python
class UnionFind:
    def __init__(self, size):
        # Initialize the parent array where each element is its own parent
        self.parent = list(range(size))

    def __repr__(self):
        return str(self.parent)

    def find(self, x):
        # Find the root of the set containing x
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        # Find the roots of the sets containing x and y
        rootX = self.find(x)
        rootY = self.find(y)
        
        # If they are in different sets, merge them by updating the parent of rootY to rootX
        if rootX != rootY:
            self.parent[rootY] = rootX

# Example usage:
uf = UnionFind(10)
# uf = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

uf.union(1, 2)
# uf = [0, 1, 1, 3, 4, 5, 6, 7, 8, 9]

uf.union(3, 4)
# uf = [0, 1, 1, 3, 3, 5, 6, 7, 8, 9]

uf.union(2, 3)
# uf = [0, 1, 1, 1, 3, 5, 6, 7, 8, 9]

print(uf.find(1))   # Output: 1
print(uf.find(4))   # Output: 1
print(uf.find(5))   # Output: 5
```


| Operation | Time Complexity | Description |
|-----------|-----------------|-------------|
| `find`    | O(n)            | In the worst case, we may need to traverse up to `n` elements to find the root. This happens when the tree is highly unbalanced. |
| `union`   | O(n)            | In the worst case, each `union` operation requires finding the roots of both elements, each of which can take up to `O(n)` time. |

### Explanation:
1. **Find Operation**:
   - In the naive implementation, the `find` operation may have to traverse up the tree from a given node to the root. If the tree is highly unbalanced (e.g., in the worst case, the tree is a straight line), this traversal can take up to `O(n)` time.

2. **Union Operation**:
   - The `union` operation first involves finding the roots of the sets containing the two elements to be united. Each `find` operation can take up to `O(n)` time in the worst case. After finding the roots, merging the sets is an `O(1)` operation. Thus, the overall complexity of `union` is dominated by the `find` operations, making it `O(n)`.

## Path Compression
```python
class UnionFind:
    def __init__(self, size):
        ...

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            x = self.parent[x]
        return x

    def union(self, x, y):
        ...

# Example usage:
uf = UnionFind(10)
uf.union(1, 2)
# uf = [0, 1, 1, 3, 4, 5, 6, 7, 8, 9]

uf.union(3, 4)
# uf = [0, 1, 1, 3, 3, 5, 6, 7, 8, 9]

uf.union(2, 3)
# uf = [0, 1, 1, 1, 3, 5, 6, 7, 8, 9]

print(uf.find(1))   # Output: 1
# uf = [0, 1, 1, 1, 3, 5, 6, 7, 8, 9]

print(uf.find(4))   # Output: 1
# uf = [0, 1, 1, 1, 1, 5, 6, 7, 8, 9]

print(uf.find(5))   # Output: 5
# uf = [0, 1, 1, 1, 1, 5, 6, 7, 8, 9]
```
