# Sorting
Sorting problems usually can be solved by borrowing ideas from sort algorithms

# Patterns
## Borrowing Idea from Selection Sort
### [Pancake Sorting](https://leetcode.com/problems/pancake-sorting)
```python
def pancakeSort(arr):
    ans = []

    def flip(rIdx, lIdx=0):
        ans.append(rIdx + 1)
        while lIdx < rIdx:
            arr[lIdx], arr[rIdx] = arr[rIdx], arr[lIdx]
            lIdx += 1
            rIdx -= 1

    r = len(arr)
    while r > 1:
        curMaxIndex = 0
        for i, num in enumerate(arr[1:r], 1):
            if num > arr[curMaxIndex]:
                curMaxIndex = i
        flip(curMaxIndex)
        flip(r - 1)
        r -= 1

    return ans


print(pancakeSort([3, 4, 2, 1]))

```

## Borrowing Idea from Merge Sort
### [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array)
```python
def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j = m - 1, n - 1
    last_item = len(nums1) - 1

    while j >= 0 and i >= 0:
        if nums2[j] >= nums1[i]:
            nums1[last_item] = nums2[j]
            last_item -= 1
            j -= 1
        else:
            nums1[last_item] = nums1[i]
            last_item -= 1
            i -= 1

    for i in range(j + 1):
        nums1[i] = nums2[i]


print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
```
