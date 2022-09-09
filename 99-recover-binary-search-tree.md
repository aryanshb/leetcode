# [99] Recover Binary Search Tree

**[tree, depth-first-search, binary-search-tree, binary-tree]**

### Statement

You are given the `root` of a binary search tree (BST), where the values of **exactly** two nodes of the tree were swapped by mistake. *Recover the tree without changing its structure*.


**Example 1:**
![](https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg)

```

**Input:** root = [1,3,null,null,2]
**Output:** [3,1,null,null,2]
**Explanation:** 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

```

**Example 2:**
![](https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg)

```

**Input:** root = [3,1,4,null,null,2]
**Output:** [2,1,4,null,null,3]
**Explanation:** 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

```

**Constraints:**
* The number of nodes in the tree is in the range `[2, 1000]`.
* `-231 <= Node.val <= 231 - 1`


**Follow up:** A solution using `O(n)` space is pretty straight-forward. Could you devise a constant `O(1)` space solution?

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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root, ls1):
            if not root: return
            inorder(root.left, ls)
            ls.append([root.val, root])
            inorder(root.right, ls)
        ls = []
        inorder(root, ls)
        target = sorted(ls)
        print(ls, target)
        for i in range(len(ls)):
            if ls[i][1] != target[i][1]:
                ls[i][1].val, target[i][1].val = target[i][1].val, ls[i][1].val
                break
                
```

<br>

### Statistics

- total accepted: 356710
- total submissions: 714648
- acceptance rate: 49.9%
- likes: 6044
- dislikes: 196

<br>

### Similar Problems

None
