# [16] 3Sum Closest

**[array, two-pointers, sorting]**

### Statement

Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.

Return *the sum of the three integers*.

You may assume that each input would have exactly one solution.


**Example 1:**

```

**Input:** nums = [-1,2,1,-4], target = 1
**Output:** 2
**Explanation:** The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

```

**Example 2:**

```

**Input:** nums = [0,0,0], target = 1
**Output:** 0
**Explanation:** The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

```

**Constraints:**
* `3 <= nums.length <= 1000`
* `-1000 <= nums[i] <= 1000`
* `-104 <= target <= 104`


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        res = nums[0] + nums[1] + nums[2]
        nums = sorted(nums)
        
        for i, x in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                currSum = x + nums[l] + nums[r]
                
                if currSum == target:
                    return currSum
                
                if abs(target - currSum) < abs(target - res):
                    res = currSum
                
                if currSum > target:
                    r -= 1
                else:
                    l += 1
            
        return res
```

<br>

### Statistics

- total accepted: 928945
- total submissions: 2007719
- acceptance rate: 46.3%
- likes: 7820
- dislikes: 426

<br>

### Similar Problems

- [3Sum](https://leetcode.com/problems/3sum) (Medium)
- [3Sum Smaller](https://leetcode.com/problems/3sum-smaller) (Medium)
