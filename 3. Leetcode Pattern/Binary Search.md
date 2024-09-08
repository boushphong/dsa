# Binary Search
# Table of Contents
* [Binary Search](#binary-search)
   * [Bisecting](#bisecting)
      * [Bisect Left (Lower Bound)](#bisect-left-lower-bound)
      * [Bisect Right (Upper Bound)](#bisect-right-upper-bound)
   * [Identifying a possible Binary Search solution](#identifying-a-possible-binary-search-solution)
      * [<a href="https://leetcode.com/problems/sqrtx/" rel="nofollow">Sqrt(x)</a>](https://leetcode.com/problems/sqrtx/)
      * [<a href="https://leetcode.com/problems/first-bad-version/" rel="nofollow">First Bad Version</a>](https://leetcode.com/problems/first-bad-version/)
* [Patterns](#patterns)
   * [Bisecting](#bisecting-1)
   * [Rotated Array Search](#rotated-array-search)
   * [Identifying BS (Monoticity)](#identifying-bs-monoticity)
   * [Identifying BS (Exclusive Search and Inclusive Search)](#identifying-bs-exclusive-search-and-inclusive-search)

**Binary search** is an efficient algorithm used for finding the position of a target value within a sorted array. It works by repeatedly dividing in half the portion of the list that could contain the target value, thereby reducing the search area by half each time. Binary search operates on the principle of divide and conquer.

- `TC`: `n * (1/2)^x = 1` > `x = log2(n)` > `O(LogN)`
- `SC`: `1`

**Searching a target**
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2  # Use this instead of (left + right) // 2 to avoid integer overflow
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## Bisecting
**Bisecting**, in the context of computer science and mathematics, refers to the method of dividing a range or dataset into two parts (halves) to quickly locate a specific value or the insertion point for a new value, ensuring that the dataset remains sorted.

**Bisecting in Python**
- `bisect_left(a, x)`: Finds the index where `x` should be inserted in the list `a` to maintain sorted order. If `x` is already present, the function returns the index before which `x` can be inserted to maintain the sorted order (leftmost insertion point).
- `bisect_right(a, x)` or `bisect(a, x)`: Similar to `bisect_left`, but if `x` is already present, it returns the index after which `x` can be inserted (rightmost insertion point).

### Bisect Left (Lower Bound)
```python
from bisect import bisect_left

array = [1,2,4,4,7]

# Insert a value into a sorted array. What would the new element index would be?
bisect_left(array, 2)  # 1
bisect_left(array, 0)  # 0 since 0 < 1 (the first element)
bisect_left(array, 3)  # 2 since 3 > 2
bisect_left(array, 8)  # 5 since 8 > 7 (the last element)
bisect_left(array, 4)  # 2 since 4 already exists, it will insert into the place of the first occurance of number 4. 
```

**Underlying implementation of Lower Bound bisect_left**
```python
def lowerBound(nums, target):
    left, right = 0, len(nums) - 1
    ans = len(nums)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans
```

### Bisect Right (Upper Bound)

```python
from bisect import bisect_right

array = [1,2,4,4,7]

# Insert a value into a sorted array. What would the new element index would be?
bisect_right(array, 2)  # 2
bisect_right(array, 4)  # 4
bisect_right(array, 4)  # 4
bisect_right(array, 3)  # 2
bisect_right(array, 0)  # 0
bisect_right(array, 8)  # 5
```

**Underlying implementation of Upper Bound bisect_right**
```python
def upperBound(nums, target):
    left, right = 0, len(nums) - 1
    ans = len(nums)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:  # While Lower Bound uses >=
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans
```

## Identifying a possible Binary Search solution
More often than not, there are situations where the search space and search target are not so readily available.
- If we can discover some kind of monotonicity, for example, if `condition(k)` is True then `condition(k + 1)` might be True as well, then we can consider binary search.
- What makes binary search work is that there exists a **function** that can map elements in left half to True, and the other half to False, or vice versa. If we can find such a function, we can apply binary search to find the boundary.
- If the problem can be converted into "the minimum number satisfying condition x" or "the maximum number satisfying condition x".

### [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
```python
def mySqrt(x: int):
    l = 0
    r = x // 2 if x != 1 else 1
    ans = None

    while l <= r:
        m = l + (r - l) // 2
        if m * m <= x:
            ans = m
            l = m + 1
        else:
            r = m - 1

    return ans

print(mySqrt(10))
"""
10
0 1 2 3 4 5
l = 0
r = 5

m = 2 (index 2)
update answer = 2 (4 <= 9)
...

3 4 5
l = 3
r = 5

m = 4 (index 4)
continue since (16 > 9)
...

3
3
m = 3 (index 3)
update answer = 3 (9 <= 9)
...

End of iteration
"""
```

In the example above, in the first iteration, we discover a possible answer which is `2`, but there might possible answer as well hence we keep searching for the closest answer.

### [First Bad Version](https://leetcode.com/problems/first-bad-version/)
```python
def firstBadVersion(n: int) -> int:
    l, r = 1, n
    while l < r:
        m = (l + r) // 2
        if isBadVersion(m):
            r = m
        else:
            l = m + 1
    return r

"""
Assuming the first bad version is 1, and there are n (4) versions.

n = 4
1 2 3 4
l = 0, r = 3
m = 1 (value = 2)
isBadVersion(True)

1 2
l = 0, r = 1
m = 0 (value = 1)
isBadVersion(True)

1
l = 0, r = 0
Break iteration

Return r

-----------------------------------------------------------------
Assuming the first bad version is 4, and there are n (4) versions.

n = 4
1 2 3 4
l = 0, r = 3
m = 1 (value = 2)
isBadVersion(False)

3 4
l = 2, r = 3
m = 2 (value = 3)
isBadVersion(False)

4
l = 3, r = 3
Break iteration

Return r
"""
```

# Patterns
## Bisecting
### [Heaters](https://leetcode.com/problems/heaters/)
```python
def findRadius(houses, heaters):
    houses.sort()
    radius = -1

    for house in houses:
        pos = bisect_right(heaters, house)
        if pos == 0:
            radius = max(radius, heaters[pos] - house)
        elif pos == len(heaters):
            radius = max(radius, house - heaters[pos - 1])
        else:
            left_radius = house - heaters[pos - 1]
            right_radius = heaters[pos] - house
            min_between_radius = min(left_radius, right_radius)
            radius = max(radius, min_between_radius)

    return radius


print(findRadius([1, 2, 3], [2])
print(findRadius([1, 2, 3, 4], [1, 4])
```

### [Minimum Array Changes to Make Differences Equal](https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal)
```python
from collections import defaultdict
from bisect import bisect_left


def minChanges(nums, k):
      frequencyMap = defaultdict(int)
      l, r = 0, len(nums) - 1
      pairRanges = []

      while l < r:
          diff = abs(nums[l] - nums[r])
          frequencyMap[diff] += 1

          maxNum = max(nums[l], nums[r])
          maxRangeExtension = k - min(nums[l], nums[r])
          pairRanges.append(max(maxNum, maxRangeExtension))
          l += 1
          r -= 1

      noPairs = len(pairRanges)
      pairRanges.sort()

      minChanges = float('inf')
      for X, occurrence in frequencyMap.items():
          needsDoubleReplacementPairs = bisect_left(pairRanges, X)
          needsSingleReplacementParis = noPairs - occurrence - needsDoubleReplacementPairs
          minChanges = min(minChanges, needsDoubleReplacementPairs * 2 + needsSingleReplacementParis)

      return minChanges



print(minChanges(nums=[1, 0, 1, 2, 4, 3], k=4))  # 2
"""Idea is to gather all the possible X values first. In the case above, {2: 1, 4:1, 1:1} Then we find out the 
maximum expand range of every pair: [3, 4, 3] 
- pair (1 3) have a maximum expand range of 3 because  
    - 3 can be replaced with k = 4 (4 - 1 = 3) 
- pair (0 4) have a maximum expand range of 4 because
    - A number can be replaced with it self hence expand range is still (4 - 0 = 4)
- pair (1 2) have a maximum expand range of 3 because
    - 2 can be replace with k = 4 (4 - 1 = 3)
    
Once maximum expand range for every pair is found, we sort this windows: [3, 3, 4]. Since we have every X candidates: 
{2: 1, 4: 1, 1: 1}. We perform binary search (bisecting) on the this windows.

For example:
- bisecting left 2 into the windows give 0. This means that no double replace operations has to be performed. Since
    this window can replace just 1 element of the pair. 

- bisecting left 4 into the windows give 2. This means that 2 double replace operations has to be performed. Since
    both maximum expand range of [3, 3] are smaller than 4. Both pairs has to replace all 2 elements in their pairs
"""
```

### [Minimum Absolute Sum Difference](https://leetcode.com/problems/minimum-absolute-sum-difference/)
```python
def minAbsoluteSumDiff(nums1, nums2):
    n = len(nums1)
    diff = [abs(num1 - num2) for num1, num2 in zip(nums1, nums2)]
    nums1.sort()

    total = ans = sum(diff)
    for i, num2 in enumerate(nums2):
        numDiff = diff[i]
        idxNum1 = bisect_left(nums1, num2)

        if idxNum1 < n:
            ans = min(ans, total - numDiff + abs(nums1[idxNum1] - num2))
        if idxNum1 > 0:
            ans = min(ans, total - numDiff + abs(nums1[idxNum1 - 1] - num2))

    return ans % (10 ** 9 + 7)


print(minAbsoluteSumDiff([1, 7, 6], [1, 3, 6]))  # 2
```

### [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence)
```python
from bisect import bisect_left


def lengthOfLIS(nums):
    if not nums:
        return 0
    stack = []

    for num in nums:
        if (stack and num > stack[-1]) or not stack:
            stack.append(num)
            continue

        pos = bisect_left(stack, num)
        stack[pos] = num

    return len(stack)


print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 1, 2, 3, 10, 4, 5]))  # 5
```

### [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
```python
def eraseOverlapIntervals(intervals):
    tails = []
    intervals.sort()

    for start, end in intervals:
        if not tails or start >= tails[-1]:
            tails.append(end)
            continue

        index = bisect_left(tails, start)
        tails[index] = min(tails[index], end)

    return len(intervals) - len(tails)


print(eraseOverlapIntervals([[1, 2], [1, 5], [2, 3], [3, 4]]))  # 1
print(eraseOverlapIntervals([[1, 8], [4, 5], [3, 4], [2, 9]]))  # 2
print(eraseOverlapIntervals([[1, 7], [5, 10], [6, 7], [7, 8], [8, 9]]))  # 1
```

### [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes)
```python
from bisect import bisect_left


def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    # find the longest increasing subsequence
    stack = []

    for _, height in envelopes:
        if (stack and height > stack[-1]) or not stack:
            stack.append(height)
            continue

        pos = bisect_left(stack, height)
        stack[pos] = height

    return len(stack)


print(maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3], [2, 4]]))  # 3
print(maxEnvelopes([[2, 10], [3, 20], [4, 30], [5, 50], [5, 40], [5, 25], [6, 37], [6, 36], [7, 38]]))  # 5
```


## Rotated Array Search
### [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array)
```python
def search(nums, target) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m

        if nums[l] <= nums[m]:  # Use <= instead of < here to handle the case where search element is the second index (index 1) in a two element search space
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        else:
            if target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1

    return -1


print(search([2, 3, 4, 5, 1], 5))  # nums[l] <= nums[m] and target > nums[m]
print(search([2, 3, 4, 5, 1], 1))  # nums[l] <= nums[m] and target < nums[l]
print(search([2, 3, 4, 5, 1], 3))  # else

print(search([5, 1, 2, 3, 4], 1))  # nums[l] < nums[m] and target < nums[m]
print(search([5, 1, 2, 3, 4], 5))  # nums[l] < nums[m] and target > nums[r]
print(search([5, 1, 2, 3, 4], 4))  # else

# Handle the case where nums[l] <= nums[m] and the search element is the second index (index 1) 
# in a two element search space
print(search([0, 1], 1))  # target > nums[m]
print(search([5, 1], 1))  # target < nums[l]
```

### [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array)
```python
def findMin(nums):
    res = float("inf")
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = l + (r - l) // 2
        res = min(res, nums[m])
        if nums[l] <= nums[m]:
            res = min(res, nums[l])
            l = m + 1
        else:
            r = m - 1
    return res


print(findMin([3, 4, 5, 1, 2]))
print(findMin([5, 1, 2, 3, 4]))
print(findMin([3, 1, 2]))
```

## Identifying BS (Monoticity)
### [Arranging Coins](https://leetcode.com/problems/arranging-coins)
Monoticity: More coins hence more rows, less coins hence less rows and vice versa.
```python
def arrangeCoins(n):
    def calCoinsByRows(row):
        return (row * (row + 1)) // 2

    ans = 0
    l, r = 1, n
    while l <= r:
        m = (l + r) // 2
        coins = calCoinsByRows(m)
        if coins > n:
            r = m - 1
        else:
            l = m + 1
            ans = m
    return ans
```
- **TC** = `O(LogN)`
- **SC** = `O(1)`
However, the TC could be a bit more optimized since we can estimate the upper bound of `r` (current `r` equals to `nRows` hence unnecessary iterartion).
- Since `(nRow * (nRow + 1)) // 2` equals to the number of coins needed to build `nRow`
- `(nRow ** 2) + nRow ~ 2*n`, discarding the `nRow` by itself because of insignificancy.
- We got `nRow ** 2 ~ 2*n`, hence `nRow = ceil(sqrt(2*n))`

```python
def arrangeCoins(n):
    ...
    l, r = 1, ceil(sqrt(n ** 2))
    ...
```

## Identifying BS (Exclusive Search and Inclusive Search)
### [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets)
**Monoticity**: More days needed to wait hence more bouquets.

**Intuition**: We search non-existant day regardless, as long as it reaches the value within the `bloomDay`. we might search days that are not within `bloomDay` (**Exclusive Search**).

```python
def minDays(bloomDay, m, k):
    left, right = min(bloomDay), max(bloomDay)
    ans = -1

    def calcBouquets(dayAt):
        countAdjFlowers = 0
        countBouquets = 0

        for day in bloomDay:
            if day <= dayAt:
                countAdjFlowers += 1
            else:
                countBouquets += countAdjFlowers // k
                countAdjFlowers = 0

        countBouquets += countAdjFlowers // k
        return countBouquets

    while left <= right:
        mid = (left + right) // 2
        if calcBouquets(mid) >= m:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


print(minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))  # 12
"""
Bouquets 1 at 7 7 7
Bouquets 2 at 7 12 7
"""
```
- **TC** = `O(N(Find min max) + (Log MAX BloomDay * N(from calcBouquets))) = O(Log MAX BloomDay * N)`
- **SC** = `O(1)`

In this example, even when we search `9` in our first iteration, which will return a valid answer but not within the `bloomDay` list. It will reach `7` because we have specified `left, right = 7, 12` hence if `9` is a valid answer, `7` will be reached and also provide a valid answer.

### [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days)
**Monoticity**: More weight hence lower required days to ship. 

**Intuition**: We search for minium weight without looking into a specific combination that sums up to the minium weight within `weights`. We search from range of `max(weights)` to `sum(weights)` because `max(weights)` will return `len(weights)` days (might be invalid) and `sum(weights)` will return 1 days (**Inclusive Search**)

```python
def shipWithinDays(weights, days):
    def isFeasible(capacity):
        tmp_weight = 0
        ship_within_days = 1
        for weight in weights:
            tmp_weight += weight
            if tmp_weight > capacity:
                tmp_weight = 0
                ship_within_days += 1
                if ship_within_days > days:
                    return False
                tmp_weight += weight
        return True

    ans = 0
    left, right = max(weights), sum(weights)
    while left <= right:
        mid = left + (right - left) // 2
        if isFeasible(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


print(shipWithinDays([3, 2, 2, 4, 1, 4], 3))  # 6
```

### [Maximize Score of Numbers in Ranges](https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/)
```python
def maxPossibleScore(start, d):
    start.sort()
    l, r = 0, start[-1] + d

    def isFeasible(score):
        cur = start[0]
        for i, num in enumerate(start[1:], 1):
            cur += score
            if cur < num:
                cur = num
            if cur > num + d:
                return False
        return True

    ans = -1
    while l <= r:
        m = l + (r - l) // 2
        if isFeasible(m):
            ans = m
            l = m + 1
        else:
            r = m - 1
    return ans


print(maxPossibleScore([6, 0, 3], 2))  # 4
print(maxPossibleScore([2, 6, 13, 13], 5))  # 5
```

### [Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/)
```python
def maxDistance(position, m):
    position.sort()
    ans = 0

    def isFeasible(force):
        mx = 1
        cur_force = position[0]
        for basket in position[1:]:
            if basket - cur_force >= force:
                mx += 1
                cur_force = basket
            if mx == m:
                return True
        return False

    left, right = 0, max(position)

    while left <= right:
        mid = (left + right) // 2
        if isFeasible(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans


print(maxDistance([1, 2, 3, 4, 6, 7, 10], 4))  # 3
"""
1   2   3   4   5   6   7   8   9   10
1   2   3   4       6   7           10
m = 4, ans = 3
"""

print(maxDistance([5, 4, 3, 2, 1, 100], 2))  # 99

print(maxDistance([79, 74, 57, 22], 4))  # 5
```
