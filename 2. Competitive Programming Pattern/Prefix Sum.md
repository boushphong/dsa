# Prefix Sum
# Table of Contents
* [Prefix Sum](#prefix-sum)
* [Patterns](#patterns)
   * [Prefix Sum + HashMap](#prefix-sum--hashmap)
   * [Prefix Sum + Kadane](#prefix-sum--kadane)
   * [Prefix + Suffix Technique](#prefix--suffix)
   * [Difference Array (Imos / Sweep Line)](#difference-array-with-line-sweep)

**Prefix sum** turns subarray queries into prefix-difference queries.

- Let `prefix[i] = sum(nums[0..i])`.
- Then `sum(nums[l..r]) = prefix[r] - prefix[l - 1]`.

When the problem asks for **number of subarrays** satisfying something about the sum, we can often count them in one pass by keeping a hashmap of previously seen prefix values (or prefix remainders).

# Patterns
## Prefix Sum + HashMap
1. Scan left to right and keep a running `prefix`.
2. Keep a hashmap `preSum` where `preSum[value] = how many times we've seen this prefix value so far`.
3. At each position, count how many previous prefixes would make the current subarray valid, add that to `res`, then record the current prefix into `preSum`.

Key pitfall:
- Initialize `preSum[0] = 1` so subarrays starting at index `0` are counted.

### [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
If `prefix[j] - prefix[i] = k`, then `prefix[i] = prefix[j] - k`.

```python
from collections import defaultdict

def subarraySum(nums, k):
    preSum = defaultdict(int)
    preSum[0] = 1
    prefix = res = 0

    for num in nums:
        prefix += num
        res += preSum[prefix - k]
        preSum[prefix] += 1
    return res
```

### [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)
```python
def subarraysDivByK(nums, k):
    preSum = defaultdict(int)
    preSum[0] = 1
    prefix = res = 0

    for num in nums:
        prefix += num
        mod = prefix % k
        res += preSum[mod]
        preSum[mod] += 1
    return res
```

## Prefix Sum + Kadane
Kadane's algorithm can be seen as a **Prefix Sum** variant.

Let `preSum[i] = sum(nums[0..i])`

So the maximum subarray sum for an index `i`:
- `max(preSum[i] - preSum[j])` for all `j < i`.

That means we can scan from left to right, maintaining:
- `minPrefix = min(preSum[0..i])`
- `ans = max(ans, preSum[i] - minPrefix)` for each `i`

### [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
```python
def maxSubArray(nums):
      res = -inf
      leftMin = preSum = 0

      for i, num in enumerate(nums):
          preSum += num
          res = max(res, preSum - leftMin)
          leftMin = min(leftMin, preSum)

      return res
```

### [Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)
Using the same idea, we can store the `maxPrefix` and `minWindow` to find the maximum sum of a circular subarray.

```python
def maxSubarraySumCircular(nums):
      curMax = -inf
      leftMax = minWindow = preSum = leftMin = 0

      for num in nums:
          preSum += num
          curMax = max(curMax, preSum - leftMin)
          leftMin = min(leftMin, preSum)
          leftMax = max(leftMax, preSum)
          minWindow = min(minWindow, preSum - leftMax)

      if preSum == minWindow:
          return curMax

      return max(curMax, preSum - minWindow)
```

## Prefix + Suffix
Use this when each index `i` needs an answer that depends on information from:

- The left side `[0..i]` (prefix aggregate), and/or
- The right side `[i..n-1]` (suffix aggregate)

Typical aggregates are `max`, `min`, `sum`, counts, etc.

1. Precompute a prefix aggregate array (ex: `preMax[i] = max(nums[0..i])`).
2. Traverse from the other side while maintaining a rolling suffix aggregate (or build a suffix array).
3. Combine prefix + suffix info in `O(1)` per index.

### [Jump Game IX](https://leetcode.com/problems/jump-game-ix/)
This problem can be solved in `O(N)` using:

- `preMax[i] = max(nums[0..i])`
- a rolling `sufMin = min(nums[i+1..n-1])` while scanning from right to left

```python
def jumpGameIX(nums):
    n = len(nums)

    preMax = [0] * n
    preMax[0] = nums[0]
    for i in range(1, n):
        preMax[i] = max(preMax[i - 1], nums[i])

    ans = [0] * n
    sufMin = inf
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            ans[i] = preMax[i]
        else:
            ans[i] = ans[i + 1] if preMax[i] > sufMin else preMax[i]

        sufMin = min(sufMin, nums[i])

    return ans
```

## Difference Array
Use this when you have many **range updates** like: "add `delta` to every index in `[l, r)`" and you want to recover the final values (or segments of constant value).

Difference array idea:
- Maintain `diff`, initially all zeros.
- For a range add on `[l, r)` do:
  - `diff[l] += delta`
  - `diff[r] -= delta`
- The actual value at position `i` is the prefix sum: `val[i] = val[i - 1] + diff[i]`.

### [Maximum Population Year](https://leetcode.com/problems/maximum-population-year/)
```python
def maximumPopulation(logs):
    earliest = 1950
    diff = [0] * 101

    for start, end in logs:
        diff[start - earliest] += 1
        diff[end - earliest] -= 1

    mostPopulatedYear = 9999
    cnt = runningCount = 0

    for year, val in enumerate(diff):
        runningCount += val
        
        if runningCount > cnt:
            mostPopulatedYear = year
            cnt = runningCount
        if runningCount >= cnt:
            mostPopulatedYear = min(year, mostPopulatedYear)

    return mostPopulatedYear + earliest
```

## Difference Array with Line Sweep
### [Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/)
```python
def minGroups(intervals):
    events = []

    for interval in intervals:
        events.append((interval[0], 1))
        events.append((interval[1] + 1, -1))

    events.sort(key=lambda x: (x[0], x[1]))

    res = maxGroup = 0
    for _, group in events:
        maxGroup += group
        res = max(
            res, maxGroup
        )

    return res
```

### [Describe the Painting](https://leetcode.com/problems/describe-the-painting/)
```python
def splitPainting(segments):
    mapping = defaultdict(int)
    for start, end, color in segments:
        mapping[start] += color
        mapping[end] -= color
        
    res = []
    prev, color = 0, 0
    for start in sorted(mapping):
        if color:
            res.append((prev, start, color))
        color += mapping[start]
        prev = start
        
    return res
```
