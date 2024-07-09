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
print(characterReplacement("AABABBA", 2))
print(characterReplacement("ABBB", 2))
print(characterReplacement("ABCBBA", 3))
```
