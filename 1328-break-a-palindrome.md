# [1328] Break a Palindrome

**[string, greedy]**

### Statement

Given a palindromic string of lowercase English letters `palindrome`, replace **exactly one** character with any lowercase English letter so that the resulting string is **not** a palindrome and that it is the **lexicographically smallest** one possible.

Return *the resulting string. If there is no way to replace a character to make it not a palindrome, return an **empty string**.*

A string `a` is lexicographically smaller than a string `b` (of the same length) if in the first position where `a` and `b` differ, `a` has a character strictly smaller than the corresponding character in `b`. For example, `"abcc"` is lexicographically smaller than `"abcd"` because the first position they differ is at the fourth character, and `'c'` is smaller than `'d'`.


**Example 1:**

```

**Input:** palindrome = "abccba"
**Output:** "aaccba"
**Explanation:** There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

```

**Example 2:**

```

**Input:** palindrome = "a"
**Output:** ""
**Explanation:** There is no way to replace a single character to make "a" not a palindrome, so return an empty string.

```

**Constraints:**
* `1 <= palindrome.length <= 1000`
* `palindrome` consists of only lowercase English letters.


<br>

### Hints

- How to detect if there is impossible to perform the replacement? Only when the length = 1.
- Change the first non 'a' character to 'a'.
- What if the string has only 'a'?
- Change the last character to 'b'.

<br>

### Solution

```py
class Solution:
    def breakPalindrome(self, p: str) -> str:
        
        n = len(p)
        if n < 2: return ''
        
        for i in range(n//2):
            
            if p[i] != 'a':
                p = p[:i] + 'a' + p[i+1:]
                break
                
        else: p = p[:-1] + 'b'
            
        return p
```

<br>

### Statistics

- total accepted: 113917
- total submissions: 214355
- acceptance rate: 53.1%
- likes: 1596
- dislikes: 621

<br>

### Similar Problems

None
