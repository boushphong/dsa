# Difference Array
**Difference Array** technique is an efficient method for performing multiple range updates on an array in O(1) time per update, rather than O(n).

- Instead of updating every element in a range `[L, R]`, we mark only the boundaries of the change:
  - Add the value at the start of the range (index `L`)
  - Subtract the value after the end of the range (index `R+1`)
- Then, we compute a prefix sum to get the final array.

## Difference Array Example

**Original Array:** `[0, 1, 0, 0, 0]`, with size `n = 5`, we create a difference array of size `n + 1` initialized to `0`.

| 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |

**Operation 1:** Add `5` to range `[1, 3]`
Instead of: `[0, 5, 5, 5, 0, 0]` (requires updating 3 elements)

| 0 | 1 | 2 | 3 | 4  | 5 |
|---|---|---|---|----|---|
| 0 | 5 | 0 | 0 | -5 | 0 |

**Operation 2:** Subtract `2` to range `[2, 3]`

| 0 | 1 | 2  | 3 | 4  | 5 |
|---|---|----|---|----|---|
| 0 | 5 | -2 | 0 | -3 | 0 |

**Compute Prefix Sum** Compute the prefix sum to get the final array.

| 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 0 | 5 | 3 | 3 | 0 | 0 |

**Update Original Array:** `[0, 1, 0, 0, 0]` + `[0, 5, 3, 3, 0]` = `[0, 6, 3, 3, 0]`

| 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 0 | 6 | 3 | 3 | 0 |

## Analyzing Complexity
- **Time:** `O(n + k)`, where `n` is the size of the array and `k` is the number of range updates.
- **Space:** `O(n)`, for storing the difference array.

## Implementation

```python
def differenceArray(arr, updates):
    n = len(arr)
    diff = [0] * (n + 1)

    for l, r, val in updates:
        diff[l] += val
        if r + 1 < n:
            diff[r + 1] -= val

    for i in range(1, n):
        diff[i] += diff[i - 1]

    for i in range(n):
        arr[i] += diff[i]

    return arr
```
