# Sieve of Eratosthenes

**Sieve of Eratosthenes** is an algorithm for finding all prime numbers up to any given limit, which has a time complexity of `O(N log(log(N))` for generating all prime numbers up to `N`. 

1. **Outer loop (over `p`)**: The loop runs from `p = 2` to `sqrt(n)`, which makes about `O(sqrt(n))` iterations.
2. **Inner operation (removing multiples)**: For each prime number `p`, it removes multiples of `p` from the set of possible primes. The number of multiples removed for each prime decreases as `p` increases.

The total number of steps for removing multiples across all primes is roughly proportional to `N log(log(N)`. This comes from the harmonic series analysis applied to the prime numbers.

## Complexity Analysis
- **Time Complexity**: `O(N log(log(N))`
- **Space Complexity**: `O(N)` due to the `primes` set holding numbers up to `N`.

## Implementation
```python
def generatePrimes(n):
    if n < 2:
        return []

    primes = set(range(2, n + 1))

    for p in range(2, int(n ** 0.5) + 1):
        pSquared = p ** 2
        if pSquared > n:
            break
        if p in primes:
            multiples = set(range(pSquared, n + 1, p))
            primes -= multiples

    return list(primes)


print(generatePrimes(100))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```
