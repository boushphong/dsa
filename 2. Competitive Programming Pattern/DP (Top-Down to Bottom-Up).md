# Dynamic Programming
## What is Dynamic Programming?
Dynamic Programming is a technique that breaks down a large problem into smaller subproblems, solving and storing the optimal results of these subproblems to reuse in finding the optimal solution for the initial problem.

Two important properties of dynamic programming:
- **Optimal Substructure**: The optimal solution of the original problem can be constructed from the optimal solutions of its subproblems.
- **Overlapping Sub-problems**: In the process of solving the problem, some subproblems are solved multiple times.

## Fibonacci
```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
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

## Top-Down to Bottom Up Conversion Tips
Typically, the conversion starts from brute force to memoization to tabulation.
- Try to mimic tabulation array like in memoization approach, which means:
  - If memo is built from the end (last recursive call), tabulation array should also be built from the end, and vice versa

# Patterns
## K Decisions Conversion
### [Number of Dice Rolls With Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/)
Brute Force: `O(N**K)`
DP: `O(N * K * T)`

```python
def numRollsToTarget(n, k, target):
    """
    n = 3, k = 3, target = 7
    n = 1
    0 (0) cache(rollNo0, total=0) = 1 + 2 + 3 = 6
        1 (1) cache(rollNo=1, total=1) = 0 + 0 + 1 = 1
            1 (2) cache(rollNo=2, total=2) = 0
                1   2   3 (base case)
            2 (2) cache(rollNo=2, total=3) = 0
                1   2   3 (base case)
            3 (2) cache(rollNo=2, total=4) = 1
                1   2   3 (base case)
        2 (1) cache(rollNo=1, total=2) = 0 + 1 + 1 = 2
            1 (2) get from cache(rollNo=2, total=3) = 0
            2 (2) get from cache(rollNo=2, total=4) = 1
            3 (2) cache(rollNo=2, total=5) = 1
                1   2 (base case)
        3 (1) cache(rollNo=1, total=3) = 1 + 1 + 1 = 3
            1 (2) get from cache(rollNo=2, total=4) = 1
            2 (2) get from cache(rollNo=2, total=5) = 1
            3 (2) cache(rollNo=2, total=6) = 1
                1 (base case)
    """
    memo = {}

    def doRecursion(rollNo=0, total=0):
        if (rollNo, total) in memo:
            return memo[(rollNo, total)]

        if rollNo == n:
            if total == target:
                return 1
            else:
                return 0

        totalWays = 0
        for roll in range(1, k + 1):
            tmpTotal = total + roll
            ways = doRecursion(rollNo + 1, tmpTotal)
            totalWays += ways
            if tmpTotal == target:
                break

        memo[(rollNo, total)] = totalWays
        return totalWays % (10 ** 9 + 7)

    return doRecursion()


print(numRollsToTarget(3, 3, 7))
# memo = {(2, 2): 0, (2, 3): 0, (2, 4): 1, (1, 1): 1, (2, 5): 1, (1, 2): 2, (2, 6): 1, (1, 3): 3, (0, 0): 6}


def numRollsToTarget(n, k, target):
    """
    3: [0, 0, 0, 0, 0, 0, 0, 1]
    2: [0, 0, 0, 0, 1, 1, 1, 0]
    1: [0, 1, 2, 3, 2, 1, 0, 0]
    0: [6, 7, 6, 3, 1, 0, 0, 0]
    """
    dp = [0] * (target + 1)
    dp[target] = 1

    for rollNo in range(n - 1, -1, -1):
        tmpDp = [0] * (target + 1)
        for total in range(target + 1):
            totalWays = sum(dp[total + 1: total + 1 + k])
            tmpDp[total] = totalWays % (10 ** 9 + 7)
        dp = tmpDp

    return dp[0]


print(numRollsToTarget(3, 3, 7))
```

