# [392] Is Subsequence

**[two-pointers, string, dynamic-programming]**

### Statement

Given two strings `s` and `t`, return `true` *if* `s` *is a **subsequence** of* `t`*, or* `false` *otherwise*.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).


**Example 1:**

```
**Input:** s = "abc", t = "ahbgdc"
**Output:** true

```
**Example 2:**

```
**Input:** s = "axc", t = "ahbgdc"
**Output:** false

```

**Constraints:**
* `0 <= s.length <= 100`
* `0 <= t.length <= 104`
* `s` and `t` consist only of lowercase English letters.


**Follow up:** Suppose there are lots of incoming `s`, say `s1, s2, ..., sk` where `k >= 109`, and you want to check one by one to see if `t` has its subsequence. In this scenario, how would you change your code?

<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        if s == "": return True
        for i in range(len(t)):
            if s[j] == t[i]: j+=1
            if(j == len(s)):
                return True
        return False

```

<br>

### Statistics

- total accepted: 585636
- total submissions: 1174789
- acceptance rate: 49.9%
- likes: 5688
- dislikes: 324

<br>

### Similar Problems

- [Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences) (Medium)
- [Shortest Way to Form String](https://leetcode.com/problems/shortest-way-to-form-string) (Medium)
