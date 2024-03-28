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

## [Find 132 Pattern](https://leetcode.com/problems/132-pattern/)
```python
def find132pattern(nums):
    """
    Decreasing Stack because the "3" part doesn't matter as much as the "2" part 
    as the "3" part is already larger than the "2" part.

    For this example: [0, 4, 2, 1, 5, 1]
    Any element that is popped out of the stack would be the "2" part because we want to keep the stack for the "3" part
    And if an element is popped out, it must be smaller that the "3" part.
    When we encounter 4. We popped 2 out from the stack, and 2 will become the new "3" part.
    ```
    max_third = {int} 2
    num = {int} 3
    nums = {list: 7} [0, 4, 2, 1, 5, 1]
    stack = {list: 2} [5, 4]
    ```
    If we do this, we will always know that the "2" part is smaller than the "3" part in the stack.
    When updating the "2" part this way, it will get bigger because when we encounter a new bigger (num) element, 
    the previous element in the stack will become the "2" part. Hence, finding the "1" part is easier.

    But only when we encounter 0, the last element when being iterated in reverse, we then know that we have a solution.
    But we don't know whether we are checking ( [0, 4, 2] , [0, 5, 1] , [0, 4, 1] ), this however doesn't matter because
    we know that we maximise the "2" part and "2" part is always smaller than the last element of the stack.
    """

    stack = []
    max_third = float("-inf")

    for num in reversed(nums):
        if num < max_third:
            return True

        while stack and num > stack[-1]:
            max_third = stack.pop()

        stack.append(num)
    return False


print(find132pattern([0, 4, 2, 1, 5, 1]))


def find132pattern(nums):
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


print(find132pattern([3, 5, 0, 5, 4, 7, 4]))
```
