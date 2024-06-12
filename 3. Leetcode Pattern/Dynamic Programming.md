<img width="1369" alt="image" src="https://github.com/boushphong/dsa/assets/59940078/b67dc10c-5e9a-46d4-893a-c3c974570dec"># Dynamic Programming
## What is Dynamic Programming?
Dynamic Programming is a technique that breaks down a large problem into smaller subproblems, solving and storing the optimal results of these subproblems to reuse in finding the optimal solution for the initial problem.

Two important properties of dynamic programming:
- **Optimal Substructure**: The optimal solution of the original problem can be constructed from the optimal solutions of its subproblems.
- **Overlapping Subproblems**: In the process of solving the problem, some subproblems are solved multiple times.

## Fibonacci
```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-2) + fib(n-1)
```

```python
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1)
│   │   │   └── fib(0)
│   │   └── fib(1)
│   └── fib(2)
│       ├── fib(1)
│       └── fib(0)
└── fib(3)
    ├── fib(2)
    │   ├── fib(1)
    │   └── fib(0)
    └── fib(1)
```

- **TC**: `O(2^N)`
  - Everytime we down a level, we perform `2^level` operation.
    - At level 0, we perform 2^0 = 1 operations at `fib(5)`
    - At level 1, we perform 2^1 = 2 operations at `fib(4)` and `fib(3)`
    - There are a total of `N-1` levels (1 + 2 + 4 + 8 ...) hence TC is `O(2^N)`
- **SC**: `O(N)`

## Fibonacci Dynamic Programming (Top-Down approach) Memoization
```python
memo = {}

def fib(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

```python
fib(5)
├── fib(4)
│   ├── fib(3)
│   └── fib(2)
└── fib(3)
    ├── fib(2)
    │   ├── fib(1)
    │   └── fib(0)
    └── fib(1)
```
- **TC**: `O(2*N)` > `O(N)`
- **SC**: `O(2*N)` > `O(N)`

## Fibonacci Dynamic Programming (Bottom-Up approach) Tabulation
```python
def fib(n):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```
- **TC**: `O(N)`
- **SC**: `O(N)`

```python
def fib(n):
    prev_dp, next_dp, dp = 0, 1, 0
    if n <= 1:
        return n

    for i in range(2, n + 1):
        dp = prev_dp + next_dp
        prev_dp = next_dp
        next_dp = dp

    return next_dp
```
- **TC**: `O(N)`
- **SC**: `O(1)`
