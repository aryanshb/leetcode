# [98] Validate Binary Search Tree

**[tree, depth-first-search, binary-search-tree, binary-tree]**

### Statement

Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.

A **valid BST** is defined as follows:

* The left subtree of a node contains only nodes with keys **less than** the node's key.
* The right subtree of a node contains only nodes with keys **greater than** the node's key.
* Both the left and right subtrees must also be binary search trees.


**Example 1:**
![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

```

**Input:** root = [2,1,3]
**Output:** true

```

**Example 2:**
![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

```

**Input:** root = [5,1,4,null,null,3,6]
**Output:** false
**Explanation:** The root node's value is 5 but its right child's value is 4.

```

**Constraints:**
* The number of nodes in the tree is in the range `[1, 104]`.
* `-231 <= Node.val <= 231 - 1`


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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def dfs(root, ans):
            if not root: return
            dfs(root.left, ans)
            ans.append(root.val)
            dfs(root.right, ans)
        dfs(root, ans)
        print(ans)
        for i in range(len(ans)-1):
            if ans[i]>= ans[i+1]: return False
        return True
```

<br>

### Statistics

- total accepted: 1652662
- total submissions: 5238115
- acceptance rate: 31.6%
- likes: 12386
- dislikes: 1000

<br>

### Similar Problems

- [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal) (Easy)
- [Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree) (Easy)
