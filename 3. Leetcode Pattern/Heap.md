<img width="1653" alt="image" src="https://github.com/boushphong/dsa/assets/59940078/350f4b8a-8f56-4f2b-be3d-7bbca7b4d70a"># Heap
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

## Heap Structure (Array)
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
- `heapify(arr)`: Build a heap from an array; **O(N)**
- `push(arr, x)`: Add an element `x` to the heap; **O(logN)**
- `pop(arr)`: Remove the top element (smallest or largest) from the heap; **O(logN)**
- `top(arr)`: Retrieve the top element (smallest or largest) of the heap; **O(1)**

### What is Heapify?
- **Heapify** is a process that ensures a binary tree maintains the heap properties.
- Heapify can be performed at any node to preserve the heap properties when there is a change in the node's value.
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
heapify(arr, 6)
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



In this example, the value `0` is moved up in the heap to maintain the heap property, swapping places with its parent nodes as necessary.
 
## Some applications of Heap Data Structure
- `Priority Queue`
- `Dijkstra` and `A*` algorithms
- `Heap Sort`
- Find k largest or k smallest elements
