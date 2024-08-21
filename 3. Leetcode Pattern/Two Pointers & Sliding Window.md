# Two pointers & Sliding window
# Patterns
## Sliding Window (Explading Window and Over Estimation)
### [Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element)
```python
def maxFrequency(nums, k):
    nums.sort()
    prefix_sum = list(accumulate(nums, initial=0))
    l, r = 0, 1

    for r, num in enumerate(nums[1:], 2):
        possible_increment = num * (r - l) - (prefix_sum[r] - prefix_sum[l])

        # if to overestimate the windows else while to shrink the windows
        if possible_increment > k:  
            l += 1

    return r - l

print(maxFrequency([1, 2, 4], 5))  # 3
print(maxFrequency([1, 4, 8, 13], 5))  # 2
```

### [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement)
```python
def characterReplacement(s, k):
    mapper = {}
    left = topFrequency = 0

    for right, rightChar in enumerate(s):
        mapper[rightChar] = mapper.get(rightChar, 0) + 1
        topFrequency = max(topFrequency, mapper[rightChar])

        if (right - left + 1) - topFrequency > k:
            leftChar = s[left]
            mapper[leftChar] -= 1
            left += 1

    return right - left + 1


print(characterReplacement("ABCBBAAAA", 2))
```

**Explanation**
- When we reduce the windows from `left, right = 1, 6` (**BCBBAA**) to `left, right = 2, 6` (**CBBAA**), we do not decrement the `topFrequency` variable because the `(right - left + 1)` keeps track of the maximum length of any valid window seen so far. As long as the condition `(right - left + 1) - topFrequency <= k` holds, the length of the current window is a candidate for the longest valid window. Even if we decrement the `topFrequency`, and update the windows, the windows' size will shrink, hence we would not get a bigger windows' size. We inherently over-estimate the `topFrequency` variable and never decrement it because we want to find the maximum windows' size, not calculing windows' size for every single window. In short, we will always maintain the maximum windows' size

## Tracking Max/Min of a Window
### [Maximum Sum of Two Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays)
```python
from itertools import accumulate


def maxSumTwoNoOverlap(nums, firstLen, secondLen):
    prefixSum = list(accumulate(nums, initial=0))

    def calc(a, b):
        ans = 0
        maxPartA = 0
        for i in range(a + b, len(prefixSum)):
            maxPartA = max(maxPartA, prefixSum[i - b] - prefixSum[i - b - a])
            curPartB = prefixSum[i] - prefixSum[i - b]
            ans = max(maxPartA + curPartB, ans)

        return ans

    first = calc(firstLen, secondLen)
    second = calc(secondLen, firstLen)

    return max(first, second)


print(maxSumTwoNoOverlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3))  # 31
print(maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 2, 1))  # 20
```

## Fixed Window
### [Minimum Swaps to Group All 1's Together](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together)
```python
def minSwaps(data):
    sumOfOnes = sum(data)

    windowCount1 = sum(data[0:sumOfOnes])
    ans = sumOfOnes - windowCount1

    for i in range(1, (len(data) - sumOfOnes) + 1):
        windowCount1 -= data[i - 1]
        windowCount1 += data[i + sumOfOnes - 1]
        ans = min(ans, sumOfOnes - windowCount1)

    return ans


print(minSwaps([1, 0, 0, 1, 0, 0, 1, 0, 1, 1]))  # 2
```

### [Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists)
```python
def smallestRange(nums):
    merged = []
    for i in range(len(nums)):
        merged.extend(zip(nums[i], [i] * len(nums[i])))

    merged.sort()
    visited = {}
    curRange = [merged[0][0], merged[-1][0]]
    curMax = merged[-1][0] - merged[0][0]

    l = 0
    for r, (v, k) in enumerate(merged):
        visited[k] = r

        while len(visited) == len(nums):
            tmpCurMax = v - merged[l][0]
            if tmpCurMax < curMax:
                curRange = [merged[l][0], v]
                curMax = v - merged[l][0]

            if l == visited.get(merged[l][1]):
                del visited[merged[l][1]]
            l += 1
    return curRange


print(
    smallestRange(
        [
            [4, 10, 15, 24, 26],
            [0, 9, 12, 20],
            [5, 18, 22, 30]
        ]
    )
)
```

## Updating Alternating Window
### [Count Binary Substrings](https://leetcode.com/problems/count-binary-substrings/)
```python
def countBinarySubstrings(s):
    consecutive = {"0": 0, "1": 0}
    l = ans = 0

    for r, v in enumerate(s):
        if v == s[l] and consecutive.get("1" if v == "0" else "0"):
            ans += min(consecutive.values())
            l = r - consecutive.get("1" if v == "0" else "0")
            consecutive[v] = 0

        consecutive[v] += 1

    ans += min(consecutive.values())
    return ans


print(countBinarySubstrings("000111000"))
```

## Sliding Window (Cyclic Array)
### [Rotate Function](https://leetcode.com/problems/rotate-function)
```python
from itertools import accumulate


def maxRotateFunction(nums):
    n = len(nums)
    endingIdx = n - 1
    sum_val = sum([nums[i] * i for i in range(n)])
    nums = nums + nums[:-1]
    preSum = list(accumulate(nums))

    ans = sum_val

    for idx, val in enumerate(nums[1:n], 1):
        sum_val += nums[idx + endingIdx] * endingIdx
        sum_val -= (preSum[idx + endingIdx - 1] - preSum[idx - 1])
        ans = max(sum_val, ans)

    return ans


print(maxRotateFunction([4, 5, 0, 6]))


"""
Double the array for sliding windows
0   4   9   9   15  19  24  24
    4   5   0   6   4   5   0 
        
    0   1   2   3
    0   5   0   18 = 23
        
        0   1   2   3                  
        0   0   12  12 = 24 or (23 + 4 * 3) - (15 - 4) = 35 - 11 = 24

            0   1   2   3
            0   6   8  15 = 29 or (24 + 5 * 3) - (19 - 9) = 39 - 10 = 29 

                0   1   2   3
                0   4   10  0 = 14 or (29 + 0 * 3) - (24 - 9) = 29 - 15 = 14
""" 
```
