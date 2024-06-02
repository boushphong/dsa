# Heap
## What is a Heap?
A **Heap** is a complete binary tree structure that satisfies the following properties:
- In a **Min Heap**, the value of each node is smaller than or equal to the values of its children.
- In a **Max Heap**, the value of each node is greater than or equal to the values of its children.

**Min Heap**
```python
      1
     / \
    3   2
   / \ / 
  4  6 5
```

**Max Heap**
```python
      6
     / \
    5   3
   / \ /
  4  2 1
```

# Heap Structure (Array)
- If a heap has **N** elements:
  - Indices from **N//2 to N-1** are leaf nodes.
  - Indices from **0 to N//2-1** are internal nodes.

- For a node with index **i**:
  - Index of the left child: **2*i + 1**
  - Index of the right child: **2*i + 2**
  - Index of the parent: **(i-1)//2**

## Visual Representation of the Heap
```python
        1 (0)
       /   \
     3 (1)  6 (2)
    / \    / 
  5 (3) 9 (4) 8 (5)

# Array Representation of the Heap

Index:  0  1  2  3  4  5
Value:  1  3  6  5  9  8
```

## Operations on Heap
1. `heapify(arr)`: Build a heap from an array; **O(N)**
2. `push(arr, x)`: Add an element `x` to the heap; **O(logN)**
3. `pop(arr)`: Remove the top element (smallest or largest) from the heap; **O(logN)**
4. `top(arr)`: Retrieve the top element (smallest or largest) of the heap; **O(1)**

### 1. Heapify
- **Heapify** is a process that ensures a binary tree maintains the heap properties.
- **Heapify** can be performed at any node to preserve the heap properties when there is a change in the node's value.
- There are two common types of heapify:
  - **Heapify-Up** (Bubble-Up, Sift-Up)
  - **Heapify-Down** (Bubble-Down, Sift-Down)
 
#### Heapify-Up
```python
def heapify_up(arr: List[int], index: int):
    while index > 0:
        parent = (index - 1) // 2
        if arr[parent] > arr[index]:
            arr[parent], arr[index] = arr[index], arr[parent]
            index = parent
        else:
            break
```
**Visual Representation of Heapify-Up:**
```python
heapify_up(arr, 6)
        1      
       / \
      3   6
     / \ / \
    5  9 8  0

        1
       / \
      3   0
     / \ / \
    5  9 8  6

        0
       / \
      3   1
     / \ / \
    5  9 8  6
```

#### Heapify-Down
```python
def heapify_down(arr: List[int], n: int, index: int):
    while True:
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest != index:
            arr[index], arr[smallest] = arr[smallest], arr[index]
            index = smallest
        else:
            break
```
**Visual Representation of Heapify-Down:**
```python
heapify_down(arr, 5, 0)  # (n) 5 is the length of array
        8
       / \
      3   6
     / \
    5   9

        3
       / \
      8   6
     / \
    5   9

        3
       / \
      5   6
     / \
    8   9
```

**NOTE:** **Heapify Up** or **Down** can either be used to build either **Min Heap** or **Max Heap**

#### Heapify into a Min Heap
```python
# n // 2 - 1 is the index of the last intermediate node (Since a heap is a complete binary tree)
def heapify(arr: List[int]):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify_down(arr, n, i)
```

### 2. Push
```python
def heap_push(arr: List[int], x: int):
    arr.append(x)
    heapify_up(arr, len(arr) - 1)
```

**Visual Representation of Pushing**
```python
heap_push(arr, 1)
         4
       /   \
      9     5
     / \   / \
   15  13 6   1  # Push 1 into the array

         4
       /   \
      9     1
     / \   / \
   15  13 6   5

         1
       /   \
      9     4
     / \   / \
   15  13 6   5
```

### 3. Pop
```python
def heap_pop(arr: List[int]) -> int:
    if len(arr) == 0:
        raise IndexError("pop from an empty heap")

    # Swap the root and the last element
    arr[0], arr[-1] = arr[-1], arr[0]

    # Pop the last element (the previous root, which is the minimum)
    popped_value = arr.pop()

    # Heapify down to maintain the heap property
    heapify_down(arr, 0)

    return popped_value
```
 
## Some applications of Heap Data Structure
- `Priority Queue`
- `Dijkstra` and `A*` algorithms
- `Heap Sort`
- Find k largest or k smallest elements

### Heap Sort
```python
def heap_sort(arr: List[int]):
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_down(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap max element with the last element of the heap.
        heapify_down(arr, i, 0)  # Make sure the heap is valid
```

# Patterns
## Top K Pattern
### [Kth Largest Element in an Array](https://www.geeksforgeeks.org/max-heap-in-python/)
```python
def findKthLargest(nums, k):
    idx = len(nums) - k
    heapify(nums)
    
    for i in range(idx + 1):
        val = heappop(nums)
    
    return val
```

- **TC** = `O((N - k) * LogN + N` (Average)
- **TC** = `O(NLogN) + N` (Worst)
- **SC** = `O(1)`

**Alternative Solution**
```python
def findKthLargest(nums, k):
    minHeap = []
    for num in nums:
        heappush(minHeap, num)
        if len(minHeap) > k:
            heappop(minHeap)

    return minHeap[0]
```

**Idea:** Keep a MinHeap of `k` elements, whenever the Heap exceeds size of `k`, heap pop out the smallest element. That way we could keep k largest element in the array.

- **TC** = `O(NLogk)` (Average) - N from `nums` itertation and LogK from heapifying the MinHeap of `k` elements.
- **TC** = `O(NLogN)` (Worst) - when `k` equals to `N`.
- **SC** = `O(k)` (Average)
- **SC** = `O(N)` (Worst) - when `k` equals to `N`.

### [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)
```python
def topKFrequent(nums, k):
    c = Counter(nums)
    items = [(v,k) for k,v in c.items()]

    heapify(items)
    while len(items) != k:
        heappop(items)

    return [v for k,v in items]
```

### [Reorganize String](https://leetcode.com/problems/reorganize-string)
```python
def reorganizeString(s):
    count = Counter(s)
    maxHeap = [[-v, k] for k, v in count.items()]
    heapify(maxHeap)  # O(N)

    result = ""
    tmp = None
    while maxHeap or tmp:
        v, k = heappop(maxHeap) if maxHeap else tmp

        if result and result[-1] == k:
            return ""

        result += k
        if tmp:
            heappush(maxHeap, tmp)
        tmp = [v + 1, k] if v + 1 != 0 else None

    return result
```

### [Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart)
```python
def rearrangeString(s, k):
    heap = [[-value, key] for key, value in Counter(s).items()]
    heapify(heap)
    idx_map = {}
    queue = deque()

    res = ""

    while heap or queue:
        if queue and len(res) - idx_map[queue[0][1]] >= k:
            value, key = queue.popleft()
            heappush(heap, [value, key])

        if not heap:
            return ""
        value, key = heappop(heap)

        res += key
        idx_map.update({key: len(res) - 1})
        if value + 1 != 0:
            queue.append([value + 1, key])

    return res
```

## Merge K Sorted
### [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums)
```python
def kSmallestPairs(nums1, nums2, k):
    heap = [[nums1[0] + nums2[0], 0, 0]]

    res = []
    aSet = set()
    while len(res) < k:
        total, idx1, idx2 = heappop(heap)
        if idx1 + 1 < len(nums1) and (idx1 + 1, idx2) not in aSet:
            heappush(heap, [nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2])
            aSet.add((idx1 + 1, idx2))

        if idx2 + 1 < len(nums2) and (idx1, idx2 + 1) not in aSet:
            heappush(heap, [nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1])
            aSet.add((idx1, idx2 + 1))

        res.append([nums1[idx1], nums2[idx2]])

    return res

print(kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=9))
"""
heap: [[2, 0, 0]]
aSet: set()
idx1: 1, idx2: 0
idx1: 0, idx2: 1
----
heap: [[2, 1, 0], [3, 0, 1]]
aSet: {(1, 0), (0, 1)}
idx1: 2, idx2: 0
idx1: 1, idx2: 1
----
heap: [[3, 0, 1], [3, 2, 0], [3, 1, 1]]
aSet: {(1, 0), (1, 1), (2, 0), (0, 1)}
idx1: 1, idx2: 1 (Already in Set. Skipping)
idx1: 0, idx2: 2
----
heap: [[3, 1, 1], [3, 2, 0], [4, 0, 2]]
aSet: {(0, 1), (1, 1), (2, 0), (0, 2), (1, 0)}
idx1: 2, idx2: 1
idx1: 1, idx2: 2
----
heap: [[3, 2, 0], [4, 0, 2], [4, 2, 1], [4, 1, 2]]
aSet: {(0, 1), (1, 2), (2, 1), (1, 1), (2, 0), (0, 2), (1, 0)}
idx1: 3, idx2: 0 (idx1 exceeds nums1's length. Skipping)
idx1: 2, idx2: 1
----
heap: [[4, 0, 2], [4, 1, 2], [4, 2, 1]]
aSet: {(0, 1), (1, 2), (2, 1), (1, 1), (2, 0), (0, 2), (1, 0)}
idx1: 1, idx2: 2 (Already in Set. Skipping)
idx1: 0, idx2: 3 (idx2 exceeds nums2's length. Skipping)
----
heap: [[4, 1, 2], [4, 2, 1]]
aSet: {(0, 1), (1, 2), (2, 1), (1, 1), (2, 0), (0, 2), (1, 0)}
idx1: 2, idx2: 2
idx1: 1, idx2: 3 (idx2 exceeds nums2's length. Skipping)
----
heap: [[4, 2, 1], [5, 2, 2]]
aSet: {(0, 1), (1, 2), (2, 1), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}
idx1: 3, idx2: 1 (idx1 exceeds nums1's length. Skipping)
idx1: 2, idx2: 2
----
heap: [[5, 2, 2]]
aSet: {(0, 1), (1, 2), (2, 1), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}
idx1: 3, idx2: 2 (idx1 exceeds nums1's length. Skipping)
idx1: 2, idx2: 3 (idx2 exceeds nums2's length. Skipping)
----
[[1, 1], [1, 1], [1, 2], [1, 2], [2, 1], [1, 3], [1, 3], [2, 2], [2, 3]]
"""
```

### [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix)
```python
def kthSmallest(matrix, k):
    heap = []

    for rows in matrix:
        for element in rows:
            heappush(heap, -element)
            if len(heap) > k:
                heappop(heap)

    return -heap[0]


print(kthSmallest([[1, 5, 9],
                   [10, 11, 13],
                   [2, 3, 4]], 2))
```

Utilizing a Max Heap we want to keep k elements in the heap, if a new element is added to the heap we push the largest element out of the heap, hence the k smallest element after the iteration will always be the index 0 of the heap.

### [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)


## Greedy. Keeping Max (or Min) element to replace
### [Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/)
```python
def furthestBuilding(heights, bricks, ladders):
    heap = []

    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff <= 0:
            continue
        if diff <= bricks:
            bricks -= diff
            heappush(heap, -diff)
        else:
            if not ladders:
                return i
            ladders -= 1

            if heap and -heap[0] > diff:
                bricks += -heappop(heap) if heap else 0
                bricks -= diff
                heappush(heap, -diff)

    return len(heights) - 1


print(furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2))
""" MAX HEAP
[4, 12, 2, 7, 3, 18, 20, 3, 19]
i = 0 (4)
diff 8 (smaller than 10)> heap = [8]
bricks = 2

i = 1 (12)
diff -10 > continue

i = 2 (2)
diff -5 (larger than bricks = 2) > stair -= 1
pop the max heap, and push diff > heap = [5]
bricks = 5

i = 3 (7)
diff -4 > continue

i = 4 (3)
diff -15 (larger than bricks = 5) > stair -= 1
won't pop the max heap because don't have enough bricks (5 < 15)

i = 5 (18)
diff 2 (smaller than 5) > heap = [5, 2]
bricks = 3

i = 6 (20)
diff -17 > continue

i = 7 (3)
diff 16 (larger than bricks = 3)
return i since ladders = 0 
"""
```
