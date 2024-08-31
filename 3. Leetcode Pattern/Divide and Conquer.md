# Divide and Conquer
Divide and Conquer is a technique to solve problems by dividing them into smaller sub-problems. It is a recursive algorithm that involves three steps at each level of the recursion:
1. **Divide**: Break the problem into smaller sub-problems that are similar to the original problem.
2. **Conquer**: Solve the sub-problems recursively. If the sub-problem is small enough, solve it directly.
3. **Combine**: Combine the solutions of the sub-problems to solve the original problem.

# Pattern
## Merge Sort
### [Merge Sort](https://leetcode.com/problems/sort-an-array/)
```python
def merge(left, right):
    sortedPortion = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedPortion.append(left[i])
            i += 1
        else:
            sortedPortion.append(right[j])
            j += 1

    sortedPortion.extend(left[i:])
    sortedPortion.extend(right[j:])
    return sortedPortion


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)


print(mergeSort([3, 2, 1, 4, 5]))  # [1, 2, 3, 4, 5]
```

### Count Inversions
Given an array of distinct integers, count the number of inversion pairs in the array.

An inversion pair (𝑖,𝑗) is defined as a pair of indices 𝑖,𝑗 such that:
- `0 ≤ i < j < n`
- `a[i] > a[j]`

For example:
Given the array: `a=[3,5,2,1,6]`
The result is `5` and the inversion pairs are
- `(3,2), (3,1), (5,2), (5,1), (2,1)`

```python
def countInversions(arr):
    invCount = 0

    def mergeAndCount(portion):
        nonlocal invCount
        tempArr = [0] * len(portion)
        left, right = 0, len(portion) - 1
        rightStart = len(portion) // 2  # Starting index for right subarray
        leftEnd = rightStart - 1
        curTmpIdx = left  # Starting index to be sorted in tempArr

        # Merge the two portions of the array and count inversions
        while left <= leftEnd and rightStart <= right:
            if portion[left] <= portion[rightStart]:
                tempArr[curTmpIdx] = portion[left]
                left += 1
            else:
                # arr[left] > arr[rightStart] indicates inversions
                tempArr[curTmpIdx] = portion[rightStart]
                invCount += (leftEnd - left) + 1  # Count inversions
                rightStart += 1
            curTmpIdx += 1

        # Copy the remaining elements of left subarray, if any
        while left <= leftEnd:
            tempArr[curTmpIdx] = portion[left]
            left += 1
            curTmpIdx += 1

        # Copy the remaining elements of right subarray, if any
        while rightStart <= right:
            tempArr[curTmpIdx] = portion[rightStart]
            rightStart += 1
            curTmpIdx += 1

        return tempArr

    def mergeSort(portion):
        if len(portion) <= 1:
            return portion

        mid = len(portion) // 2
        leftPortion = mergeSort(portion[:mid])
        rightPortion = mergeSort(portion[mid:])

        mergedPortion = mergeAndCount(leftPortion + rightPortion)
        return mergedPortion

    mergeSort(arr)
    return invCount


print(countInversions([1, 3, 5, 2, 4, 6]))  # 3
# (3,2), (5,2), (5,4)
```

## Multi-Dimensional
### [Closest Pair of Points](https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/)
Given a set of points in a plane, find the closest pair of points.

```python
from math import sqrt


def closestPairOfPoints(points):
    def calculateDistance(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def mergeCandidates(leftPortion, rightPortion):
        mergedPortion = []
        i = j = 0
        while i < len(leftPortion) and j < len(rightPortion):
            if leftPortion[i][1] < rightPortion[j][1]:
                mergedPortion.append(rightPortion[j])
                j += 1
            else:
                mergedPortion.append(leftPortion[i])
                i += 1

        if i < len(leftPortion):
            mergedPortion.extend(leftPortion[i:])

        if j < len(rightPortion):
            mergedPortion.extend(rightPortion[j:])
        return mergedPortion

    def updateMinDistance(leftPoint, rightCandidates, startIndex, minDistance):
        for k in range(startIndex, min(startIndex + 4, len(rightCandidates))):
            minDistance = min(
                minDistance,
                calculateDistance(leftPoint[0], leftPoint[1], rightCandidates[k][0], rightCandidates[k][1])
            )
        return minDistance

    points.sort()

    def divideAndConquer(portion):
        if len(portion) <= 3:
            return min(
                calculateDistance(portion[i][0], portion[i][1], portion[j][0], portion[j][1])
                for i in range(len(portion))
                for j in range(i + 1, len(portion))
            ), sorted(portion, key=lambda x: -x[1])

        mid = len(portion) // 2
        midPoint = (portion[mid - 1][0] + portion[mid][0]) / 2
        left, leftSorted = divideAndConquer(portion[:mid])
        right, rightSorted = divideAndConquer(portion[mid:])

        minDistance = min(left, right)
        leftCandidates = [point for point in leftSorted if midPoint - point[0] <= minDistance]
        rightCandidates = [point for point in rightSorted if point[0] - midPoint <= minDistance]

        lenLeft, lenRight = len(leftCandidates), len(rightCandidates)
        i = j = 0
        while i < lenLeft and j < lenRight:
            if leftCandidates[i][1] < rightCandidates[j][1]:
                minDistance = updateMinDistance(leftCandidates[i], rightCandidates, j, minDistance)
                i += 1
            else:
                minDistance = updateMinDistance(rightCandidates[j], leftCandidates, i, minDistance)
                j += 1

        return minDistance, mergeCandidates(leftSorted, rightSorted)

    res, _ = divideAndConquer(points)
    return res


print(closestPairOfPoints([(0, 5), (0, 6), (3, 2), (3, 3), (5, 3), (5, 4), (8, 1), (8, 5)]))  # 2.0
```
You can either:
- Iterate 7 times for each point if you decide to merge the two sorted arrays first
- Iterate 4 times for each point in both the left and right sorted arrays if you decide to merge the two sorted arrays later.

Proof of the closest pair of points algorithm: [Closest Pair of Points Proof](https://www.youtube.com/watch?v=kCLGVat2SHk&t=945s)
