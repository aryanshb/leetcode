# [754] Reach a Number

**[math, binary-search]**

### Statement

You are standing at position `0` on an infinite number line. There is a destination at position `target`.

You can make some number of moves `numMoves` so that:

* On each move, you can either go left or right.
* During the `ith` move (starting from `i == 1` to `i == numMoves`), you take `i` steps in the chosen direction.



Given the integer `target`, return *the **minimum** number of moves required (i.e., the minimum* `numMoves`*) to reach the destination*.


**Example 1:**

```

**Input:** target = 2
**Output:** 3
**Explanation:**
On the 1st move, we step from 0 to 1 (1 step).
On the 2nd move, we step from 1 to -1 (2 steps).
On the 3rd move, we step from -1 to 2 (3 steps).

```

**Example 2:**

```

**Input:** target = 3
**Output:** 2
**Explanation:**
On the 1st move, we step from 0 to 1 (1 step).
On the 2nd move, we step from 1 to 3 (2 steps).

```

**Constraints:**
* `-109 <= target <= 109`
* `target != 0`


<br>

### Hints

None

<br>

### Solution

```py
"""
imagine we have the target 10.
Thats just 1 + 2 +3 + 4.
Now if we have target 11. We can start with
1 + 2 + 3 + 4 -5 + 6
To get to 12
1 + 2 + 3 +4 -5 + 6 -7 + 8.
Notice that by alternating signs of adjacent sums, you can always have the ability to add a only a one at the cost of 2 steps!
"""
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        if target % 2 == 0:
            return k
        else:
            return k+1+k%2
```

<br>

### Statistics

- total accepted: 41732
- total submissions: 98417
- acceptance rate: 42.4%
- likes: 1319
- dislikes: 691

<br>

### Similar Problems

- [Number of Ways to Reach a Position After Exactly k Steps](https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps) (Medium)
