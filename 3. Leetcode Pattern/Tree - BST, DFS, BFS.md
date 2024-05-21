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
| Name         | Priority Order       | Technique | Example    |
|--------------|----------------------|-----------|------------|
| In-Order      | Left > Parent > Right| DFS       | ABCDEFGHI  |
| Pre-Order     | Parent > Left > Right| DFS       | FBADCEGIH  |
| Post-Order    | Left > Right > Parent| DFS       | ACEDBHIGF  |
| Level-Order  | Top to bottom, left to right | BFS | FBGADICEH |

**Sample Code**

**In-Order Traversal**
```python
def traverse_in_order(node):
    if node.left_node:
        self.traverse_in_order(node.left_node)
    print(node.data)
    if node.right_node:
        self.traverse_in_order(node.right_node)
```

**Pre-Order Traversal**
```python
def traverse_pre_order(node):
    print(node.data)
    if node.left_node:
        self.traverse_pre_order(node.left_node)
    if node.right_node:
        self.traverse_pre_order(node.right_node)
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
