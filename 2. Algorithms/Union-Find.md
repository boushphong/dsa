# Union Find
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
| `find`    | O(n)            | In the worst case (of a single `find` operation), we may need to traverse up to `n` elements to find the root. This happens when the tree is degenerated (highly unbalanced). |
| `union`   | O(n)            | In the worst case (of a single `union` operation), each `union` operation requires finding the roots of both elements, each of which can take up to `O(n)` time. |

### Explanation:
1. **Find Operation**:
   - In the naive implementation, the `find` operation may have to traverse up the tree from a given node to the root. If the tree is highly unbalanced (e.g., in the worst case, the tree is a straight line), this traversal can take up to `O(n)` time.

2. **Union Operation**:
   - The `union` operation first involves finding the roots of the sets containing the two elements to be united. Each `find` operation can take up to `O(n)` time in the worst case. After finding the roots, merging the sets is an `O(1)` operation. Thus, the overall complexity of `union` is dominated by the `find` operations, making it `O(n)`.

## Optimizations
### Path Compression
```python
class UnionFind:
    ...

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            x = self.parent[x]
        return x
    ...
```

Doing it iteratively
```python
class UnionFind:
    ...

    def find(self, x):
        stack = []
        while self.parent[x] != x:
            stack.append(x)
            x = self.parent[x]

        for idx in stack:
            self.parent[idx] = x

        return x
    ...
```

```python
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

```python
"""
Let the subset {0, 1, .. 9} be represented as below and find() is called for element 3.
           --9--
         /   |   \  
        4    5    6
       /         /  \
      0         7    8
     /        
    3
   / \         
  1   2
"""

"""
When find() is called for 3, we traverse up and find 9 as representative
of this subset. With path compression, we also make 3 and 0 as the child of 9 so 
that when find() is called next time for 0, 1, 2 or 3, the path to root is reduced.

        --------9-------
      /   /    /  \      \
     0   4    5    6       3 
                  /  \    /  \
                 7    8   1   2
"""
```

**Worst Case**
```python
uf = UnionFind(8)
uf.union(0, 1)
uf.union(2, 3)
uf.union(4, 5)
uf.union(6, 7)  # [0, 0, 2, 2, 4, 4, 6, 6]
uf.union(0, 4)  # [0, 0, 2, 2, 0, 4, 6, 6]
"""
0
├── 1
└── 4
    └── 5
2
└── 3
6
└── 7
"""

uf.union(2, 6)  # [0, 0, 2, 2, 0, 4, 2, 6]
"""
0
├── 1
└── 4
    └── 5
2
├── 3
└── 6
    └── 7
"""

uf.find(7)
# This will take O(LogN) = O(Log8) = 3 operations (iterate from element 7 to 6 to 3)

uf.union(5, 7)
# Same Idea
```

| Operation | Time Complexity | Description |
|-----------|-----------------|-------------|
| `find`    | O(LogN)            | In the worst case (of a single `find` operation), we may need to traverse up to `LogN` elements to find the root. This happens when there are 2 trees, each with a depth of 3 |
| `union`   | O(LogN)            | In the worst case (of a single `union` operation), each `union` operation requires finding the roots of both elements, each of which can take up to `O(LogN)` time. |

### Union By Rank (with Path Compression)
**Worst Case: Before Union By Rank Optimization**
```python
uf = UnionFind(8)
uf.union(0, 1)
uf.union(2, 3)
uf.union(4, 5)
uf.union(6, 7)  # [0, 0, 2, 2, 4, 4, 6, 6]
uf.union(2, 0)  # [2, 0, 2, 2, 0, 4, 6, 6]

"""
2
├── 0
|   └── 4
|       └── 5  (Maximum Depth is 4) (Unbalanced)
└── 3
    └── 5 
6
└── 7
"""
```



**After Union-By-Rank Optimization**

```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        ...

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


# Example usage:
uf = UnionFind(8)
uf.union(0, 1)
uf.union(2, 3)
uf.union(4, 5)
uf.union(6, 7)  # [0, 0, 2, 2, 4, 4, 6, 6]
uf.union(2, 0)  # [0, 0, 0, 2, 0, 4, 6, 6]

"""
0
├── 1
├── 2
|   └── 3 (Maximum Depth is 3) (Balanced)
└── 4
    └── 5 (Maximum Depth is 3) (Balanced)
6
└── 7
"""
```

| Operation | Time Complexity | Description |
|-----------|-----------------|-------------|
| `find`    | O(LogN)            | In the worst case (of a single `find` operation), we may need to traverse up to `LogN` elements to find the root. This happens when there are 2 trees, each with a depth of 3 |
| `union`   | O(LogN)            | In the worst case (of a single `union` operation), each `union` operation requires finding the roots of both elements, each of which can take up to `O(LogN)` time. |

### Amortized Complexity Analysis of Both Optizations

| Operation | Time Complexity    | Description |
|-----------|--------------------|-------------|
| `find`    | O(α(n))            | The amortized time complexity is nearly constant due to path compression, making future `find` operations more efficient. |
| `union`   | O(α(n))            | The amortized time complexity is nearly constant due to union by rank and path compression, ensuring the tree remains shallow. |

- **Amortized Complexity:** It is the average time taken per operation, over a sequence of operations. It accounts for the fact that while some operations may be expensive (take a long time), they make subsequent operations cheaper. Thus, when we average out the time taken over a large number of operations, the cost per operation appears lower.

- **Sequence of Operations:** This typically involves considering the performance of the algorithm over multiple operations (e.g., multiple find and union operations in the Union-Find algorithm).

### Applications of Union-Find
- Check if an undirected graph has a cycle.
- Find the minimum spanning tree (Kruskal's algorithm).
