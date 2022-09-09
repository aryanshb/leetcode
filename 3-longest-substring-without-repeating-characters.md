# [3] Longest Substring Without Repeating Characters

**[hash-table, string, sliding-window]**

### Statement

Given a string `s`, find the length of the **longest substring** without repeating characters.


**Example 1:**

```

**Input:** s = "abcabcbb"
**Output:** 3
**Explanation:** The answer is "abc", with the length of 3.

```

**Example 2:**

```

**Input:** s = "bbbbb"
**Output:** 1
**Explanation:** The answer is "b", with the length of 1.

```

**Example 3:**

```

**Input:** s = "pwwkew"
**Output:** 3
**Explanation:** The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

**Constraints:**
* `0 <= s.length <= 5 * 104`
* `s` consists of English letters, digits, symbols and spaces.


<br>

### Hints

None

<br>

### Solution

```py
# Bruteforce
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = [i for i in s]
        ma = 0
        if len(s)<2: return len(s)
        for i in range(len(s)):
            for j in range(i, len(s)):
                l = s[i:j+1]
                if len(set(l)) != len(l): break
                ma = max(len(l), ma)
        return ma  
# Sliding Glass
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2: return len(s)
        print(s)
        a = set()
        i, j, ans = 0, 0, 0
        while i<len(s) and j<len(s):
            if s[j] in a:
                a.remove(s[i])
                i+=1
                # print(a, "s[j] in a", "max=", ans)
                
            else:
                a.add(s[j])
                # print(a, "not", "ans=", ans, j-i)
                ans = max(ans, j-i)
                j+=1
        return ans+1
```

<br>

### Statistics

- total accepted: 3799216
- total submissions: 11280174
- acceptance rate: 33.7%
- likes: 28400
- dislikes: 1215

<br>

### Similar Problems

- [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters) (Medium)
- [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters) (Medium)
- [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers) (Hard)
- [Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value) (Medium)
- [Number of Equal Count Substrings](https://leetcode.com/problems/number-of-equal-count-substrings) (Medium)
- [Minimum Consecutive Cards to Pick Up](https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up) (Medium)
- [Longest Nice Subarray](https://leetcode.com/problems/longest-nice-subarray) (Medium)
