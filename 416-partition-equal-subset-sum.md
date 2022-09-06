# [416] Partition Equal Subset Sum

**[array, dynamic-programming]**

### Statement

Given a **non-empty** array `nums` containing **only positive integers**, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.


**Example 1:**

```

**Input:** nums = [1,5,11,5]
**Output:** true
**Explanation:** The array can be partitioned as [1, 5, 5] and [11].

```

**Example 2:**

```

**Input:** nums = [1,2,3,5]
**Output:** false
**Explanation:** The array cannot be partitioned into equal sum subsets.

```

**Constraints:**
* `1 <= nums.length <= 200`
* `1 <= nums[i] <= 100`


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False 
        target = sum(nums)/2
        #iterative
        #start from the first element and calcualte all possible 
        #sums that can be obtained at the current element
        values = set([0, nums[0]])    
        i = 1
        #exit once we reach the target
        while target not in values and i < len(nums):
            values = values.union([v+nums[i] for v in values])
            i += 1   
        return target in values


```

<br>

### Statistics

- total accepted: 515219
- total submissions: 1102394
- acceptance rate: 46.7%
- likes: 8707
- dislikes: 141

<br>

### Similar Problems

- [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets) (Medium)
- [Minimize the Difference Between Target and Chosen Elements](https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements) (Medium)
- [Maximum Number of Ways to Partition an Array](https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array) (Hard)
- [Partition Array Into Two Arrays to Minimize Sum Difference](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference) (Hard)
