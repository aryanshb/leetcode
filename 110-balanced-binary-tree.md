# [110] Balanced Binary Tree

**[tree, depth-first-search, binary-tree]**

### Statement

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:


> 
> a binary tree in which the left and right subtrees of *every* node differ in height by no more than 1.
> 


**Example 1:**
![](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

```

**Input:** root = [3,9,20,null,null,15,7]
**Output:** true

```

**Example 2:**
![](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

```

**Input:** root = [1,2,2,3,3,null,null,4,4]
**Output:** false

```

**Example 3:**

```

**Input:** root = []
**Output:** true

```

**Constraints:**
* The number of nodes in the tree is in the range `[0, 5000]`.
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return 0
            return  1+(max(dfs(root.left), dfs(root.right)))
        if not root: return True
        # return abs(dfs(root.left)-dfs(root.right)) <=1
        return abs(dfs(root.left)-dfs(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
```

<br>

### Statistics

- total accepted: 936055
- total submissions: 1948112
- acceptance rate: 48.0%
- likes: 7423
- dislikes: 390

<br>

### Similar Problems

- [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree) (Easy)
