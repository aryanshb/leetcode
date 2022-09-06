# [118] Pascal's Triangle

**[array, dynamic-programming]**

### Statement

Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:
![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
**Example 1:**

```
**Input:** numRows = 5
**Output:** [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

```
**Example 2:**

```
**Input:** numRows = 1
**Output:** [[1]]

```

**Constraints:**
* `1 <= numRows <= 30`


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans
            
            
```

<br>

### Statistics

- total accepted: 981929
- total submissions: 1438598
- acceptance rate: 68.3%
- likes: 7700
- dislikes: 254

<br>

### Similar Problems

- [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii) (Easy)
