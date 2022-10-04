# [112] Path Sum

**[tree, depth-first-search, breadth-first-search, binary-tree]**

### Statement

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.


**Example 1:**
![](https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg)

```

**Input:** root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
**Output:** true
**Explanation:** The root-to-leaf path with the target sum is shown.

```

**Example 2:**
![](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

```

**Input:** root = [1,2,3], targetSum = 5
**Output:** false
**Explanation:** There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

```

**Example 3:**

```

**Input:** root = [], targetSum = 0
**Output:** false
**Explanation:** Since the tree is empty, there are no root-to-leaf paths.

```

**Constraints:**
* The number of nodes in the tree is in the range `[0, 5000]`.
* `-1000 <= Node.val <= 1000`
* `-1000 <= targetSum <= 1000`


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
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        def dfs(root, target):
            if not root: return
            target -= root.val
            if not root.left and not root.right: return target == 0
            else:
                return dfs(root.left, target) or dfs(root.right, target)
        return dfs(root, target)
```

<br>

### Statistics

- total accepted: 1007283
- total submissions: 2148967
- acceptance rate: 46.9%
- likes: 6773
- dislikes: 845

<br>

### Similar Problems

- [Path Sum II](https://leetcode.com/problems/path-sum-ii) (Medium)
- [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum) (Hard)
- [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers) (Medium)
- [Path Sum III](https://leetcode.com/problems/path-sum-iii) (Medium)
- [Path Sum IV](https://leetcode.com/problems/path-sum-iv) (Medium)
