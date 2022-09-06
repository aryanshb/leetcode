# [417] Pacific Atlantic Water Flow

**[array, depth-first-search, breadth-first-search, matrix]**

### Statement

There is an `m x n` rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The **Pacific Ocean** touches the island's left and top edges, and the **Atlantic Ocean** touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the **height above sea level** of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return *a **2D list** of grid coordinates* `result` *where* `result[i] = [ri, ci]` *denotes that rain water can flow from cell* `(ri, ci)` *to **both** the Pacific and Atlantic oceans*.


**Example 1:**
![](https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg)

```

**Input:** heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
**Output:** [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
**Explanation:** The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
      [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
      [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
      [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
      [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
      [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
      [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

```

**Example 2:**

```

**Input:** heights = [[1]]
**Output:** [[0,0]]
**Explanation:** The water can flow from the only cell to the Pacific and Atlantic oceans.

```

**Constraints:**
* `m == heights.length`
* `n == heights[r].length`
* `1 <= m, n <= 200`
* `0 <= heights[r][c] <= 105`


<br>

### Hints

None

<br>

### Solution

```py

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        r, c = len(heights), len(heights[0])
        atlantic = [[False for i in range(c)] for j in range(r)]
        pacific = [[False for i in range(c)] for j in range(r)]

        ans = []
        for i in range(r):
            self.dfs(heights, i, 0, r, c, pacific)
            self.dfs(heights, i, c-1, r, c, atlantic)
        # print(pacific)
        # print(atlantic)
        for i in range(c):
            self.dfs(heights, 0, i, r, c, pacific)
            self.dfs(heights, r-1, i, r, c, atlantic)
            
        for i in range(r):
            for j in range(c):
                if atlantic[i][j] and pacific[i][j]:
                    ans.append([i, j])
        
        return ans
    
    def dfs(self, heights, i, j, r, c, visited):
        visited[i][j] = True
        for direction in self.dir:
            x, y = i + direction[0], j + direction[1]
            if x < 0 or y < 0 or x >= r or y >=c or heights[x][y] < heights[i][j] or visited[x][y]:
                continue
            self.dfs(heights, x, y, r, c, visited)
            
                
```

<br>

### Statistics

- total accepted: 278970
- total submissions: 525893
- acceptance rate: 53.0%
- likes: 5336
- dislikes: 1011

<br>

### Similar Problems

None
