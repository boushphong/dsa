# Weighted Graph
# Patterns
## Explore all shortest paths of every node with Floyd-Warshall
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

## Explore all shortest paths of a node
### [Network Delay Time](https://leetcode.com/problems/network-delay-time)
```python
def networkDelayTime(times, n, k):
    graph = {i: {} for i in range(1, n + 1)}
    for from_node, to_node, weight in times:
        graph[from_node][to_node] = weight

    dist = [float('inf')] * (n + 1)
    dist[k] = 0
    heap = [(0, k)]

    while heap:
        curDistance, curV = heappop(heap)
        if curDistance > dist[curV]:
            continue

        for neighbor, weight in graph.get(curV).items():
            distance = curDistance + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heappush(heap, (distance, neighbor))

    dist[k] = float("-inf")
    res = max(dist[1:])
    if res == float("inf"):
        return -1
    return res


print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # 2
print(networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 1]], 3, 2))  # -1
```

### [Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/)
**Dijikstra** works with motonic increasing (for shortest path hence min-heap) or decreasing behavior (max-heap).
- Maximum probability is found by multiplying 2 large probability together. Hence decreasing behavior is found (multipling probability will guarantee to have a smaller or equal probability), hence we would use a max-heap to track the largest probability along the path till we reach the destination.

```python
def maxProbability(n, edges, succProb, start_node, end_node):
    graph = {i: {} for i in range(n)}
    for (from_node, to_node), weight in zip(edges, succProb):
        graph[from_node][to_node] = weight
        graph[to_node][from_node] = weight

    distance = [0] * n
    distance[start_node] = -1
    heap = [(-1, start_node)]

    while heap:
        curProb, curV = heappop(heap)
        if abs(curProb) < distance[curV]:
            continue

        for neighbor, weight in graph.get(curV).items():
            prob = abs(curProb) * weight

            if prob > distance[neighbor]:
                distance[neighbor] = prob
                if neighbor != end_node:
                    heappush(heap, (-prob, neighbor))

    return distance[end_node]


print(maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))  # 0.25
```
