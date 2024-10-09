# Dynamic Programming
# Table of Contents
* [Patterns](#patterns)
   * [Fibonacci Style (1D)](#fibonacci-style-1d)
   * [Fibonacci Style (2D)](#fibonacci-style-2d)
   * [Linear Sequences with Constant Transition (1D)](#linear-sequences-with-constant-transition-1d)
   * [Linear Sequences with non-constant Transition](#linear-sequences-with-non-constant-transition)
   * [Matrix (Grid) Pattern](#matrix-grid-pattern)

# Patterns
## Fibonacci Style (1D)
Result of `N` is equal to `N - 1 + N - 2`
### [Climbing Stairs](https://leetcode.com/problems/climbing-stairs)
**Top-Down**
```python
def climbStairs(n):
    memo = {}

    def doRecursion(step=0):
        if step > n:
            return 0
        if step == n:
            return 1
        if step in memo:
            return memo[step]

        climbSingleStep = doRecursion(step + 1)
        climbDoubleStep = doRecursion(step + 2)

        memo[step] = climbSingleStep + climbDoubleStep
        return memo[step]

    return doRecursion(0)


print(climbStairs(5))  # 8
```

**Bottom-Up**
```python
def climbStairs(n):
    step1, step2, step = 0, 1, 0
    for i in range(n):
        step = step1 + step2
        step1 = step2
        step2 = step

    return step
```

## Fibonacci Style (2D)
### [Target Sum](https://leetcode.com/problems/target-sum/)
**Top-Down**
```python
def findTargetSumWays(nums, target):
    n = len(nums)
    memo = {}

    def dp(i=0, total=0):
        if (i, total) in memo:
            return memo[(i, total)]
        if i == n:
            if total == target:
                return 1
            else:
                return 0

        plus = total + nums[i]
        plusWays = dp(i + 1, plus)

        minus = total - nums[i]
        minusWays = dp(i + 1, minus)

        memo[(i, total)] = plusWays + minusWays
        return plusWays + minusWays

    return dp()


print(findTargetSumWays([1, 1, 1, 1, 1], 3))  # 5
```

Explanation
- The state variables are the current index and the current total sum at that index.
  - At every state, we memoize how many different valid paths that sums up to the target.
    - For example, at state `dp(2, 0)`, there is only one valid path, hence we cache `1` for this state.
    - Later down the recursive call, we encounter this state again inside `dp(1, -1)`, which calls onto `dp(2, 0)`, hence we could just get the result from the cache. 
  - Therefore, at later recursive calls, if we encounter a pre-computed state's result, we can get the result from the cache.
```python
findTargetSumWays([1, 1, 1, 1, 1], 3)
  └─ dp(0, 0) (cache ways=5)
       ├─ dp(1, 1) (cache ways=4)
       │    ├─ dp(2, 2) (cache ways=3)
       │    │    ├─ dp(3, 3) (cache ways=2)
       │    │    │    ├─ dp(4, 4) (cache ways=1)
       │    │    │    │    └─ dp(5, 3) (valid path)
       │    │    │    └─ dp(4, 2) (cache ways=1)
       │    │    │         └─ dp(5, 3) (valid path)
       │    │    └─ dp(3, 1) (cache ways=1)
       │    │         └─ dp(4, 2) (get from cache ways=1)
       │    └─ dp(2, 0) (cache ways=1)
       │         └─ dp(3, 1) (get from cache ways=1)
       └─ dp(1, -1) (cache ways=1)
            └─ dp(2, 0) (get from cache ways=1)
```

**Bottom-Up**
```python
def findTargetSumWays(nums, target):
    totalSum = sum(nums)
    if abs(target) > totalSum:
        return 0

    dp = [0] * (2 * totalSum + 1)
    dp[totalSum] = 1

    for num in nums:
        tmpDp = [0] * (2 * totalSum + 1)
        for s in range(-totalSum, totalSum + 1):
            if dp[s + totalSum] > 0:
                tmpDp[s + num + totalSum] += dp[s + totalSum]
                tmpDp[s - num + totalSum] += dp[s + totalSum]
        dp = tmpDp

    return dp[target + totalSum]


print(findTargetSumWays([1, 1, 3, 1, 1], 3))  # 6
"""
0: [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
1: [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
1: [0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0]
3: [0, 0, 1, 0, 2, 0, 1, 0, 1, 0, 2, 0, 1, 0, 0]
1: [0, 1, 0, 3, 0, 3, 0, 2, 0, 3, 0, 3, 0, 1, 0]
1: [1, 0, 4, 0, 6, 0, 5, 0, 5, 0, 6, 0, 4, 0, 1]
6
"""
```



## Linear Sequences with Constant Transition (1D)
Requires us to solve the sub-problem on every prefix (or suffix) of the array. 
- The definition of a prefix of an array is a subarray from `0` to `i` for some `i`.
- The definition of a suffix of an array is a subarray from `i` to `n - 1` for some `i`. (`n` is the length of the array)

### [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)
**Top-Down:** Solving Suffix 
```python
def minCostClimbingStairs(cost):
    memo = {}

    def doRecursion(step):
        if step in memo:
            return memo[step]
        if step > len(cost) - 1:
            return 0

        climbSingleStep = cost[step] + doRecursion(step + 1)
        climbDoubleStep = cost[step] + doRecursion(step + 2)

        memo[step] = min(climbSingleStep, climbDoubleStep)
        return memo[step]

    startAt0 = doRecursion(0)
    startAt1 = doRecursion(1)
    return min(startAt1, startAt0)


print(minCostClimbingStairs([10, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 15
```

**Bottom-Up**: Solving Prefix
```python
def minCostClimbingStairs(cost):
    first = cost[0]
    second = cost[1]
    for c in cost[2:]:
        curCost = min(c + first, c + second)
        first = second
        second = curCost
    return min(first, second)
```


### [Decode Ways](https://leetcode.com/problems/decode-ways)
**Top-Down**
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
"""
i = 0 (1)                                       (Step 8)
    i = 1 (0) > invalid > return 0              (Step 1)

    i = 2 (2) > 3 > cache 2: 3                  (Step 7)
        i = 3 (1) > 2 > cache 3: 2              (Step 5)
            i = 4 (1) > 1 > cache 4: 1          (Step 3)
                i = 5 > (None) > return 1       (Step 2)
            i = 5 > (None) > return 1           (Step 4)
        i = 4 (1) > 1 > get from memo           (Step 6)

i = 0 (1) = 0 + 3 = 3
"""

print(numDecodings("1121"))
"""
i = 0 (1)                                       (Step 8)
    i = 1 (1) > 3 > cache 1: 3                  (Step 6)
        i = 2 (2) > 2 > cache 2: 2              (Step 4)
            i = 3 (1) > 1 > cache 3: 1          (Step 2)
                i = 4 > (None) > return 1       (Step 1)
            i = 4 > (None) > 1 > get from memo  (Step 3)
        i = 3 (1) > 1 > get from memo           (Step 5)
    i = 2 (2) > 2 > get from memo               (Step 7)

i = 0 (1) = 3 + 2 = 5
"""
```

**Bottom-Up**
```python
def numDecodings(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 1
    for i in range(n - 1, -1, -1):
        if s[i] != '0':
            dp[i] += dp[i+1]

        if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
            dp[i] += dp[i+2]

    return dp[0]
```

```python
def numDecodings(s):
    n = len(s)
    dp = [0, 1, 0]
    for i in range(n - 1, -1, -1):
        if s[i] != '0':
            dp[0] += dp[1]

        if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
            dp[0] += dp[2]

        dp[2] = dp[1]
        dp[1] = dp[0]
        dp[0] = 0
    return dp[1]


print(numDecodings("1121"))
"""
3 [0, 1, 1]
2 [0, 2, 1]
1 [0, 3, 2]
0 [0, 5, 3]

Possible combinations
1 1 2 1
1 12 1
1 1 21
11 2 1
11 21
"""
```


## Linear Sequences with non-constant Transition
Requires us to solve the sub-problem on every prefix (or suffix) of the array. However, transitions may not be simple and require a linear amount of options from indices `j < i` (or `j > i`).

### [Largest Sum of Averages](https://leetcode.com/problems/largest-sum-of-averages)
```python
def largestSumOfAverages(nums, k):
    n = len(nums)
    dp = [0] * (n + 1)
    sums = [0] * (n + 1)

    for i in range(1, n + 1):
        sums[i] = sums[i - 1] + nums[i - 1]
        dp[i] = sums[i] / i

    for atK in range(2, k + 1):
        new_dp = [0] * (n + 1)
        for i in range(atK, n + 1):
            for j in range(atK - 1, i):
                new_dp[i] = max(new_dp[i], dp[j] + (sums[i] - sums[j]) / (i - j))
        dp = new_dp

    return dp[n]


print(largestSumOfAverages([9, 1, 2, 3, 9], 3))  # 20.0
```

Explanation
|   k\i   |   9   |   1   |   2   |   3   |   9   |
|:-------:|:-----:|:-----:|:-----:|:-----:|:-----:|
|   k=1   |   9   |   5   |   4   |  3.75 |  4.8  |
|   k=2   |   -   |  9+1  | 9+1.5 | 9+2   | 9+3.75|
|         |       |       | 5+2   | 5+2.5 | 5+4.67|
|         |       |       |       | 4+3   | 4+6   |
|         |       |       |       |       | 3.75+9|
|   k=3   |   -   |   -   | 10+2  | 10+2.5| 10+4.67|
|         |       |       |       | 10.5+3| 10.5+6|
|         |       |       |       |       | 11+9  |

#### Longest Increasing Subsequence Variation
### [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
**Top-Down**
```python
def lengthOfLIS(nums):
    n, ans = len(nums), 0

    @cache
    def dp(start=0):
        nonlocal ans

        longest = 0
        for idx in range(start + 1, n):
            tmpLongest = dp(idx)
            if nums[start] < nums[idx]:
                longest = max(longest, tmpLongest)

        ans = max(ans, longest + 1)
        return longest + 1

    dp()
    return ans
```

**Bottom-Up**
```python
def lengthOfLIS(nums):
    dp = [1] * len(nums)
    
    for i, num in enumerate(nums):
        maximum_LIS = dp[i]
        for j in range(i - 1, -1, -1):
            if num > nums[j]:
                maximum_LIS = max(maximum_LIS, dp[j] + dp[i])
        dp[i] = maximum_LIS
    
    return max(dp)


print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
"""
0: [1, 1, 1, 1, 1, 1, 1, 1]
1: [1, 1, 1, 1, 1, 1, 1, 1]
2: [1, 1, 1, 1, 1, 1, 1, 1]
3: [1, 1, 1, 2, 1, 1, 1, 1]
4: [1, 1, 1, 2, 2, 1, 1, 1]
5: [1, 1, 1, 2, 2, 3, 1, 1]
6: [1, 1, 1, 2, 2, 3, 4, 1]
7: [1, 1, 1, 2, 2, 3, 4, 4]
"""
```

### [Longest Arithmetic Subsequence](https://leetcode.com/problems/longest-arithmetic-subsequence)
```python
def longestArithSeqLength(nums):
    dp = {}

    for i in range(len(nums)):
        for j in range(i - 1, -1, -1):
            diff = nums[i] - nums[j]
            dp[(i, diff)] = max(dp.get((i, diff), 0), dp.get((j, diff), 1) + 1)
            # max to handle multiple identical (i, diff) when there are multiple identical nums[j]

    return max(dp.values())


print(longestArithSeqLength([2, 1, 2, 3]))  # 3
```

### [Minimum Number of Coins for Fruits](https://leetcode.com/problems/minimum-number-of-coins-for-fruits)
```python
def minimumCoins(prices):
    n = len(prices)
    endIdx = (n // 2) - 1
    endIdx -= 1 if n % 2 == 0 else 0

    for i in range(endIdx, -1, -1):
        maxReachable = (i + 1) * 2
        prices[i] = prices[i] + min(prices[i + 1:maxReachable + 1])

    return prices[0]


print(minimumCoins([1, 10, 100, 1, 50]))  # 12
```

### [Count Number of Teams](https://leetcode.com/problems/count-number-of-teams)
**Top-Down**
```python
def numTeams(rating):
    stack = []
    memo = {}
    ans = []

    def doRecursion(start):
        if len(stack) == 3:
            ans.append(stack.copy())
            return 1

        if (start, len(stack)) in memo:
            return memo[(start, len(stack))]

        total = 0
        for i in range(start, len(rating)):
            cur_num = rating[i]

            if stack and cur_num < stack[-1]:
                continue

            stack.append(cur_num)
            total += doRecursion(i + 1)
            stack.pop()

        memo[(start, len(stack))] = total
        return total

    final_1 = doRecursion(0)
    stack.clear()
    memo.clear()
    rating = list(reversed(rating))
    final_2 = doRecursion(0)
    return final_1 + final_2


print(numTeams([2, 5, 3, 4, 1, 6]))
"""
2   5   3   4   1   6
2
    5
        3 SKIP
        4 SKIP
        1 SKIP
        6 take (CACHE) 1
    3 CACHE(2)
        4 take (CACHE) 1
        1 SKIP
        6 take (CACHE) 1
    4 GET FROM CACHE
    1 SKIP
5
    3 SKIP
    4 SKIP
    1 SKIP
3
    4 GET FROM CACHE 1
    1 SKIP
4
    1 SKIP
"""
```

**Bottom-Up**
```python
def numTeams(rating):
    """
    Reuse the idea of Longest Increasing Subsequence
    """
    n = len(rating)
    if n < 3:
        return 0

    increasing = [0] * n
    decreasing = [0] * n

    # Count increasing sequences
    for j in range(1, n):
        for i in range(j):
            if rating[i] < rating[j]:
                increasing[j] += 1

    # Count decreasing sequences
    for j in range(1, n):
        for i in range(j):
            if rating[i] > rating[j]:
                decreasing[j] += 1

    # Calculate the total number of teams
    total_teams = 0
    for j in range(n):
        for k in range(j + 1, n):
            if rating[j] < rating[k]:
                total_teams += increasing[j]
            if rating[j] > rating[k]:
                total_teams += decreasing[j]

    return total_teams


print(numTeams([2, 5, 3, 4, 1, 6]))
```

### [Best Team With No Conflicts](https://leetcode.com/problems/best-team-with-no-conflicts)
```python
def bestTeamScore(scores, ages):
    n = len(scores)
    array = list(zip(ages, scores))
    array.sort()

    dp = [score for age, score in array]
    for i in range(1, n):
        curAge, curScore = array[i][0], array[i][1]
        tmp_ans = curScore
        seen = 0
        for j in range(i - 1, -1, -1):
            if curScore >= array[j][1] and array[j][0] != seen:
                seen = array[j][0]
                tmp_ans = max(dp[i] + dp[j], tmp_ans)

        dp[i] = tmp_ans

    return max(dp)


print(bestTeamScore([4, 4, 4, 5, 6, 5, 3], [2, 2, 2, 1, 2, 1, 1]))  # 21
"""
dp = [(1, 3), (1, 8), (1, 13), (2, 7), (2, 11), (2, 15), (2, 21)]
"""
print(bestTeamScore([4, 4, 4, 5, 6, 5, 3, 5], [2, 2, 2, 1, 2, 1, 1, 1]))  # 24
```

## Matrix (Grid) Pattern
Requires us to solve the sub-problem on every sub-grids.
### [Unique Paths](https://leetcode.com/problems/unique-paths)
**Top-Down**
```python
def uniquePaths(m, n):
    @cache
    def dp(row=0, col=0):
        if row == m - 1 and col == n - 1:
            return 1

        rowCnt = 0
        if col < n - 1:
            rowCnt += dp(row, col + 1)

        colCnt = 0
        if row < m - 1:
            colCnt += dp(row + 1, col)

        return rowCnt + colCnt

    return dp()
```

**Bottom-Up**
```python
def uniquePaths(m, n):
    dp = [1] * n

    for i in range(m - 1):
        tmp = 0
        for num in range(n - 1, -1, -1):
            dp[num] += tmp
            tmp = dp[num]

    return dp[0]


print(uniquePaths(3, 7))
```


Explanation
```python
m = 3
n = 7
"""
28 21 15 10 6  3  1  
7  6  5  4  3  2  1
1  1  1  1  1  1  1
"""
```

### [Unique Paths II](https://leetcode.com/problems/unique-paths-ii)
**Top-Down**
```python
def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    @cache
    def dp(row=0, col=0):
        if obstacleGrid[row][col]:
            return 0
            
        if row == m - 1 and col == n - 1:
            return 1

        rowCnt = 0
        if col < n - 1:
            rowCnt += dp(row, col + 1)

        colCnt = 0
        if row < m - 1:
            colCnt += dp(row + 1, col)

        return rowCnt + colCnt

    return dp()
```

**Bottom-Up**
```python
def uniquePathsWithObstacles(obstacleGrid):
    elements_each_row = len(obstacleGrid[0])
    dp = obstacleGrid[-1].copy()

    tmp = 1
    for i in range(elements_each_row - 1, -1, -1):
        if dp[i] == 1:
            tmp = 0
        dp[i] = tmp

    for i in range(len(obstacleGrid) - 2, -1, -1):
        tmp = 0
        for j in range(elements_each_row - 1, -1, -1):
            if obstacleGrid[i][j]:
                dp[j] = 0
                tmp = 0
            dp[j] = dp[j] + tmp
            tmp = dp[j]

    return dp[0]


print(uniquePathsWithObstacles([[0, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0]]))

"""
2 2 2 1
0 0 1 1    
0 0 0 1
"""
```
