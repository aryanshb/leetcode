# [658] Find K Closest Elements

**[array, two-pointers, binary-search, sorting, heap-priority-queue]**

### Statement

Given a **sorted** integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:

* `|a - x| < |b - x|`, or
* `|a - x| == |b - x|` and `a < b`


**Example 1:**

```
**Input:** arr = [1,2,3,4,5], k = 4, x = 3
**Output:** [1,2,3,4]

```
**Example 2:**

```
**Input:** arr = [1,2,3,4,5], k = 4, x = -1
**Output:** [1,2,3,4]

```

**Constraints:**
* `1 <= k <= arr.length`
* `1 <= arr.length <= 104`
* `arr` is sorted in **ascending** order.
* `-104 <= arr[i], x <= 104`


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l1 = sorted(arr, key=lambda i: abs(x - i))
        return sorted(l1[:k])
```

<br>

### Statistics

- total accepted: 369915
- total submissions: 796400
- acceptance rate: 46.4%
- likes: 5966
- dislikes: 492

<br>

### Similar Problems

- [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower) (Easy)
- [Guess Number Higher or Lower II](https://leetcode.com/problems/guess-number-higher-or-lower-ii) (Medium)
- [Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance) (Hard)
- [Find Closest Number to Zero](https://leetcode.com/problems/find-closest-number-to-zero) (Easy)
