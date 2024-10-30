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
    queue, res = deque(), []
    for i, num in enumerate(nums[:k]):
        while queue and num > nums[queue[-1]]:
            queue.pop()
        queue.append(i)

    res.append(nums[queue[0]])
    for i, num in enumerate(nums[k:], k):
        if queue and queue[0] <= i - k:
            queue.popleft()
        while queue and num > nums[queue[-1]]:
            queue.pop()

        queue.append(i)
        res.append(nums[queue[0]])
    return res


print(maxSlidingWindow([1, 2, 3, 4, 5, 6, 7, 8], 3))  # [3, 4, 5, 6, 7, 8]
print(maxSlidingWindow([4, 3, -1, -3, 5, 3, 6, 7], 3))  # [4, 3, 5, 5, 6, 7]
```

## Tracking Maximum/Mininum Element of a Dynamic Sliding Window
### [Maximum Number of Robots Within Budget](https://leetcode.com/problems/maximum-number-of-robots-within-budget/)
```python
def maximumRobots(chargeTimes, runningCosts, budget):
    l = res = 0
    curMax = deque()
    preSum = list(accumulate(runningCosts, initial=0))

    for r, charge in enumerate(chargeTimes):
        while curMax and chargeTimes[curMax[-1]] <= charge:
            curMax.pop()

        while curMax and curMax[0] < l:
            curMax.popleft()

        curMax.append(r)
        limit = chargeTimes[curMax[0]] + ((r - l + 1) * (preSum[r + 1] - preSum[l]))

        if limit <= budget:
            res = max(res, r - l + 1)
        else:
            l += 1

    return res


print(maximumRobots([3, 6, 1, 3, 4], [2, 1, 3, 4, 5], 25))  # 3
```

## Tracking Both Maximum and Mininum Element of a Sliding Window (Two Queues)
This pattern can also be solved by using the **Two Heaps** pattern. But the time complexity of the **Two Queues** pattern is more efficient at `O(N)`.
### [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)
```python
def longestSubarray(nums, limit):
    incDeque, decDeque = deque(), deque()
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
    incDeque, decDeque = deque(), deque()
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
