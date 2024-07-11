# Floyd-Warshall
**Floyd-Warshall** is used to find the shortest path between all pairs of vertices in a weighted graph.
- Negative edges are allowed but there has to be no negative cycles.

**Example:**

Graph representation
```mermaid
graph TD;
    1 -->|3| 2;
    2 -->|2| 3;
    3 -->|1| 4;
    4 -->|2| 1;
    1 -->|7| 4;
    2 -->|8| 1;
```

Matrix Representation

