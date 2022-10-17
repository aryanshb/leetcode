# [1832] Check if the Sentence Is Pangram

**[hash-table, string]**

### Statement

A **pangram** is a sentence where every letter of the English alphabet appears at least once.

Given a string `sentence` containing only lowercase English letters, return`true` *if* `sentence` *is a **pangram**, or* `false` *otherwise.*
**Example 1:**

```

**Input:** sentence = "thequickbrownfoxjumpsoverthelazydog"
**Output:** true
**Explanation:** sentence contains at least one of every letter of the English alphabet.

```

**Example 2:**

```

**Input:** sentence = "leetcode"
**Output:** false

```

**Constraints:**
* `1 <= sentence.length <= 1000`
* `sentence` consists of lowercase English letters.


<br>

### Hints

- Iterate over the string and mark each character as found (using a boolean array, bitmask, or any other similar way).
- Check if the number of found characters equals the alphabet length.

<br>

### Solution

```py
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a = 'abcdefghijklmnopqrstuvwxyz'
        a = enumerate(a)
        print(a)
        b = enumerate(sentence)
        for i in a:
            if i not in b: return False
        return True
```

<br>

### Statistics

- total accepted: 162756
- total submissions: 194586
- acceptance rate: 83.6%
- likes: 1711
- dislikes: 40

<br>

### Similar Problems

None
