# Two Pointers & Sliding Window
# Patterns (Two Pointers)
## Three Pointers
This approach keeps track of the minimum and maximum lengths of the window needed to solve the subarray counting problem.
### [Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/)
```python
def countSubarrays(nums, minK, maxK):
    ans = 0
    leftBound = lastMinK = lastMaxK = -1

    for i, num in enumerate(nums):
        if num < minK or nums[i] > maxK:
            leftBound = i
        if num == minK:
            lastMinK = i
        if num == maxK:
            lastMaxK = i

        if lastMinK > leftBound and lastMaxK > leftBound:
            ans += min(lastMinK, lastMaxK) - leftBound

    return ans


print(countSubarrays(nums=[1, 3, 1, 5, 5, 2], minK=1, maxK=5))  # 9
```


### [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers)
```python
def subarraysWithKDistinct(nums, k):
    res = lMin = lMax = 0
    cnt = Counter()

    for r, num in enumerate(nums):
        cnt[num] += 1

        while len(cnt) > k:
            cnt[nums[lMin]] -= 1
            if not cnt[nums[lMin]]:
                cnt.pop(nums[lMin])
            lMin += 1
            lMax = lMin
            
        while cnt[nums[lMin]] > 1:
            cnt[nums[lMin]] -= 1
            lMin += 1

        if len(cnt) == k:
            res += (lMin - lMax) + 1

    return res


print(subarraysWithKDistinct([1,2,1,2,3], 2))  # 7
```

### [Count of Substrings Containing Every Vowel and K Consonants II](https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii)
```python
def countOfSubstrings(word, k):
    vowels = {'a','e','i','o','u'}
    consonants = res = lMin = lMax = 0
    cnt = Counter()

    for r, letter in enumerate(word):
        if letter in vowels:
            cnt[letter] += 1
        else:
            consonants += 1

        while consonants > k:
            if word[lMin] in vowels:
                cnt[word[lMin]] -= 1
                if not cnt[word[lMin]]:
                    cnt.pop(word[lMin])
            else:
                consonants -= 1
            lMin += 1
            lMax = lMin
        
        while lMin < r and cnt[word[lMin]] > 1:
            if word[lMin] in vowels and cnt[word[lMin]] - 1:
                cnt[word[lMin]] -= 1
                lMin += 1
            else:
                break

        if len(cnt) == 5 and consonants == k:
            res += (lMin - lMax) + 1

    return res


print(countOfSubstrings("iqeaouqi", 2)))  # 3
```

# Patterns (Sliding Window)
## Expanding Window and Over Estimation
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

### [Reschedule Meetings for Maximum Free Time I](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i)
```python
def maxFreeTime(eventTime, k, startTime, endTime):
    startTime.extend([eventTime, 0])
    endTime.extend([eventTime, 0])
    res = total = 0
    l = -1

    for r, (start, end) in enumerate(zip(startTime, endTime)):
        prevEnd = endTime[r - 1]
        total += start - prevEnd
        if r - (l + 1) > k:
            lastEnd = endTime[l]
            lastStart = startTime[l + 1]
            total -= lastStart - lastEnd
            l += 1
        res = max(res, total)

    return res


print(maxFreeTime(34, 2, [0, 17], [14, 19]))  # 18
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

## Dynamic Window (Shrinking Window)
⚠️ Shrinking window pattern usually doesn’t work when negative numbers are involved. 
- This is especially true for problems where you’re trying to find a subarray with **sum >= target**. Since negative numbers can increase the sum when shrinking the window, the logic becomes unreliable.
- In such cases, prefer prefix sums, hash maps, or other techniques.
### [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/description/?envType=problem-list-v2&envId=apwwkhc6)
```python
def numSubarraysWithSum(nums, goal):
    l = consecutiveZeroes = total = res = 0

    # The sliding window [l, r] tracks a valid subarray (without leading zeroes) whose sum is at most goal.
    for r, num in enumerate(nums):
        total += num

        while l < r and (nums[l] == 0 or total > goal):
            if nums[l] == 1:
                consecutiveZeroes = 0
            else:
                consecutiveZeroes += 1

            total -= nums[l]
            l += 1

        if total == goal:
            res += 1 + consecutiveZeroes

    return res


print(numSubarraysWithSum([1,0,1,0,1], 2))  # 4
print(numSubarraysWithSum([0,0,1,0,0], 1))  # 9
print(numSubarraysWithSum([0,0,0,0,0], 0))  # 15
print(numSubarraysWithSum([0,0,0,0,0,0,1,0,0,0], 0))  # 27
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

## [Take K of Each Character From Left and Right](https://leetcode.com/problems/take-k-of-each-character-from-left-and-right)
```python
def takeCharacters(s, k):
    cnt = Counter(s)
    matches = sum(cnt.get(_, 0) >= k for _ in "abc")
    if matches < 3:
        return -1
    res = n = len(s)
    l = 0

    for r, letter in enumerate(s, n):
        while l < n and cnt[s[l]] - 1 >= k:
            cnt[s[l]] -= 1
            l += 1

        res = min(res, r - l)
        cnt[letter] += 1
    return res


print(takeCharacters("ccbabcc", 1))  # 4
```
