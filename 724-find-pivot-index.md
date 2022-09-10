# [724] Find Pivot Index

**[array, prefix-sum]**

### Statement

Given an array of integers `nums`, calculate the **pivot index** of this array.

The **pivot index** is the index where the sum of all the numbers **strictly** to the left of the index is equal to the sum of all the numbers **strictly** to the index's right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return *the **leftmost pivot index***. If no such index exists, return -1.


**Example 1:**

```

**Input:** nums = [1,7,3,6,5,6]
**Output:** 3
**Explanation:**
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

```

**Example 2:**

```

**Input:** nums = [1,2,3]
**Output:** -1
**Explanation:**
There is no index that satisfies the conditions in the problem statement.
```

**Example 3:**

```

**Input:** nums = [2,1,-1]
**Output:** 0
**Explanation:**
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

```

**Constraints:**
* `1 <= nums.length <= 104`
* `-1000 <= nums[i] <= 1000`


**Note:** This question is the same as1991:<https://leetcode.com/problems/find-the-middle-index-in-array/>

<br>

### Hints

- We can precompute prefix sums P[i] = nums[0] + nums[1] + ... + nums[i-1].

Then for each index, the left sum is P[i], and the right sum is P[P.length - 1] - P[i] - nums[i].

<br>

### Solution

```py
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = [nums[0]]
        for i in range(1, len(nums)):
            l.append(nums[i]+l[i-1])
        ans = l[-1]
        print(l)
        for i in range(len(l)):
            if l[i]-nums[i] == ans-l[i]: return i
        return -1
        
```

<br>

### Statistics

- total accepted: 495960
- total submissions: 933465
- acceptance rate: 53.1%
- likes: 4647
- dislikes: 505

<br>

### Similar Problems

- [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k) (Medium)
- [Find the Middle Index in Array](https://leetcode.com/problems/find-the-middle-index-in-array) (Easy)
- [Number of Ways to Split Array](https://leetcode.com/problems/number-of-ways-to-split-array) (Medium)
- [Maximum Sum Score of Array](https://leetcode.com/problems/maximum-sum-score-of-array) (Medium)
