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
