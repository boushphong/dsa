# Dynamic Programming (Advanced)
# Table of Contents
* [Patterns](#patterns)
   * [Dual Sequence](#dual-sequence)
   * [Interval](#interval)
   * [Knapsack 1D](#knapsack-1d)
   * [Knapsack 2D](#knapsack-2d)
   * [Dynamic Memoization](#dynamic-memoization)
   * [State Machine](#state-machine)

# Patterns

## Dual Sequence
Requires us to calculate some value related to two sequences. `Dp[i][j]` will store the answer to the sub-problem solved on prefix of sequence 1 with length `i`, and prefix on sequence 2 with length `j`.
### [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence)
**Top-Down**
```python
def longestCommonSubsequence(text1, text2):
    memo = {}
    
    def dp(i=0, j=0):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == len(text1) or j == len(text2):
            return 0
        
        if text1[i] == text2[j]:
            memo[(i, j)] = 1 + dp(i + 1, j + 1)
        else:
            memo[(i, j)] = max(dp(i, j + 1), dp(i + 1, j))
        
        return memo[(i, j)]
    
    return dp()


print(longestCommonSubsequence("abcde", "ace"))  # 3
```

Explanation
```python
memo = {(4, 2): 1, (3, 2): 1, (2, 2): 1, (1, 2): 1, (2, 1): 2, (1, 1): 2, (0, 0): 3}

longestCommonSubsequence("abcde", "ace")
  └─ dp(0, 0)  # a -> increment and max (cache 3)
       └─ dp(1, 1)  # max (cache 2)
            ├─ dp(1, 2)  # max (cache 1) 
            │    ├─ dp(1, 3) 
            │    └─ dp(2, 2)  # max (cache 1)
            │         ├─ dp(2, 3)  
            │         └─ dp(3, 2)  # max (cache 1)
            │              ├─ dp(3, 3)
            │              └─ dp(4, 2)  # e -> increment (cache 1)
            │                   └─ dp(5, 3)
            └─ dp(2, 1)  # c -> increment and max (cache 2)
                 └─ dp(4, 2)  # e -> (get cache 1)
```

**Bottom-Up**
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

print(longestCommonSubsequence("abcdegace", "bace"))  # 4
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
**Top-Down**
```python
def minDistance(word1, word2):
    n, m = len(word1), len(word2)
    memo = {}

    if not n:
        return m
    if not m:
        return n
    
    def dp(i=n - 1, j=m - 1):
        if (i, j) in memo:
            return memo[(i, j)]
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        
        if word1[i] == word2[j]:
            return dp(i - 1, j - 1)

        removeOp = dp(i - 1, j)
        insertOp = dp(i, j - 1)
        replaceOp = dp(i - 1, j - 1)

        memo[(i, j)] = min(removeOp, insertOp, replaceOp) + 1
        
        return memo[(i, j)]

    return dp()

print(minDistance("horse", "ros"))  # 3
```

Explanation
```python
memo = {(0, 0): 1, (1, 1): 1, (2, 0): 2, (1, 0): 2, (2, 1): 2, (3, 2): 2, (3, 0): 3, (3, 1): 3, (4, 0): 4, (4, 1): 4, (4, 2): 3}

minDistance("horse", "ros")
  └─ dp(4, 2)  # e != s -> min(remove, insert, replace) + 1 (cache 3)
       ├─ dp(3, 2)  # s == s -> (cache 2)
       │    └─ dp(2, 1)  # r != o -> (cache 2)
       │         ├─ dp(1, 1)  # o == o -> (cache 1)
       │         │    └─ dp(0, 0)  # h != r -> (cache 1)
       │         │         ├─ dp(-1, 0)  # 1
       │         │         ├─ dp(0, -1)  # 1
       │         │         └─ dp(-1, -1)  # 0
       │         ├─ dp(2, 0)  # r == r (cache 2)
       │         │    └─ dp(1, -1)  # 2
       │         └─ dp(1, 0)  # o != r -> (cache 2)
       │              ├─ dp(0, 0)  # (get cache 1)
       │              ├─ dp(1, -1)  # 2
       │              └─ dp(0, -1)  # 1
       ├─ dp(4, 1)  # e != o -> (cache 4)
       │    ├─ dp(3, 1)  # s != o -> (cache 3)
       │    │    ├─ dp(2, 1)  # (get cache 2)
       │    │    ├─ dp(3, 0)  # s != r -> (cache 3)
       │    │    │    ├─ dp(2, 0)  # (get cache 2)
       │    │    │    ├─ dp(3, -1)  # 4
       │    │    │    └─ dp(2, -1)  # 3
       │    │    └─ dp(2, 0)  # (get cache 1)
       │    ├─ dp(4, 0)  # e != r -> (cache 4)
       │    │    ├─ dp(3, 0)  # (get cache 3)
       │    │    ├─ dp(4, -1)  # 5
       │    │    └─ dp(3, -1)  # 4
       │    └─ dp(3, 0)  # (get cache 3)
       └─ dp(3, 1)  # (get cache 2)
```

**Bottom-Up**
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


print(minDistance("horse", "ros"))  # 3
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
**Top-Down**
```python
def wordBreak(s, wordDict):
    n = len(s)

    def dp(i=0):
        if i == n:
            return True

        isValid = False
        for word in wordDict:
            if s[i:].startswith(word):
                isValid = isValid or dp(i + len(word))

        return isValid

    return dp()
```

**Bottom-Up**
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
Requires us to memoize sub-problems' results on a dynamic data structure (eg. HashMap) to store intermediate results of sub-problems. 
- Can be used to prevent overriding the best optimal result for sub-problems that have already been solved, which is crucial when overlapping sub-problems occur. This ensures that the most optimal result for a sub-problem is preserved and can be re-used whenever needed.
- Can be used to cut TC if many similar keys are accessed repeatedly.

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

### [Make Array Strictly Increasing](https://leetcode.com/problems/make-array-strictly-increasing)
```python
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

### [Longest Ideal Subsequence](https://leetcode.com/problems/longest-ideal-subsequence/)
```python
def longestIdealString(s, k):
    hm = defaultdict(int)
    for i, letter in enumerate(s):
        ordLetter = ord(letter)
        cur = 1
        for letterInRange in range(ordLetter - k, ordLetter + k + 1):
            cur = max(cur, hm.get(chr(letterInRange), 0) + 1)
        hm[letter] = max(hm[letter], cur)

    return max(hm.values())


print(longestIdealString("acfgbd", 2))  # 4
print(longestIdealString("pvjcci", 4))  # 2
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
