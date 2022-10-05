# [226] Invert Binary Tree

**[tree, depth-first-search, breadth-first-search, binary-tree]**

### Statement

Given the `root` of a binary tree, invert the tree, and return *its root*.


**Example 1:**
![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

```

**Input:** root = [4,2,7,1,3,6,9]
**Output:** [4,7,2,9,6,3,1]

```

**Example 2:**
![](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

```

**Input:** root = [2,1,3]
**Output:** [2,3,1]

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
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```

<br>

### Statistics

- total accepted: 1264328
- total submissions: 1730563
- acceptance rate: 73.1%
- likes: 9957
- dislikes: 136

<br>

### Similar Problems

- [Reverse Odd Levels of Binary Tree](https://leetcode.com/problems/reverse-odd-levels-of-binary-tree) (Medium)
