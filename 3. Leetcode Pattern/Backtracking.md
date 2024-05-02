# Backtracking

**Backtracking** means when you make changes in the recursion call, you have to undo the changes that the recursion call made for the parent recursion call to continue (usually right about when the function finishes its execution).

In the Maze Problems (All directions) below, we constantly make changes to the global `maze` variable, but once a recursion call is finished, we will change the `maze` variable again to the original parent recursion call's `maze` variable state so the parent recursion call would be valid for other child recursion call.

## Backtracking the Maze Problems (All directions)
```python
def getMazePathsAllDirections(r, c, p=''):
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        return [p]

    if not maze[r][c]:
        return None

    maze[r][c] = False
    path = []

    if r < len(maze) - 1:
        down = getMazePathsAllDirections(r + 1, c, p + 'D')
        path.extend(down) if down else None

    if c < len(maze[0]) - 1:
        right = getMazePathsAllDirections(r, c + 1, p + 'R')
        path.extend(right) if right else None

    if r > 0:
        up = getMazePathsAllDirections(r - 1, c, p + 'U')
        path.extend(up) if up else None

    if c > 0:
        left = getMazePathsAllDirections(r, c - 1, p + 'L')
        path.extend(left) if left else None

    maze[r][c] = True

    return path


# Example usage:
maze = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]

print(getMazePathsAllDirections(0, 0))
# ['DDRR', 'DDRURD', 'DDRUURDD', 'DRDR', 'DRRD', 'DRURDD', 'RDDR', 'RDRD', 'RDLDRR', 'RRDD', 'RRDLDR', 'RRDLLDRR']

```
