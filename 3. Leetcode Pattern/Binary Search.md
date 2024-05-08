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
