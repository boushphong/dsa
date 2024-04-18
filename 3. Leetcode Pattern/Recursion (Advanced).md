# Recursion (Advanced)
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
```python
subset_string("", "abc")                # 15
├── subset_string("a", "bc")            # 7
│   ├── subset_string("ab", "c")        # 3
│   │   ├── subset_string("abc", "")
│   │   │   └── ["abc"]                 # 1
│   │   └── subset_string("ab", "")
│   │       └── ["ab"]                  # 2
│   └── subset_string("a", "c")         # 6
│       ├── subset_string("ac", "")
│       │   └── ["ac"]                  # 4
│       └── subset_string("a", "")
│           └── ["a"]                   # 5
└── subset_string("", "bc")             # 14
    ├── subset_string("b", "c")         # 10
    │   ├── subset_string("bc", "")
    │   │   └── ["bc"]                  # 8
    │   └── subset_string("b", "")
    │       └── ["b"]                   # 9
    └── subset_string("", "c")          # 13
        ├── subset_string("c", "")
        │   └── ["c"]                   # 11
        └── subset_string("", "")
            └── []                      # 12
```
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
**Time Complexity:** `N!`

**Space Complexity:** `N!`
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
