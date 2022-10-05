# [257] Binary Tree Paths

**[string, backtracking, tree, depth-first-search, binary-tree]**

### Statement

Given the `root` of a binary tree, return *all root-to-leaf paths in **any order***.

A **leaf** is a node with no children.


**Example 1:**
![](https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg)

```

**Input:** root = [1,2,3,null,5]
**Output:** ["1->2->5","1->3"]

```

**Example 2:**

```

**Input:** root = [1]
**Output:** ["1"]

```

**Constraints:**
* The number of nodes in the tree is in the range `[1, 100]`.
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return
        ans = []
        def dfs(root, path, ans):
            if not root: return
            if root.left == None and root.right == None:
                l = path + str(root.val)
                ans.append(l)
            else:
                dfs(root.left, "{}{}->".format(path, root.val), ans)
                dfs(root.right, "{}{}->".format(path, root.val), ans)
        dfs(root, '', ans)
        return ans
```

<br>

### Statistics

- total accepted: 564765
- total submissions: 935699
- acceptance rate: 60.4%
- likes: 4953
- dislikes: 213

<br>

### Similar Problems

- [Path Sum II](https://leetcode.com/problems/path-sum-ii) (Medium)
- [Smallest String Starting From Leaf](https://leetcode.com/problems/smallest-string-starting-from-leaf) (Medium)
- [Step-By-Step Directions From a Binary Tree Node to Another](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another) (Medium)
