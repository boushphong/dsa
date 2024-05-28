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
## Finding Kth largest element
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
