# Greedy
**Greedy** algorithm is nothing but a paradigm which builds problems piece by piece. In recursion, we keep on dividing a big problem into multiple smaller chunks and solving those sub problems which is finally used to solve our actual problem. But this isn't the case for Greedy. In this, at any instant, we choose a piece of solution which will offer the most obvious and immediate benefit.

# Pattern
## Tracking Minimum/Maximum Reachable Value
### [Minimum Number of Coins to be Added](https://leetcode.com/problems/minimum-number-of-coins-to-be-added/)
Sorting would work too, but using heap is less error prone because you don't have to check wether the index is out of bound.
```python
def minimumAddedCoins(coins: List[int], target: int) -> int:
    heapify(coins)
    curIdx = ans = 0
    reachable = 0

    while reachable < target:
        if not coins or reachable < coins[0] - 1:
            reachable = reachable + reachable + 1
            ans += 1
            continue

        if coins:
            reachable += heappop(coins)
            curIdx += 1
    return ans


print(minimumAddedCoins([6, 6, 6, 15, 4], 31))  # 2 (1, 2)
print(minimumAddedCoins([15, 1, 12], 43))  # 4 (2, 4, 8)
print(minimumAddedCoins([1, 1, 1], 20))  # (4, 8, 16)
print(minimumAddedCoins([1, 4, 10, 5, 7, 19], 19))  # 1  (2)
print(minimumAddedCoins([1, 4, 10], 19))  # 2 (2, 8)
```

### [Jump Game](https://leetcode.com/problems/jump-game/)
```python
def canJump(nums):
    maxReachable = 0
    for i in range(len(nums)):
        if i > maxReachable:
            return False
        maxReachable = max(maxReachable, i + nums[i])  # 2
        if maxReachable >= len(nums) - 1:
            return True
    return False


print(canJump([2, 3, 1, 1, 4]))  # True
print(canJump([2, 2, 1, 0, 1, 4]))  # False
```

### [Jump Game II](https://leetcode.com/problems/jump-game-ii/)
```python
def jump(nums):
    if len(nums) <= 2:
        return len(nums) - 1

    reachableIndex = 0
    previousReachableIndex = 0
    count = 0

    for i, v in enumerate(nums):
        reachableIndex = max(reachableIndex, i + v)

        if reachableIndex >= len(nums) - 1:
            return count + 1

        if i == previousReachableIndex:
            count += 1
            previousReachableIndex = reachableIndex


print(jump([2, 3, 1, 1, 4, 1]))  # 3
"""
Greedy Approach
Starting from index 0
1. Can jump to index 1 and 2.
    - Update jump count
2. Check maximum jump point from index 1 and 2. If the maximum jump point is reached (index 2) and we can still not finish jumping to the last index. Update jump count.
    - Index 1 can jump to 4
    - Index 2 can jump to 3
        - Reach index 2 and last index jump is still not possible. Update jump count.
3. Repeat for the next windows and so on ...
    Checking maximum jump point from index 3 and 4 ...
"""
print(jump([2, 3, 1, 1, 4]))  # 2
print(jump([1, 2, 3]))  # 2
```

## Tracking Minimum/Maximum
### [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)
```python
def maxProfit(prices):
    m = 0
    curMin = prices[0]
    for price in prices[1:]:
        if price > curMin:
            m = max(m, price - curMin)
        else:
            curMin = price
    return m

print(maxProfit([7, 1, 5, 3, 6, 4]))
```

### [Minimum Cost for Cutting Cake I](https://leetcode.com/problems/minimum-cost-for-cutting-cake-i)
```python
def minimumCost(m, n, horizontalCut, verticalCut):
    h = sorted(horizontalCut)
    v = sorted(verticalCut)
    sumH = sum(h)
    sumV = sum(v)
    res = 0
    while h and v:
        if h[-1] > v[-1]:
            res += h[-1] + sumV
            sumH -= h.pop()
        else:
            res += v[-1] + sumH
            sumV -= v.pop()
    return res + sumH + sumV


print(minimumCost(3, 3, [1, 4], [5, 1]))  # 18
"""
      5   1
    *   *   *
1
    *   *   *
4
    *   *   *

Same as:

      5   1
    * | *   *
4   - |
    * | *   *
1   - |
    * | *   *
ans = 0 + 5 + 4 + 1 = 10

      5   1
    * | *   * 
1   - |       
    * | *   *
4   - | - - -
    * | * | *

ans = 10 + 4 + 1 = 15
...
"""
```

#### Interval
Usually can be solved by sorting the intervals and keep track of a maximum/minimum of an interval and update it gradually.
### [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
```python
def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    ans = 0
    k = -inf

    for start, end in intervals:
        if start >= k:
            k = end
        else:
            ans += 1

    return ans


print(eraseOverlapIntervals([[1, 8], [4, 5], [3, 4], [2, 9]]))  # 2
print(eraseOverlapIntervals([[1, 5], [5, 10], [4, 7], [7, 8], [8, 9]]))  # 2
```

## Tracking Minimum/Maximum (Monotonicity)
### [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii)
```python
def maxProfit(prices):
    boughAt = 0
    ans = 0
    for i, value in enumerate(prices[1:], 1):
        if value > prices[boughAt]:
            ans += (value - prices[boughAt])
            boughAt = i
        else:
            boughAt = i
    return ans

print(maxProfit([7, 1, 5, 3, 6, 4]))  # 7
```

### [Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)
```python
def maxProfit(prices, fee):
    boughtAt = prices[0]
    ans = 0
    for i, value in enumerate(prices[1:], 1):
        if value > boughtAt + fee:
            ans += (value - boughtAt - fee)
            boughtAt = value - fee
        else:
            boughtAt = min(boughtAt, prices[i])
    return ans


print(maxProfit(prices=[1, 3, 2, 8, 13], fee=2))  # 10
print(maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3))  # 6
```

## Early Feasibility Check
### [Gas Station](https://leetcode.com/problems/gas-station/)
```python
def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    total = 0
    start = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])
        if total < 0:
            total = 0
            start = i + 1

    return start


print(canCompleteCircuit([1, 2, 2, 4, 10], [3, 4, 1, 6, 2]))  # 4
print(canCompleteCircuit([5, 1, 4, 1], [2, 1, 5, 3]))  # 0
```

## Greedy. Keeping Max (or Min) element to replace with Heap
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

### [Minimum Number of Seconds to Make Mountain Height Zero](https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/)
```python
def minNumberOfSeconds(mountainHeight, workerTimes):
    heap = [(time, time, 0) for time in workerTimes]
    heapify(heap)
    
    while mountainHeight > -1:
        totalTime, originalTime, multiplier = heap[0]
        newMultiplier = multiplier + 1
        newTotalTime = originalTime * ((newMultiplier * (newMultiplier + 1)) // 2)
        heapreplace(heap, (newTotalTime, originalTime, newMultiplier))
        mountainHeight -= 1
    return heappop(heap)[0]


print(minNumberOfSeconds(4, [5, 1]))  # 6
"""
Heap:  [(1, 1, 1), (5, 5, 1)]
---
Popping from heap: (1, 1, 1)
New Total Time: 3 , Original Time: 1 , New Multiplier: 2
Heap: [(3, 1, 2), (5, 5, 1)]

---
Popping from heap: (3, 1, 2)
New Total Time: 6 , Original Time: 1 , New Multiplier: 3
Heap: [(5, 5, 1), (6, 1, 3)]

---
Popping from heap: (5, 5, 1)
New Total Time: 15 , Original Time: 5 , New Multiplier: 2
Heap: [(6, 1, 3), (15, 5, 2)]

---
Answer = `totalTime` of the first element of the heap.
Answer = 6
"""
```
