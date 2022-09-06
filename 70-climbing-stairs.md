# [70] Climbing Stairs

**[math, dynamic-programming, memoization]**

### Statement

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?


**Example 1:**

```

**Input:** n = 2
**Output:** 2
**Explanation:** There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

```

**Example 2:**

```

**Input:** n = 3
**Output:** 3
**Explanation:** There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

```

**Constraints:**
* `1 <= n <= 45`


<br>

### Hints

- To reach nth step, what could have been your previous steps? (Think about the step sizes)

<br>

### Solution

```py
class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n+1);
        if(n == 0 | n == 1){
            return 1;
        }
        dp[1] = 1;
        dp[2] = 2;
        for(int i = 3; i<=n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
```

<br>

### Statistics

- total accepted: 1822775
- total submissions: 3532159
- acceptance rate: 51.6%
- likes: 14029
- dislikes: 414

<br>

### Similar Problems

- [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs) (Easy)
- [Fibonacci Number](https://leetcode.com/problems/fibonacci-number) (Easy)
- [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number) (Easy)
- [Minimum Rounds to Complete All Tasks](https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks) (Medium)
- [Count Number of Ways to Place Houses](https://leetcode.com/problems/count-number-of-ways-to-place-houses) (Medium)
