# [718] Maximum Length of Repeated Subarray

**[array, binary-search, dynamic-programming, sliding-window, rolling-hash, hash-function]**

### Statement

Given two integer arrays `nums1` and `nums2`, return *the maximum length of a subarray that appears in **both** arrays*.


**Example 1:**

```

**Input:** nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
**Output:** 3
**Explanation:** The repeated subarray with maximum length is [3,2,1].

```

**Example 2:**

```

**Input:** nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
**Output:** 5

```

**Constraints:**
* `1 <= nums1.length, nums2.length <= 1000`
* `0 <= nums1[i], nums2[i] <= 100`


<br>

### Hints

- Use dynamic programming.  dp[i][j] will be the answer for inputs A[i:], B[j:].

<br>

### Solution

```py
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        # left to right sliding 
        for k in range(len(nums1)):
            s = 0 
            for (x1,x2) in zip(nums1[k:],nums2):
                if x1==x2:
                    s += 1 
                else:
                    res = max(res,s)
                    s = 0 
            res = max(res,s)
        # right to left sliding 
        for k in range(len(nums2)):
            s = 0 
            for (x1,x2) in zip(nums2[k:],nums1):
                if x1==x2:
                    s += 1 
                else:
                    res = max(res,s)
                    s = 0 
            res = max(res,s)
        return res 
```

<br>

### Statistics

- total accepted: 221062
- total submissions: 428988
- acceptance rate: 51.5%
- likes: 5220
- dislikes: 125

<br>

### Similar Problems

- [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum) (Medium)
- [Longest Common Subpath](https://leetcode.com/problems/longest-common-subpath) (Hard)
