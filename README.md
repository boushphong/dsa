# Read List
- [Substring](https://leetcode.com/problems/minimum-window-substring/solutions/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems/)
- [Dynamic Programming](https://leetcode.com/discuss/study-guide/458695/Dynamic-Programming-Patterns)
- [Backtracking](https://leetcode.com/problems/permutations/solutions/18239/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partioning))
- [Two pointers](https://leetcode.com/discuss/study-guide/1688903/Solved-all-two-pointers-problems-in-100-days)
- [Binary Search](https://leetcode.com/discuss/study-guide/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems)
- [Sliding Windows](https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1175088/C++-Maximum-Sliding-Window-Cheatsheet-Template/)
- [Graph](https://leetcode.com/discuss/study-guide/655708/Graph-For-Beginners-Problems-or-Pattern-or-Sample-Solutions)

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
