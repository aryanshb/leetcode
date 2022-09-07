# [101] Symmetric Tree

**[tree, depth-first-search, breadth-first-search, binary-tree]**

### Statement

Given the `root` of a binary tree, *check whether it is a mirror of itself* (i.e., symmetric around its center).


**Example 1:**
![](https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg)

```

**Input:** root = [1,2,2,3,4,4,3]
**Output:** true

```

**Example 2:**
![](https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg)

```

**Input:** root = [1,2,2,null,3,null,3]
**Output:** false

```

**Constraints:**
* The number of nodes in the tree is in the range `[1, 1000]`.
* `-100 <= Node.val <= 100`


**Follow up:** Could you solve it both recursively and iteratively?

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and root2 and root1.val == root2.val:
                return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
            return False
        return dfs(root.left, root.right)
```

<br>

### Statistics

- total accepted: 1372759
- total submissions: 2610826
- acceptance rate: 52.6%
- likes: 10889
- dislikes: 254

<br>

### Similar Problems

None
