# [54] Spiral Matrix

**[array, matrix, simulation]**

### Statement

Given an `m x n` `matrix`, return *all elements of the* `matrix` *in spiral order*.


**Example 1:**
![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

```

**Input:** matrix = [[1,2,3],[4,5,6],[7,8,9]]
**Output:** [1,2,3,6,9,8,7,4,5]

```

**Example 2:**
![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

```

**Input:** matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
**Output:** [1,2,3,4,8,12,11,10,9,5,6,7]

```

**Constraints:**
* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 10`
* `-100 <= matrix[i][j] <= 100`


<br>

### Hints

- Well for some problems, the best way really is to come up with some algorithms for simulation. Basically, you need to simulate what the problem asks us to do.
- We go boundary by boundary and move inwards. That is the essential operation. First row, last column, last row, first column, and then we move inwards by 1 and repeat. That's all. That is all the simulation that we need.
- Think about when you want to switch the progress on one of the indexes. If you progress on i out of [i, j], you'll shift in the same column. Similarly, by changing values for j, you'd be shifting in the same row.
Also, keep track of the end of a boundary so that you can move inwards and then keep repeating. It's always best to simulate edge cases like a single column or a single row to see if anything breaks or not.

<br>

### Solution

```py
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        result = []
        i = 0
        j = 0
        while i < m and j < n:
            for k in range(j, n):
                result.append(matrix[i][k])
            i += 1
            for k in range(i, m):
                result.append(matrix[k][n-1])
            n -= 1
            if i < m:
                for k in range(n-1, j-1, -1):
                    result.append(matrix[m-1][k])
                m -= 1
            if j < n:
                for k in range(m-1, i-1, -1):
                    result.append(matrix[k][j])
                j += 1
        return result
```

<br>

### Statistics

- total accepted: 872598
- total submissions: 2007454
- acceptance rate: 43.5%
- likes: 9165
- dislikes: 927

<br>

### Similar Problems

- [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii) (Medium)
- [Spiral Matrix III](https://leetcode.com/problems/spiral-matrix-iii) (Medium)
- [Spiral Matrix IV](https://leetcode.com/problems/spiral-matrix-iv) (Medium)
