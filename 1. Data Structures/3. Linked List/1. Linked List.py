# Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        # this is the first node of the linked list
        # WE CAN ACCESS THIS NODE EXCLUSIVELY !!!
        self.head = None
        self.num_of_nodes = 0

    # O(1) constant running time
    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # the head is NULL (so the data structure is empty)
        if self.head is None:
            self.head = new_node
        # so this is when the linked list is not empty
        else:
            # we have to update the references
            new_node.next_node = self.head
            self.head = new_node

    # O(N)
    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # check if the linked list is empty
        if self.head is None:
            self.head = new_node
        else:
            # this is when the linked list is not empty
            actual_node = self.head

            # this is why it has O(N) linear running time
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            # actual_node is the last node: so we insert the new_node
            # right after the actual_node
            actual_node.next_node = new_node

    # O(1) constant running time
    def size_of_list(self):
        return self.num_of_nodes

    # O(N) linear running time
    def traverse(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node

    # O(N) linear running time complexity
    def get_middle_node(self):

        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer

    # O(N) linear running time
    def remove(self, data):

        # the list is empty
        if self.head is None:
            return

        actual_node = self.head
        # we have to track the prev node for future pointer updates
        # this is why doubly linked lists are better - we can get the prev
        # node (here with linked lists it is impossible)
        prev_node = None

        # search for the item we want to remove (data)
        # If the data you want to search is in the first Node. Then this while loop won't run and prev Node will stay None
        while actual_node is not None and actual_node.data != data:
            prev_node = actual_node
            actual_node = actual_node.next_node

        # search miss
        if actual_node is None:
            return

        # update the references (so we have the data we want to remove)
        # the head node is the one we want to remove
        if prev_node is None:
            self.head = actual_node.next_node
        else:
            # remove an internal node by updating the pointers
            # NO NEED TO del THE NODE BECAUSE THE GARBAGE COLLECTOR WILL DO THAT
            prev_node.next_node = actual_node.next_node

    # O(N) running time complexity without extra memory
    def reverse(self):
        current_node = self.head
        prev_node = None
        next_node = None

        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node
