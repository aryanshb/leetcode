# [111] Minimum Depth of Binary Tree

**[tree, depth-first-search, breadth-first-search, binary-tree]**

### Statement

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note:**A leaf is a node with no children.


**Example 1:**
![](https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg)

```

**Input:** root = [3,9,20,null,null,15,7]
**Output:** 2

```

**Example 2:**

```

**Input:** root = [2,null,3,null,4,null,5,null,6]
**Output:** 5

```

**Constraints:**
* The number of nodes in the tree is in the range `[0, 105]`.
* `-1000 <= Node.val <= 1000`


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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans = []
        if not root: return 0
        def dfs(root, lvl, ans):
            if not root:
                return
            if not root.left and not root.right: ans.append(lvl+1)
            dfs(root.left, lvl+1, ans)
            dfs(root.right, lvl+1, ans)
        dfs(root, 0, ans)
        return min(ans)
                
```

<br>

### Statistics

- total accepted: 828776
- total submissions: 1914596
- acceptance rate: 43.3%
- likes: 4804
- dislikes: 996

<br>

### Similar Problems

- [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal) (Medium)
- [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree) (Easy)
