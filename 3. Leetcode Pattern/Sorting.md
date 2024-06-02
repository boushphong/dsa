# Sorting
Sorting problems usually can be solved by borrowing ideas from sort algorithms

# Table of Contents
* [Sorting](#sorting)
   * [Implementing Merge Sort](#implementing-merge-sort)
   * [Implementing Quick Select](#implementing-quick-select)
* [Patterns](#patterns)
   * [Borrowing Idea from Selection Sort](#borrowing-idea-from-selection-sort)
      * [<a href="https://leetcode.com/problems/pancake-sorting" rel="nofollow">Pancake Sorting</a>](https://leetcode.com/problems/pancake-sorting)
   * [Borrowing Idea from Merge Sort](#borrowing-idea-from-merge-sort)
      * [<a href="https://leetcode.com/problems/merge-sorted-array" rel="nofollow">Merge Sorted Array</a>](https://leetcode.com/problems/merge-sorted-array)
      * [Count Inversions](#count-inversions)
   * [Borrowing Idea from Quick Sort](#borrowing-idea-from-quick-sort)
      * [<a href="https://leetcode.com/problems/sort-colors/" rel="nofollow">Sort Colors</a>](https://leetcode.com/problems/sort-colors/)
   * [Borrowing Idea from Bucket Sort](#borrowing-idea-from-bucket-sort)
      * [<a href="https://leetcode.com/problems/sort-characters-by-frequency/" rel="nofollow">Sort Characters By Frequency</a>](https://leetcode.com/problems/sort-characters-by-frequency/)
      * [<a href="https://leetcode.com/problems/kth-largest-element-in-an-array/" rel="nofollow">Kth Largest Element in an Array</a>](https://leetcode.com/problems/kth-largest-element-in-an-array/)
   * [Borrowing Idea from Quick Select (Quick Sort)](#borrowing-idea-from-quick-select-quick-sort)
      * [<a href="https://leetcode.com/problems/kth-largest-element-in-an-array/" rel="nofollow">Kth Largest Element in an Array</a>](https://leetcode.com/problems/kth-largest-element-in-an-array/)
   * [Implementing a Custom Comparator](#implementing-a-custom-comparator)
      * [<a href="https://leetcode.com/problems/largest-number/" rel="nofollow">Largest Number</a>](https://leetcode.com/problems/largest-number/)

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

## Implementing Quick Select
- Move the **last element** of the array to its desired index (when sorted), with every element to the left smaller than the selected element and every element to the right larger than the selected element. Once done, return the index of the selected element.

**Choosing a fixed index**
```python
def partition(arr, l, r):
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

print(partition([15, 10, 4, 3, 20, 7], 0, 5))  # 2
# The array after modification: [4, 3, 7, 10, 20, 15]
```

- Move a **random element** of the array to its desired index (when sorted), with every element to the left smaller than the selected element and every element to the right larger than the selected element. Once done, return the index of the selected element.

**Choosing a random index**
```python
from random import randint


def partition(arr, l, r):
    # Choose a random pivot index and swap with the end
    pivot_index = randint(l, r)
    arr[pivot_index], arr[r] = arr[r], arr[pivot_index]

    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i
```

**Implemntation**

```python
def quick_select(arr, l, r, k):
    if l == r:
        return arr[l]

    pivot = partition(arr, l, r)
    if pivot == k:
        return arr[pivot]
    elif pivot < k:
        return quick_select(arr, pivot + 1, r, k)
    else:
        return quick_select(arr, l, pivot - 1, k)


print(quick_select([15, 10, 4, 3, 20, 7], 0, 5, 3))  # 10
# The array after modification: [4, 3, 7, 10, 15, 20]
```

- **TC (Average):** `O(2N)` - > `O(N)`
  - `O(2N)` every step, the array is divided in half hence `N/16 + N/8 + N/4 ... N/1 ~ 2N`.
- **TC (Worst):** `O(N**2))`
  - `O(N**2))` happens when the array is already sorted, hence selecting the last element always yield `pivot = r` and the next recursive call won't halve the arr but only decrement the pivot to 1 by `pivot = pivot - 1`.
- **SC:** `O(LogN)`
  - `O(LogN)` because the algorithm modifies the array in place, hence the depth of the recursion is the space.

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

### Count Inversions
Given an array of distinct integers, count the number of inversion pairs in the array.

An inversion pair (𝑖,𝑗) is defined as a pair of indices 𝑖,𝑗 such that:
- `0 ≤ i < j < n`
- `a[i] > a[j]`

For example:
Given the array: `a=[3,5,2,1,6]`
The result is `5` and the inversion pairs are
- `(3,2), (3,1), (5,2), (5,1), (2,1)`

```python
inv_count = 0


def merge_and_count(arr):
    global inv_count
    temp_arr = [0] * len(arr)
    left = 0  # Starting index for left subarray
    right = len(arr) - 1
    right_start = len(arr) // 2  # Starting index for right subarray
    left_end = right_start - 1
    cur_tmp_idx = left  # Starting index to be sorted in temp_arr

    # Merge the two portions of the array and count inversions
    while left <= left_end and right_start <= right:
        if arr[left] <= arr[right_start]:
            temp_arr[cur_tmp_idx] = arr[left]
            left += 1
        else:
            # arr[left] > arr[right_start] indicates inversions
            temp_arr[cur_tmp_idx] = arr[right_start]
            inv_count += (left_end - left) + 1  # Count inversions
            right_start += 1
        cur_tmp_idx += 1

    # Copy the remaining elements of left subarray, if any
    while left <= left_end:
        temp_arr[cur_tmp_idx] = arr[left]
        left += 1
        cur_tmp_idx += 1

    # Copy the remaining elements of right subarray, if any
    while right_start <= right:
        temp_arr[cur_tmp_idx] = arr[right_start]
        right_start += 1
        cur_tmp_idx += 1

    return temp_arr


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_portion = mergeSort(arr[:mid])
    right_portion = mergeSort(arr[mid:])

    merged_portion = merge_and_count(left_portion + right_portion)
    return merged_portion


def countInversions(arr):
    mergeSort(arr)
    return inv_count


print(countInversions([1, 3, 5, 2, 4, 6]))  # 3
# (3,2), (5,2), (5,4)
```

This utilizes the **Divide and Conquer** technique in **Merge Sort**. 
- When we split the portion into **left** and **right** portions, we already know that indices from the **left** portion are smaller than indices from the **right** portion.
- We recursively divide the array by half at each step, and increment the `inv_count` if there is any when we do `merge_and_count` and then sort the array.
-  Once a side is sorted, there won't be any inversion pairs from that portion. Then we escape the current function and return the result of the sorted array for the lower depth function call.

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

**Optimal**
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
    # [[], []]

    for c, freq in mapper.items():
        bucket[freq].append(c)
    # [[], ['a', 'b', 'c', 'd', 'e', 'f']]

    ans = []
    for freq in reversed(bucket):
        for letter in freq:
            ans.append(letter * mapper[letter])
    return "".join(ans)


print(frequencySort("abcdef"))
```

### [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
```python
from collections import Counter


def findKthLargest(nums, k):
    minimum = min(nums)
    absolute = (abs(minimum) + 1)
    if minimum < 0:
        nums = [num + absolute for num in nums]

    maximum = max(nums)

    cnt = Counter(nums)
    buckets = [None] * (maximum + 1)

    for item in cnt:
        buckets[item] = cnt.get(item)

    largest = 0
    for idx, count in zip(range(maximum, -1, -1), reversed(buckets)):
        if not count:
            continue

        largest += count
        if largest >= k:
            break

    return idx - absolute if minimum < 0 else idx


print(findKthLargest([-1, -1], 2))
print(findKthLargest([6, 5, 3, 3, 5, 2, 1, 2], 4))  # [1, 2, 2, 3, 3, 5, 5, 6] -> 3
```


## Borrowing Idea from Quick Select (Quick Sort)
### [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
```python
from random import choice


def findKthLargest(nums, k):
    if not nums:
        return
    pivot = choice(nums)
    greater = [x for x in nums if x > pivot]
    equal = [x for x in nums if x == pivot]
    smaller = [x for x in nums if x < pivot]

    lenGreater, lenEqual = len(greater), len(equal)

    if k <= lenGreater:
        return findKthLargest(greater, k)
    elif k > lenEqual + lenGreater:
        return findKthLargest(smaller, k - lenGreater - lenEqual)
    else:
        return equal[0]


print(findKthLargest([0, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1], 1))
```
**TC** and **SC** are `O(2N)` > `O(N)`

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
