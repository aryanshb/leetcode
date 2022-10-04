# [17] Letter Combinations of a Phone Number

**[hash-table, string, backtracking]**

### Statement

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
![](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)
**Example 1:**

```

**Input:** digits = "23"
**Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

```

**Example 2:**

```

**Input:** digits = ""
**Output:** []

```

**Example 3:**

```

**Input:** digits = "2"
**Output:** ["a","b","c"]

```

**Constraints:**
* `0 <= digits.length <= 4`
* `digits[i]` is a digit in the range `['2', '9']`.


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def letterCombinations(self, digits):
        dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", 
            '8':"tuv", '9':"wxyz"}
        cmb = [''] if digits else []
        for d in digits:
            cmb = [p + q for p in cmb for q in dict[d]]
        return cmb
```

<br>

### Statistics

- total accepted: 1373757
- total submissions: 2479613
- acceptance rate: 55.4%
- likes: 12738
- dislikes: 763

<br>

### Similar Problems

- [Generate Parentheses](https://leetcode.com/problems/generate-parentheses) (Medium)
- [Combination Sum](https://leetcode.com/problems/combination-sum) (Medium)
- [Binary Watch](https://leetcode.com/problems/binary-watch) (Easy)
- [Count Number of Texts](https://leetcode.com/problems/count-number-of-texts) (Medium)
