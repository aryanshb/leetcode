# [557] Reverse Words in a String III

**[two-pointers, string]**

### Statement

Given a string `s`, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.


**Example 1:**

```
**Input:** s = "Let's take LeetCode contest"
**Output:** "s'teL ekat edoCteeL tsetnoc"

```
**Example 2:**

```
**Input:** s = "God Ding"
**Output:** "doG gniD"

```

**Constraints:**
* `1 <= s.length <= 5 * 104`
* `s` contains printable **ASCII** characters.
* `s` does not contain any leading or trailing spaces.
* There is **at least one** word in `s`.
* All the words in `s` are separated by a single space.


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split()])
```

<br>

### Statistics

- total accepted: 531999
- total submissions: 662630
- acceptance rate: 80.3%
- likes: 3437
- dislikes: 196

<br>

### Similar Problems

- [Reverse String II](https://leetcode.com/problems/reverse-string-ii) (Easy)
