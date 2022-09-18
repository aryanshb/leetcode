# [336] Palindrome Pairs

**[array, hash-table, string, trie]**

### Statement

Given a list of **unique** words, return all the pairs of the***distinct*** indices `(i, j)` in the given list, so that the concatenation of the two words`words[i] + words[j]` is a palindrome.


**Example 1:**

```

**Input:** words = ["abcd","dcba","lls","s","sssll"]
**Output:** [[0,1],[1,0],[3,2],[2,4]]
**Explanation:** The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

```

**Example 2:**

```

**Input:** words = ["bat","tab","cat"]
**Output:** [[0,1],[1,0]]
**Explanation:** The palindromes are ["battab","tabbat"]

```

**Example 3:**

```

**Input:** words = ["a",""]
**Output:** [[0,1],[1,0]]

```

**Constraints:**
* `1 <= words.length <= 5000`
* `0 <= words[i].length <= 300`
* `words[i]` consists of lower-case English letters.


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def palindromePairs(self, words):
        lookup = {w:i for i,w in enumerate(words)}
        res = []
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                pre, pos = w[:j], w[j:]
                if pre==pre[::-1] and pos[::-1] != w \
                    and pos[::-1] in lookup:
                        res.append([lookup[pos[::-1]], i])
                if j != len(w) and pos==pos[::-1] \
                    and pre[::-1] != w and pre[::-1] in lookup:
                        res.append([i, lookup[pre[::-1]]])
        return res
```

<br>

### Statistics

- total accepted: 172983
- total submissions: 491924
- acceptance rate: 35.2%
- likes: 3683
- dislikes: 369

<br>

### Similar Problems

- [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring) (Medium)
- [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome) (Hard)
- [Longest Palindrome by Concatenating Two Letter Words](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words) (Medium)
