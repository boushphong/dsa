# Bit Manipulation
| X | Y | X&Y | X\|Y | X^Y | ~(X) |
|---|---|-----|-----|-----|------|
| 0 | 0 |  0  |  0  |  0  |  1   |
| 0 | 1 |  0  |  1  |  1  |  1   |
| 1 | 0 |  0  |  1  |  1  |  0   |
| 1 | 1 |  1  |  1  |  0  |  0   |

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

### Flip k_th bit of number x
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
