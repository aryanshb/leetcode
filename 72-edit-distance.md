# [72] Edit Distance

**[string, dynamic-programming]**

### Statement

Given two strings `word1` and `word2`, return *the minimum number of operations required to convert `word1` to `word2`*.

You have the following three operations permitted on a word:

* Insert a character
* Delete a character
* Replace a character


**Example 1:**

```

**Input:** word1 = "horse", word2 = "ros"
**Output:** 3
**Explanation:** 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

```

**Example 2:**

```

**Input:** word1 = "intention", word2 = "execution"
**Output:** 5
**Explanation:** 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

```

**Constraints:**
* `0 <= word1.length, word2.length <= 500`
* `word1` and `word2` consist of lowercase English letters.


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])  # insert, delete and replace

        return dp[m][n]
```

<br>

### Statistics

- total accepted: 524140
- total submissions: 1004565
- acceptance rate: 52.2%
- likes: 9761
- dislikes: 111

<br>

### Similar Problems

- [One Edit Distance](https://leetcode.com/problems/one-edit-distance) (Medium)
- [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings) (Medium)
- [Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings) (Medium)
- [Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines) (Medium)
- [Minimum White Tiles After Covering With Carpets](https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets) (Hard)
