# [814] Binary Tree Pruning

**[tree, depth-first-search, binary-tree]**

### Statement

Given the `root` of a binary tree, return *the same tree where every subtree (of the given tree) not containing a* `1` *has been removed*.

A subtree of a node `node` is `node` plus every node that is a descendant of `node`.


**Example 1:**
![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png)

```

**Input:** root = [1,null,0,0,1]
**Output:** [1,null,0,null,1]
**Explanation:** 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

```

**Example 2:**
![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png)

```

**Input:** root = [1,0,1,0,0,0,1]
**Output:** [1,null,1,null,1]

```

**Example 3:**
![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png)

```

**Input:** root = [1,1,0,1,1,0,1,0]
**Output:** [1,1,0,1,1,null,1]

```

**Constraints:**
* The number of nodes in the tree is in the range `[1, 200]`.
* `Node.val` is either `0` or `1`.


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
    def pruneTree(self, root):
        def dfs(node):
            if not node: return True
            left, right = dfs(node.left), dfs(node.right)
            if left: node.left = None
            if right: node.right = None
            return left and right and node.val == 0
        ans = dfs(root)
        return root if not ans else None
```

<br>

### Statistics

- total accepted: 160088
- total submissions: 224824
- acceptance rate: 71.2%
- likes: 2769
- dislikes: 78

<br>

### Similar Problems

None
