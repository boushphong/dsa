# Bit Manipulation
| X | Y | X&Y | X\|Y | X^Y | ~(X) |
|---|---|-----|------|-----|------|
| 0 | 0 | 0   | 0    | 0   | 1    |
| 0 | 1 | 0   | 1    | 1   | 1    |
| 1 | 0 | 0   | 1    | 1   | 0    |
| 1 | 1 | 1   | 1    | 0   | 0    |

## Bit Representation
```
a = 12   →  00000000 00000000 00000000 00001100

b = 10   →  00000000 00000000 00000000 00001010

a & b    →  00000000 00000000 00000000 00001000

a | b    →  00000000 00000000 00000000 00001110

a ^ b    →  00000000 00000000 00000000 00000110

~a       →  11111111 11111111 11111111 11110011
```

## Signed Numbers: 2's complement
The sign of the binary number is determined by the leading (furthest left) digit.
- 0 for positive
- 1 for negative

```
a = 12   →  00000000 00000000 00000000 00001100

~a       →  11111111 11111111 11111111 11110011

-a       →  11111111 11111111 11111111 11110100

11110011 (0011 = 3) -> 11110100 (0100 = 4) 
```

## Converting a Positive Integer to Negative
In Python, negative integers are represented using **two's complement** when working with bits. Here's how it works:

### Example:
Let's represent `-5` in an 8-bit format:
1. First, take the binary of `5`: `00000101` (in 8 bits).
2. Flip the bits: `11111010`.
3. Add 1: `11111010 + 1 = 11111011`.

So, `-5` is represented as `11111011` in an 8-bit two's complement format.

**Note:** Add 1 means to "carry" to the next bit. If the rightmost bit is already 1 then the next rightmost 0 will be replaced with 1.

## Common Tricks
- **x ^ 0s = x**
- **x ^ 1s = ~x**
- **x ^ x = 0**
- **x & 0s = 0**
- **x & 1s = x**
- **x & x = x**
- **x | 0s = x**
- **x | 1s = 1s**
- **x | x = x**

## Bit Shifting
### Left Shift (Arithmetic)
```
a = 6   →  00000000 00000000 00000000 00000110

a << 1  →  00000000 00000000 00000000 00001100
```

### Right Shift (Arithmetic)
```
a = 6   →  00000000 00000000 00000000 00000110

a >> 1  →  00000000 00000000 00000000 00000011
```

### Logical vs Arithmetic Shifting 
```
a = -3  →  00000000 00000000 00000000 00000110

a >> 1  →  11111111 11111111 11111111 11111110 (a = -2) (Arithmetic)

a >> 1  →  01111111 11111111 11111111 11111110 (a = 2147483646) (Logical)
```

# Patterns
## Common Patterns
### Get k-th bit of number x
```python
def getBit(x, k):
    return (x >> k) & 1

getBit(13, 2) # 1
"""
00001101 (x)
00000011 (x >> 2)
00000001 (1)
00000001 (x >> 2) & 1
"""

getBit(8, 1) # 0
"""
00001000 (x)
00000100 (x >> 1)
00000001 (1)
00000000 (x >> 1) & 1
"""
```

### Set k-th bit of number x to 1
```python
def setBit(x, k):
    return x | (1 << k)

setBit(13, 4) # 24
"""
00000001 (1)
00010000 (1 << 4)
00001101 (x)
00011101 x | (1 << 4)
"""
```

### Set k-th bit of number x to 0
```python
def clearBit(x, k):
    return x & (~(1 << k))

clearBit(13, 2) # 9
"""
00000001 (1)
00000100 (1 << 2)
11111011 ~(1 << 2)
00001101 (x)
00001001 x & (~(1 << 2))
"""
```

### Flip k-th bit of number x
```python
def flipBit(x, k):
    return x ^ (1 << k)

flipBit(13 , 4) # 29
"""
00000001 (1)
00010000 (1 << 4)
00001101 (x)
00011101 x ^ (1 << 4)
"""
```

### [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits)
```python
def hammingWeight(n):
    res = 0
    while n != 0:
        res += (n & 1)
        n = n >> 1 
    return res


print(hammingWeight(4))  # 1
"""
TC: O(K) (K is the number of bits)
00000100 1st
n >> 1

00000010 2st
n >> 1

00000001 3rd (res += 1)
n >> 1

00000000 end loop
"""
```

```python
def hammingWeight(n):
    res = 0
    while n != 0:
        res += 1
        n = n & (n - 1)
    return res

print(hammingWeight(10))  # 2
"""
TC: O(K) (K is the number of 1 bits)
x           = 00001010
x - 1       = 00001001
x & (x - 1) = 00001000


x           = 00001000
x - 1       = 00000111
x & (x - 1) = 00000000
"""
```

### [Power of Two](https://leetcode.com/problems/power-of-two/)
```python
def isPowerOfTwo(n):
    if n == 0:
        return False
    return n & (n - 1) == 0


print(isPowerOfTwo(2))  # True
print(isPowerOfTwo(3))  # False
"""
00000010 (2)
00000001 (1)
00000000 (0) 2 & 1 -> True

00000011 (3)
00000010 (2)
00000010 (2) 3 & 2 -> False
"""

def isPowerOfTwo(n):
    if n == 0:
        return False
    return n & (-n) == n


print(isPowerOfTwo(2))  # True
print(isPowerOfTwo(3))  # False
"""
00000010 (2)
11111110 (-2)
00000010 (2) 2 & -2 -> True

00000011 (3)
11111101 (-3)
00000001 (1) 3 & -3 -> False
"""
```

### [Number Complement](https://leetcode.com/problems/number-complement/)
```python
# Flip Bit by Bit
def findComplement(num):
    flipRange = floor(log2(num)) + 1
    for i in range(flipRange):
        num ^= (1 << i)
    return num


# Flip only once
def findComplement(num):
    flipNum = floor(log2(num)) + 1
    return num ^ ((1 << flipNum) - 1)


print(findComplement(5))  # 2
```

### [Reverse Bits](https://leetcode.com/problems/reverse-bits/)
**Get and Set**
```python
def reverseBits(n):
    def getBit(x, k):
        return (x >> k) & 1
    
    def setBit(x, k, i):
        if i:
            return x | (1 << k)
        else:
            return x & (~(1 << k))
    
    l, r = 0, 31
    
    while l < r:
        i = getBit(n, l)
        j = getBit(n, r)
        n = setBit(n, l, j)
        n = setBit(n, r, i)
        l += 1
        r -= 1
    
    return n


print(reverseBits(reverseBits(1)))  # 2147483648
```

**Flip**
```python
def reverseBits(n):
    def getBit(x, k):
        return (x >> k) & 1

    def flipBit(x, k):
        return x ^ (1 << k)

    l, r = 0, 31

    while l < r:
        i = getBit(n, l)
        j = getBit(n, r)
        if i != j:
            n = flipBit(n, l)
            n = flipBit(n, r)
        l += 1
        r -= 1
    
    return n
```

### [Single Number](https://leetcode.com/problems/single-number/)
```python
def singleNumber(nums):
    ans = 0
    for _ in nums:
        ans ^= _
    return ans


print(singleNumber([4,1,2,1,2]))  # 4
"""
An integer XORs with itself will return 0
X ^ Y ^ Z ^ Y ^ Z = X ^ (Y ^ Y) ^ (Z ^ Z) = X ^ 0 ^ 0 = X
"""
```

## Subsets
### [Subsets](https://leetcode.com/problems/subsets/)
```python
def subsets(nums):
    def getSubset(i):
        subset = []
        idx = 0

        while i != 0:
            if i & 1:
                subset.append(nums[idx])
            i >>= 1
            idx += 1
        return subset

    aRange = [i for i in range(2 ** len(nums))]

    ans = []
    for _ in aRange:
        ans.append(getSubset(_))

    return ans


print(subsets([1, 2, 3]))
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

## Representing Integer Set (Space Optimization)
### [Can I Win](https://leetcode.com/problems/can-i-win)
```python
def canIWin(maxChoosableInteger, desiredTotal):
    def getBit(x, k):
        return (x >> k) & 1

    def setBit(x, k):
        return x | (1 << k)

    if maxChoosableInteger >= desiredTotal:
        return True

    if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
        return False

    @cache
    def dp(total=0, seen=0):
        if total >= desiredTotal:
            return False

        for num in range(maxChoosableInteger, 0, -1):
            if getBit(seen, num - 1):
                continue
            newSeen = setBit(seen, num - 1)
            if not dp(total + num, newSeen):
                return True

        return False

    return dp()


print(canIWin(maxChoosableInteger=10, desiredTotal=40))  # False
print(canIWin(maxChoosableInteger=10, desiredTotal=0))  # True
print(canIWin(maxChoosableInteger=10, desiredTotal=11))  # False
print(canIWin(maxChoosableInteger=10, desiredTotal=20))  # True
print(canIWin(maxChoosableInteger=10, desiredTotal=21))  # True
```
