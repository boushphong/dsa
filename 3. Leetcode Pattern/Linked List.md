# Linked List
`OrderedDict` in Python is implemented using a combination of a **Doubly Linked List** and a **Hash Map** (dictionary).
1. **Hash Map (Dictionary):** The main storage is a regular dictionary where keys are mapped to their corresponding values. In addition to storing the value, each key also points to a node in the doubly linked list.
2. **Doubly Linked List:** This is used to maintain the order of the keys. Each node in the list contains a key and two pointers—one pointing to the previous node and one pointing to the next node. This allows for efficient insertion, deletion, and reordering of elements while maintaining the order.

### Key Operations:
- **Insertion:** When a new key-value pair is inserted into an `OrderedDict`, a new node is added to the end of the doubly linked list, and the key is stored in the dictionary pointing to this node.
  - `O(1)` (Insertion and Update Value)
- **Deletion:** When a key is deleted, the corresponding node is removed from the doubly linked list, and the key is removed from the dictionary.
  - Average Case: `O(1)`
  - Worst case: `O(N)`
    - If the underlying hash table needs to be resized or rehashed, which can involve scanning or reorganizing the entire hash table.
- **Reordering:** Since the linked list maintains the order, any reordering operations (like moving an item to the end or beginning) are efficient.
  - `O(1)`
