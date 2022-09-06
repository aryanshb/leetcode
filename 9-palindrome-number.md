# [9] Palindrome Number

**[math]**

### Statement

Given an integer `x`, return `true` if `x` is palindrome integer.

An integer is a **palindrome** when it reads the same backward as forward.

* For example, `121` is a palindrome while `123` is not.


**Example 1:**

```

**Input:** x = 121
**Output:** true
**Explanation:** 121 reads as 121 from left to right and from right to left.

```

**Example 2:**

```

**Input:** x = -121
**Output:** false
**Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```

**Example 3:**

```

**Input:** x = 10
**Output:** false
**Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.

```

**Constraints:**
* `-231<= x <= 231- 1`


**Follow up:** Could you solve it without converting the integer to a string?

<br>

### Hints

- Beware of overflow when you reverse the integer.

<br>

### Solution

```py
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
        
```

<br>

### Statistics

- total accepted: 2409063
- total submissions: 4568271
- acceptance rate: 52.7%
- likes: 6968
- dislikes: 2271

<br>

### Similar Problems

- [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list) (Easy)
- [Find Palindrome With Fixed Length](https://leetcode.com/problems/find-palindrome-with-fixed-length) (Medium)
