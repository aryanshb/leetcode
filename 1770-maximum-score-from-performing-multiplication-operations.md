# [1770] Maximum Score from Performing Multiplication Operations

**[array, dynamic-programming]**

### Statement

You are given two integer arrays `nums` and `multipliers`of size `n` and `m` respectively, where `n >= m`. The arrays are **1-indexed**.

You begin with a score of `0`. You want to perform **exactly** `m` operations. On the `ith` operation **(1-indexed)**, you will:

* Choose one integer `x` from **either the start or the end** of the array `nums`.
* Add `multipliers[i] * x` to your score.
* Remove `x` from the array `nums`.



Return *the **maximum** score after performing* `m` *operations.*
**Example 1:**

```

**Input:** nums = [1,2,3], multipliers = [3,2,1]
**Output:** 14
**Explanation:**An optimal solution is as follows:
- Choose from the end, [1,2,**3**], adding 3 \* 3 = 9 to the score.
- Choose from the end, [1,**2**], adding 2 \* 2 = 4 to the score.
- Choose from the end, [**1**], adding 1 \* 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.
```

**Example 2:**

```

**Input:** nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
**Output:** 102
**Explanation:** An optimal solution is as follows:
- Choose from the start, [**-5**,-3,-3,-2,7,1], adding -5 \* -10 = 50 to the score.
- Choose from the start, [**-3**,-3,-2,7,1], adding -3 \* -5 = 15 to the score.
- Choose from the start, [**-3**,-2,7,1], adding -3 \* 3 = -9 to the score.
- Choose from the end, [-2,7,**1**], adding 1 \* 4 = 4 to the score.
- Choose from the end, [-2,**7**], adding 7 \* 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.

```

**Constraints:**
* `n == nums.length`
* `m == multipliers.length`
* `1 <= m <= 103`
* `m <= n <= 105`
* `-1000 <= nums[i], multipliers[i] <= 1000`


<br>

### Hints

- At first glance, the solution seems to be greedy, but if you try to greedily take the largest value from the beginning or the end, this will not be optimal.
- You should try all scenarios but this will be costy.
- Memoizing the pre-visited states while trying all the possible scenarios will reduce the complexity, and hence dp is a perfect choice here.

<br>

### Solution

```py
# TLE for some reason
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        l, r, i = 0, n-1, 0
        dp = [[0 for i in range(1000)]for i in range(1000)]
        def sol(nums, multipliers, l, r, i, dp):
            if i >= m: return 0
            if dp[i][l]: return dp[i][l]
            dp[i][l] = max(multipliers[i]*nums[l]+sol(nums, multipliers, l+1, r, i+1, dp),
                          multipliers[i]*nums[r]+sol(nums, multipliers, l, r-1, i+1, dp))
            return dp[i][l]
        return sol(nums, multipliers, l, r, 0, dp)
```

```py
class Solution:
    def maximumScore(self, nums: List[int], muls: List[int]) -> int:
        n, m = len(nums), len(muls)
        dp = [[0] * (m+1) for _ in range(m+1)]
        
        for l in range(m-1, -1, -1):
            for i in range(m-1, -1, -1):
                r = n - (i-l) - 1
                if r < 0 or r >= n: break
                leftPick = dp[l+1][i+1] + nums[l] * muls[i]
                rightPick = dp[l][i+1] + nums[r] * muls[i]
                dp[l][i] = max(leftPick, rightPick)
                
        return dp[0][0]
```



<br>

### Statistics

- total accepted: 70180
- total submissions: 198857
- acceptance rate: 35.3%
- likes: 1862
- dislikes: 436

<br>

### Similar Problems

- [Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards) (Medium)
- [Stone Game VII](https://leetcode.com/problems/stone-game-vii) (Medium)
