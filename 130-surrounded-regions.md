# [130] Surrounded Regions

**[array, depth-first-search, breadth-first-search, union-find, matrix]**

### Statement

Given an `m x n` matrix `board` containing `'X'` and `'O'`, *capture all regions that are 4-directionallysurrounded by* `'X'`.

A region is **captured** by flipping all `'O'`s into `'X'`s in that surrounded region.


**Example 1:**
![](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)

```

**Input:** board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
**Output:** [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
**Explanation:** Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

```

**Example 2:**

```

**Input:** board = [["X"]]
**Output:** [["X"]]

```

**Constraints:**
* `m == board.length`
* `n == board[i].length`
* `1 <= m, n <= 200`
* `board[i][j]` is `'X'` or `'O'`.


<br>

### Hints

None

<br>

### Solution

```py
# perform dfs on edges to mark edge 'O' and its component as visited
# flip remaining 'O's to 'X' and turn the 'Z's back to 'O's 
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def dfs(r, c):
            board[r][c] = 'Z'
            for dx, dy in (0,1), (1,0), (-1,0), (0,-1):
                x, y = r+dx, c+dy
                if x<0 or y<0 or x>=len(board) or y>=len(board[0]) or board[x][y] != 'O':
                    continue
                dfs(x, y)
                
        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or i==m-1 or j==n-1:
                    if board[i][j] == 'O':
                        dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                elif board[i][j] == 'Z': board[i][j] = 'O'
                    
        for i in range(m):
            for j in range(n):
                print(board[i][j], end = " ")
            print("")
            
```

<br>

### Statistics

- total accepted: 465644
- total submissions: 1309637
- acceptance rate: 35.6%
- likes: 5761
- dislikes: 1347

<br>

### Similar Problems

- [Number of Islands](https://leetcode.com/problems/number-of-islands) (Medium)
- [Walls and Gates](https://leetcode.com/problems/walls-and-gates) (Medium)
