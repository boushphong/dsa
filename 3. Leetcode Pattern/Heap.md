# Heap
# Table of Contents
* [Heap](#heap)
* [Patterns](#patterns)
   * [Top K Pattern](#top-k-pattern)
      * [<a href="https://leetcode.com/problems/kth-largest-element-in-an-array" rel="nofollow">Kth Largest Element in an Array</a>](https://leetcode.com/problems/kth-largest-element-in-an-array)
      * [<a href="https://leetcode.com/problems/top-k-frequent-elements" rel="nofollow">Top K Frequent Elements</a>](https://leetcode.com/problems/top-k-frequent-elements)
      * [<a href="https://leetcode.com/problems/reorganize-string" rel="nofollow">Reorganize String</a>](https://leetcode.com/problems/reorganize-string)
      * [<a href="https://leetcode.com/problems/rearrange-string-k-distance-apart" rel="nofollow">Rearrange String k Distance Apart</a>](https://leetcode.com/problems/rearrange-string-k-distance-apart)
   * [Merge K Sorted](#merge-k-sorted)
      * [<a href="https://leetcode.com/problems/find-k-pairs-with-smallest-sums" rel="nofollow">Find K Pairs with Smallest Sums</a>](https://leetcode.com/problems/find-k-pairs-with-smallest-sums)
      * [<a href="https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix" rel="nofollow">Kth Smallest Element in a Sorted Matrix</a>](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix)
      * [<a href="https://leetcode.com/problems/merge-k-sorted-lists" rel="nofollow">Merge K Sorted Lists</a>](https://leetcode.com/problems/merge-k-sorted-lists)
   * [Minimum Number](#minimum-number)
      * [<a href="https://leetcode.com/problems/kth-largest-element-in-an-array" rel="nofollow">Kth Largest Element in an Array (Alternative Solution)</a>](https://leetcode.com/problems/kth-largest-element-in-an-array)
      * [<a href="https://leetcode.com/problems/meeting-rooms-ii" rel="nofollow">Meeting Rooms II</a>](https://leetcode.com/problems/meeting-rooms-ii)
   * [Two Heaps](#two-heaps)
      * [<a href="https://leetcode.com/problems/sliding-window-median" rel="nofollow">Sliding Window Median</a>](https://leetcode.com/problems/sliding-window-median)
   * [Greedy. Keeping Max (or Min) element to replace](#greedy-keeping-max-or-min-element-to-replace)
      * [<a href="https://leetcode.com/problems/furthest-building-you-can-reach/" rel="nofollow">Furthest Building You Can Reach</a>](https://leetcode.com/problems/furthest-building-you-can-reach/)

## Top K Pattern
Usually invoving heapifying the input array right away.
### [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array)
```python
def findKthLargest(nums, k):
    idx = len(nums) - k
    heapify(nums)
    
    for i in range(idx + 1):
        val = heappop(nums)
    
    return val
```

- **TC** = `O((N - k) * LogN + N` (Average)
- **TC** = `O(NLogN) + N` (Worst)
- **SC** = `O(1)`

### [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)
```python
def topKFrequent(nums, k):
    c = Counter(nums)
    items = [(v,k) for k,v in c.items()]

    heapify(items)
    while len(items) != k:
        heappop(items)

    return [v for k,v in items]
```

### [Reorganize String](https://leetcode.com/problems/reorganize-string)
```python
def reorganizeString(s):
    count = Counter(s)
    maxHeap = [[-v, k] for k, v in count.items()]
    heapify(maxHeap)  # O(N)

    result = ""
    tmp = None
    while maxHeap or tmp:
        v, k = heappop(maxHeap) if maxHeap else tmp

        if result and result[-1] == k:
            return ""

        result += k
        if tmp:
            heappush(maxHeap, tmp)
        tmp = [v + 1, k] if v + 1 != 0 else None

    return result
```

### [Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart)
```python
def rearrangeString(s, k):
    heap = [[-value, key] for key, value in Counter(s).items()]
    heapify(heap)
    idx_map = {}
    queue = deque()

    res = ""

    while heap or queue:
        if queue and len(res) - idx_map[queue[0][1]] >= k:
            value, key = queue.popleft()
            heappush(heap, [value, key])

        if not heap:
            return ""
        value, key = heappop(heap)

        res += key
        idx_map.update({key: len(res) - 1})
        if value + 1 != 0:
            queue.append([value + 1, key])

    return res
```

## Merge K Sorted
### [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums)
```python
def kSmallestPairs(nums1, nums2, k):
    heap = [[nums1[0] + nums2[0], 0, 0]]

    res = []
    aSet = set()
    while len(res) < k:
        total, idx1, idx2 = heappop(heap)
        if idx1 + 1 < len(nums1) and (idx1 + 1, idx2) not in aSet:
            heappush(heap, [nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2])
            aSet.add((idx1 + 1, idx2))

        if idx2 + 1 < len(nums2) and (idx1, idx2 + 1) not in aSet:
            heappush(heap, [nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1])
            aSet.add((idx1, idx2 + 1))

        res.append([nums1[idx1], nums2[idx2]])

    return res

print(kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=9))
"""
heap: [[2, 0, 0]]
aSet: set()
idx1: 1, idx2: 0
idx1: 0, idx2: 1
----
heap: [[2, 1, 0], [3, 0, 1]]
aSet: {(1, 0), (0, 1)}
idx1: 2, idx2: 0
idx1: 1, idx2: 1
----
heap: [[3, 0, 1], [3, 2, 0], [3, 1, 1]]
aSet: {(1, 0), (1, 1), (2, 0), (0, 1)}
idx1: 1, idx2: 1 (Already in Set. Skipping)
idx1: 0, idx2: 2
----
heap: [[3, 1, 1], [3, 2, 0], [4, 0, 2]]
aSet: {(0, 1), (1, 1), (2, 0), (0, 2), (1, 0)}
idx1: 2, idx2: 1
idx1: 1, idx2: 2
----
heap: [[3, 2, 0], [4, 0, 2], [4, 2, 1], [4, 1, 2]]
aSet: {(0, 1), (1, 2), (2, 1), (1, 1), (2, 0), (0, 2), (1, 0)}
idx1: 3, idx2: 0 (idx1 exceeds nums1's length. Skipping)
idx1: 2, idx2: 1
----
heap: [[4, 0, 2], [4, 1, 2], [4, 2, 1]]
aSet: {(0, 1), (1, 2), (2, 1), (1, 1), (2, 0), (0, 2), (1, 0)}
idx1: 1, idx2: 2 (Already in Set. Skipping)
idx1: 0, idx2: 3 (idx2 exceeds nums2's length. Skipping)
----
heap: [[4, 1, 2], [4, 2, 1]]
aSet: {(0, 1), (1, 2), (2, 1), (1, 1), (2, 0), (0, 2), (1, 0)}
idx1: 2, idx2: 2
idx1: 1, idx2: 3 (idx2 exceeds nums2's length. Skipping)
----
heap: [[4, 2, 1], [5, 2, 2]]
aSet: {(0, 1), (1, 2), (2, 1), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}
idx1: 3, idx2: 1 (idx1 exceeds nums1's length. Skipping)
idx1: 2, idx2: 2
----
heap: [[5, 2, 2]]
aSet: {(0, 1), (1, 2), (2, 1), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}
idx1: 3, idx2: 2 (idx1 exceeds nums1's length. Skipping)
idx1: 2, idx2: 3 (idx2 exceeds nums2's length. Skipping)
----
[[1, 1], [1, 1], [1, 2], [1, 2], [2, 1], [1, 3], [1, 3], [2, 2], [2, 3]]
"""
```

### [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix)
```python
def kthSmallest(matrix, k):
    heap = []

    for rows in matrix:
        for element in rows:
            heappush(heap, -element)
            if len(heap) > k:
                heappop(heap)

    return -heap[0]


print(kthSmallest([[1, 5, 9],
                   [10, 11, 13],
                   [2, 3, 4]], 2))
```

Utilizing a Max Heap we want to keep k elements in the heap, if a new element is added to the heap we push the largest element out of the heap, hence the k smallest element after the iteration will always be the index 0 of the heap.

### [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)
```

```

## Minimum Number
This pattern aims to create an external min heap variable (empty first) to track the minimum element and updating it gradually. It sometimes pairs up with sorting to solve specific problems.

### [Kth Largest Element in an Array (Alternative Solution)](https://leetcode.com/problems/kth-largest-element-in-an-array)
```python
def findKthLargest(nums, k):
    minHeap = []
    for num in nums:
        heappush(minHeap, num)
        if len(minHeap) > k:
            heappop(minHeap)

    return minHeap[0]
```

**Idea:** Keep a MinHeap of `k` elements, whenever the Heap exceeds size of `k`, heap pop out the smallest element. That way we could keep k largest element in the array.

- **TC** = `O(NLogk)` (Average) - N from `nums` itertation and LogK from heapifying the MinHeap of `k` elements.
- **TC** = `O(NLogN)` (Worst) - when `k` equals to `N`.
- **SC** = `O(k)` (Average)
- **SC** = `O(N)` (Worst) - when `k` equals to `N`.

### [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii)
```python
def minMeetingRooms(intervals):
    intervals.sort(key=lambda x: x[0])

    meetingRooms = [intervals[0][1]]
    for v1, v2 in intervals[1:]:
        if v1 >= meetingRooms[0]:
            heapreplace(meetingRooms, v2)
        else:
            heappush(meetingRooms, v2)

    return len(meetingRooms)

print(minMeetingRooms([[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]))
"""
meetingRooms: [10]
----
v1: 2, v2: 7
meetingRooms: [7, 10]
----
v1: 3, v2: 19
meetingRooms: [7, 10, 19]
----
v1: 8, v2: 12
meetingRooms: [10, 12, 19]
----
v1: 10, v2: 20
meetingRooms: [12, 20, 19]
----
v1: 11, v2: 30
meetingRooms: [12, 20, 19, 30]
----
"""
```

## Two Heaps
### [Sliding Window Median](https://leetcode.com/problems/sliding-window-median)
```python

```

## Greedy. Keeping Max (or Min) element to replace
### [Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/)
```python
def furthestBuilding(heights, bricks, ladders):
    heap = []

    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff <= 0:
            continue
        if diff <= bricks:
            bricks -= diff
            heappush(heap, -diff)
        else:
            if not ladders:
                return i
            ladders -= 1

            if heap and -heap[0] > diff:
                bricks += -heappop(heap) if heap else 0
                bricks -= diff
                heappush(heap, -diff)

    return len(heights) - 1


print(furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2))
""" MAX HEAP
[4, 12, 2, 7, 3, 18, 20, 3, 19]
i = 0 (4)
diff 8 (smaller than 10)> heap = [8]
bricks = 2

i = 1 (12)
diff -10 > continue

i = 2 (2)
diff -5 (larger than bricks = 2) > stair -= 1
pop the max heap, and push diff > heap = [5]
bricks = 5

i = 3 (7)
diff -4 > continue

i = 4 (3)
diff -15 (larger than bricks = 5) > stair -= 1
won't pop the max heap because don't have enough bricks (5 < 15)

i = 5 (18)
diff 2 (smaller than 5) > heap = [5, 2]
bricks = 3

i = 6 (20)
diff -17 > continue

i = 7 (3)
diff 16 (larger than bricks = 3)
return i since ladders = 0 
"""
```
