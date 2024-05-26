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

## BFS
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

### [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
```python
def zigzagLevelOrder(root):
    if not root:
        return []

    reverse = True
    queue = deque([root])
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            if reverse:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                node = queue.pop()
                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)
            
            level.append(node.val)

        reverse = not reverse
        result.append(level)
    return result
```
### [Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees)
```python
def numOfMinutes(n, headID, manager, informTime):
    """
    n = 6, headID = 2, 
    manager = [2,2,-1,2,2,3], 
    informTime = [0,0,1,4,0,0]
    buckets = [[], [], [0,1,3,4],[5], [], []]
    
    queue[(2, 0)] pop
    add
    queue[(0, 0 + 1)]
    queue[(1, 0 + 1)]
    queue[(3, 0 + 1)]
    queue[(4, 0 + 1)]

    queue[(0, 0 + 1)] pop
    add [] None hence calculate max time max(0, 0 + 1)

    queue[(1, 0 + 1)] pop
    add [] None hence calculate max time max(0, 0 + 1)

    queue[(3, 0 + 1)] pop
    add [5] 

    queue becomes
    queue[(4, 0 + 1)]
    queue[(5, 1 + 4)]
    ...
    Update max inform time when the len(subordinate list) of a manager is None

    """
    buckets = [[] for _ in range(n)]

    for i, man in enumerate(manager):
        if man == -1:
            continue
        buckets[man].append(i)

    ans = 0

    queue = deque([(headID, 0)])

    while queue:
        sub, cur_time = queue.popleft()
        sub_list = buckets[sub]
        if not sub_list:
            ans = max(ans, cur_time)

        for man in sub_list:
            queue.append((man, cur_time + informTime[sub]))

    return ans

print(numOfMinutes(n=6, headID=2, manager=[2, 2, -1, 2, 2, 3], informTime=[0, 0, 1, 4, 0, 0]))
```


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

## DFS
### [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view)
All DFS techniques would technically work, but we are using pre-order in this case because the len of `ans` is used at each recursive call so that if a new depth is discovered, we want to add an element to the `ans` list immediately after seeing a new depth. And when if that depth is already discovered, we can modify the `ans` result.
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

### [Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees)
```python
def numOfMinutes(n, headID, manager, informTime):
    buckets = [[] for i in range(n)]

    for i, man in enumerate(manager):
        if man == -1:
            continue
        buckets[man].append(i)

    ans = 0

    def doRecursion(root=headID, inform=informTime[headID]):
        nonlocal ans
        if len(buckets[root]) == 0:
            ans = max(inform, ans)
            return inform

        for man in buckets[root]:
            sub_inform = informTime[man]
            doRecursion(man, inform + sub_inform)

        return ans

    return doRecursion()

print(numOfMinutes(n=6, headID=2, manager=[2, 2, -1, 2, 2, 3], informTime=[0, 0, 1, 4, 0, 0]))
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

    dfs()
    return ans
```

### [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree)
Find P or Q node first, then immediately return, then we check the other side of the subtree, if P or Q is found there, we carry the return result. If P or Q is not found in the other subtree, then either P or Q is already the lower common ancestor. 
```python
def lowestCommonAncestor(root, p, q):
    def dfs(node):
        if node.val == p.val:
            return p
        elif node.val == q.val:
            return q

        left = None
        if node.left:
            left = dfs(node.left)

        right = None
        if node.right:
            right = dfs(node.right)

        if left and right:
            return node

        return left or right

    node = dfs(root)
    return node

```

### [Find Leaves of Binary Tree](https://leetcode.com/problems/find-leaves-of-binary-tree)
```python
def findLeaves(root):
    res = [[]]

    def dfs(node=root):
        if not node.left and not node.right:
            res[0].append(node.val)
            return 1

        left_level = 0
        if node.left:
            left_level += dfs(node.left)

        right_level = 0
        if node.right:
            right_level += dfs(node.right)

        cur_level = max(left_level, right_level)
        if len(res) < cur_level + 1:
            res.append([])

        # node.left, node.right = None, None (Only if being asked to actually remove the node one by one)
        res[cur_level].append(node.val)
        return cur_level + 1

    dfs()
    # root = None (Only if being asked to actually remove the node one by one)
    return res
```

## Binary Search Tree (BST)
### [Path Sum](https://leetcode.com/problems/path-sum/)
```python
def hasPathSum(root, targetSum):
    if not root:
        return 0
    def dfs(node=root, total=root.val):
        if not node.left and not node.right:
            if total == targetSum:
                return True
            else:
                return False

        left = False
        if node.left:
            left = dfs(node.left, total + node.left.val)

        right = False
        if node.right:
            right = dfs(node.right, total + node.right.val)

        return left or right

    return dfs()
```

### [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
**Bottom Up Approach**
```python
def isValidBST(root):
    ans = True

    def dfs(node):
        nonlocal ans
        if not node.left and not node.right:
            return node.val, node.val

        left_min, left_max = float('inf'), float('-inf')
        if node.left:
            left_min, left_max = dfs(node.left)
            if left_max >= node.val:
                ans = False

        right_min, right_max = float('inf'), float('-inf')
        if node.right:
            right_min, right_max = dfs(node.right)
            if right_min <= node.val:
                ans = False

        min_val = min(left_min, node.val)
        max_val = max(right_max, node.val)

        return min_val, max_val

    dfs(root)
    return ans

"""
     55
   /    \
  36     44
 / \    /
33  39 40
"""
root = TreeNode(55)
root.left = TreeNode(36)
root.right = TreeNode(44)
root.left.left = TreeNode(33)
root.left.right = TreeNode(39)
root.right.left = TreeNode(40)

print(isValidBST(root))
```

**Top Down Approach**
```python
def isValidBST(root):
    def dfs(node, lower, upper):
        if not node:
            return True

        if node.val <= lower or node.val >= upper:
            return False

        left_val = dfs(node.left, lower, node.val)
        if not left_val:
            return False

        right_val = dfs(node.right, node.val, upper)
        if not right_val:
            return False

        return True

    return dfs(root, float("-inf"), float("inf"))

"""
     10
    /  \
   5    20
       /   \
     15     30
    /  \    / \
  12   18  25 35
 / \   / \
11 13 17 19
"""
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(30)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(18)
root.right.right.left = TreeNode(25)
root.right.right.right = TreeNode(35)
root.right.left.left.left = TreeNode(11)
root.right.left.left.right = TreeNode(13)
root.right.left.right.left = TreeNode(17)
root.right.left.right.right = TreeNode(19)

print(isValidBST(root))
```
