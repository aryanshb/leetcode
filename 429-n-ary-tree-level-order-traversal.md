# [429] N-ary Tree Level Order Traversal

**[tree, breadth-first-search]**

### Statement

Given an n-ary tree, return the *level order* traversal of its nodes' values.

*Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).*
**Example 1:**
![](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

```

**Input:** root = [1,null,3,2,4,null,5,6]
**Output:** [[1],[3,2,4],[5,6]]

```

**Example 2:**
![](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)

```

**Input:** root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
**Output:** [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

```

**Constraints:**
* The height of the n-ary tree is less than or equal to `1000`
* The total number of nodes is between `[0, 104]`


<br>

### Hints

None

<br>

### Solution

```py
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def dfs(root, level):
            if root == None: 
                return
            if level == len(ans):
                ans.append([])
            ans[level].append(root.val)
            for child in root.children:
                dfs(child, level + 1)
        ans = []
        dfs(root, 0)
        return ans
        
```

<br>

### Statistics

- total accepted: 236951
- total submissions: 337573
- acceptance rate: 70.2%
- likes: 2845
- dislikes: 112

<br>

### Similar Problems

- [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal) (Medium)
- [N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal) (Easy)
- [N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal) (Easy)
- [The Time When the Network Becomes Idle](https://leetcode.com/problems/the-time-when-the-network-becomes-idle) (Medium)
