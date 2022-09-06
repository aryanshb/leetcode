# [509] Fibonacci Number

**[math, dynamic-programming, recursion, memoization]**

### Statement

The **Fibonacci numbers**, commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,


```

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

```


Given `n`, calculate `F(n)`.


**Example 1:**

```

**Input:** n = 2
**Output:** 1
**Explanation:** F(2) = F(1) + F(0) = 1 + 0 = 1.

```

**Example 2:**

```

**Input:** n = 3
**Output:** 2
**Explanation:** F(3) = F(2) + F(1) = 1 + 1 = 2.

```

**Example 3:**

```

**Input:** n = 4
**Output:** 3
**Explanation:** F(4) = F(3) + F(2) = 2 + 1 = 3.

```

**Constraints:**
* `0 <= n <= 30`


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        fib = [0]*(n+1)
        fib[1] = 1
        for i in range(2,n+1):
            fib[i] = fib[i-1] + fib[i-2]
        return fib[n]
```

<br>

### Statistics

- total accepted: 1021831
- total submissions: 1478372
- acceptance rate: 69.1%
- likes: 4998
- dislikes: 288

<br>

### Similar Problems

- [Climbing Stairs](https://leetcode.com/problems/climbing-stairs) (Easy)
- [Split Array into Fibonacci Sequence](https://leetcode.com/problems/split-array-into-fibonacci-sequence) (Medium)
- [Length of Longest Fibonacci Subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence) (Medium)
- [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number) (Easy)
