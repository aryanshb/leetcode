# [11] Container With Most Water

**[array, two-pointers, greedy]**

### Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.


**Example 1:**
![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```

**Input:** height = [1,8,6,2,5,4,8,3,7]
**Output:** 49
**Explanation:** The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

```

**Example 2:**

```

**Input:** height = [1,1]
**Output:** 1

```

**Constraints:**
* `n == height.length`
* `2 <= n <= 105`
* `0 <= height[i] <= 104`


<br>

### Hints

- If you simulate the problem, it will be O(n^2) which is not efficient.
- Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.
- How can you calculate the amount of water at each step?

<br>

### Solution

```py
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        tem = 0
        while l<r:
            ar = (r-l)*min(height[l], height[r])
            tem = max(ar, tem)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return tem
```

<br>

### Statistics

- total accepted: 1707661
- total submissions: 3154504
- acceptance rate: 54.1%
- likes: 19668
- dislikes: 1048

<br>

### Similar Problems

- [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water) (Hard)
