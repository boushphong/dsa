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


print(findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))  # 700
```

## Explore all shortest paths of every node
#### With Floyd-Warshall
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

#### With Dijikstra
To explore all shortest paths of every node with Dijikstra **at once**. We have to add all vertices into the heap first before the while loop. However, the TC also would differ, be reduced from the original (1st) method.
1. **Dijikstra (explore all shortest paths of a node |V| times):** `O(|V| * ((|V| + |E|) * Log(|V|))` (With Fibonacci Heap)
2. **Dijikstra (explore all shortest paths of every node at once):** `O((|V| + |E|) * Log(|V| + |E|))` (With Fibonacci Heap)

```python
def findTheCity(n, edges, distanceThreshold):
    graph = defaultdict(dict)

    for cityA, cityB, cost in edges:
        graph[cityA].update({cityB: cost})
        graph[cityB].update({cityA: cost})

    reachableCities = defaultdict(set)
    heap = [(0, _, _) for _ in range(n)]
    distances = set()

    while heap:
        curDistance, curCity, originCity = heappop(heap)

        if (originCity, curCity) in distances:
            continue
        else:
            distances.add((originCity, curCity))

        for neighbor, cost in graph[curCity].items():
            if originCity == neighbor:
                continue
            distance = curDistance + cost

            if distance <= distanceThreshold:
                reachableCities[originCity].add(neighbor)
                if distance < distanceThreshold:
                    heappush(heap, (distance, neighbor, originCity))

    minReachable = n
    ans = n - 1
    for city in range(n - 1, -1, -1):
        tmpMinReachable = len(reachableCities[city])
        if tmpMinReachable < minReachable:
            ans = city
            minReachable = tmpMinReachable

    return ans


print(findTheCity(6, [[0, 3, 7], [2, 4, 1], [0, 1, 5], [2, 3, 10], [1, 3, 6], [1, 2, 1]], 417))  # 5
print(findTheCity(6, [[0, 1, 10], [0, 2, 1], [2, 3, 1], [1, 3, 1], [1, 4, 1], [4, 5, 10]], 20))  # 5
print(findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4))  # 3
```

### [Minimum Cost to Buy Apples](https://leetcode.com/problems/minimum-cost-to-buy-apples/)
```python
def minCost(n, roads, appleCost, k):
    graph = defaultdict(dict)

    for cityA, cityB, cost in roads:
        graph[cityA - 1].update({cityB - 1: cost})
        graph[cityB - 1].update({cityA - 1: cost})

    result = appleCost.copy()

    heap = [(cost, start) for start, cost in enumerate(appleCost)]
    heapify(heap)

    while heap:
        totalCost, curCity = heappop(heap)

        if result[curCity] < totalCost:
            continue

        for neighbor, cost in graph[curCity].items():
            if result[neighbor] > result[curCity] + (k + 1) * cost:
                result[neighbor] = result[curCity] + (k + 1) * cost
                heappush(heap, (result[neighbor], neighbor))

    return result


print(minCost(4, [[1, 2, 4], [2, 3, 2], [2, 4, 5], [3, 4, 1], [1, 3, 4]], [56, 42, 102, 301], 2))  # [54, 42, 48, 51]
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
    graph = defaultdict(dict)
    for (fromNode, toNode), weight in zip(edges, succProb):
        graph[fromNode].update({toNode: weight})
        graph[toNode].update({fromNode: weight})

    distance = [0] * n
    distance[start_node] = -1
    heap = [(-1, start_node)]
    seen = set()

    while heap:
        curProb, curV = heappop(heap)
        seen.add(curV)
        if curProb > distance[curV]:
            continue

        for neighbor, weight in graph[curV].items():
            if neighbor in seen:
                continue
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
    graph = defaultdict(dict)
    for fromNode, toNode, weight in edges:
        graph[fromNode - 1].update({toNode - 1: weight})
        graph[toNode - 1].update({fromNode - 1: weight})

    dist = [float('inf')] * n
    dist[n - 1] = 0
    heap = [(0, n - 1)]

    while heap:
        curDistance, curV = heappop(heap)
        if curDistance > dist[curV]:
            continue

        for neighbor, weight in graph[curV].items():
            distance = curDistance + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heappush(heap, (distance, neighbor))

    @lru_cache(None)
    def dfs(node=0):
        if node == n - 1:
            return 1

        ans = 0
        for neighbor, _ in graph[node].items():
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


print(findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))  # 700
```

#### In Matrix
### [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
```python
def minimumEffortPath(heights):
    m, n = len(heights), len(heights[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    distance = [[inf] * n for _ in range(m)]
    distance[0][0] = 0
    heap = [(0, 0, 0)]

    while heap:
        curDistance, curRow, curCol = heappop(heap)
        if curDistance > distance[curRow][curCol]:
            continue

        if curRow == m - 1 and curCol == n - 1:
            return curDistance

        for movedByRow, movedByCol in directions:
            tmpCurRow, tmpCurCol = curRow + movedByRow, curCol + movedByCol
            if tmpCurRow in {-1, m} or tmpCurCol in {-1, n}:
                continue
            toNewNodeDistance = max(curDistance, abs(heights[tmpCurRow][tmpCurCol] - heights[curRow][curCol]))

            if toNewNodeDistance < distance[tmpCurRow][tmpCurCol]:
                distance[tmpCurRow][tmpCurCol] = toNewNodeDistance
                heappush(heap, (toNewNodeDistance, tmpCurRow, tmpCurCol))


print(
    minimumEffortPath(
        [
            [1, 2, 2],
            [3, 8, 2],
            [5, 3, 5]
        ]
    )
)  # 2


print(
    minimumEffortPath(
        [
            [1, 2, 1, 1, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 1, 1, 2, 1]
        ]
    )
)  # 0
```
