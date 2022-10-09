# [46] Permutations

**[array, backtracking]**

### Statement

Given an array `nums` of distinct integers, return *all the possible permutations*. You can return the answer in **any order**.


**Example 1:**

```
**Input:** nums = [1,2,3]
**Output:** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

```
**Example 2:**

```
**Input:** nums = [0,1]
**Output:** [[0,1],[1,0]]

```
**Example 3:**

```
**Input:** nums = [1]
**Output:** [[1]]

```

**Constraints:**
* `1 <= nums.length <= 6`
* `-10 <= nums[i] <= 10`
* All the integers of `nums` are **unique**.


<br>

### Hints

None

<br>

### Solution

```py
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        a = permutations(nums)
        return a
```

<br>

### Statistics

- total accepted: 1376531
- total submissions: 1847119
- acceptance rate: 74.5%
- likes: 13234
- dislikes: 221

<br>

### Similar Problems

- [Next Permutation](https://leetcode.com/problems/next-permutation) (Medium)
- [Permutations II](https://leetcode.com/problems/permutations-ii) (Medium)
- [Permutation Sequence](https://leetcode.com/problems/permutation-sequence) (Hard)
- [Combinations](https://leetcode.com/problems/combinations) (Medium)
