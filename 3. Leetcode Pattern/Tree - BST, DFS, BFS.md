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
| Inorder      | Left > Parent > Right| DFS       | ABCDEFGHI  |
| Preorder     | Parent > Left > Right| DFS       | FBADCEGIH  |
| Postorder    | Left > Right > Parent| DFS       | ACEDBHIGF  |
| Level-order  | Top to bottom, left to right | BFS | FBGADICEH |
