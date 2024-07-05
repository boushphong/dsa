# Big O Complexity
- `Time Complexity`: The amount of time the algorithm needs to run relative to the input size
- `Space Complexity`: The amount of memory allocated by the algorithm when run relative to the input size

When talking about complexity, there are normally three cases:

- Best case scenario
- Average case scenario
- Worst case scenario

We measure complexity by how the amount of operations/memory needed by the algorithm grows as the arguments tend to infinity. (as `N` grow to infinity). Because the variables are tending to infinity, **`Constants` are always ignored**. That means that **O(999N)** = **O(3N)** = **O(N)** = **O(N/5)** 
- Because 999 * Infinity = 3 * Infinity = Infinity = Infinity / 5

**NOTE:** Only **`Constants`** are ignored.
- O(3N) : 3 is a Constant hence O(N) 
- O(N) : 1 is a Constant
- O(N^2) : No Constant
- O(2^N) : No Constant
- O(logN) : No Constant
- O(N\*M) : No Constant

Example:
- **O(2^N + N^2 - 500N) = O(2^N)** because as N tends to Infinity, 2^N completely dominates the other two terms

![image](https://user-images.githubusercontent.com/59940078/235910304-7c9bef41-5d6c-4a3d-bd03-9192cea0aee3.png)
