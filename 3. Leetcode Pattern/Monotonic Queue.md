# Monotonic Queue
Monotonic stacks are generally used for solving questions of the type - next greater element, next smaller element, previous greater element and previous smaller element. Likewise, **Monotonic Queue** can also be used to solve these kind of questions, but it excels at Finding the maximum or minimum element in a **Sliding Window**.

# Patterns
## Tracking Maximum/Mininum Element of a Fixed Sliding Window
### [Jump Game VI](https://leetcode.com/problems/jump-game-vi/)
Decreasing Monotonic Queue
```python
def maxResult(nums, k):
    res = nums[0]
    queue = deque([(res, 0)])

    for i, num in enumerate(nums[1:], 1):
        while queue[0][1] + k < i:
            queue.popleft()

        res = queue[0][0] + num

        while queue and res >= queue[-1][0]:
            queue.pop()
        queue.append((res, i))

    return res


print(maxResult([1, -1, -2, 4, 7, 3], 2))  # 14
print(maxResult([-123], 10))  # -123
```

### [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
Decreasing Monotonic Queue
```python
def maxSlidingWindow(nums, k):
    dq, res = deque(), []
    for i, num in enumerate(nums[:k]):
        while dq and num > nums[dq[-1]]:
            dq.pop()
        dq.append(i)

    res.append(nums[dq[0]])
    for i, num in enumerate(nums[k:], k):
        if dq and dq[0] <= i - k:
            dq.popleft()
        while dq and num > nums[dq[-1]]:
            dq.pop()

        dq.append(i)
        res.append(nums[dq[0]])
    return res


print(maxSlidingWindow([1, 2, 3, 4, 5, 6, 7, 8], 3))  # [3, 4, 5, 6, 7, 8]
print(maxSlidingWindow([4, 3, -1, -3, 5, 3, 6, 7], 3))  # [4, 3, 5, 5, 6, 7]
```

## Tracking Both Maximum and Mininum Element of a Sliding Window (Two Queues)
This pattern can also be solved by using the **Two Heaps** pattern. But the time complexity of the **Two Queues** pattern is more efficient at `O(N)`.
### [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)
```python
def longestSubarray(nums: List[int], limit: int) -> int:
    decrDeque = deque()
    incrDeque = deque()
    left = maxLength = 0

    for right, num in enumerate(nums):
        while decrDeque and num > decrDeque[-1]:
            decrDeque.pop()
        decrDeque.append(num)

        while incrDeque and num < incrDeque[-1]:
            incrDeque.pop()
        incrDeque.append(num)

        # Check if the current window exceeds the limit
        while decrDeque[0] - incrDeque[0] > limit:
            # Remove the elements that are out of the current window
            if decrDeque[0] == nums[left]:
                decrDeque.popleft()
            if incrDeque[0] == nums[left]:
                incrDeque.popleft()
            left += 1

        maxLength = max(maxLength, right - left + 1)

    return maxLength


print(longestSubarray([10, 1, 2, 4, 7, 2], 5))  # 4
print(longestSubarray([8, 4, 2, 7], 4))  # 2
```

### [Continuous Subarrays](https://leetcode.com/problems/continuous-subarrays/)
```python
def longestSubarray(nums):
    incDeque = deque()
    decDeque = deque()
    left = countSubarray = countDuplicateSubarray = 0

    for right, num in enumerate(nums):
        windowSize = 0
        while incDeque and num < incDeque[-1]:
            incDeque.pop()
        incDeque.append(num)

        while decDeque and num > decDeque[-1]:
            decDeque.pop()
        decDeque.append(num)

        while decDeque[0] - incDeque[0] > 2:
            if not windowSize:
                windowSize = right - left
                countSubarray += (windowSize * (windowSize + 1) // 2)
            if incDeque[0] == nums[left]:
                incDeque.popleft()
            if decDeque[0] == nums[left]:
                decDeque.popleft()
            left += 1

        if windowSize:
            duplicateWindow = (right - left)
            countDuplicateSubarray += (duplicateWindow * (duplicateWindow + 1)) // 2

    lastWindowSize = (right - left + 1)
    lastCountSubarray = (lastWindowSize * (lastWindowSize + 1)) // 2
    return countSubarray + lastCountSubarray - countDuplicateSubarray


print(longestSubarray([65, 66, 67, 66, 66, 65, 64, 65, 65, 64]))  # 43
print(longestSubarray([5, 4, 2, 4]))  # 8
```
