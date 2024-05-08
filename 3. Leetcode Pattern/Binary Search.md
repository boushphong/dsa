# Binary Search
**Binary search** is an efficient algorithm used for finding the position of a target value within a sorted array. It works by repeatedly dividing in half the portion of the list that could contain the target value, thereby reducing the search area by half each time. Binary search operates on the principle of divide and conquer.

- `TC`: `n * (1/2)^x = 1` -> `x = log2(n)` -> `O(LogN)`
- `SC`: `1`

**Searching a target**
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
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
