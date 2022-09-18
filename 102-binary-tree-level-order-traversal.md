# [102] Binary Tree Level Order Traversal

**[tree, breadth-first-search, binary-tree]**

### Statement

Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).


**Example 1:**
![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```

**Input:** root = [3,9,20,null,null,15,7]
**Output:** [[3],[9,20],[15,7]]

```

**Example 2:**

```

**Input:** root = [1]
**Output:** [[1]]

```

**Example 3:**

```

**Input:** root = []
**Output:** []

```

**Constraints:**
* The number of nodes in the tree is in the range `[0, 2000]`.
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, lvl, levels):
            if not root: return
            if lvl not in levels: levels[lvl] = []
            levels[lvl].append(root.val)
            dfs(root.left, lvl+1, levels)
            dfs(root.right, lvl+1, levels)
            
        levels = {}
        dfs(root, 0, levels)
        return [i for i in levels.values()]
                
```

<br>

### Statistics

- total accepted: 1509769
- total submissions: 2398614
- acceptance rate: 62.9%
- likes: 10806
- dislikes: 201

<br>

### Similar Problems

- [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal) (Medium)
- [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii) (Medium)
- [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree) (Easy)
- [Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal) (Medium)
- [Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree) (Easy)
- [N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal) (Medium)
- [Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree) (Easy)
