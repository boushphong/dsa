# Weighted Graph
# Patterns
## Exploring all shortest paths with Floyd-Warshall
### [Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
```python
def findTheCity(n, edges, distanceThreshold):
    dist = [[float("inf")] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, weight in edges:
        dist[u][v] = weight
        dist[v][u] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    minReachable = float("inf")
    ans = n - 1

    for node in range(n - 1, -1, -1):
        tmpMinReachable = sum([1 if _ <= distanceThreshold else 0 for _ in dist[node]])
        if tmpMinReachable < minReachable:
            ans = node
            minReachable = tmpMinReachable

    return ans


print(findTheCity(4, [
    [0, 1, 3], 
    [1, 2, 1], 
    [1, 3, 4], 
    [2, 3, 1]
], 4))  # 3
```