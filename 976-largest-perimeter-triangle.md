# [976] Largest Perimeter Triangle

**[array, math, greedy, sorting]**

### Statement

Given an integer array `nums`, return *the largest perimeter of a triangle with a non-zero area, formed from three of these lengths*. If it is impossible to form any triangle of a non-zero area, return `0`.


**Example 1:**

```

**Input:** nums = [2,1,2]
**Output:** 5

```

**Example 2:**

```

**Input:** nums = [1,2,1]
**Output:** 0

```

**Constraints:**
* `3 <= nums.length <= 104`
* `1 <= nums[i] <= 106`


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::-1]
        for i in range(len(nums)-2):
            if nums[i]<nums[i+1]+nums[i+2]: return nums[i]+nums[i+1]+nums[i+2]
            
        return 0
```

<br>

### Statistics

- total accepted: 161294
- total submissions: 294853
- acceptance rate: 54.7%
- likes: 2241
- dislikes: 304

<br>

### Similar Problems

- [Largest Triangle Area](https://leetcode.com/problems/largest-triangle-area) (Easy)
