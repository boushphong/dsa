# Two pointers & Sliding window
# Patterns
## Sliding Window (Over Estimation)
### [Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element)
```python
def maxFrequency(nums, k):
    nums.sort()
    prefix_sum = [0] + list(accumulate(nums))
    l, r = 0, 1

    for r, num in enumerate(nums[1:], 2):
        possible_increment = num * (r - l) - (prefix_sum[r] - prefix_sum[l])

        # if to overestimate the windows else while to shrink the windows
        if possible_increment > k:  
            l += 1

    return r - l

print(maxFrequency([1, 2, 4], 5))  # 3
print(maxFrequency([1, 4, 8, 13], 5))  # 2
```

### [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement)
```python
def characterReplacement(s, k):
    mapper = {}
    left = topFrequency = 0

    for right, rightChar in enumerate(s):
        mapper[rightChar] = mapper.get(rightChar, 0) + 1
        topFrequency = max(topFrequency, mapper[rightChar])

        if (right - left + 1) - topFrequency > k:
            leftChar = s[left]
            mapper[leftChar] -= 1
            left += 1

    return right - left + 1


print(characterReplacement("ABCBBAAAA", 2))
```

**Explanation**
- When we reduce the windows from `left, right = 1, 6` (**BCBBAA**) to `left, right = 2, 6` (**CBBAA**), we do not decrement the `topFrequency` variable because the `(right - left + 1)` keeps track of the maximum length of any valid window seen so far. As long as the condition `(right - left + 1) - topFrequency <= k` holds, the length of the current window is a candidate for the longest valid window. Even if we decrement the `topFrequency`, and update the windows, the windows' size will shrink, hence we would not get a bigger windows' size. We inherently over-estimate the `topFrequency` variable and never decrement it because we want to find the maximum windows' size, not calculing windows' size for every single window. In short, we will always maintain the maximum windows' size.
