# Sorting
Sorting problems usually can be solved by borrowing ideas from sort algorithms

## Implementing Merge Sort
```python
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    left_portion = mergeSort(arr[:m])
    right_portion = mergeSort(arr[m:])

    merged_portion = merge(left_portion, right_portion)

    return merged_portion


print(mergeSort([11, 5, 2, 6, 7, 9, 13]))
```

- **TC:** `O(N * Log(N))`
  - `Log(N)` is the depth of the recursive stack call. At each level, `N` operations are performed
- **SC:** `O(3N)` > `O(N)`
  - `3N` SC occurs at the last recursive stack call of the last branch and until the recursive call finishes.
```
  16
  / \
 8   8
    / \
   4   4
      / \
     2   2
        / \
       1   1
```

# Patterns
## Borrowing Idea from Selection Sort
### [Pancake Sorting](https://leetcode.com/problems/pancake-sorting)
- We continuously look for the largest element and throw it to the end of the array.
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

print(pancakeSort([3,2,4,1]))
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


print(merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))

print(merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[0, 0, 0], n=3))
# For at the end to hand the case where nums1 = [1,2,3,1,2,3]
```

## Borrowing Idea from Quick Sort
### [Sort Colors](https://leetcode.com/problems/sort-colors/)
- We throw every element less than 1 (equals to 0 in this case) to it's desired index first, then we do the same with 1
```python
def sortColors(nums):
    l = 0

    for r in range(1, len(nums)):
        if nums[r] == 0:
            while nums[l] == 0 and l < r:
                l += 1
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

    while l != len(nums) and nums[l] == 0:
        l += 1

    for r in range(l, len(nums)):
        if nums[r] == 1:
            while nums[l] == 1 and l < r:
                l += 1
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

    return nums


print(sortColors([2, 0, 2, 1, 1, 0]))
print(sortColors([0, 0, 0, 1, 1, 0]))
print(sortColors([0, 1]))
print(sortColors([0]))
```

## Borrowing Idea from Bucket Sort
### [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)
```python
def frequencySort(s):
    cur_max = 0
    mapper = {}
    for letter in s:
        new_increment = 1 + mapper.get(letter, 0)
        cur_max = max(cur_max, new_increment)
        mapper[letter] = new_increment

    # {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1}

    bucket = [[] for _ in range(cur_max + 1)]
    # [[], [], [], [], [], [], []]

    for c, freq in mapper.items():
        bucket[freq].append(c)
    # [[], ['a', 'b', 'c', 'd', 'e', 'f'], [], [], [], [], []]

    ans = []
    for freq in reversed(bucket):
        for letter in freq:
            ans.append(letter * mapper[letter])
    return "".join(ans)

print(frequencySort("abcdef"))
# Will do at most O(2N) operations to iterate through bucket
```

## Implementing a Custom Comparator
### [Largest Number](https://leetcode.com/problems/largest-number/)
```python
def largestNumber(nums):
    if min(nums) == 0 and max(nums) == 0:
        return "0"

    # Custom Comparator
    def compare(a, b):
        return str(a) + str(b) > str(b) + str(a)

    # Bubble Sort
    start = len(nums) - 1
    while start > 0:
        for i in range(start):
            if compare(nums[i], nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        start -= 1

    return "".join([str(num) for num in reversed(nums)])
```

