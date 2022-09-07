# [117] Populating Next Right Pointers in Each Node II

**[linked-list, tree, depth-first-search, breadth-first-search, binary-tree]**

### Statement

Given a binary tree


```

struct Node {
  int val;
  Node \*left;
  Node \*right;
  Node \*next;
}

```


Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.


**Example 1:**
![](https://assets.leetcode.com/uploads/2019/02/15/117_sample.png)

```

**Input:** root = [1,2,3,4,5,null,7]
**Output:** [1,#,2,3,#,4,5,7,#]
**Explanation:** Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

```

**Example 2:**

```

**Input:** root = []
**Output:** []

```

**Constraints:**
* The number of nodes in the tree is in the range `[0, 6000]`.
* `-100 <= Node.val <= 100`


**Follow-up:**
* You may only use constant extra space.
* The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.


<br>

### Hints

None

<br>

### Solution

```py
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        lvls = dict()
        def dfs(root, lvl):
            if not root: return
            if lvl not in lvls:
                lvls[lvl] = []
            lvls[lvl].append(root)
            dfs(root.left, lvl+1)
            dfs(root.right,lvl+1)
        dfs(root, 0)
        for i in lvls.values():
            for j in range(len(i)-1):
                i[j].next = i[j+1]
        return root
```

<br>

### Statistics

- total accepted: 507629
- total submissions: 1029636
- acceptance rate: 49.3%
- likes: 4789
- dislikes: 274

<br>

### Similar Problems

- [Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node) (Medium)
