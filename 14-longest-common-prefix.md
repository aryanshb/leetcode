# [14] Longest Common Prefix

**[string]**

### Statement

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.


**Example 1:**

```

**Input:** strs = ["flower","flow","flight"]
**Output:** "fl"

```

**Example 2:**

```

**Input:** strs = ["dog","racecar","car"]
**Output:** ""
**Explanation:** There is no common prefix among the input strings.

```

**Constraints:**
* `1 <= strs.length <= 200`
* `0 <= strs[i].length <= 200`
* `strs[i]` consists of only lowercase English letters.


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=lambda x:len(x))
        d = {}
        for i in strs:
            d[i] = 1
        prefix = []
        for i in range(len(strs[0])+1):
            prefix.append(strs[0][:i])
        prefix = prefix[::-1]
        ans=''
        for i in prefix:
            lol=0
            for j in d:
                if i in j[:len(i)]:lol+=1
            if lol==len(d): return i
        return ""
```

<br>

### Statistics

- total accepted: 1914852
- total submissions: 4710938
- acceptance rate: 40.6%
- likes: 10666
- dislikes: 3431

<br>

### Similar Problems

None
