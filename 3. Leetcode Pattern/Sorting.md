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
