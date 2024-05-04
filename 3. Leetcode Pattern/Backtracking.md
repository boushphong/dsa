# Backtracking

**Backtracking** means when you make changes in the recursion call, you have to undo the changes that the recursion call made for the parent recursion call to continue (usually right about when the function finishes its execution).

In the Maze Problems (All directions) below, we constantly make changes to the global `maze` variable, but once a recursion call is finished, we will change the `maze` variable again to the original parent recursion call's `maze` variable state so the parent recursion call would be valid for other child recursion call.

# Patterns
## Undoing the Global Variable
### Maze Problems
```python
def getMazePathsAllDirections(n: int):
    maze = [[True] * n for _ in range(n)]
    stack = []
    res = []

    def doRecursion(row=0, col=0):
        if not maze[row][col]:
            return None

        if row == len(maze) - 1 and col == len(maze) - 1:
            return res.append("".join(stack))

        maze[row][col] = False

        if row < len(maze) - 1:
            stack.append("D")
            doRecursion(row + 1, col)
            stack.pop()

        if col < len(maze) - 1:
            stack.append("R")
            doRecursion(row, col + 1)
            stack.pop()

        if row > 0:
            stack.append("U")
            doRecursion(row - 1, col)
            stack.pop()

        if col > 0:
            stack.append("L")
            doRecursion(row, col - 1)
            stack.pop()

        maze[row][col] = True

    doRecursion()
    return res


print(getMazePathsAllDirections(3))
# ['DDRR', 'DDRURD', 'DDRUURDD', 'DRDR', 'DRRD', 'DRURDD', 'RDDR', 'RDRD', 'RDLDRR', 'RRDD', 'RRDLDR', 'RRDLLDRR']
```


### [Combination Sum](https://leetcode.com/problems/combination-sum)
```python
def combinationSum(candidates, target):
    candidates.sort()
    res = []
    stack = []

    def doRecursion(start=0, total=0):
        if total == target:
            return res.extend([stack.copy()])

        for idx in range(start, len(candidates)):
            new_total = total + candidates[idx]
            if new_total > target:
                break
            stack.append(candidates[idx])
            doRecursion(idx, total=new_total)
            stack.pop()

    doRecursion()
    return res

print(combinationSum([2, 3, 6, 7], 7))
```

## Copying the Global Variable
### [N-Queens](https://leetcode.com/problems/n-queens)
```python
def solveNQueens(n: int):
    def markSlots(r, c, board):
        board_length = len(board)

        # Mark right direction
        for col in range(c + 1, board_length):
            board[r][col] = False

        # Mark down direction
        for row in range(r + 1, board_length):
            board[row][c] = False

        # Mark left direction
        for col in range(c - 1, -1, -1):
            board[r][col] = False

        # Mark up direction
        for row in range(r - 1, -1, -1):
            board[row][c] = False

        # Mark right diagonal
        row, col = r - 1, c + 1
        while row >= 0 and col < board_length:
            board[row][col] = False
            row -= 1
            col += 1

        # Mark left diagonal
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            board[row][col] = False
            row -= 1
            col -= 1

        # Mark right-up diagonal
        row, col = r + 1, c + 1
        while row < board_length and col < board_length:
            board[row][col] = False
            row += 1
            col += 1

        # Mark left-up diagonal
        row, col = r + 1, c - 1
        while row < board_length and col >= 0:
            board[row][col] = False
            row += 1
            col -= 1

    # Start Here
    chessBoard = [[True] * n for _ in range(n)]
    res = []

    def doRecursion(row=0):
        nonlocal chessBoard
        if row == n:
            return res.extend([[''.join(['Q' if item else '.' for item in inner_list]) for inner_list in chessBoard]])

        for col in range(n):
            if chessBoard[row][col]:
                chess_board_copy = deepcopy(chessBoard)
                markSlots(row, col, chessBoard)
                doRecursion(row + 1)
                chessBoard = chess_board_copy

    doRecursion()
    return res


print(solveNQueens(4))
```
**With Carrying Argument**
```python
def solveNQueens(n: int):
    ...
    # Start here
    res = []

    def doRecursion(row=0, chessBoard=[[True] * n for _ in range(n)]):
        if row == n:
            return res.extend([[''.join(['Q' if item else '.' for item in inner_list]) for inner_list in chessBoard]])

        for col in range(n):
            if chessBoard[row][col]:
                chess_board_copy = deepcopy(chessBoard)
                markSlots(row, col, chess_board_copy)
                doRecursion(row + 1, chess_board_copy)

    doRecursion()
    return res
```

## Skipping Duplicates and Index Shifting 
### [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
```python
def combinationSum2(candidates, target):
    candidates.sort()
    res = []
    stack = []

    def doRecursion(idx=0, cur_total=0):
        if cur_total == target:
            return res.append(stack.copy())

        if idx == len(candidates) or cur_total + candidates[idx] > target:
            return

        cur = candidates[idx]
        stack.append(cur)
        doRecursion(idx + 1, cur_total + candidates[idx])
        stack.pop()

        while candidates[idx] == cur:
            idx += 1
            if idx == len(candidates):
                break

        doRecursion(idx, cur_total)

    doRecursion()
    return res


print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(combinationSum2([2, 5, 2, 1, 2], 5))
```

```python
doRecursion
├── 1
│   ├── 1
│   │   ├── 2
│   │   │   ├── 5 (PRUNE)
│   │   │   └── X (PRUNE)
│   │   └── X
│   │       ├── 5
│   │       │   ├── 6 (PRUNE)
│   │       │   └── X (PRUNE)
│   │       └── X
│   │           ├── 6 (GET)
│   │           └── X (PRUNE)
│   └── X
│       ├── 2
│       │   ├── 5 (GET)
│       │   └── X (PRUNE)
│       └── X
│           ├── 5
│           │   ├── 6 (PRUNE)
│           │   └── X (PRUNE)
│           └── X
│               ├── 6
│               │   ├── 7 (PRUNE)
│               │   └── X (PRUNE)
│               └── X
│                   ├── 7 (GET)
│                   └── X (PRUNE)
├── 1 (SKIPPED)
│
├── 2
│   ├── ...
...
```

### [Subsets II](https://leetcode.com/problems/subsets-ii/)
```python
def subsetsWithDup(nums):
    nums.sort()
    res = []
    subset = []

    def doRecursion(idx=0):
        if idx == len(nums):
            return res.append(subset.copy())

        cur = nums[idx]
        subset.append(cur)
        doRecursion(idx + 1)
        subset.pop()

        while nums[idx] == cur:
            idx += 1
            if idx == len(nums):
                break

        doRecursion(idx)

    doRecursion()
    return res


print(subsetsWithDup([1, 2, 2]))
```

```python
doRecursion
├── 1
│   ├── 2
│   │   ├── 2 (GET)
│   │   └── X (GET)
│   └── X
│       ├── 2 (SKIPPED)
│       └── X (GET)
└── X
    ├── 2
    │   ├── 2 (GET)
    │   └── X (GET)
    └── X
        ├── 2 (SKIPPED)
        └── X (GET)
```

## Early Branch Pruning (Without Pruning in the Base Case)
### [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
```python
    def is_palindrome(subset):
        return subset == subset[::-1]

    res = []
    stack = []

    def doRecursion(idx=0):
        if idx == len(s):
            return res.append(stack.copy())

        if not stack or is_palindrome(stack[-1]):
            stack.append(s[idx])
            doRecursion(idx + 1)
            stack.pop()

        if stack:
            stack[-1] += s[idx]
            if not is_palindrome(stack[-1]) and idx + 1 == len(s):
                return
            doRecursion(idx + 1)

    doRecursion()
    return res


print(partition("aba"))
print(partition("aabb"))
```

```python
doRecursion(aba)
└── "a"
    ├── "a" "a"
    │   ├── "a" "a" "b" (GET)
    │   └── "a" "ab" (PRUNE)
    └── "ab"
        ├── "ab" "a" (PRUNE)
        └── "aba" (GET)

doRecursion(aabb)
└── "a"
    ├── "a" "a"
    │   ├── "a" "a" "b"
    │   │   ├── "a" "a" "b" "b" (GET)
    │   │   └── "a" "a" "bb" (GET)
    │   └── "a" "ab" (PRUNE)
    └── "aa"
        ├── "aa" "b"
        │   ├── "aa" "b" "b" (GET)
        │   └── "aa" "bb" (GET)
        └── "aab" (PRUNE)
```
