# Two pointers & Sliding window
## Patterns
### [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement)
```python
def characterReplacement(s, k):
    mapper = {}
    left = longest = topFrequency = 0

    for right, rightChar in enumerate(s):
        mapper[rightChar] = mapper.get(rightChar, 0) + 1
        topFrequency = max(topFrequency, mapper[rightChar])

        while (right - left + 1) - topFrequency > k:
            leftChar = s[left]
            mapper[leftChar] -= 1
            left += 1

        longest = max(longest, right - left + 1)
        right += 1

    return longest


print(characterReplacement("ABCBBAAAA", 2))
```

**Explanation**
- When we reduce the windows from `left, right = 1, 6` (**BCBBAA**) to `left, right = 2, 6` (**CBBAA**), we do not decrement the `topFrequency` variable because the `longest` variable keeps track of the maximum length of any valid window seen so far. As long as the condition `(right - left + 1) - topFrequency <= k` holds, the length of the current window is a candidate for the longest valid window. Even if we decrement the `topFrequency`, and update the windows, the windows' size will shrink, hence we would not get a new updated `longest` variable. We inherently over-estimate the `topFrequency` variable and never decrement it because we want to find the maximum windows' size, not calculing windows' size for every single window.
