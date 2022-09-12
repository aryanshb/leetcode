# [74] Search a 2D Matrix

**[array, binary-search, matrix]**

### Statement

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:

* Integers in each row are sorted from left to right.
* The first integer of each row is greater than the last integer of the previous row.


**Example 1:**
![](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

```

**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
**Output:** true

```

**Example 2:**
![](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)

```

**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
**Output:** false

```

**Constraints:**
* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 100`
* `-104 <= matrix[i][j], target <= 104`


<br>

### Hints

None

<br>

### Solution

```py
# O(m+n)
import sys
input = sys.stdin.readline
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target <= i[-1]:
                if target == i[-1]: return True
                for j in i:
                    if j == target: return True
                    
        return False
            

```

<br>

### Statistics

- total accepted: 968353
- total submissions: 2088192
- acceptance rate: 46.4%
- likes: 9559
- dislikes: 303

<br>

### Similar Problems

- [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii) (Medium)
