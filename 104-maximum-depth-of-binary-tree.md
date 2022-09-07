# [104] Maximum Depth of Binary Tree

**[tree, depth-first-search, breadth-first-search, binary-tree]**

### Statement

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth**is the number of nodes along the longest path from the root node down to the farthest leaf node.


**Example 1:**
![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

```

**Input:** root = [3,9,20,null,null,15,7]
**Output:** 3

```

**Example 2:**

```

**Input:** root = [1,null,2]
**Output:** 2

```

**Constraints:**
* The number of nodes in the tree is in the range `[0, 104]`.
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        cur = 0
        ma = 0
        def dfs(root, cur):
            nonlocal ma
            if not root:
                return
            dfs(root.left, cur+1)
            dfs(root.right, cur+1)
            ma = max(cur, ma)

        dfs(root, cur)
        return ma+1
            
```

<br>

### Statistics

- total accepted: 1910504
- total submissions: 2623003
- acceptance rate: 72.8%
- likes: 8331
- dislikes: 138

<br>

### Similar Problems

- [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree) (Easy)
- [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree) (Easy)
- [Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree) (Easy)
- [Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees) (Medium)
- [Amount of Time for Binary Tree to Be Infected](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected) (Medium)
