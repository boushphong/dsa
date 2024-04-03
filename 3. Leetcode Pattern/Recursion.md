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

```python
def skipAString(string, skip_string):
    if len(skip_string) > len(string):
        return string

    if string[0:len(skip_string)] == skip_string:
        return skipAString(string[len(skip_string):], skip_string)
    else:
        return string[0] + skipAString(string[1:], skip_string)


print(skipAString("abadapple", "apple")) # abad
print(skipAString("abadappleapplez", "apple")) # abadz
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

## Subset
### Subset String
```python
def subset_string(subset="", string=""):
    if not string:
        return [subset] if subset else []

    sub_left = subset_string(subset + string[0], string[1:])
    sub_right = subset_string(subset, string[1:])

    return sub_left + sub_right


print(subset_string(string="abc"))  # ['abc', 'ab', 'ac', 'a', 'bc', 'b', 'c']
```
![image](https://github.com/boushphong/Recursion/assets/59940078/a5637c3e-96a8-404e-9ee2-a049555ae38f)

### Subset String (Iterative Solution)
```python
def subset_string_iterative(string):
    unique_string_set = []

    for i in string:
        cp = unique_string_set.copy()
        for s in cp:
            unique_string_set.append(s + i)
        unique_string_set.append(i)
    return unique_string_set

print(subset_string_iterative("abc"))  # ['a', 'ab', 'b', 'ac', 'abc', 'bc', 'c']
```
**Logic**: Explore all the possible values at each iteration.

**Time Complexity**: `N * 2^N`
- `N`: Time it takes at each level.
- `2^N`: Number of subsets that would be created.

![image](https://github.com/boushphong/Recursion/assets/59940078/16a9a3e4-7131-4ff9-8856-2549c3c0f0a1)

## Permutation
### Permutation String

**Solution 1:**
```python
def get_permutation(subset, string):
    if not string:
        return [subset] if subset else []

    permutation = []
    for i in range(len(string)):
        current_char = string[i]
        remaining_chars = string[:i] + string[i + 1:]
        sub_permutations = get_permutation(subset + current_char, remaining_chars)
        permutation.extend(sub_permutations)

    return permutation


# Example usage:
input_string = "abc"
permutations = get_permutation('', input_string)
print(permutations)  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```
![image](https://github.com/boushphong/Recursion/assets/59940078/997736b8-7633-4bf2-ae69-eab7b47f9220)

**Solution 2:**
```python
def get_permutation(subset, string):
    if not string:
        return [subset] if subset else []

    char = string[0]
    permutation = []

    for i in range(len(subset) + 1):
        first_string = subset[:i]
        second_string = subset[i:]
        sub_permutations = get_permutation(first_string + char + second_string, string[1:])
        permutation.extend(sub_permutations)

    return permutation


# Example usage:
input_string = "abc"
permutations = get_permutation('', input_string)
print(permutations)  # ['cba', 'bca', 'bac', 'cab', 'acb', 'abc']
```
![image](https://github.com/boushphong/Recursion/assets/59940078/adcec105-2a74-4d8b-9df5-dfeabb378091)

### Permutation String (Counting Number of Permutations)
```python
def get_permutation(subset, string):
    if not string:
        return 1

    char = string[0]
    count = 0

    for i in range(len(subset) + 1):
        first_string = subset[:i]
        second_string = subset[i:]
        count = count + get_permutation(first_string + char + second_string, string[1:])

    return count


# Example usage:
input_string = "abc"
count = get_permutation('', input_string)
print(count)
```
![image](https://github.com/boushphong/Recursion/assets/59940078/b27f2212-cabb-4cee-845d-1437bb2e34ac)

### [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/)


```python
m = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

def letterCombinations(subset, digits):
    if not digits:
        return [subset] if subset else []

    char = digits[0]
    permutations = []

    string = m.get(int(char))

    if string:
        for s in string:
            sub_permutation = letterCombinations(subset + s, digits[1:])
            permutations.extend(sub_permutation)
    else:
        sub_permutation = letterCombinations(subset, digits[1:])
        permutations.extend(sub_permutation)

    return permutations
```

```python
def letterCombinations(subset, digits):
    if not digits:
        return 1 if subset else 0

    char = digits[0]
    count = 0

    string = m.get(int(char))

    if string:
        for s in string:
            sub_count = letterCombinations(subset + s, digits[1:])
            count += sub_count
    else:
        sub_count = letterCombinations(subset, digits[1:])
        count += sub_count

    return count


# Example usage:
input_string = "12341"
count = letterCombinations('', input_string)
print(count)
```

