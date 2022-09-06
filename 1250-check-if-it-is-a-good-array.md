# [1250] Check If It Is a Good Array

**[array, math, number-theory]**

### Statement

Given an array `nums` ofpositive integers. Your task is to select some subset of `nums`, multiply each element by an integer and add all these numbers.The array is said to be**good**if you can obtain a sum of`1`from the array by any possible subset and multiplicand.

Return`True`if the array is **good**otherwisereturn`False`.


**Example 1:**

```

**Input:** nums = [12,5,7,23]
**Output:** true
**Explanation:** Pick numbers 5 and 7.
5\*3 + 7\*(-2) = 1

```

**Example 2:**

```

**Input:** nums = [29,6,10]
**Output:** true
**Explanation:** Pick numbers 29, 6 and 10.
29\*1 + 6\*(-3) + 10\*(-1) = 1

```

**Example 3:**

```

**Input:** nums = [3,6]
**Output:** false

```

**Constraints:**
* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`


<br>

### Hints

- Eq.  ax+by=1 has solution x, y if gcd(a,b) = 1.
- Can you generalize the formula?.  Check B�zout's lemma.

<br>

### Solution

```py
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(gcd, nums) == 1
        
```

<br>

### Statistics

- total accepted: 14963
- total submissions: 25536
- acceptance rate: 58.6%
- likes: 306
- dislikes: 307

<br>

### Similar Problems

None
