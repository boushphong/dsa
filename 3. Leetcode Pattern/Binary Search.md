# Binary Search
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
    def feasible(capacity):
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
        if feasible(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


print(shipWithinDays([3, 2, 2, 4, 1, 4], 3))  # 6
```