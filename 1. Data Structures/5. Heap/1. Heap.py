CAPACITY = 10


# maximum heap (root node will be the largest item)
class Heap:
    def __init__(self):
        # This is the actual number of items in the data structure
        self.heap_size = 0
        # The underlying list data structure
        self.heap = [0] * CAPACITY

    def insert(self, item):
        # when the heap is full
        if self.heap_size == CAPACITY:
            return None

        self.heap[self.heap_size] = item
        self.heap_size += 1

        # check the heap properties
        self.fix_up(self.heap_size - 1)

    # starting with the actual node we have inserted up to the root node
    # we have to compare the values whether to make swap operations
    # LogN it has O(LogN) running time complexity
    def fix_up(self, index):
        parent_index = (index - 1) // 2
        # we consider all the items above till we hit the root node
        # if heap property if violated then we swap the parent-child
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[index],
            )
            self.fix_up(parent_index)

    # peek() return with the max item in O(1)
    def get_max(self):
        return self.heap[0]

    # return the max and removes it as well
    # remove the root node of the heap

    def poll(self):
        max_item = self.get_max()
        # swap the root node with the last item and "heapify"
        self.heap[0], self.heap[self.heap_size - 1] = (
            self.heap[self.heap_size - 1],
            self.heap[0],
        )
        self.heap_size = self.heap_size - 1
        # make sure the heap is "heapify"
        self.fix_down(0)
        return max_item

    # starting with the root node downwards until the heap properties are no longer violated - O(logN)
    def fix_down(self, index):
        index_left = 2 * index + 1
        index_right = 2 * index + 2
        # in a max heap the parent is always greater than the children
        largest_index = index
        # looking for the largest (parent or left node)
        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            largest_index = index_left
        # if the right child is greater than the left child: largest is the right child
        if (
            index_right < self.heap_size
            and self.heap[index_right] > self.heap[largest_index]
        ):
            largest_index = index_right
        # if the parent is larger than the children: it is a valid heap so we terminate the recursive function calls
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = (
                self.heap[largest_index],
                self.heap[index],
            )
            self.fix_down(largest_index)

    # we consider N items - it takes O(LogN) to get the max (poll function)
    # N*O(LogN) = O(NLogN)
    def heap_sort(self):
        for _ in range(self.heap_size):
            max_item = self.poll()
            print(max_item)


if __name__ == "__main__":
    heap = Heap()
    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(8)
    heap.insert(1)
    heap.insert(-5)
    heap.insert(99)

    print(heap.heap)
    # [99, 8, 13, -2, 1, -5, 0, 0, 0, 0]

    heap.heap_sort()
    # 99
    # 13
    # 8
    # 1
    # 0
    # -2
    # -5
