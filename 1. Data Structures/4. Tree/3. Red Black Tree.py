class Color:
    RED = 1
    BLACK = 2


class Node:
    def __init__(self, data, parent=None, color=Color.RED):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.settle_violation(self.root)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left_node is not None:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
                self.settle_violation(node.left_node)
        else:
            if node.right_node is not None:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                self.settle_violation(node.right_node)

    def traverse(self):
        if self.root:
            self.in_order_traversal(self.root)

    def in_order_traversal(self, node):
        if node.left_node:
            self.in_order_traversal(node.left_node)
        print(node.data)
        if node.right_node:
            self.in_order_traversal(node.right_node)

    def rotate_right(self, node):
        print("Rotating to the right on node ", node.data)
        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node
        node.left_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node

        if node == self.root:
            self.root = temp_left_node

    def rotate_left(self, node):
        print("Rotating to the left on node ", node.data)
        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node

        if node == self.root:
            self.root = temp_right_node

    def settle_violation(self, node):
        while node != self.root and self.is_red(node) and self.is_red(node.parent):
            parent_node = node.parent
            grand_parent_node = parent_node.parent

            # parent is a left child of it's parent (so the grandparent)
            if parent_node == grand_parent_node.left_node:
                uncle = grand_parent_node.right_node

                # case 1.) and case 4.) Recoloring
                if uncle and self.is_red(uncle):
                    print("Re-coloring node %s to RED" % grand_parent_node.data)
                    grand_parent_node.color = Color.RED
                    print("Re-coloring node %s to BLACK" % grand_parent_node.data)
                    parent_node.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = grand_parent_node
                # case 2.) uncle node is black and node is a right child
                else:
                    if node == parent_node.right_node:
                        self.rotate_left(parent_node)
                        node = parent_node
                        parent_node = node.parent

                    # case 3.) rotation on the grandparent + parent and grandparent switch color
                    parent_node.color = Color.BLACK
                    grand_parent_node.color = Color.RED
                    print("Re-color %s to BLACK" % parent_node.data)
                    print("Re-color %s to RED" % grand_parent_node.data)
                    self.rotate_right(grand_parent_node)
            else:
                uncle = grand_parent_node.left_node
                if uncle and self.is_red(uncle):
                    # case 1 and case 4
                    print("Re-coloring node %s to RED" % grand_parent_node.data)
                    grand_parent_node.color = Color.RED
                    print("Re-coloring node %s to BLACK" % parent_node.data)
                    parent_node.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = grand_parent_node
                else:
                    # case 2.) uncle node is black and node is a right child
                    if node == parent_node.left_node:
                        self.rotate_right(parent_node)
                        node = parent_node
                        parent_node = node.parent
                    # case 3.)
                    parent_node.color = Color.BLACK
                    grand_parent_node = Color.RED
                    print("Re-color %s to BLACK" % parent_node.data)
                    print("Re-color %s to RED" % grand_parent_node.data)
                    self.rotate_left(grand_parent_node)

        if self.is_red(self.root):
            print("Recoloring the root to black ...")
            self.root.color = Color.BLACK

    def is_red(self, node):
        if node is None:
            return False

        return node.color == Color.RED


if __name__ == '__main__':
    tree = RedBlackTree()

    tree.insert(32)
    tree.insert(10)
    tree.insert(55)
    tree.insert(1)
    tree.insert(19)
    tree.insert(79)
    tree.insert(16)
    tree.insert(23)
    tree.insert(12)

    # Recoloring the root to black ...
    # Re-coloring node 32 to RED
    # Re-coloring node 32 to BLACK
    # Recoloring the root to black ...
    # Re-coloring node 10 to RED
    # Re-coloring node 19 to BLACK
    # Re-coloring node 19 to RED
    # Re-coloring node 19 to BLACK
    # Rotating to the left on node 10
    # Re-color 19 to BLACK
    # Re-color 32 to RED
    # Rotating to the right on node 32

    tree.traverse()
    # 1
    # 10
    # 12
    # 16
    # 19
    # 23
    # 32
    # 55
    # 79