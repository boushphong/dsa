# Monotonic Stack
Monotonic stacks are generally used for solving questions of the type - **next greater element**, **next smaller element**, **previous greater element** and **previous smaller element**.

# Table of Contents
* [Monotonic Stack](#monotonic-stack)
   * [What is monotonic stack?](#what-is-monotonic-stack)
   * [A Generic Template](#a-generic-template)
      * [Problems](#problems)
* [Patterns](#patterns)
   * [Prefix Patterns](#prefix-patterns)
   * [Over-estimation](#over-estimation)
   * [Sorting](#sorting)

## What is monotonic stack?

There could be four types of monotonic stacks.
- **Strictly increasing** - every element of the stack is strictly greater than the previous element. Example - [1, 4, 5, 8, 9]
- **Non-decreasing** - every element of the stack is greater than or equal to the previous element. Example - [1, 4, 5, 5, 8, 9, 9]
- **Strictly decreasing** - every element of the stack is strictly smaller than the previous element - [9, 8, 5, 4, 1]
- **Non-increasing** - every element of the stack is smaller than or equal to the previous element. - [9, 9, 8, 5, 5, 4, 1]

## A Generic Template
```python
def solveMonoStack(arr):
    stack = []
    for i in stack:
        while stack and (condition operation on the top of stack) ... stack[-1]:
            # If previous condition is satisfied, we pop the top element
            tmp = stack.pop()
            # Do something
            
    if len(stack):
        # if stack has some elements left
        # Do something with the stack top here.

    # Push the current index to the stack at the end
    stack.append(i)
```

Finding next greater and previous greater elements require building a monotone decreasing stack. For finding next smaller and previous smaller requires building a monotone increasing stack. To help you remember this, think of this as an inverse relation - **Greater requires Decreasing**, **Smaller requires Increasing stacks.**

### Problems
**Decreasing Stack Example:**
```python
def find_next_greater_indexes(arr: List[int]) -> List[int]:
    stack = []
    next_greater = [-1] * len(arr)
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            stack_top = stack.pop()
            next_greater[stack_top] = i
        
        stack.append(i)
    
    return next_greater
```

```python
def find_previous_greater_indexes(arr):
    stack = []
    previous_greater = [-1] * len(arr)
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        
        if stack:
            previous_greater[i] = stack[-1]
        
        stack.append(i)
    
    return previous_greater
```

# Patterns
## Prefix Patterns
We need more information about the current array before creating the stack and do a final iteration.

### [Find 132 Pattern](https://leetcode.com/problems/132-pattern/)

```python
def find132pattern(nums: List[int]) -> bool:
    """
    We find the last min element (From right to left) for every element in the array.
    If an element doesn't have first min, it means that the element is not worth considering
    because it won't be greater than the "1" part, hence we skip.
    """
    first_min = [None] * len(nums)
    minimum = float('inf')

    for i in range(len(nums)):
        if nums[i] > minimum:
            first_min[i] = minimum
        else:
            minimum = nums[i]

    stack = []
    for i, num in enumerate(nums):
        if first_min[i] is None:
            continue
        while stack and num >= stack[-1][1]:
            stack.pop()
        if stack and first_min[stack[-1][0]] < num < stack[-1][1]:
            return True

        stack.append((i, num))

    return False


print(find132pattern([3, 5, 0, 3, 2]))
print(find132pattern([3, 5, 0, 3, 4]))
```

### [Beautiful Towers I](https://leetcode.com/problems/beautiful-towers-i)
```python
def maximumSumOfHeights(maxHeights: List[int]) -> int:
    stack = []
    prev_smaller = [-1] * len(maxHeights)
    for i, num in enumerate(maxHeights):
        while stack and num <= stack[-1][1]:
            stack.pop()
        if stack:  # and num > stack[-1][1]:
            prev_smaller[i] = stack[-1][0]
        stack.append((i, num))

    stack.clear()

    next_smaller = [-1] * len(maxHeights)
    for i, num in enumerate(maxHeights):
        while stack and num < stack[-1][1]:
            next_smaller[stack.pop()[0]] = i
        stack.append((i, num))

    prefix_sum = [0] * len(maxHeights)
    for i, num in enumerate(maxHeights):
        if prev_smaller[i] == -1:
            prefix_sum[i] = num * (i + 1)
        else:
            prefix_sum[i] = num * (i - prev_smaller[i]) + prefix_sum[prev_smaller[i]]

    suffix_sum = [0] * len(maxHeights)
    for i, num in zip(range(len(maxHeights) - 1, -1, -1), reversed(maxHeights)):
        if next_smaller[i] == -1:
            suffix_sum[i] = num * (len(maxHeights) - i)
        else:
            suffix_sum[i] = num * (next_smaller[i] - i) + suffix_sum[next_smaller[i]]

    maximum = 0
    for i, num in enumerate(maxHeights):
        maximum = max(prefix_sum[i] + suffix_sum[i] - num, maximum)
    return maximum
```

### [Maximum Subarray](https://leetcode.com/problems/maximum-subarray)
```python
def maxSubArray(nums):
    preSum = [0] + list(accumulate(nums))
    ans = float("-inf")

    stack = []
    for num in preSum:
        if stack and num < stack[-1]:
            ans = max(ans, num - stack.pop())
        if stack:
            ans = max(ans, num - stack[-1])
        if not stack or num < stack[-1]:
            stack.append(num)

    return ans

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
```

For Maximum Subarray optimal solution, refer **Kadane’s Algorithm**.

## Over-estimation 
Don't push everything in the stack unless we really have to. 
This pattern usually push all the necessary elements into the stack first. Then another iteration will be used to gradually remove (all) elements in the stack, which means the stack's size will always be decreasing in the second iteration unlike other monotonic stacks patterns which the stack's size could vary because we dynamically remove and add elements into the stack under just one iteration.

### [Maximum Width Ramp](https://leetcode.com/problems/maximum-width-ramp/)
```python
def maxWidthRamp(nums: List[int]) -> int:
    """
    Maintaining stack in decreasing order, because if the next element is larger the previous element, we can omit it
    because adding it would be an over-estimation since the previous number is already small, hence it would provide
    larger width. We don't push 10 into the stack because it's not necessary to do so Since 9 < 10. pushing 10 into
    the stack would be an over-estimation
    """
    stack = []
    n = len(nums)
    for i in range(n):
        if not stack or nums[stack[-1]] > nums[i]:
            stack.append(i)

    ans = 0
    for i in range(n - 1, -1, -1):
        while stack and nums[i] >= nums[stack[-1]]:
            idx = stack.pop()
            ans = max(ans, i - idx)
    return ans

print(maxWidthRamp([9, 10, 6, 1, 2, 1, 7]))
```

### [Maximum Length of Semi-Decreasing Subarrays](https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays)
```python
def maxSubarrayLength(nums):
    stack = []
    for i, num in enumerate(nums):
        if not stack or (stack and num > nums[stack[-1]]):
            stack.append(i)

    ans = 0
    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[stack[-1]] > nums[i]:
            ans = max(ans, i - stack[-1] + 1)
            stack.pop()
    return ans


print(maxSubarrayLength([57, 55, 50, 60, 61, 58, 63, 59, 64, 60, 63]))  # 6
print(maxSubarrayLength([7, 6, 5, 4, 3, 2, 1, 6, 10, 11]))  # 8
```

## Sorting
Sort the sequece before proceeding

### [Car Fleet](https://leetcode.com/problems/car-fleet/)
```python
def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    cars_list = list(zip(position, speed))
    cars_list = sorted(cars_list, key=lambda x: x[0], reverse=True)
    stack = []

    for pos, spe in cars_list:
        till_finish_line = (target - pos) / spe
        if stack and till_finish_line <= stack[-1]:
            continue
        stack.append(till_finish_line)
    return len(stack)
```

## Left and Right Bound Index
### [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water)
```python
def trap(height):
    stack = []
    ans = 0
    for rIdx, rHeight in enumerate(height):
        while stack and rHeight > stack[-1][1]:
            _, tmpHeight = stack.pop()
            if stack:
                lIndex, lHeight = stack[-1][0], stack[-1][1]
                vol = min(rHeight, lHeight)
                ans += (rIdx - lIndex - 1) * (vol - tmpHeight)

        stack.append((rIdx, rHeight))

    return ans


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
```

### [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram)
```python
def largestRectangleArea(heights):
    stack = []
    ans = max(heights)
    for rIdx, rHeight in enumerate(heights + [0]):
        if stack and rHeight < stack[-1][1]:
            idx, height = stack.pop()
            volR = min(rHeight, height) * (rIdx - idx + 1)
            ans = max(ans, rHeight, volR)

            tmpIdx = idx
            while stack and rHeight < stack[-1][1]:
                tmpIdx, tmpHeight = stack.pop()
                volTmp = min(tmpHeight, height) * (idx - tmpIdx + 1)
                volR = rHeight * (rIdx - tmpIdx + 1)
                ans = max(ans, volTmp, volR)

            stack.append((tmpIdx, rHeight))
        stack.append((rIdx, rHeight))

    return ans


print(largestRectangleArea([2, 1, 5, 6, 2, 3]))
```
