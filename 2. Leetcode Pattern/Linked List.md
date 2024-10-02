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


# Patterns
## Implement LRU Cache
### [LRU Cache](https://leetcode.com/problems/lru-cache/)
```python
class Node:
    def __init__(self, val, key=None):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

    def __repr__(self):
        return "Node: " + str(self.val)


class DoublyLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(None)
        self.tail = None
        self.curCapacity = 0

    def __len__(self):
        return self.curCapacity

    def __repr__(self):
        return "Head: " + str(self.head.next) + ", Tail: " + str(self.tail)

    def addNode(self, node):
        tmpKey = node.key
        if not self.tail:
            self.head.next = node
            node.prev = self.head
            self.tail = node
        else:
            tmpFront = self.head.next
            tmpFront.prev = node
            node.next = tmpFront
            self.head.next = node
            node.prev = self.head

        self.curCapacity += 1

        if len(self) > self.capacity:
            tmpKey = self.tail.key
            tmpBack = self.tail.prev
            self.tail = tmpBack
            if self.tail:
                self.tail.next = None
            self.curCapacity -= 1
            return tmpKey
        return tmpKey

    def rebalance(self, node):
        if node is self.head.next:
            return

        # Remove the node from its current position
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next

        # If the node is the tail, update the tail pointer
        if node is self.tail:
            self.tail = node.prev

        # Move the node to the front
        tmpFront = self.head.next
        tmpFront.prev = node
        node.next = tmpFront
        node.prev = self.head
        self.head.next = node


class LRUCache:
    def __init__(self, capacity: int):
        self.storage = DoublyLinkedList(capacity)
        self.cache = {}

    def __repr__(self):
        return str(self.storage)

    def get(self, key: int) -> int:
        tmpNode = self.cache.get(key)
        if not tmpNode:
            return -1
        # Rebalance the node to the front if it's not already the most recent
        if tmpNode is not self.storage.head.next:
            self.storage.rebalance(tmpNode)
        return tmpNode.val

    def put(self, key: int, value: int) -> None:
        # If the key is already present, update the value and rebalance
        if key in self.cache:
            self.cache[key].val = value
            if self.cache[key] is not self.storage.head.next:
                self.storage.rebalance(self.cache[key])
            return

        # Otherwise, add a new node
        tmpNode = Node(value, key)
        self.cache[key] = tmpNode
        tmpKey = self.storage.addNode(tmpNode)

        # If adding the node exceeded capacity, remove the least recently used node
        if tmpKey != key and tmpKey in self.cache:
            del self.cache[tmpKey]


obj = LRUCache(2)
print(obj.get(4))  # -1
obj.put(1, 10)
obj.put(2, 20)
obj.put(3, 30)
obj.put(4, 40)
print(obj.get(1))  # -1
```

