# Linked List
## Singly Linked List
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"{self.val} -> {self.next.val if self.next else None}"


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"{self.head.val if self.head else None}"

    def append(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node


if __name__ == '__main__':
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
```

## Doubly Linked List
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"{self.prev.val if self.prev else None} <- {self.val} -> {self.next if self.next else None}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f"{(self.head.val if self.head else None)}, {(self.tail.val if self.tail else None)}"

    def append(self, val):
        node = Node(val)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
```


## Ordered Dict (LRU Cache)
`OrderedDict` in Python is implemented using a combination of a **Doubly Linked List** and a **Hash Map** (dictionary).
1. **Hash Map (Dictionary):** The main storage is a regular dictionary where keys are mapped to their corresponding values. In addition to storing the value, each key also points to a node in the doubly linked list.
2. **Doubly Linked List:** This is used to maintain the order of the keys. Each node in the list contains a key and two pointers—one pointing to the previous node and one pointing to the next node. This allows for efficient insertion, deletion, and reordering of elements while maintaining the order.

**Key Operations:**
- **Insertion:** When a new key-value pair is inserted into an `OrderedDict`, a new node is added to the end of the doubly linked list, and the key is stored in the dictionary pointing to this node.
  - `O(1)` (Insertion and Update Value)
- **Deletion:** When a key is deleted, the corresponding node is removed from the doubly linked list, and the key is removed from the dictionary.
  - Average Case: `O(1)`
  - Worst case: `O(N)`
    - If the underlying hash table needs to be resized or rehashed, which can involve scanning or reorganizing the entire hash table.
- **Reordering:** Since the linked list maintains the order, any reordering operations (like moving an item to the end or beginning) are efficient.
  - `O(1)`

