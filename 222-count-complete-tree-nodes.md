# [222] Count Complete Tree Nodes

**[binary-search, tree, depth-first-search, binary-tree]**

### Statement

Given the `root` of a **complete** binary tree, return the number of the nodes in the tree.

According to **[Wikipedia](http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees)**, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between `1` and `2h` nodes inclusive at the last level `h`.

Design an algorithm that runs in less than`O(n)`time complexity.


**Example 1:**
![](https://assets.leetcode.com/uploads/2021/01/14/complete.jpg)

```

**Input:** root = [1,2,3,4,5,6]
**Output:** 6

```

**Example 2:**

```

**Input:** root = []
**Output:** 0

```

**Example 3:**

```

**Input:** root = [1]
**Output:** 1

```

**Constraints:**
* The number of nodes in the tree is in the range `[0, 5 * 104]`.
* `0 <= Node.val <= 5 * 104`
* The tree is guaranteed to be **complete**.


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
        def countNodes(self, root):
            if not root:
                return 0
            leftDepth = self.getDepth(root.left)
            rightDepth = self.getDepth(root.right)
            if leftDepth == rightDepth:
                return pow(2, leftDepth) + self.countNodes(root.right)
            else:
                return pow(2, rightDepth) + self.countNodes(root.left)
    
        def getDepth(self, root):
            if not root:
                return 0
            return 1 + self.getDepth(root.left)
```

<br>

### Statistics

- total accepted: 449659
- total submissions: 785506
- acceptance rate: 57.2%
- likes: 5756
- dislikes: 333

<br>

### Similar Problems

- [Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value) (Easy)
