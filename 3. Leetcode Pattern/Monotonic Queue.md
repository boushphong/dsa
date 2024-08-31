# Monotonic Queue
Monotonic stacks are generally used for solving questions of the type - next greater element, next smaller element, previous greater element and previous smaller element. Likewise, **Monotonic Queue** can also be used to solve these kind of questions, but it excels at Finding the maximum or minimum element in a **Sliding Window**.

# Patterns
## Tracking Maximum/Mininum Element of a Fixed Sliding Window.
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
