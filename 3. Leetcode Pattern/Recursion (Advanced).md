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

**Time Complexity**: `2^N`

Since every function call would recursive call 2 recursive calls (just like fibbonacci)

**Space Complexity**: `2^N`

`2^N` if we calculate the SC based on the `sub_left` + `sub_right` variable

`Len(string) ^ N` if we calculate the SC based on space of the input arguments of `string + subset`

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

![image](https://github.com/boushphong/Recursion/assets/59940078/16a9a3e4-7131-4ff9-8856-2549c3c0f0a1)

## Permutation
**Time Complexity**: `N!`

Iteration over Characters: The function iterates over each character in the input string string. The loop runs for each character in the string, resulting in a time complexity of O(N), where N is the length of the input string.

Recursion: For each character in the input string, the function recursively generates permutations of the remaining characters. Each recursive call reduces the size of the input string by 1. Therefore, for each character in the input string, there are N - 1 recursive calls (one for each remaining character after removing the current character). Since there are N characters in total, the total number of recursive calls is N * (N - 1) * ... * 1, which is N!.

Combining these factors, the overall time complexity is O(N!).

**Space Complexity**: `N!`

Permutation List: The algorithm maintains a list (permutation) to store all generated permutations. In the worst case, there can be N! permutations (where N is the length of the input string), so the space complexity for this part is O(N!).

Recursion Stack: As the function is recursive, there is additional space used on the call stack to keep track of function calls and their local variables. The maximum depth of recursion is equal to the length of the input string N.

Combining these factors, the overall space complexity remains O(N!) for the permutations list and O(N) for the recursion stack.
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
m = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

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
def letterCombinations(digits: str):
    current_solution = []
    ans = []

    def choose(i):
        if i == len(digits):
            ans.append("".join(current_solution))
            return

        for next_char in m.get(int(digits[i])):
            current_solution.append(next_char)

            choose(i + 1)

            current_solution.pop()

    choose(0)
    return ans
```

**TC**: `O(4^N)`

**Iteration over Digits**: The function iterates over each digit in the input string once. So, the time complexity for this part is `O(N)`, where `N` is the length of the input string.

**Recursion**: Inside the recursive function choose, for each digit, it explores all possible letters it maps to. The depth of recursion can be at most equal to the length of the input string. At each level of recursion, it explores at most 4 letters (the maximum number of letters a digit can map to, which is for digit 7 or 9). Hence, the time complexity of the recursive part is O(4^N), where N is the length of the input string.

Combining both, the overall time complexity of the function is `O(4^N) + O(N)`, where N is the length of the input string. Hence `O(N)` TC

**SC**: `O(4^N)`

`current_solution`: The current_solution list is used to keep track of the current combination of letters being built. At any given point in the recursion, this list holds at most N characters (where N is the length of the input string) as it grows and shrinks with the depth of the recursion.

`ans`: The ans list stores all the valid combinations of letters generated by the algorithm. Its size depends on the number of valid combinations, which can be at most 4^N, as each digit can map to up to 4 characters.

`Recursion Stack`: As the function is recursive, there is additional space used on the call stack to keep track of function calls and their local variables. The maximum depth of recursion is equal to the length of the input string N.

Combining these factors, the space complexity of the algorithm is:

    O(N) for the current_solution list.
    O(4^N) for the ans list.
    O(N) for the recursion stack.

So, the overall space complexity is `O(4^N + N +N)`. Hence `O(4^N)` SC
