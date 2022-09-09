# [94] Binary Tree Inorder Traversal

**[stack, tree, depth-first-search, binary-tree]**

### Statement

Given the `root` of a binary tree, return *the inorder traversal of its nodes' values*.


**Example 1:**
![](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

```

**Input:** root = [1,null,2,3]
**Output:** [1,3,2]

```

**Example 2:**

```

**Input:** root = []
**Output:** []

```

**Example 3:**

```

**Input:** root = [1]
**Output:** [1]

```

**Constraints:**
* The number of nodes in the tree is in the range `[0, 100]`.
* `-100 <= Node.val <= 100`


**Follow up:** Recursive solution is trivial, could you do it iteratively?

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        def inorder(root, l):
            if not root: return
            inorder(root.left, l)
            l.append(root.val)
            inorder(root.right, l)
        inorder(root, l)
        return l
```

<br>

### Statistics

- total accepted: 1716418
- total submissions: 2363310
- acceptance rate: 72.6%
- likes: 9519
- dislikes: 451

<br>

### Similar Problems

- [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree) (Medium)
- [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal) (Easy)
- [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal) (Easy)
- [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator) (Medium)
- [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst) (Medium)
- [Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii) (Hard)
- [Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst) (Medium)
- [Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list) (Medium)
- [Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes) (Easy)
