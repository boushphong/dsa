# Sorting
# Complexity
| Sorting Algorithm | TC (Best)  | TC (Average) | TC (Worst) | SC (Worst) | Stable |
|-------------------|------------|--------------|------------|------------|--------|
| `Bubble Sort`     | O(N)       | O(N^2)       | O(N^2)     | O(1)       | Yes    |
| `Merge Sort`      | O(NLog(N)) | O(NLog(N))   | O(NLog(N)) | O(N)       | Yes    |
| `Quick Sort`      | O(NLog(N)) | O(NLog(N))   | O(N^2)     | O(Log(N))  | No     |
| `Heap Sort`       | O(NLog(N)) | O(NLog(N))   | O(NLog(N)) | O(1)       | No     |
| `Tim Sort`        | O(N)       | O(NLog(N))   | O(NLog(N)) | O(N)       | Yes    |


## Bubble Sort
The key idea behind bubble sort is to repeatedly compare adjacent elements in the input list and swap them if they are in the wrong order, with the ultimate goal of "bubbling up" the largest elements to the end of the list.

1. Start at the beginning of the list. (elements 0 and 1)
2. Compare the first two elements. If the first element is greater than the second element, swap them.
3. Move to the next pair of adjacent elements (elements 1 and 2) and repeat step 2.
4. Continue this process until the end of the list is reached.
5. If any swaps were made in step 2-4, repeat the process from step 1 again. Otherwise, the list is sorted. At this step, The largest element is now at the end of the list. So we only need to sort the list 1 index less.

```python
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        swaps = False  # initialize a boolean flag to check if any swaps occurred
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps = True  # set the flag to True if a swap occurred

        # If no swaps occurred in the inner loop, the array is already sorted
        if not swaps:
            break
```

Visualization: https://www.youtube.com/watch?v=xli_FI7CuzA

## Merge Sort
The key idea behind merge sort is to repeatedly divide the input list into halves until each sub-list contains only one element, which is trivially sorted. The sorted sub-lists are then merged back together using a helper function that compares the elements of each sub-list and selects the smaller element to add to the merged sub-list. This process is repeated recursively until the original list is reconstructed in sorted order

1. If the input list has only one element, it is already sorted, so return the list as is.
2. Otherwise, divide the input list into two halves and recursively sort each half using merge sort.
3. Merge the two sorted sub-lists back together in order to obtain a sorted sub-list. This is done by comparing the first elements of each sub-list and selecting the smaller element to add to the new merged sub-list. Repeat this process until all elements from both sub-lists have been added to the merged sub-list.
4. Repeat steps 2-3 recursively for each pair of sub-lists until the original list is reconstructed in sorted order.

```python
def mergeSort(array):
    if len(array) == 1:
        return array

    m = len(array) // 2

    l = array[:m]
    r = array[m:]
    
    lp = mergeSort(l)
    rp = mergeSort(r)

    return merge(lp, rp)


def merge(lp, rp):
    result = []
    i = j = 0
    while i < len(lp) and j < len(rp):
        if lp[i] < rp[j]: 
            result.append(lp[i])
            i += 1
        else:
            result.append(rp[j])
            j += 1

    result += lp[i:]
    result += rp[j:]

    return result 
```

Visualization: https://www.youtube.com/watch?v=5Z9dn2WTg9o

Visualization: https://www.youtube.com/watch?v=Hoixgm4-P4M

## Quick Sort
The key idea behind quicksort is to divide the input list into two partitions, based on a chosen "pivot" element, such that all elements in the left partition are smaller than the pivot, and all elements in the right partition are greater than or equal to the pivot. This partitioning is then repeated recursively for each partition until the entire list is sorted.

1. Choose a "pivot" element from the input list. This can be any element, but typically it is chosen based on a certain strategy (median of three, first, last ...).
2. Partition the input list into two partitions, such that all elements in the left partition are smaller than the pivot, and all elements in the right partition are greater than or equal to the pivot. This partitioning is done by iterating through the list from left to right, and swapping any element that is smaller than the pivot with the first unsorted element to its right. Once all elements have been processed, swap the pivot with the first element in the right partition.
3. Recursively apply steps 1-2 to each partition until the entire list is sorted.

```python
def partition(array, low, high):
    pivot = array[high]
    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
```

Visualization: https://www.youtube.com/watch?v=SLauY6PpjW4

## Heap Sort
The key idea behind heapsort is to use a binary heap data structure to sort an array of elements by repeatedly removing the maximum (or minimum) element from the heap and placing it at the end of the sorted array. This process is repeated until all elements are sorted. The heap data structure ensures that the maximum (or minimum) element is always at the root, allowing for efficient removal and sorting.

1. Build a max heap from the input array.
2. The largest item is now stored at the root of the heap. Replace it with the last item of the heap and reduce the size of the heap by 1.
3. Heapify the root of the heap. This means that we swap the root with its larger child, and repeat this process recursively with the new subtree until the heap property is restored.
4. Repeat steps 2 and 3 until the size of the heap is 1.

```python
def heapify(arr, n, i):  # (TC = O(Log(N)))
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a max-heap from the input array (TC = O(N))
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap in descending order
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr
```

Visualization: https://www.youtube.com/watch?v=2DmK_H7IdTo
