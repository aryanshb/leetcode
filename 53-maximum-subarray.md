# [53] Maximum Subarray

**[array, divide-and-conquer, dynamic-programming]**

### Statement

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return *its sum*.

A **subarray** is a **contiguous** part of an array.


**Example 1:**

```

**Input:** nums = [-2,1,-3,4,-1,2,1,-5,4]
**Output:** 6
**Explanation:** [4,-1,2,1] has the largest sum = 6.

```

**Example 2:**

```

**Input:** nums = [1]
**Output:** 1

```

**Example 3:**

```

**Input:** nums = [5,4,-1,7,8]
**Output:** 23

```

**Constraints:**
* `1 <= nums.length <= 105`
* `-104 <= nums[i] <= 104`


**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def maxSubArray(self, nums):
        maxSubarray = nums[0]
        currentSum = 0
		
        for n in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += n
            maxSubarray = max(maxSubarray, currentSum)
			
        return maxSubarray
```

<br>

### Statistics

- total accepted: 2669286
- total submissions: 5352763
- acceptance rate: 49.9%
- likes: 24441
- dislikes: 1139

<br>

### Similar Problems

- [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) (Easy)
- [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray) (Medium)
- [Degree of an Array](https://leetcode.com/problems/degree-of-an-array) (Easy)
- [Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray) (Medium)
- [Maximum Score Of Spliced Array](https://leetcode.com/problems/maximum-score-of-spliced-array) (Hard)
- [Maximum Absolute Sum of Any Subarray](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray) (Medium)
- [Maximum Subarray Sum After One Operation](https://leetcode.com/problems/maximum-subarray-sum-after-one-operation) (Medium)
- [Substring With Largest Variance](https://leetcode.com/problems/substring-with-largest-variance) (Hard)
- [Count Subarrays With Score Less Than K](https://leetcode.com/problems/count-subarrays-with-score-less-than-k) (Hard)
