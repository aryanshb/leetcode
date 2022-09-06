# [62] Unique Paths

**[math, dynamic-programming, combinatorics]**

### Statement

There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The test cases are generated so that the answer will be less than or equal to `2 * 109`.


**Example 1:**
![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

```

**Input:** m = 3, n = 7
**Output:** 28

```

**Example 2:**

```

**Input:** m = 3, n = 2
**Output:** 3
**Explanation:** From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

```

**Constraints:**
* `1 <= m, n <= 100`


<br>

### Hints

None

<br>

### Solution

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        
        vector<vector<int>> dp(m, vector<int>(n, 1));
        dp[0][0] = 1;
        for(int i=1;i<m;i++){
            for(int j=1;j<n;j++){
                dp[i][j] = dp[i-1][j]+dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
        
    }
};
```

<br>

### Statistics

- total accepted: 1146469
- total submissions: 1853739
- acceptance rate: 61.8%
- likes: 11500
- dislikes: 344

<br>

### Similar Problems

- [Unique Paths II](https://leetcode.com/problems/unique-paths-ii) (Medium)
- [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum) (Medium)
- [Dungeon Game](https://leetcode.com/problems/dungeon-game) (Hard)
- [Minimum Path Cost in a Grid](https://leetcode.com/problems/minimum-path-cost-in-a-grid) (Medium)
- [Minimum Cost Homecoming of a Robot in a Grid](https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid) (Medium)
