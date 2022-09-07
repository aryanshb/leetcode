# [100] Same Tree

**[tree, depth-first-search, breadth-first-search, binary-tree]**

### Statement

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


**Example 1:**
![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

```

**Input:** p = [1,2,3], q = [1,2,3]
**Output:** true

```

**Example 2:**
![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

```

**Input:** p = [1,2], q = [1,null,2]
**Output:** false

```

**Example 3:**
![](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

```

**Input:** p = [1,2,1], q = [1,1,2]
**Output:** false

```

**Constraints:**
* The number of nodes in both trees is in the range `[0, 100]`.
* `-104 <= Node.val <= 104`


<br>

### Hints

None

<br>

### Solution

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and root2:
                if root1.val == root2.val:
                    return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
            return False
            
        return dfs(p,q)
```

<br>

### Statistics

- total accepted: 1202871
- total submissions: 2142065
- acceptance rate: 56.2%
- likes: 6965
- dislikes: 149

<br>

### Similar Problems

None
