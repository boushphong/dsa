# Heap
# Table of Contents
* [Heap](#heap)
* [Patterns](#patterns)
   * [Top K Pattern](#top-k-pattern)
   * [Merge K Sorted](#merge-k-sorted)
   * [Minimum Number](#minimum-number)
   * [Greedy. Keeping Max (or Min) element to replace](#greedy-keeping-max-or-min-element-to-replace)

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
    minHeap = []  # val, r, c
    for r in range(len(matrix)):
        heappush(minHeap, (matrix[r][0], r, 0))  # 1 5 6

    ans = None
    for i in range(k):
        ans, r, c = heappop(minHeap)
        if c + 1 < len(matrix):
            heappush(minHeap, (matrix[r][c + 1], r, c + 1))
    return ans


print(kthSmallest([[1, 3, 7], 
                   [5, 10, 12], 
                   [6, 10, 15]], 
                  4))

```

- Since each of the rows in matrix are already sorted, we can understand the problem as finding the kth smallest element from amongst `M` sorted rows.
- We start the pointers to point to the beginning of each rows, then we iterate `k` times, for each time `ith`, the top of the `minHeap` is the `ith` smallest element in the matrix. We pop the top from the `minHeap` then add the next element which has the same row with that top to the `minHeap`.

- **TC** = `O(k * logk)`
- **SC** = `O(k)`


### [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)
```python
def mergeKLists(lists):
    ListNode.__lt__ = lambda self, other: self.val < other.val

    heap = []
    for _ in lists:
        if _:
            heappush(heap, _)

    dummy = head = ListNode()

    while heap:
        node = heappop(heap)
        head.next = node
        head = head.next
        node = node.next

        if node:
            heappush(heap, node)

    return dummy.next
```
- **TC** = `O(NLogk)`
- **SC** = `O(k)`

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

### [Employee Free Time](https://leetcode.com/problems/employee-free-time)
```python
def employeeFreeTime(schedule):
    # collect first events of all employees
    heap = []
    for i, employee in enumerate(schedule):
        # (event.start, employee index, event index)
        heappush(heap, (employee[0][0], i, 0))

    res = []
    _, i, j = heap[0]
    prev_end = schedule[i][j][1]
    while heap:
        _, i, j = heappop(heap)
        # check for next employee event and push it
        if j + 1 < len(schedule[i]):
            heappush(heap, (schedule[i][j + 1][0], i, j + 1))

        event = schedule[i][j]
        if event[0] > prev_end:
            res.append([prev_end, event[0]])
        prev_end = max(prev_end, event[1])
    return res


print(employeeFreeTime([[[1, 3], [6, 7]], [[2, 5], [9, 12]], [[2, 4]]]))
# [[5, 6], [7, 9]]
```

- **TC** = `O(NLogk)` - We still iterate through `N` elements, but the heap only contains at max `k` elemnents at a time.
- **SC** = `O(k)` Only keep `k` elements in the heap

### [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii)
```python
def minMeetingRooms(intervals):
    intervals.sort(key=lambda x: x[0])

    meetingRooms = [intervals[0][1]]
    for v1, v2 in intervals[1:]:
        if v1 >= meetingRooms[0]:
            heapreplace(meetingRooms, v2)  # replace first element and bubble down
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

## Simulation
### [Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii)
```python
from collections import defaultdict
from heapq import *


def mostBooked(n, meetings):
    meetings.sort()

    available = [_ for _ in range(n)]
    unavailable = []
    count = defaultdict(int)

    for start, end in meetings:
        while unavailable and start >= unavailable[0][0]:
            _, room = heappop(unavailable)
            heappush(available, room)

        if not available:
            end_time, room = heappop(unavailable)
            end = end_time + (end - start)
            heappush(available, room)

        room = heappop(available)
        heappush(unavailable, (end, room))
        count[room] += 1

    largestIdx = 0
    curMax = 1
    for i, v in count.items():
        if v > curMax:
            largestIdx = i
            curMax = v

    return largestIdx


print(mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]))  # 0
print(mostBooked(4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]))  # 0
```

## Two Heaps
### [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)
```python
def longestSubarray(nums, limit):
    maxHeap = []
    minHeap = []

    left = 0
    maxLength = 0

    for right in range(len(nums)):
        heappush(maxHeap, (-nums[right], right))
        heappush(minHeap, (nums[right], right))

        while -maxHeap[0][0] - minHeap[0][0] > limit:
            left = min(maxHeap[0][1], minHeap[0][1]) + 1

            while maxHeap[0][1] < left:
                heappop(maxHeap)
            while minHeap[0][1] < left:
                heappop(minHeap)

        maxLength = max(maxLength, right - left + 1)

    return maxLength


print(longestSubarray([10, 1, 2, 4, 7, 2], 5))  # 4
print(longestSubarray([8, 4, 2, 7], 4))  # 2
```

### [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream)
```python

```

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
                bricks += -heappop(heap)
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

### [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops)
```python
def minRefuelStops(target, startFuel, stations):
    heap = []
    ans = 0
    stations += [[target, 0]]
    for i, [station, fuel] in enumerate(stations):
        startFuel -= station - stations[i - 1][0] if i != 0 else station

        while heap and startFuel < 0:
            tmp_fuel = heappop(heap)
            startFuel += -tmp_fuel
            ans += 1

        if startFuel < 0:
            return -1

        heappush(heap, -fuel)
    return ans


print(minRefuelStops(130, 20, [[10, 60], [30, 30], [40, 10], [60, 70]]))
print(minRefuelStops(100, 1, [[10, 100]]))
```

## K Number of Heaps 
### [Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists)
```python
def smallestRange(nums):
    cur_max = float("-inf")

    heap = []
    for i in range(len(nums)):
        cur_max = max(cur_max, nums[i][0])
        heap.append((heappop(nums[i]), i))

    heapify(heap)

    aRange = [heap[0][0], cur_max]
    cur_range = cur_max - heap[0][0]

    while True:
        _, tmpIdx = heap[0]

        if not nums[tmpIdx]:
            return aRange
        num = heappop(nums[tmpIdx])

        if num > cur_max:
            cur_max = num

        heapreplace(heap, (num, tmpIdx))
        if cur_max - heap[0][0] < cur_range:
            aRange = [heap[0][0], cur_max]
            cur_range = cur_max - heap[0][0]


print(
    smallestRange(
        [
            [4, 10, 15, 24, 26],
            [0, 9, 12, 20],
            [5, 18, 22, 30]
        ]
    )
)
```
