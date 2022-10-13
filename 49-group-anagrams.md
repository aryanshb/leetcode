# [49] Group Anagrams

**[array, hash-table, string, sorting]**

### Statement

Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


**Example 1:**

```
**Input:** strs = ["eat","tea","tan","ate","nat","bat"]
**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

```
**Example 2:**

```
**Input:** strs = [""]
**Output:** [[""]]

```
**Example 3:**

```
**Input:** strs = ["a"]
**Output:** [["a"]]

```

**Constraints:**
* `1 <= strs.length <= 104`
* `0 <= strs[i].length <= 100`
* `strs[i]` consists of lowercase English letters.


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            l = tuple(sorted([j for j in i]))
            if l not in d: d[l] = [i]
            else: d[l]+=[i]
        return [j for i,j in d.items()]
```

<br>

### Statistics

- total accepted: 1633405
- total submissions: 2480321
- acceptance rate: 65.9%
- likes: 12054
- dislikes: 374

<br>

### Similar Problems

- [Valid Anagram](https://leetcode.com/problems/valid-anagram) (Easy)
- [Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings) (Medium)
- [Find Resultant Array After Removing Anagrams](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams) (Easy)
