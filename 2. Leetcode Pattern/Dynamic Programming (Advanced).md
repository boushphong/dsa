# Dynamic Programming (Advanced)
# Table of Contents
* [Patterns](#patterns)
   * [Dual Sequence](#dual-sequence)
   * [Interval](#interval)
   * [Unbounded Knapsack](#unbounded-knapsack)
   * [0/1 Knapsack](#01-knapsack)
   * [State Machine](#state-machine)
   * [Game Theory](#game-theory)
   * [Dynamic Memoization](#dynamic-memoization)


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

<details>
<summary>Explanation</summary>

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
</details>

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

<details>
<summary>Explanation</summary>

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
</details>

### [Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines)
```python
def maxUncrossedLines(nums1, nums2):
    n, m = len(nums1), len(nums2)

    @cache
    def dp(i=0, j=0):
        if i == n or j == m:
            return 0

        if nums1[i] == nums2[j]:
            uncrossedCnt = (1 + dp(i + 1, j + 1))
        else:
            uncrossedCnt = max(dp(i, j + 1), dp(i + 1, j))
        return uncrossedCnt

    return dp()


print(maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))  # 3
print(maxUncrossedLines([1, 4, 2], [1, 2, 4]))  # 2
```

### [Edit Distance](https://leetcode.com/problems/edit-distance)
**Top-Down (Backward)**
```python
def minDistance(word1, word2):
    n, m = len(word1), len(word2)
    memo = {}

    def dp(i=n - 1, j=m - 1):
        if (i, j) in memo:
            return memo[(i, j)]
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        
        if word1[i] == word2[j]:
            memo[(i, j)] = dp(i - 1, j - 1)
        else:
            removeOp = dp(i - 1, j)
            insertOp = dp(i, j - 1)
            replaceOp = dp(i - 1, j - 1)
            memo[(i, j)] = min(removeOp, insertOp, replaceOp) + 1
        
        return memo[(i, j)]

    return dp()

print(minDistance("horse", "ros"))  # 3
```

<details>
<summary>Explanation</summary>

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
</details>

**Top-Down (Forward)**
```python
def minDistance(word1, word2):
    n, m = len(word1), len(word2)
    memo = {}
    
    def dp(i=0, j=0):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == n:
            return m - j
        if j == m:
            return n - i
        
        if word1[i] == word2[j]:
            memo[(i, j)] = dp(i + 1, j + 1)
        else:
            removeOp = dp(i + 1, j)
            insertOp = dp(i, j + 1)
            replaceOp = dp(i + 1, j + 1)
            memo[(i, j)] = min(removeOp, insertOp, replaceOp) + 1

        return memo[(i, j)]

    return dp()


print(minDistance("horse", "ros"))  # 3
```

<details>
<summary>Explanation</summary>

```python
memo = {(4, 2): 1, (4, 1): 2, (3, 2): 1, (3, 1): 2, (2, 0): 2, (2, 2): 2, (1, 1): 2, (2, 1): 2, (1, 0): 3, (1, 2): 3, (0, 2): 4, (0, 1): 3, (0, 0): 3}

minDistance("horse", "ros")
  └─ dp(0, 0)  # h != r -> (cache 3)
      ├─ dp(1, 0)  # o != r -> (cache 3)
      │    ├─ dp(2, 0)  # r == r (cache 2)
      │    │    └─ dp(3, 1)  # s != o -> (cache 2)
      │    │         ├─ dp(4, 1)  # e != o -> (cache 3)
      │    │         │    ├─ dp(5, 1)  # 2
      │    │         │    ├─ dp(4, 2)  # e != s -> (cache 2)
      │    │         │    │    ├─ dp(5, 2)  # 1
      │    │         │    │    ├─ dp(4, 3)  # 1
      │    │         │    │    └─ dp(5, 3)  # 0
      │    │         │    └─ dp(5, 2)  # 1
      │    │         ├─ dp(3, 2)  # s == s (cache 1)
      │    │         │    └─ dp(4, 3)  # 1
      │    │         └─ dp(4, 2)  # (get cache 2)
      │    ├─ dp(1, 1)  # o == o (cache 2)
      │    │    └─ dp(2, 2)  # r != s -> (cache 1)
      │    │         ├─ dp(3, 2)  # (get cache 1)
      │    │         ├─ dp(2, 3)  # 2
      │    │         └─ dp(3, 3)  # 0
      │    └─ dp(2, 1)  # r != o -> (cache 2)
      │         ├─ dp(3, 1)  # (get cache 2)
      │         ├─ dp(2, 2)  # (get cache 1)
      │         └─ dp(3, 2)  # (get cache 1)
      ├─ dp(0, 1)  # h != o -> (cache 4)
      │    ├─ dp(1, 1)  # (get cache 2)
      │    ├─ dp(0, 2)  # h != s -> (cache 3)
      │    │    ├─ dp(1, 2)  # o != s -> (cache 2)
      │    │    │    ├─ dp(2, 2)  # (get cache 1)
      │    │    │    ├─ dp(1, 3)  # 2
      │    │    │    └─ dp(2, 3)  # 1
      │    │    ├─ dp(0, 3)  # 3
      │    │    └─ dp(1, 3)  # 2
      │    └─ dp(1, 2)  # (get cache 2)
      └─ dp(1, 1)  # (get cache 2)
```
</details>


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

<details>
<summary>Explanation</summary>

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
</details>

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
```

<details>
<summary>Explanation</summary>

```python
longestPalindromeSubseq("cbbabab")
  └─ dp(0, 6)  # c != b -> (cache 5)
      ├─ dp(1, 6)  # b == b -> (cache 5)
      │    └─ dp(2, 5)  # b != a -> (cache 3)
      │         ├─ dp(3, 5)  # a != a -> (cache 3)
      │         │    └─ dp(4, 4)  # b == b (cache 1)
      │         └─ dp(2, 4)  # b == b -> (cache 3)
      │              └─ dp(3, 3)  # a == a (cache 1)
      └─ dp(0, 5)  # c != a -> (cache 3)
           ├─ dp(1, 5)  # b != a -> (cache 3)
           │    ├─ dp(2, 5)  # (get cache 3)
           │    └─ dp(1, 4)  # b == b -> (cache 3)
           │         ├─ dp(2, 3)  # b != a -> (cache 1)
           │         │    ├─ dp(3, 3)  # (get cache 1)
           │         │    └─ dp(2, 2)  # b == b (cache 1)
           │         └─ dp(2, 1)  # 0
           └─ dp(1, 4)  # (get cache 3)
```
</details>

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
```

<details>
<summary>Explanation</summary>

```python
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
```
</details>

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


## Unbounded Knapsack
Unbounded Knapsack problem involves determining how many times each item can be included, without any restrictions on the number of times an item can be chosen, to maximize the total value while staying within a specified weight limit or to determine if the end goal can be reachable or not.
### [Unbounded Knapsack](https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1)
**Top-Down**
```python
def unboundedKnapsack(values, weights, m):
    memo = {}

    def dp(capacity=m):
        if capacity == 0:
            return 0
        if capacity in memo:
            return memo[capacity]

        maxValue = 0
        for i, value in enumerate(values):
            if weights[i] <= capacity:
                maxValue = max(maxValue, value + dp(capacity - weights[i]))

        memo[capacity] = maxValue
        return maxValue

    return dp()


print(unboundedKnapsack([1, 5, 7, 14], [1, 2, 3, 5], 9))  # 24
```

**Bottom-Up**
```python
def unboundedKnapsack(values, weights, m):
    dp = [0] * (m + 1)

    for value, weight in zip(values, weights):
        for w in range(weight, m + 1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[-1]


print(unboundedKnapsack([1, 5, 7, 14], [1, 2, 3, 5], 9))  # 24
```

<details>
<summary>Explanation</summary>

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
At every iteration of a pair of (value and weight), we consider if there is a possible answer by looking the best answer of the previous pair. We only iterate from starting weight to ending weight of the item and we update dp INPLACE.
- At first item iteration (value = 1, weight = 1), we look at a previous pair of (value = 0, weight = 0)
    - At weight i = 1, we get the best answer from previous dp (dp[1] = 0).
    - Compare it with the possible best answer dp[w - weight] + value = dp[1 - 1] + 1 = 0 + 1 = 1
    - Hence, we get 1
...
"""
```
</details>


### [Perfect Squares](https://leetcode.com/problems/perfect-squares)
```python
def numSquares(n):
    perfectSquares = []
    square = 1

    while square ** 2 <= n:
        perfectSquares.append(square ** 2)
        square += 1

    @cache
    def dp(total=0):
        if total == n:
            return 0

        minVal = inf
        for i, aSquare in enumerate(perfectSquares):
            if total + aSquare <= n:
                minVal = min(minVal, 1 + dp(total + aSquare))

        return minVal

    return dp()


print(numSquares(12))  # 3
print(numSquares(13))  # 2
```

### [Coin Change](https://leetcode.com/problems/coin-change)
**Top-Down**
- **TC**: `O(N * amount)`
- **SC**: `O(N * amount)`
```python
def coinChange(coins, amount):
    @cache
    def dp(idx=0, total=0):
        if total == amount:
            return 0
        if total > amount or idx == len(coins):
            return inf

        pick = 1 + dp(idx, total + coins[idx])
        notPick = dp(idx + 1, total)

        return min(pick, notPick)

    return dp() if dp() != inf else -1
```

**Top-Down (Space Optimized)**
- **TC**: `O(N * amount)`
- **SC**: `O(amount)`
```python
def coinChange(coins, amount):
    @cache
    def dp(remaining=amount):
        if remaining == 0:
            return 0
        
        minimumCoins = inf
        for i, coin in enumerate(coins):
            if coin <= remaining:
                minimumCoins = min(minimumCoins, 1 + dp(remaining - coin))

        return minimumCoins
    
    return dp() if dp() != inf else -1
```

**Bottom Up**
```python
def coinChange(coins, amount):
    dp = [inf] * (amount + 1)
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

    return dp[amount] if dp[amount] != inf else -1


print(coinChange([2, 3, 5], 13))  # 3
print(coinChange([1], 1))  # 1
print(coinChange([1], 0))  # 0
```

### [Coin Change II](https://leetcode.com/problems/coin-change-ii)
For unbounded knapsack problems that asks for the number of unique combinations, we can't optimize the space by reducing the number of state arguments (from **2 to 1**) like in Coin Change I problem. In such case, we have to use the **Pick and Not Pick** pattern (eg. Subset), because this pattern will ensure unique combinations and it will not lead to a bug in double counting.
```python
def change(amount, coins):
    @cache
    def dp(idx=0, total=0):
        if total == amount:
            return 1
        if total > amount or idx == len(coins):
            return 0

        pick = dp(idx, total + coins[idx])
        notPick = dp(idx + 1, total)

        return pick + notPick

    return dp()


print(change(5, [1, 2, 5]))  # 4
```

### [Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling)
```python
def numTilings(n):
    # (2, 2) block is (0, 2) and (2, 0) being placed together, This is to avoid handling counting duplication
    # Moving either of these blocks first will not generate more unique combinations
    fEqualS = [(1, 1), (2, 2), (2, 1), (1, 2)]
    fLargerS = [(0, 2), (1, 2)]
    fSmallerS = [(2, 0), (2, 1)]

    movesMap = {
        0: fEqualS,
        1: fLargerS,
        -1: fSmallerS
    }

    @cache
    def dp(f=0, s=0):
        if f == n and s == n:
            return 1
        if f > n or s > n:
            return 0

        rowDiff = f - s
        moves = movesMap[(rowDiff > 0) - (rowDiff < 0)]

        cnt = 0
        for movedByRow, movedByCol in moves:
            cnt += dp(f + movedByRow, s + movedByCol)

        return cnt

    return dp() % (10 ** 9 + 7)


print(numTilings(3))  # 5
```

### [Word Break](https://leetcode.com/problems/word-break/)
**Top-Down**
```python
def wordBreak(s, wordDict):
    n = len(s)

    @cache
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

## 0/1 Knapsack
0/1 Knapsack problem resembles subset problems, as it requires making binary decisions about including or excluding items to find the optimal solution.
### [0/1 Knapsack](https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1)
**Top-Down**
```python
def knapsack01(values, weights, wt):
    n = len(values)
    memo = {}

    def dp(k=wt, i=0):
        if (k, i) in memo:
            return memo[(k, i)]
        if k < 0:
            return -inf
        if i == n:
            return 0

        pick = values[i] + dp(k - weights[i], i + 1)
        notPick = dp(k, i + 1)
        memo[(k, i)] = max(pick, notPick)
        return memo[(k, i)]

    return dp()


print(knapsack01([20, 30, 15, 25, 10], [6, 13, 7, 10, 3], 20))  # 60
```

<details>
<summary>Explanation</summary>

```python
knapsack01([20, 30, 15, 25, 10], [6, 13, 7, 10, 3], 20)
  └─ dp(20, 0)  # (Pick) 20 + 35 = 55 -- (Not Pick) 50 -> Res = 55 
      ├─ dp(14, 1)  # (Not Pick) (Cache 35)
      │    ├─ dp(1, 2)   # Can't pick item 2 (Weight Exceeded)
      │    │   └─ dp(1, 3)  # Can't pick item 2 (Weight Exceeded)
      │    │       └─ dp(1, 4)  # Can't pick item 2 (Weight Exceeded)
      │    └─ dp(14, 2)  # (Not Pick) (Cache 35)
      │        ├─ dp(7, 3) # (Not Pick) (Cache 10)
      │        │   └─ dp(7, 4)  # (Pick) (Cache 10)
      │        └─ dp(14, 3)  # (Pick) (Cache 35)
      │            ├─ dp(4, 4)  # (Pick) (Cache 10) 
      │            └─ dp(14, 4)  # (Pick) (Cache 10)
      └─ dp(20, 1)  # (Pick) (Cache 50)
          ├─ dp(7, 2)  # (Pick) (Cache 15)
          │    ├─ dp(0, 3)  # Can't pick item 3 (Weight Exceeded)
          │    │    └─ dp(0, 4)  # Can't pick item 4 (Weight Exceeded)
          │    └─ dp(7, 3)  # (Get From Cache 10) 
          └─ dp(20, 2)  # (Pick) (Cache 50)
              ├─ dp(13, 3)  # (Pick) (Cache 35)
              │    ├─ dp(3, 4)  # (Pick) (Cache 10)
              │    └─ dp(13, 4)  # (Pick) (Cache 10)
              └─ dp(20, 3)  # (Pick) (Cache 35)
                  ├─ dp(10, 4)  # (Pick) (Cache 10)
                  └─ dp(20, 4)  # (Pick) (Cache 10)
```
</details>

**Bottom-Up**
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

<details>
<summary>Explanation</summary>

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
</details>

### [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum)
**Top-Down**
```python
def canPartition(nums):
    n = len(nums)
    totalSum = sum(nums)

    if totalSum % 2 != 0:
        return False

    @cache
    def dp(i=0, total=0):
        if total == totalSum // 2:
            return True
        if total > totalSum:
            return False
        if i == n:
            return False

        pick = dp(i + 1, total + nums[i])
        if pick:
            return True
        notPick = dp(i + 1, total)
        if notPick:
            return True
        return False

    return dp()
```

**Bottom-Up**
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

### [Stone Game II](https://leetcode.com/problems/stone-game-ii)
```python
def stoneGameII(piles: List[int]) -> int:
    n = len(piles)
    preSum = list(accumulate(piles, initial=0))

    @cache
    def dp(idx=0, m=1, alice=True):
        if idx >= n:
            return 0

        pick = 0 if alice else inf
        for i in range(1, (m * 2) + 1):
            if alice:
                stones = preSum[idx + i] - preSum[idx] if idx + i <= n else 0
                pick = max(pick, stones + dp(idx + i, max(m, i), not alice))
            else:
                pick = min(pick, dp(idx + i, max(m, i), not alice))
        return pick

    return dp()


print(stoneGameII([1, 2, 3, 4, 5, 100]))  # 104
print(stoneGameII([2, 7, 9, 4, 4]))  # 10
print(stoneGameII([1]))  # 1
```

### [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/)
By returning `-inf` when the limits are exceeded, the code effectively communicates that this path should not contribute to the maximum count of strings. This logic is needed because in **0/1 knapsack**, we try to increment the count first by picking the item however this might lead to a bug where the picked item violates the limits. Hence we either have to check limit in the new recursion call or check if limit would be valid before picking an item.

```python
def findMaxForm(strs, m, n):
    @cache
    def dp(idx=0, cntZero=0, cntOne=0):
        if cntZero > m or cntOne > n:
            return -inf
        if idx == len(strs):
            return 0
        
        zeroes = strs[idx].count("0")
        ones = strs[idx].count("1")
        
        pick = 1 + dp(idx + 1, cntZero + zeroes, cntOne + ones)
        notPick = dp(idx + 1, cntZero, cntOne)

        return max(pick, notPick)

    return dp()


print(findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))  # 4
```

Checking limits before picking new item
```python
def findMaxForm(strs, m, n):
    @cache
    def dp(idx=0, cntZero=0, cntOne=0):
        if idx == len(strs):
            return 0
        
        zeroes = strs[idx].count("0")
        ones = strs[idx].count("1")
        
        pick = 0
        if cntZero + zeroes <= m and cntOne + ones <= n:
            pick = 1 + dp(idx + 1, cntZero + zeroes, cntOne + ones)
        notPick = dp(idx + 1, cntZero, cntOne)

        return max(pick, notPick)

    return dp()
```

## State Machine
Requires us to memoize sub-problems' most optimal results for every state. This is usually can be solved by creating a memoize dp for every possible state. 
### [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
**Top-Down**
- TC: `O(2N)` -> `O(N)`
  - `2N` -> `O(N)` because `canBuy` has only 2 possible states **True** and **False**, hence this can be treated as constant.
- SC: `O(2N)` -> `O(N)`
```python
def maxProfit(prices):
    n = len(prices)

    def dp(idx=0, canBuy=True):
        if idx >= n:
            return 0

        if canBuy:
            buy = -prices[idx] + dp(idx + 1, canBuy=False)
            hold = dp(idx + 1)
            return max(buy, hold)
        else:
            sell = prices[idx] + dp(idx + 2)
            delay = dp(idx + 1, canBuy=False)
            return max(sell, delay)

    return dp()


print(maxProfit([1, 2, 3, 0, 2]))  # 3
print(maxProfit([1]))  # 0
```

**Bottom-Up**
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

### [Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)
```python
def maxProfit(prices, fee):
    n = len(prices)

    def dp(idx=0, canBuy=True):
        if idx == n:
            return 0

        if canBuy:
            buy = -prices[idx] + dp(idx + 1, not canBuy)
            hold = dp(idx + 1)
            return max(buy, hold)
        else:
            sell = prices[idx] + dp(idx + 1) - fee
            hold = dp(idx + 1, canBuy=False)
            return max(sell, hold)

    return dp()


print(maxProfit([1, 3, 2, 8, 13], 2))  # 10
print(maxProfit([1, 3, 7, 5, 10, 3], 3))  # 6
```

### [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv)
```python
def maxProfit(k, prices):
    n = len(prices)

    @cache
    def dp(idx=0, canBuy=True, limit=0):
        if idx == n or limit == k:
            return 0

        if canBuy:
            buy = -prices[idx] + dp(idx + 1, False, limit)
            hold = dp(idx + 1, True, limit)
            return max(buy, hold)
        else:
            sell = prices[idx] + dp(idx + 1, True, limit + 1)
            hold = dp(idx + 1, False, limit)
            return max(sell, hold)

    return dp()


print(maxProfit(2, [3, 2, 6, 5, 0, 3]))  # 7
```

## Game Theory
Requires us to memoize sub-problems' optimal results for every possible state in a competitive environment where multiple players make decisions. This approach helps determine the best strategy for each player involved.

In a game where two players take turns choosing numbers, Game Theory requires us to:
- Define the state as the current total and the set of available numbers.
- Evaluate each player's optimal move by recursively exploring all possible future states.
- Memoize results to avoid recomputation, ultimately returning the best outcome for the player whose turn it is.

### [Can I Win](https://leetcode.com/problems/can-i-win)
```python
def canIWin(maxChoosableInteger, desiredTotal):
    def getBit(x, k):
        return (x >> k) & 1

    def setBit(x, k):
        return x | (1 << k)

    if maxChoosableInteger >= desiredTotal:
        return True

    if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
        return False

    @cache
    def dp(total=0, seen=0):
        if total >= desiredTotal:
            return False

        for num in range(maxChoosableInteger, 0, -1):
            if getBit(seen, num - 1):
                continue
            newSeen = setBit(seen, num - 1)
            opponentCanWin = dp(total + num, newSeen)
            if not opponentCanWin:
                return True

        return False

    return dp()


print(canIWin(3, 5))  # True
print(canIWin(10, 0))  # True
print(canIWin(10, 11))  # False
print(canIWin(10, 20))  # True
print(canIWin(10, 21))  # True
```
<details>
<summary>Explanation</summary>

```python
canIWin(3, 5)
  └─ dp(0, 0)  # opponentCanWin = False -> Return True 
      ├─ dp(0 + 3 = 3, {3})  # opponentCanWin = True
      │   ├─ dp(3, {3})  # 3 In seen (SKIP)
      │   └─ dp(3 + 2 = 5, {2, 3})  # opponentCanWin = False
      │        └─ dp(5, {2, 3})  # return False (Base Case)
      ├─ dp(0 + 2 = 2, {2})  # opponentCanWin = True
      │   └─ dp(2 + 3 = 5, {2, 3})  # opponentCanWin = False (GET FROM CACHE)
      └─ dp(0 + 1 = 2, {1})  # opponentCanWin = False  <- (FOUND CASE)
          └─ dp(1 + 3 = 4, {1, 3})  # opponentCanWin = True  <- (FOUND CASE)
               ├─ dp(4, {1, 3})  # 3 In seen (SKIP)
               ├─ dp(4 + 2 = 6, {1, 2, 3})  # opponentCanWin = False
               │    └─ dp(6, {1, 2, 3})  # return False (Base Case)  <- (FOUND CASE)
               └─ dp(4, {1, 3})  # 1 In seen (SKIP)
```
</details>

Given `maxChoosableInteger = M` and `desiredTotal = N`
- TC: `O(2**M) * M`
  - **Number of States**: `O(2**M)` - Represent every possible game state (combinations set or subset).
  - **Work per State**: `O(M)` - For each game state, the algorithm may loop over all `M` integers to check which number to pick next.
  - Why not `O(2**M) * N`? 
    - A game state of `M` always map to a `total N`. Hence, caching just `M` is enough.
    - `N` is also cached just for ease of use in the base case. This would work just as fine
      - ```python
        def dp(total=0, seen=0):
            if seen in memo:
                return memo[seen]
            if total >= desiredTotal:
                return False
            ...
        ```
- SC: `O(2**M)`

## Dynamic Memoization
Requires us to memoize sub-problems' results on a dynamic data structure (eg. HashMap) to store intermediate results of sub-problems. 
- Can be used to prevent overriding the best optimal result for sub-problems that have already been solved, or to override the sub-problems result if a new optimal result is found, which is crucial when overlapping sub-problems occur. This ensures that the most optimal result for a sub-problem is preserved and can be re-used whenever needed.
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

    for idx, val in enumerate(arr1[1:], 1):
        tmpDp = {}
        for prev, operations in dp.items():
            if val > prev:
                tmpDp[val] = min(operations, tmpDp.get(val, inf))
            tmpIdx = bisect_right(arr2, prev)
            if tmpIdx < len(arr2):
                tmpDp[arr2[tmpIdx]] = min(1 + dp[prev], tmpDp.get(arr2[tmpIdx], inf))
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
