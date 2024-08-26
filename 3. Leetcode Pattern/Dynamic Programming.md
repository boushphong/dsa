# Dynamic Programming
# Table of Contents
* [Patterns](#patterns)
   * [Fibonacci Style (1D)](#fibonacci-style-1d)
   * [Linear Sequences with Constant Transition (1D)](#linear-sequences-with-constant-transition-1d)
   * [Linear Sequences with non-constant Transition](#linear-sequences-with-non-constant-transition)
   * [Matrix (Grid) Pattern](#matrix-grid-pattern)
   * [Dual Sequence](#dual-sequence)
   * [Interval](#interval)
   * [Knapsack 1D](#knapsack-1d)
   * [Knapsack 2D](#knapsack-2d)
   * [Dynamic Memoization](#dynamic-memoization)
   * [State Machine](#state-machine)

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

## Dual Sequence
Requires us to calculate some value related to two sequences. `Dp[i][j]` will store the answer to the sub-problem solved on prefix of sequence 1 with length `i`, and prefix on sequence 2 with length `j`.
### [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence)
```python
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [0] * (n + 1)

    for i in range(1, m + 1):
        tmp = [0] * (n + 1)
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                tmp[j] = 1 + dp[j - 1]
            else:
                tmp[j] = max(dp[j], tmp[j - 1])
        dp = tmp

    return dp[-1]

print(longestCommonSubsequence("abcdegace", "bace"))
```

Explanation
```python
      b  a  c  e
  [0, 0, 0, 0, 0]
a [0, 0, 1, 1, 1]
b [0, 1, 1, 1, 1]
c [0, 1, 1, 2, 2]
d [0, 1, 1, 2, 2]
e [0, 1, 1, 2, 3]
g [0, 1, 1, 2, 3]
a [0, 1, 2, 2, 3] # Get element of index 1 (num = 1) in the previous array (left-up diagonal)
c [0, 1, 2, 3, 3]
e [0, 1, 2, 3, 4]

"""
Get element of index 1 (num = 1) in the previous array (left-up diagonal). When we encounter 'a' again, we check the previous letter 'b' in text2 to get it's longest common subsequence.
We get the left-up diagonal element because we would like to check wether the longest common subsequence of the previous letter 
"""
```


### [Edit Distance](https://leetcode.com/problems/edit-distance)
```python
def minDistance(word1, word2):
    dp = list(range(len(word2), -1, -1))

    tmp = 0
    for i in range(len(word1) - 1, -1, -1):
        tmp_dp = [0] * (len(word2) + 1)
        tmp += 1
        tmp_dp[-1] = tmp

        for j in range(len(word2) - 1, -1, -1):
            right = tmp_dp[j + 1]
            down = dp[j]
            diag = dp[j + 1]
            if word1[i] == word2[j]:
                tmp_dp[j] = diag
            else:
                tmp_dp[j] = min(right, down, diag) + 1

        dp = tmp_dp

    return dp[0]


print(minDistance("horse", "ros"))
```

Explanation
```python
    r   o   s  ''
h   3   3   4   5    < string horse takes 5 operation to make it become '' (remove 5 times)
o   3   2   3   4
r   2   2   2   3
s   3   2   1   2    ...
e   3   2   1   1    < string e takes 1 operation to make it become '' (remove)
''  3   2   1   0    < 2 empty string takes 0 operation to make them equal. 
            ^
            empty string takes 1 operation to become 's' insert

"""
- Down means deletion (i + 1, j)
- Diag means replacement (i + 1, j + 1)
- Right means insertion (i, j + 1)

First Row:
- We start from the bottom at string 'e' and 's'. They are not equal, hence it took 1 replacement (by going diagonally and +1 operation)
- Then we look at string 'e' and 'os'. We know that the previous step took 1 replacement, hence we can either
    - Go down (2 + 1) = 3 operations. delete 'e' then add 'o' and 's'.
    - Go right (1 + 1) = 2 operations. right of the previous step (already calculated) is replacement. hence replace 'e' to 's' then insert 'o' anywhere. (Reuse 1)
    - Go diag (1 + 1) = 2 operations. replace 'e' to 'o' then insert 's'. (Reuse 2)
...

Second Row:
- We start from the bottom at string 'se' and 's'. Matching 's', we take the diag operations = 1 operations. delete 'e'
- Then we look at string 'se' and 'os'.
    - go down (2 + 1) = 3 operations. delete 's', which becomes 'e' and 'os'. Reuse the step above (go right or go diag, Reuse 1 or 2)
    ...

"""
```

## Interval
Requires us to solve sub-problems based on every single interval (sub-array) of the array
### [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence)
**Top-Down**
```python
def longestPalindromeSubseq(s):
    memo = {}

    def dp(l=0, r=len(s) - 1):
        if (l, r) in memo:
            return memo[(l, r)]
        if l == r:
            return 1
        if l > r:
            return 0

        if s[l] == s[r]:
            cnt = 2 + dp(l + 1, r - 1)
        else:
            cnt1 = dp(l + 1, r)
            cnt2 = dp(l, r - 1)
            cnt = max(cnt1, cnt2)

        memo[(l, r)] = cnt
        return cnt

    return dp()


print(longestPalindromeSubseq("cbbabab"))
"""
0   6 (5)
    1   6 (5)
        2   5 (3)
            3   5 (3)
                4   4 (1)
            2   4 (3)
                3   3 (1)
    0   5 (3)
        1   5 (3)
            2   5 (3) 
            1   4 (3)
                2   4 (3)
                1   3 (2)
                    2   3 (1)
                        3   3 (1)
                    1   2 (2)
                        2   1 (0)
        1   4 (3)
"""
```

[**Bottom-Up**](https://www.youtube.com/watch?v=TLaGwTnd3HY&t=207s&ab_channel=GeeksforGeeks)
```python
def longestPalindromeSubseq(s):
    dp = [0] * len(s)

    for i in range(len(s) - 1, -1, -1):
        tmp_dp = [0] * len(s)
        tmp_dp[i] = 1
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                tmp_dp[j] = 2 + dp[j - 1]
            else:
                tmp_dp[j] = max(dp[j], tmp_dp[j - 1])
        dp = tmp_dp
    return dp[-1]


print(longestPalindromeSubseq("babcbab"))  # 7
print(longestPalindromeSubseq("cbbabab"))  # 5
```

### [Stone Game VII](https://leetcode.com/problems/stone-game-vii)
**Top-Down:** Use `lru_cache(maxsize=3000)` instead of `memo` for cache eviction to pass `Memory Limit Exceeded` on LeetCode.
```python
from itertools import accumulate


def stoneGameVII(stones):
    prefix_sum = list(accumulate(stones, initial=0))
    memo = {}

    def dp(l=0, r=len(stones) - 1):
        if l == r:
            return 0

        if (l, r) in memo:
            return memo[(l, r)]

        total_sum = prefix_sum[r + 1] - prefix_sum[l]
        left_choice = total_sum - stones[l] - dp(l + 1, r)
        right_choice = total_sum - stones[r] - dp(l, r - 1)

        result = max(left_choice, right_choice)
        memo[(l, r)] = result
        return result

    return dp()


print(stoneGameVII([5, 3, 1, 4, 2]))
"""
memo = {(3, 4): 4, (2, 3): 4, (2, 4): 2, (1, 2): 3, (1, 3): 1, (1, 4): 7, (0, 1): 5, (0, 2): 3, (0, 3): 7, (0, 4): 6}
stoneGameVII([5, 3, 1, 4, 2])
  └─ dp(0, 4)  # diff = 6 -> max(15 - 7 - 3, 15 - 7 - 2)
       ├─ dp(1, 4)  # diff = 7 (cache)
       │    ├─ dp(2, 4)  # diff = 2 (cache)
       │    │    ├─ dp(3, 4)  # diff = 4 (cache)
       │    │    │    ├─ dp(4, 4)    
       │    │    │    └─ dp(3, 3)  
       │    │    └─ dp(2, 3)  # diff = 4 (cache)
       │    │         ├─ dp(3, 3)  
       │    │         └─ dp(2, 2)
       │    └─ dp(1, 3)  # diff = 1 (cache)
       │         ├─ dp(2, 3)  # diff = 4 (use cache)
       │         └─ dp(1, 2)  # diff = 3 (cache)
       │              ├─ dp(2, 2)
       │              └─ dp(1, 1)
       └─ dp(0, 3)  # diff = 7 (cache)
            ├─ dp(1, 3)  # diff = 1 (use cache)
            └─ dp(0, 2)  # diff = 3 (cache)
                 ├─ dp(1, 2)  # diff = 3 (use cache)
                 └─ dp(0, 1)  # diff = 5 (cache)
                      ├─ dp(1, 1)
                      └─ dp(0, 0)
"""
```

**Bottom-Up**
```python
def stoneGameVII(stones):
    n = len(stones)
    prefix_sum = list(accumulate(stones, initial=0))
    dp = [0] * n

    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            total_sum = prefix_sum[r + 1] - prefix_sum[l]
            dp[l] = max(
                total_sum - stones[l] - dp[l + 1],
                total_sum - stones[r] - dp[l]
            )
            
    return dp[0]
```


## Knapsack 1D
### [Unbounded Knapsack](https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1)
```python
def knapsack(values, weights, m):
    dp = [0] * (m + 1)

    for value, weight in zip(values, weights):
        for w in range(weight, m + 1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[-1]


print(knapsack([1, 5, 7, 14], [1, 2, 3, 5], 9))
# print(knapsack01([7, 1, 14, 5], [3, 1, 5, 2], 9))
```

Explanation
```python
m = 9
values = [1, 5, 7, 14]
weights = [1, 2, 3, 5]
v   w   0   1   2   3   4   5   6   7   8   9
-   -   0   0   0   0   0   0   0   0   0   0
1   1   0   1   2   3   4   5   6   7   8   9
5   2   0   1   5   6  10  11  15  16  20  21
7   3   0   1   5   7  10  12  15  16  20  21
14  5   0   1   5   7  10  14  15  19  21  24

"""
At every iteration of a pair of (value and weight), we consider if there is a posible answer by looking the best answer of the previous pair. We only iterate from starting weight to ending weight of the item and we update dp INPLACE.
- At first item iteration (value = 1, weight = 1), we look at a previous pair of (value = 0, weight = 0)
    - At weight i = 1, we get the best answer from previous dp (dp[1] = 0).
    - Compare it with the possible best answer dp[w - weight] + value = dp[1 - 1] + 1 = 0 + 1 = 1
    - Hence, we get 1
...
"""
```

### [Coin Change](https://leetcode.com/problems/coin-change)
```python
def coinChange(coins, amount):
    dp = [float("inf")] * (amount + 1)
    minimum = min(coins)
    if amount < minimum:
        return -1 if amount else 0

    for i in range(0, amount + 1):
        for c in coins:
            if c == i:
                dp[i] = 1
                break

            if i - c >= minimum:
                dp[i] = min(dp[i], dp[c] + dp[i - c])

    return dp[amount] if dp[amount] != float("inf") else -1


print(coinChange([2, 3, 5], 13))
print(coinChange([1], 1))
print(coinChange([1], 0))
```


### [Word Break](https://leetcode.com/problems/word-break/)
```python
def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for word in wordDict:
            if len(word) > i or dp[i]:
                continue

            tmpWord = s[i - len(word):i]
            if word == tmpWord:
                dp[i] = True and dp[i - len(word)]
    return dp[-1]


print(wordBreak("dogs", ["dog", "s", "gs"]))  # True
"""
0   1   2   3   4 
    d   o   g   s
T   F   F   T   T
"""
```

## Knapsack 2D
### [0/1 Knapsack](https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1)
```python
def knapsack01(values, weights, m):
    dp = [0] * (m + 1)

    for value, weight in zip(values, weights):
        tmp_dp = [0] * (m + 1)
        for i in range(1, len(tmp_dp)):
            if i >= weight:
                tmp_dp[i] = max(dp[i], dp[i - weight] + value)
            else:
                tmp_dp[i] = dp[i]
        dp = tmp_dp
    return dp[-1]


print(knapsack01([2, 1, 4, 6], [1, 2, 3, 5], 8))
```

Explanation
```python
m = 8
values = [2, 1, 4, 6]
weights = [1, 2, 3, 5]
v   w   0   1   2   3   4   5   6   7   8
-   -   0   0   0   0   0   0   0   0   0
2   1   0   2   2   2   2   2   2   2   2
1   2   0   2   2   3   3   3   3   3   3
4   3   0   2   2   4   6   6   7   7   7
6   5   0   2   2   4   6   6   8   8  10

"""
At every iteration of a pair of (value and weight), we consider if there is a posible answer by looking the best answer of the previous pair.
- At the first iteration, we look at previous pair of (value = 0, weight = 0)
    - At weight i = 1, we get the best answer from previous dp (dp[1] = 0).
    - Compare it with the possible best answer dp[i - weight] + value = dp[1 - 1] + 2 = 2
    - Hence, we get 2.
- We do this to determine the best possible value at weight = 1.
    - At first item iteration (value = 2, weight = 1) and at i = 1. If we want to know the best possible value by including this item, we need to know the best possible value of at weight (1 - 1 = 0). At weight 0, the best possible value is 0.
...
"""
```

### [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum)
```python
def canPartition(nums):
    if sum(nums) % 2:
        return False

    target = sum(nums) // 2

    if max(nums) > target:
        return False

    dp = [False] * target

    for i, v in enumerate(nums):
        tmp_dp = [False] * target
        tmp_dp[v - 1] = True
        for iSum in range(v + 1, target + 1):
            if dp[iSum - 1]:
                tmp_dp[iSum - 1] = True
                continue

            tmp_dp[iSum - 1] = (tmp_dp[v - 1] and dp[iSum - v - 1])

        if tmp_dp[-1]:
            return True
        dp = [v1 or v2 for v1, v2 in zip(dp, tmp_dp)]

    return False


print(canPartition([1, 5, 10, 6]))
print(canPartition([4, 4, 2, 1, 5]))
"""
    1   2   3   4   5   6   7   8
4   F   F   F   T   F   F   F   F
4   F   F   F   T   F   F   F   T
2   F   T   F   T   F   T   F   T
1   T   T   T   T   T   T   T   T
5   T   T   T   T   T   T   T   T
"""
```

## Dynamic Memoization
Requires us to memoize sub-problems' results on a dynamic data structure (eg. HashMap) to store intermediate results of sub-problems. This technique is employed to prevent overriding the best optimal result for sub-problems that have already been solved, which is crucial when overlapping sub-problems occur. This ensures that the most optimal result for a sub-problem is preserved and can be re-used whenever needed.
### [Longest Arithmetic Subsequence](#longest-arithmetic-subsequence)

### [Make Array Strictly Increasing](https://leetcode.com/problems/make-array-strictly-increasing)
```python
from bisect import bisect_right


def makeArrayIncreasing(arr1, arr2):
    arr2.sort()
    dp = {arr1[0]: 0}
    if arr2[0] < arr1[0]:
        dp.update({arr2[0]: 1})
    INF = float("inf")

    for idx, val in enumerate(arr1[1:], 1):
        tmpDp = {}
        for prev, operations in dp.items():
            if val > prev:
                tmpDp[val] = min(operations, tmpDp.get(val, INF))
            tmpIdx = bisect_right(arr2, prev)
            if tmpIdx < len(arr2):
                tmpDp[arr2[tmpIdx]] = min(1 + dp[prev], tmpDp.get(arr2[tmpIdx], INF))
        dp = tmpDp

    return min(dp.values()) if dp else -1


print(makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[1, 3, 2, 4]))  # 1
print(makeArrayIncreasing(arr1=[9, 5, 3, 6, 7], arr2=[1, 3, 2, 4]))  # 2
```


## State Machine
Requires us to memoize sub-problems' most optimal results for every state. This is usually can be solved by creating a memoize dp for every possible state. 
### [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
```python
def maxProfit(prices):
    sold, bought, reset = 0, -prices[0], 0

    for price in prices[1:]:
        pre_sold = sold
        sold = bought + price
        bought = max(bought, reset - price)
        reset = max(reset, pre_sold)

    return max(sold, reset)


print(maxProfit([1, 2, 3, 0, 2]))  # 3
```
| price |      | 1    | 2  | 3  | 0  | 2 |
|-------|------|------|----|----|----|---|
| sold  | -inf | -inf | 1  | 2  | -1 | 3 |
| held  | -inf | -1   | -1 | -1 | 1  | 1 |
| reset | 0    | 0    | 0  | 1  | 2  | 2 |
