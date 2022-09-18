# [2414] Length of the Longest Alphabetical Continuous Substring



### Statement

An **alphabetical continuous string** is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string `"abcdefghijklmnopqrstuvwxyz"`.

* For example, `"abc"` is an alphabetical continuous string, while `"acb"` and `"za"` are not.



Given a string `s` consisting of lowercase letters only, return the *length of the **longest** alphabetical continuous substring.*
**Example 1:**

```

**Input:** s = "abacaba"
**Output:** 2
**Explanation:** There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring.

```

**Example 2:**

```

**Input:** s = "abcde"
**Output:** 5
**Explanation:** "abcde" is the longest continuous substring.

```

**Constraints:**
* `1 <= s.length <= 105`
* `s` consists of only English lowercase letters.


<br>

### Hints

- What is the longest possible continuous substring?
- The size of the longest possible continuous substring is at most 26, so we can just brute force the answer.

<br>

### Solution

```py
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 1
        for i in range(len(s)):
            cur = 1
            while i<len(s)-1 and ord(s[i+1])-ord(s[i]) == 1:
                i += 1
                cur += 1
            ans = max(cur, ans)
        return ans
```

<br>

### Statistics

- total accepted: 15206
- total submissions: 28902
- acceptance rate: 52.6%
- likes: 63
- dislikes: 2

<br>

### Similar Problems

- [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence) (Medium)
- [Arithmetic Slices](https://leetcode.com/problems/arithmetic-slices) (Medium)
- [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones) (Easy)
- [Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length) (Medium)
- [Number of Zero-Filled Subarrays](https://leetcode.com/problems/number-of-zero-filled-subarrays) (Medium)
