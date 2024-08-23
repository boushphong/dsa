# Weighted Graph
# Patterns
## BFS
### [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
```python
def findCheapestPrice(n, flights, src, dst, k):
    graph = defaultdict(dict)

    for fromNode, toNode, weight in flights:
        graph[fromNode].update({toNode: weight})

    distance = [float("inf")] * n
    distance[src] = 0

    queue = deque([(src, 0)])
    stops = 0

    while stops <= k and queue:
        for _ in range(len(queue)):
            curNode, curCost = queue.popleft()
            for neighbor, price in graph[curNode].items():
                if price + curCost >= distance[neighbor]:
                    continue
                distance[neighbor] = price + curCost
                queue.append((neighbor, distance[neighbor]))
        stops += 1

    return -1 if distance[dst] == float("inf") else distance[dst]


print(findCheapestPrice(n=4,
                        flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
                        src=0,
                        dst=3,
                        k=1))  # 700
```

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

## Explore all shortest paths of a node with Dijikstra
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

### [Number of Restricted Paths From First to Last Node](https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/)
```python
def countRestrictedPaths(n, edges):
    graph = {i: {} for i in range(n)}

    for fromNode, toNode, weight in edges:
        graph[fromNode - 1][toNode - 1] = weight
        graph[toNode - 1][fromNode - 1] = weight

    dist = [float('inf')] * n
    dist[n - 1] = 0
    heap = [(0, n - 1)]

    while heap:
        curDistance, curV = heappop(heap)
        if curDistance > dist[curV]:
            continue

        for neighbor, weight in graph.get(curV).items():
            distance = curDistance + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heappush(heap, (distance, neighbor))

    @lru_cache(None)
    def dfs(node=0):
        if node == n - 1:
            return 1

        ans = 0
        for neighbor, _ in graph.get(node).items():
            if dist[neighbor] < dist[node]:
                ans += dfs(neighbor)

        return ans

    return dfs() % (10**9 + 7)


print(countRestrictedPaths(5, [[1, 2, 3], [1, 3, 3], [2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1], [5, 4, 10]]))  # 3
```

### [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
**Dijikstra** has a special characteristic that once a node is popped out of the heap, that means we have found the shortest distance to that node.

```python
def findCheapestPrice(n, flights, src, dst, k):
    graph = defaultdict(dict)

    for fromNode, toNode, weight in flights:
        graph[fromNode].update({toNode: weight})

    visited = {}
    heap = [(0, src, 0)]
    while heap:
        curDistance, curNode, stop = heappop(heap)
        if curNode == dst:
            return curDistance

        if (curNode, stop) in visited and curDistance >= visited[(curNode, stop)]:
            continue
        visited[(curNode, stop)] = curDistance

        for neighbor, cost in graph[curNode].items():
            toDistance = curDistance + cost
            if neighbor != dst and stop == k:
                continue
            heappush(heap, (toDistance, neighbor, stop + 1))

    return -1


print(findCheapestPrice(n=4,
                        flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
                        src=0,
                        dst=3,
                        k=1))  # 700
```
