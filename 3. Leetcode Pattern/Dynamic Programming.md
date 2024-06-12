# Dynamic Programming
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
# Top-Down approach
- Idea is to build `memo` as we get result from every recursion call. Hence later recursive calls can re-use the result from the `memo` that we have built.

## Fibonacci Dynamic Programming (Memoization)
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

# Bottom-Up approach
- Idea is to fills up the `DP table` iteratively. It starts from the smallest subproblems (which are the base cases) and uses these to solve slightly larger subproblems.
- Each entry in the `DP table/array` is filled based on the previously computed values, ensuring that all the necessary information to solve a subproblem is already computed and stored.

## Fibonacci Dynamic Programming (Tabulation)
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

## Top-Down DP vs Bottom-Up DP
- Bottom-up DP usually performs better than Top-down DP because:
  - It uses an array to cache memoization table or hash table (if Top-down DP also uses array, then this point is negated).
  - It avoids the memory overhead of the recursion stack (recursion depth * stack frame size) and prevents `RecursionError: maximum recursion depth exceeded` (which can be fixed by increasing the recursion limit, Python default is 1000).
  - Using Bottom-up DP can help optimize space complexity.
- Top-down DP is only faster in scenarios where only a part of the subproblems need to be solved, and there is no need to solve all subproblems as in Bottom-up DP. For example, see: [https://www.spoj.com/problems/COINS/](https://www.spoj.com/problems/COINS/), where n <= 10^9.
- Top-down solutions are easier to set up initially and focus on building sub-problems as needed, without being limited by array indices (as they can dynamically handle numbers >= the size of the array).

# Patterns
## Top-Down DP
### [Decode Ways](https://leetcode.com/problems/decode-ways)
```python
def numDecodings(s):
    n = len(s)
    memo = {n: 1}

    def dp(i):
        if i in memo:
            return memo[i]

        ans = 0
        if s[i] != '0':
            ans += dp(i + 1)
        else:
            return ans

        if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
            ans += dp(i + 2)

        memo[i] = ans
        return ans

    res = dp(0)
    return res


print(numDecodings("10211"))
print(numDecodings("1121"))
```

```python
Example: 10211

i = 0 (1)                                       (Step 8)
    i = 1 (0) > invalid > return 0              (Step 1)

    i = 2 (2) > 3 > cache 2: 3                  (Step 7)
        i = 3 (1) > 2 cache 3: 2                (Step 5)
            i = 4 (1) > 1 cache 4: 1            (Step 3)
                i = 5 > (None) > return 1       (Step 2)
            i = 5 > (None) > return 1           (Step 4)
        i = 4 (1) > 1 > get from memo           (Step 6)

i = 0 (1) = 0 + 3 = 3

Example: 1121

i = 0 (1)                                       (Step 8)
    i = 1 (1) > 3 > cache 1: 3                  (Step 6)
        i = 2 (2) > 2 > cache 2: 2              (Step 4)
            i = 3 (1) > 1 > cache 3: 1          (Step 2)
                i = 4 > (None) > return 1       (Step 1)
            i = 4 > (None) > 1 > get from memo  (Step 3)
        i = 3 (1) > 1 > get from memo           (Step 5)
    i = 2 (2) > 2 > get from memo               (Step 7)

i = 0 (1) = 3 + 2 = 5
```
