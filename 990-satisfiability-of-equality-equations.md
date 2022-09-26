# [990] Satisfiability of Equality Equations

**[array, string, union-find, graph]**

### Statement

You are given an array of strings `equations` that represent relationships between variables where each string `equations[i]` is of length `4` and takes one of two different forms: `"xi==yi"` or `"xi!=yi"`.Here, `xi` and `yi` are lowercase letters (not necessarily different) that represent one-letter variable names.

Return `true` *if it is possible to assign integers to variable names so as to satisfy all the given equations, or* `false` *otherwise*.


**Example 1:**

```

**Input:** equations = ["a==b","b!=a"]
**Output:** false
**Explanation:** If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.

```

**Example 2:**

```

**Input:** equations = ["b==a","a==b"]
**Output:** true
**Explanation:** We could assign a = 1 and b = 1 to satisfy both equations.

```

**Constraints:**
* `1 <= equations.length <= 500`
* `equations[i].length == 4`
* `equations[i][0]` is a lowercase letter.
* `equations[i][1]` is either `'='` or `'!'`.
* `equations[i][2]` is `'='`.
* `equations[i][3]` is a lowercase letter.


<br>

### Hints

None

<br>

### Solution

```py
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def dfs(ch, visited1, visited2):
            visited1.add(ch)
            visited2.add(ch)
            for ch2, w in adj[ch]:
                if not w and ch2 in visited2:
                    return False
                if w and ch2 not in visited2:
                    if not dfs(ch2, visited1, visited2):
                        return False
            
            return True
            
        adj = collections.defaultdict(lambda: [])
        for eqn in equations:
            ch1, ch2 = eqn[0], eqn[3]
            if eqn[1] == "!":
                adj[ch1].append((ch2, 0))
                adj[ch2].append((ch1, 0))
            else:
                adj[ch1].append((ch2, 1))
                adj[ch2].append((ch1, 1))
        
        visited1 = set()
        visited2 = set()
        
        for ch in string.ascii_lowercase:
            if ch not in visited1:
                if not dfs(ch, visited1, visited2):
                    return False
                visited2.clear()
        return True
```

<br>

### Statistics

- total accepted: 76406
- total submissions: 152058
- acceptance rate: 50.2%
- likes: 2449
- dislikes: 36

<br>

### Similar Problems

None
