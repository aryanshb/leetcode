# [42] Trapping Rain Water

**[array, two-pointers, dynamic-programming, stack, monotonic-stack]**

### Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.


**Example 1:**
![](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

```

**Input:** height = [0,1,0,2,1,0,1,3,2,1,2,1]
**Output:** 6
**Explanation:** The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

```

**Example 2:**

```

**Input:** height = [4,2,0,3,2,5]
**Output:** 9

```

**Constraints:**
* `n == height.length`
* `1 <= n <= 2 * 104`
* `0 <= height[i] <= 105`


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def trap(self, height: List[int]) -> int:
    
    
        def trapTomax(height):
            cur_max  =0
            water = 0
            for h in height:
                if h < cur_max:
                    water += cur_max - h
                else:
                    cur_max = h
            return water
        
        if not height:
            return 0
        
        max_pos = height.index(max(height))
        
        return trapTomax(height[:max_pos]) + trapTomax(reversed(height[max_pos+1:]))
```

<br>

### Statistics

- total accepted: 1265775
- total submissions: 2190370
- acceptance rate: 57.8%
- likes: 21558
- dislikes: 293

<br>

### Similar Problems

- [Container With Most Water](https://leetcode.com/problems/container-with-most-water) (Medium)
- [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self) (Medium)
- [Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii) (Hard)
- [Pour Water](https://leetcode.com/problems/pour-water) (Medium)
