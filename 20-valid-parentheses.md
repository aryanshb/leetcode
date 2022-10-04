# [20] Valid Parentheses

**[string, stack]**

### Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.


**Example 1:**

```

**Input:** s = "()"
**Output:** true

```

**Example 2:**

```

**Input:** s = "()[]{}"
**Output:** true

```

**Example 3:**

```

**Input:** s = "(]"
**Output:** false

```

**Constraints:**
* `1 <= s.length <= 104`
* `s` consists of parentheses only `'()[]{}'`.


<br>

### Hints

- Use a stack of characters.
- When you encounter an opening bracket, push it to the top of the stack.
- When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.

<br>

### Solution

```py
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        ans = True
        while i!= len(s):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')' or s[i] == '}' or s[i] == ']':
                if len(stack) == 0: return False
                if stack[-1] == '(' and s[i] == ')':stack.pop()
                elif stack[-1] == '{' and s[i] == '}':stack.pop()
                elif stack[-1] == '[' and s[i] == ']':stack.pop()
                else:
                    ans = False
                    break
            i+=1
        return len(stack)==0
```

<br>

### Statistics

- total accepted: 2698806
- total submissions: 6627022
- acceptance rate: 40.7%
- likes: 15927
- dislikes: 796

<br>

### Similar Problems

- [Generate Parentheses](https://leetcode.com/problems/generate-parentheses) (Medium)
- [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses) (Hard)
- [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses) (Hard)
- [Check If Word Is Valid After Substitutions](https://leetcode.com/problems/check-if-word-is-valid-after-substitutions) (Medium)
- [Check if a Parentheses String Can Be Valid](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid) (Medium)
- [Move Pieces to Obtain a String](https://leetcode.com/problems/move-pieces-to-obtain-a-string) (Medium)
