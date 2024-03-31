## [Find 132 Pattern](https://leetcode.com/problems/132-pattern/)
```python
def find132pattern(nums):
    """
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

## [Maximum Width Ramp](https://leetcode.com/problems/maximum-width-ramp/)
```python
def maxWidthRamp(nums: List[int]) -> int:
    """
    Maintaining stack in decreasing order we don't push 10 into the stack because it's not necessary to do so 
    Since 9 < 10. pushing 10 into the stack would be an over-estimation
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
