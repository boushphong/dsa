# Greedy
**Greedy** algorithm is nothing but a paradigm which builds problems piece by piece. In recursion, we keep on dividing a big problem into multiple smaller chunks and solving those sub problems which is finally used to solve our actual problem. But this isn't the case for Greedy. In this, at any instant, we choose a piece of solution which will offer the most obvious and immediate benefit.

# Pattern
## Tracking Maximum Reachable Value
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

print(maxProfit([7, 1, 5, 3, 6, 4]))
```

### [Minimum Cost for Cutting Cake I](https://leetcode.com/problems/minimum-cost-for-cutting-cake-i)
```python
def minimumCost(m, n, horizontalCut, verticalCut):
    h = sorted(h)
    v = sorted(v)
    sumh = sum(h)
    sumv = sum(v)
    res = 0
    while h and v:
        if h[-1] > v[-1]:
            res += h[-1] + sumv
            sumh -= h.pop()
        else:
            res += v[-1] + sumh
            sumv -= v.pop()
    return res + sumh + sumv


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


print(minimumCost(3, 3, [1, 4], [5, 1]))
```

### [Jump Game](https://leetcode.com/problems/jump-game/)
```python
def canJump(nums):
    max_reachable = 0
    for i in range(len(nums)):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + nums[i])  # 2
        if max_reachable >= len(nums) - 1:
            return True
    return False


print(canJump([2, 3, 1, 1, 4]))
print(canJump([2, 3, 1, 0, 1, 4]))
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
