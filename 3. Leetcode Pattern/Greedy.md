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
