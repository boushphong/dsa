# Heap
### What is a Heap?
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

### Operations on Heap
- `heapify(arr)`: Build a heap from an array; **O(N)**
- `push(arr, x)`: Add an element `x` to the heap; **O(logN)**
- `pop(arr)`: Remove the top element (smallest or largest) from the heap; **O(logN)**
- `top(arr)`: Retrieve the top element (smallest or largest) of the heap; **O(1)**

### Some applications of Heap Data Structure
- `Priority Queue`
- `Dijkstra` and `A*` algorithms
- `Heap Sort`
- Find k largest or k smallest elements
