class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.right_node = None
        self.left_node = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # we have to go to the left subtree
        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)  # Recursive call
            else:
                node.left_node = Node(data, node)  # Base
        # we have to visit the right subtree
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)  # Recursive call
            else:
                node.right_node = Node(data, node)  # Base

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if node is None:
            return
        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node...%d" % node.data)
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None
                if parent is None:
                    self.root = None
                del node

            elif node.left_node is None and node.right_node is not None:  # node !!!
                print("Removing a node with single right child...")
                parent = node.parent
                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.right_node
                    if parent.right_node == node:
                        parent.right_node = node.right_node
                else:
                    self.root = node.right_node
                node.right_node.parent = parent
                del node

            elif node.right_node is None and node.left_node is not None:
                print("Removing a node with single left child...")
                parent = node.parent
                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.left_node
                else:
                    self.root = node.left_node
                node.left_node.parent = parent
                del node

            else:
                print("Removing node with two children....")
                predecessor = self.get_predecessor(node.left_node)
                # Swap data then remove the leaf node
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)
        return node

    # Get Maximum value
    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)

    def get_max_value(self, node):
        if node.right_node:
            self.get_max_value(node.right_node)
        return node.data

    # Get Minimum value
    def get_min(self):
        if self.root:
            return self.get_min_value(self.root)

    def get_min_value(self, node):
        if node.right_node:
            self.get_min_value(node.left_node)
        return node.data

    # Traverse in Order
    def traverse_in(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)
        print(node.data)
        if node.right_node:
            self.traverse_in_order(node.right_node)

    # Traverse pre Order
    def traverse_pre(self):
        if self.root is not None:
            self.traverse_pre_order(self.root)

    def traverse_pre_order(self, node):
        print(node.data)
        if node.left_node:
            self.traverse_pre_order(node.left_node)
        if node.right_node:
            self.traverse_pre_order(node.right_node)

    # Traverse post Order
    def traverse_post(self):
        if self.root is not None:
            self.traverse_post_order(self.root)

    def traverse_post_order(self, node):
        if node.left_node:
            self.traverse_post_order(node.left_node)
        if node.right_node:
            self.traverse_post_order(node.right_node)
        print(node.data)

    def traverse_level(self):
        if self.root is not None:
            self.traverse_level_order(self.root)
            print(self.root.data)

    def traverse_level_order(self, node):
        if node.left_node:
            self.traverse_level_order(node.left_node)
        if node.right_node:
            self.traverse_level_order(node.right_node)
        if node.left_node:
            print(node.left_node.data)
        if node.right_node:
            print(node.right_node.data)


class TreeComparator:
    def compare(self, node1, node2):
        # check the base-case (so these node1 and node2 may be the nodes
        # of a leaf node)
        # node1 may be a None or node2 may be a None
        if node1 is None or node2 is None:
            return node1 == node2
        # we have to check the values in the nodes
        if node1.data is not node2.data:
            return False
        # check all the left and right subtrees (children) recursively
        return self.compare(node1.left_node, node2.left_node) and self.compare(
            node1.right_node, node2.right_node
        )


if __name__ == "__main__":
    bst1 = BinarySearchTree()
    bst1.insert(3)
    bst1.insert(1)
    bst1.insert(4)
    bst1.insert(5)
    bst1.insert(-5)
    bst1.insert(0)
    bst1.insert(10)

    bst2 = BinarySearchTree()
    bst2.insert(3)
    bst2.insert(1)
    bst2.insert(4)
    bst2.insert(5)
    bst2.insert(-5)
    bst2.insert(0)
    bst2.insert(10)

    comparator = TreeComparator()
    print(comparator.compare(bst1.root, bst2.root))
    # True

    bst1.remove(3)
    # Removing node with two children....
    # Removing a node with single left child...

    bst1.traverse_in()
    # -5
    # 0
    # 1
    # 4
    # 5
    # 10

    bst1.remove(4)
    # Removing a node with single right child...

    bst1.traverse_in()
    # -5
    # 0
    # 1
    # 5
    # 10

    bst1.traverse_pre()
    # 1
    # -5
    # 0
    # 5
    # 10

    bst1.traverse_post()
    # 0
    # -5
    # 10
    # 5
    # 1

    bst1.traverse_level()
    # 0
    # 10
    # -5
    # 5
    # 1
