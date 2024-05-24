# Tree
A representation of a tree.
```
    0
   /|\
  1 2 3
 /    /\
4    5  6
```
- The height of a node is the length of the longest path to a descendant node of it. The height of a tree is the height of the root node.
  - Height of node `2` is 1 (No descendant)
  - Height of node `0` is 3 (`4`, `5`, `6` descendant)

- The depth of a node is the length of the unique path from the root to that node.
  - Depth of node `0` is 1
  - Depth of node `5` is 3
 
**Sample Code:**
```python
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.children = []

class Tree:
    def __init__(self, key):
        self.root = TreeNode(key)
        return self.root

root = Tree(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

root.children = [node1, node2, node3]
node1.children = [node4]
node3.children = [node5, node6]
```

# Traversal
```
    F
   / \
  B   G
 / \   \
A   D   I
   / \   \
  C   E   H
```
| Name         | Priority Order       | Technique | Example    | Applications | Note |
|--------------|----------------------|-----------|------------|--------------|------|
| Pre-Order     | Parent > Left > Right| DFS       | FBADCEGIH  | Explore parents nodes first then leaf nodes | Applicable with all Trees |
| In-Order      | Left > Parent > Right| DFS       | ABCDEFGHI  | Explore nodes in ascending order (smallest to largest) in **BST**. Parents are visited between the subtrees (starting left > parent > right) | Applicable only with Trees that have left and right node |
| Post-Order    | Left > Right > Parent| DFS       | ACEDBHIGF  | Explore leaf nodes before visiting parent nodes | Applicable with all Trees |
| Level-Order  | Top to bottom, left to right | BFS | FBGADICEH | Explore nodes at every depth first | Applicable with all Trees |

**Sample Code**

**Pre-Order Traversal**
```python
def traverse_pre_order(node):
    print(node.data)
    if node.left_node:
        self.traverse_pre_order(node.left_node)
    if node.right_node:
        self.traverse_pre_order(node.right_node)
```

**In-Order Traversal**
```python
def traverse_in_order(node):
    if node.left_node:
        self.traverse_in_order(node.left_node)
    print(node.data)
    if node.right_node:
        self.traverse_in_order(node.right_node)
```

**Post-Order Traversal**
```python
def traverse_post_order(node):
    if node.left_node:
        self.traverse_post_order(node.left_node)
    if node.right_node:
        self.traverse_post_order(node.right_node)
    print(node.data)
```

**Level-Order Traversal**
```python
from collections import deque


def traverse_level_order(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data)
        if node.left_node:
            queue.append(node.left_node)
        if node.right_node:
            queue.append(node.right_node)
```

# Patterns
## Tree Comparison
### [Symmetric Tree](https://leetcode.com/problems/symmetric-tree)
```python
def isSymmetric(root):
    def doRecursion(left=root.left, right=root.right):
        if left is None:
            return right is None
        if right is None:
            return False
        if left.val != right.val:
            return False

        res1 = doRecursion(left.left, right.right)
        res2 = doRecursion(left.right, right.left)

        return res1 and res2

    return doRecursion()
```

## Level-Order
### [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal)
```python
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def levelOrder(root):
    if not root:
        return []

    cur_depth = 0
    queue = deque([(root, cur_depth)])
    result = []
    level = []
    while queue:
        node, node_depth = queue.popleft()
        if node_depth > cur_depth:
            result.append(level.copy())
            cur_depth += 1
            level.clear()
        if node.left:
            queue.append((node.left, node_depth + 1))
        if node.right:
            queue.append((node.right, node_depth + 1))

        level.append(node.val)

    if level:
        result.append(level)

    return result

# Alternative Solution
def levelOrder(root):
    if not root:
        return []

    queue = deque([root])
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


root = TreeNode(4)
root2 = TreeNode(3)
root.left = root2

root2.left = TreeNode(9)
root2.right = TreeNode(20)

root2.left.left = TreeNode(1)
root2.left.right = TreeNode(2)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)

"""
4 pop end iteration
queue 3

3 pop end iteration
queue 9 20

9 pop 
add 1 2
20 pop
add 15 7
end iteration

queue 1 2 15 7
1 pop no children add queue
2 pop no children add queue
15 pop no children add queue
7 pop no children add queue
"""
```
- `TC`: `O(N)`
  - Iterate through every nodes
- `SC`: `O(1)` (Best Case)
  - Best case when the binary tree is degenerated
- `SC`: `O(N)` (Worst Case)
  - Best case when the binary tree is not degenerated, and well balanced
  - Since maximum space we have to store is the total of `Height + (Height - 1)` (the last depth and second last depth)
  - Hence the `SC` would be `O(2**H - 1 - 2**(H-2) - 1)`. (`O(2**H - 1)` is used to approximately calculate the total nodes in a well-balanced tree, given `H` is the height.
      - This simplifies: `2**H - 2**(H-2) - 2` -> `2**H - 2**(H-2)`
      - The upper portion `2**(H-2)` is always approximately 25% (`2**(H-2) / 2**H`) when `H` grows. Hence the `2**H - 2**(H-2)` is 75%.
        - `2**H - 2**(H-2)` -> `2**H - 2**H/2**(H-2)` -> `(1 * 2**H) - (1/4 * 2**H)` ->  `(1 - 1/4) * 2**H` -> `0.75H`
      - Since `N = 2**H - 1` -> `N = 2**H`
      - Hence `2**H - 2**(H-2)` -> `1N - 0.25N = 0.75N` -> `N`


### [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view)
```python
from collections import deque


def rightSideView(root):
    if not root:
        return []

    cur_depth = 0
    queue = deque([(root, cur_depth)])
    result = []
    level = None
    while queue:
        node, node_depth = queue.popleft()
        if node_depth == cur_depth:
            level = node.val
        elif node_depth > cur_depth:
            result.append(level)
            cur_depth += 1
            level = node.val

        if node.left:
            queue.append((node.left, node_depth + 1))
        if node.right:
            queue.append((node.right, node_depth + 1))

    result.append(level)

    return result
```

## DFS (Pre-Order)
### [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view)
```python
def levelOrder(root):
    if not root:
        return []

    ans = []

    def dfs(node=root, depth=0):
        if depth == len(ans):
            ans.append(node.val)
        else:
            ans[depth] = node.val
        if node.left:
            dfs(node.left, depth + 1)
        if node.right:
            dfs(node.right, depth + 1)

    dfs()
    return ans
```

### [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree)
```python
def diameterOfBinaryTree(root):
    if not root.left and not root.right:
        return 0

    ans = 0

    def dfs(node=root):
        nonlocal ans
        if not node.left and not node.right:
            return 1
        left_len = 0
        if node.left:
            left_len = dfs(node.left)
        right_len = 0
        if node.right:
            right_len = dfs(node.right)
        ans = max(ans, left_len + right_len)
        return max(left_len, right_len) + 1

    dfs()

    return ans
```

### [Count Univalue Subtrees](https://leetcode.com/problems/count-univalue-subtrees)
```python
def countUnivalSubtrees(root):
    ans = 0
    if not root:
        return ans

    def dfs(node=root):
        nonlocal ans
        if not node:
            return False
        if not node.right and not node.left:
            ans += 1
            return True

        left = node.left
        left_val = dfs(node.left)

        right = node.right
        right_val = dfs(node.right)

        if right_val and left_val:
            if right.val == left.val == node.val:
                ans += 1
                return True
            else:
                return False
        elif right_val and not left_val:
            if left:
                return False
            if node.val == right.val:
                ans += 1
                return True
        elif left_val and not right_val:
            if right:
                return False
            if node.val == left.val:
                ans += 1
                return True
```
