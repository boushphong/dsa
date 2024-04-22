# Recursion
## How to detect if a problem can be solved with recursion or not?
- When a problem can be divided to smaller problems.

**Hint:**
- Break it down to smaller problems.
- The base condition is represented by answer we already have
  - In the fibonacci problem, the answers we already have are:
  ```python
  fib(0) = 0
  fib(1) = 1
  ```
- Figure out out the recursive tree

```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)

                    fib(4)
                /           \
           fib(3)         fib(2)
         /       \       /       \
     fib(2)    fib(1)   fib(1)  fib(0)
    /      \
fib(1)   fib(0)
```

**Stack Trace: (From bottom to top)**
| Stack | Removal Order | Execution Order |
| --- | --- | --- |
| f(0) | 7th | 9th |
| f(1) | 6th | 8th |
| f(2) | 8th | 7th |
| f(1) | 4th | 6th |
| f(0) | 2nd | 5th |
| f(1) | 1st | 4th |
| f(2) | 3th | 3rd |
| f(3) | 5th | 2nd |
| f(4) | 9th | 1st |
    
## How to approach a recursion problem step by step?
1. Identify if you can break down problem into smaller problems
2. Write the recurrence relation
  - `F(n) = F(n-2) - F(n-1)` (Fibonacci)
3. Draw the recursive tree
4. Inspect the tree
  - See the flow of functions
  - How each function gets into the stack
  - Identify and focus on the left tree call then right tree call
  - Use the debugger to see the flow (or write it down with pen and paper)
5. See how the value is returned at each step and see where the function call will come out.

## Type of recurrence relation
1. Linear (Fibonacci)
2. Divide and Conquer (Binary Search)

## Binary Search with Recursion
Binary Search with Recursion is a Divide and Conquer problem. With recursion:
1. Compare the middle number with the target number. Constant time O(1)
2. Divide the array into 2 halfs and search one half recursively, discard the other half.

The recurrence relation would be.
- `F(N) = O(1) + F(N/2)` (Binary Search)
  - F(N): represents the time complexity of binary search on an array of size N
  - O(1): Comparision
  - F(N/2): Dividing the array into 2 halfs

**TIP:** Determine the variable of the:
1. Return type
2. Arguments: `low` and `high`, variables that are put in the function's argument will go the next recursive function call.
  - Put these variables (needed to go the next function call) to the function's argument 
4. Body of the function: `mid`, variable that are valuable in the function call only and you don't need to pass it to future recursive function.
  - You don't pass `mid` to the next function call, it is most useful to compare the `target` number. However, the `mid` variable does have its role to manipulate the parameter that will be passed to the next function call. 

```python
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Base case: target not found

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid  # Base case: target found at index mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)  # Search in the left half
    else:
        return binary_search_recursive(arr, target, mid + 1, high)  # Search in the right half
```

**NOTE:** We will `return` recursively to the parent function. It's the same as:
```python
def f1():
    return f2()

def f2():
    return f3()

def f3():
    return 3

f1() # return 3
```

# Patterns
## Single Argument 
```python3
# 123 -> 6
def sum_a_number(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_a_number(n // 10)
```

```python
from math import floor, log10, pow

# 12345 -> 54321
def reverse_a_number(n):
    if n // 10 == n:
        return n
    else:
        return int((n % 10) * pow(10, floor(log10(n)))) + reverse_a_number(n // 10)
```

```python
# 301200 -> 3
def count_zero_in_number(n):
    if n < 10:
        return 0
    else:
        return (1 if n % 10 == 0 else 0) + count_zero_in_number(n // 10)
```

```python
# 12321 -> True
# 1221 -> True
# 1211 -> False
def is_palindrome(number):
    # Base case: if the number has 0 or 1 digit, it is a palindrome
    if number < 10:
        return True

    # Get the number of digits in the number
    num_digits = floor(log10(number)) + 1

    # Extract the first and last digits
    first_digit = number // (10 ** (num_digits - 1))
    last_digit = number % 10

    # Check if the first and last digits are equal
    if first_digit == last_digit:
        # Recursively check the number without the first and last digits
        new_number = (number % (10 ** (num_digits - 1))) // 10
        return is_palindrome(new_number)
    else:
        return False
```

## Multiple Arguments 
```python
def check_sorted(array, i=0) -> bool:
    if i == len(array) - 1:
        return True
    else:
        return array[i] <= array[i + 1] and check_sorted(array, i+1)
```

```python
def linear_search(array, target, index=0):
    if array[index] == target:
        return index
    elif index == len(array) - 1:
        return -1
    else:
        return linear_search(array, target, index + 1)
```

```python
def binary_search_recursive(nums, target, l, r):
    if r < l:
        return -1
    m = (l + r) // 2
    if nums[m] == target:
        return m
    elif nums[m] < target:
        return binary_search_recursive(nums, target, m + 1, r)
    else:
        return binary_search_recursive(nums, target, l, m - 1)
```

## Multiple Arguments (with Carrying Argument) 
```python
def linear_search_all(array, target, index=0, nums=[]):
    if array[index] == target:
        nums.append(index)
    if index == len(array) - 1:
        return nums
    return linear_search_all(array, target, index + 1, nums)
```

## Multiple Arguments (with Result Carrying Variable) 
```python
def linear_search_all_without_num_param(array, target, index=0):
    nums = []
    if index == len(array):
        return nums
    if array[index] == target:
        nums.append(index)

    carry_nums = linear_search_all_without_num_param(array, target, index + 1)
    nums.extend(carry_nums)

    return nums
```

## Multiple Arguments (with Multiple Arguments Modification)
```python
# ***
# **
# *
def print_tri_back(r, c=0):
    if r == 0:
        return
    if c < r:
        print("*", end="")
        print_tri_back(r, c+1)
    else:
        print()
        print_tri_back(r-1, 0)

print_tri_back(3)
```

```python
s = "baccad"

def skipAChar(s, remove, l=0):
    if l == len(s):
        return ""
    if s[l] == remove:
        return skipAChar(s, remove, l+1)
    else:
        return s[l] + skipAChar(s, remove, l+1)

print(skipAChar(s, "a")) # bccd

```

### Bubble Sort
```python
array = [1, 5, 3, 2]

def bubble(arr, r, l=0):
    if r == 0:
        return
    if l < r:
        if arr[l] > arr[l + 1]:
            arr[l], arr[l + 1] = arr[l + 1], arr[l]
        bubble(arr, r, l + 1)
    else:
        bubble(arr, r - 1)

bubble(array, len(array) - 1)
print(array)
```

### Selection Sort
```python
# Throw largest number to the end
def selection(arr, r, l=0, max=0):
    if r == 0:
        return
    if l <= r:
        if arr[l] > arr[max]:
            selection(arr, r, l + 1, l)
        else:
            selection(arr, r, l + 1, max)
    else:
        arr[r], arr[max] = arr[max], arr[r]
        selection(arr, r - 1)

arr = [3,2,4]
selection(arr, len(arr) - 1)
```

## Multiple Arguments (with Multiple Arguments Modification) (Backward Execution)
Backward Execution is when you enter another nested recursion in the middle of the current function.

```python
# *
# **
# ***
def print_tri(r, c=0):
    if r == 0:
        return
    if c < r:
        print_tri(r, c+1)
        print("*", end="")
    else:
        print_tri(r-1, 0)
        print()

print_tri(3)
```

![image](https://github.com/boushphong/Recursion/assets/59940078/67551972-85ee-49d5-b06a-1a9f926025bb)

```python
s = "baccad"

def skipAChar(s, remove, l=0):
    if l == len(s):
        return ""
    st = skipAChar(s, remove, l+1)
    if s[l] == remove:
        return st
    else:
        return s[l] + st

print(skipAChar(s, "a")) # bccd
```

### Merge Sort
```python
def mergeSort(array):
    if len(array) == 1:
        return array

    m = len(array) // 2

    l = array[:m]
    r = array[m:]

    lp = mergeSort(l)
    rp = mergeSort(r)

    return merge(lp, rp)

def merge(lp, rp):
    result = []
    i = j = 0
    while i < len(lp) and j < len(rp):
        if lp[i] < rp[j]: 
            result.append(lp[i])
            i += 1
        else:
            result.append(rp[j])
            j += 1

    result += lp[i:]
    result += rp[j:]

    return result
```

### Merge Sort In Place
```python
def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        merge(arr, l, m, r)

def merge(arr, start, mid, end):
    start2 = mid + 1

    if arr[mid] <= arr[start2]:
        return

    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2

            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            start += 1
            mid += 1
            start2 += 1
```
![image](https://github.com/boushphong/Recursion/assets/59940078/f62e6119-b3e0-4e99-9df1-153c01485837)

# Complexity Analysis
## [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)
**Base Case**: F(i, 0) =  F(i, i) = 1 (Leftest and Rightest block will always be 1)

**Recurrence Relation**: F(i - 1, j - 1) + F(i - 1, j)

**TC**: O(N^2). 

Assuming numRows is N, at row i (by index) there are i + 1 blocks and There are N rows. At the last row at N - 1 (by index). 
We have to calculate: `(N) + (N - 1) + (N - 2) + ... + 1 = N * (N + 1)/2 = N^2` elements.

**SC**: O(N^2).
Since we store the result for every `(i, j)`.

We have to store: `(N) + (N - 1) + (N - 2) + ... + 1 = N * (N + 1)/2 = N^2` elements.
```python
def gernerate(numRows):
    @lru_cache(None)
    def F(i, j):
        if j == 0 or j == i:
            return 1
        return F(i - 1, j - 1) + F(i - 1, j)

    ans = []
    for i in range(numRows):
        ans.append([])
        for j in range(i + 1):
            ans[-1].append(F(i, j))
    return ans
```

## [Fibonacci Number](https://leetcode.com/problems/fibonacci-number)
**TC**: O(N)
At the first calculation `fib(n-1)`, we already cache all the result from `n - 1` to `1`. Any subsequents right call `fib(n - 2)` will access the cached result instantly. Hence the `O(N)` TC

**Recursive solution TC**: `O(N^2)`

**SC**: O(N)
At the first calculation `fib(n-1)`, we already cache all the result from `n - 1` to `1`. Hence we need to store `(n - 1)` results. Hence the `O(N)` SC

**Recursive solution SC**: `O(N)`

```python
@lru_cache(None)
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
```
