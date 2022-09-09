# [199] Binary Tree Right Side View

**[tree, depth-first-search, breadth-first-search, binary-tree]**

### Statement

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return *the values of the nodes you can see ordered from top to bottom*.


**Example 1:**
![](https://assets.leetcode.com/uploads/2021/02/14/tree.jpg)

```

**Input:** root = [1,2,3,null,5,null,4]
**Output:** [1,3,4]

```

**Example 2:**

```

**Input:** root = [1,null,3]
**Output:** [1,3]

```

**Example 3:**

```

**Input:** root = []
**Output:** []

```

**Constraints:**
* The number of nodes in the tree is in the range `[0, 100]`.
* `-100 <= Node.val <= 100`


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
import sys
input = sys.stdin.readline
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = dict()
        def dfs(root, lvl, levels):
            if not root: return
            if lvl not in levels:
                levels[lvl] = []
                levels[lvl].append(root.val)
            dfs(root.right, lvl+1, levels)
            dfs(root.left, lvl+1, levels)
        l = []
        dfs(root, 0, levels)
        for i in levels.values():
            l.append(i[-1])
        return l
```

<br>

### Statistics

- total accepted: 819093
- total submissions: 1343276
- acceptance rate: 61.0%
- likes: 8452
- dislikes: 492

<br>

### Similar Problems

- [Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node) (Medium)
- [Boundary of Binary Tree](https://leetcode.com/problems/boundary-of-binary-tree) (Medium)
