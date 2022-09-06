# [628] Maximum Product of Three Numbers

**[array, math, sorting]**

### Statement

Given an integer array `nums`, *find three numbers whose product is maximum and return the maximum product*.


**Example 1:**

```
**Input:** nums = [1,2,3]
**Output:** 6

```
**Example 2:**

```
**Input:** nums = [1,2,3,4]
**Output:** 24

```
**Example 3:**

```
**Input:** nums = [-1,-2,-3]
**Output:** -6

```

**Constraints:**
* `3 <= nums.length <=104`
* `-1000 <= nums[i] <= 1000`


<br>

### Hints

None

<br>

### Solution

```py
class Solution(object):
    def maximumProduct(self, nums):
        x=sorted(nums)
        a = x[0]*x[1]*x[-1]
        b=x[-1]*x[-2]*x[-3]
        return max(a,b)
```

<br>

### Statistics

- total accepted: 228803
- total submissions: 491423
- acceptance rate: 46.6%
- likes: 3077
- dislikes: 553

<br>

### Similar Problems

- [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray) (Medium)
