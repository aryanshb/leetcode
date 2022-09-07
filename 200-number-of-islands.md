# [200] Number of Islands

**[array, depth-first-search, breadth-first-search, union-find, matrix]**

### Statement

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


**Example 1:**

```

**Input:** grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
**Output:** 1

```

**Example 2:**

```

**Input:** grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
**Output:** 3

```

**Constraints:**
* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 300`
* `grid[i][j]` is `'0'` or `'1'`.


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(grid, r, c, m, n):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(grid, r+1, c, m, n)
            dfs(grid, r-1, c, m, n)
            dfs(grid, r, c+1, m, n)
            dfs(grid, r, c-1, m, n)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans +=1
                    dfs(grid, i, j, m, n)
        print(grid)
        return ans            
            
```

<br>

### Statistics

- total accepted: 1839195
- total submissions: 3296315
- acceptance rate: 55.8%
- likes: 16810
- dislikes: 386

<br>

### Similar Problems

- [Surrounded Regions](https://leetcode.com/problems/surrounded-regions) (Medium)
- [Walls and Gates](https://leetcode.com/problems/walls-and-gates) (Medium)
- [Number of Islands II](https://leetcode.com/problems/number-of-islands-ii) (Hard)
- [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph) (Medium)
- [Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands) (Medium)
- [Max Area of Island](https://leetcode.com/problems/max-area-of-island) (Medium)
- [Count Sub Islands](https://leetcode.com/problems/count-sub-islands) (Medium)
- [Find All Groups of Farmland](https://leetcode.com/problems/find-all-groups-of-farmland) (Medium)
- [Count Unreachable Pairs of Nodes in an Undirected Graph](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph) (Medium)
