# Greedy
**Greedy** algorithm is nothing but a paradigm which builds problems piece by piece. In recursion, we keep on dividing a big problem into multiple smaller chunks and solving those sub problems which is finally used to solve our actual problem. But this isn't the case for Greedy. In this, at any instant, we choose a piece of solution which will offer the most obvious and immediate benefit.

# Pattern
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
print(jump([2, 3, 1, 1, 4]))  # 2
print(jump([1, 2, 3]))  # 2
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
