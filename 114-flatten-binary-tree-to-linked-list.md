# [114] Flatten Binary Tree to Linked List

**[linked-list, stack, tree, depth-first-search, binary-tree]**

### Statement

Given the `root` of a binary tree, flatten the tree into a "linked list":

* The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
* The "linked list" should be in the same order as a [**pre-order** **traversal**](https://en.wikipedia.org/wiki/Tree_traversal#Pre-order,_NLR) of the binary tree.


**Example 1:**
![](https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg)

```

**Input:** root = [1,2,5,3,4,null,6]
**Output:** [1,null,2,null,3,null,4,null,5,null,6]

```

**Example 2:**

```

**Input:** root = []
**Output:** []

```

**Example 3:**

```

**Input:** root = [0]
**Output:** [0]

```

**Constraints:**
* The number of nodes in the tree is in the range `[0, 2000]`.
* `-100 <= Node.val <= 100`


**Follow up:** Can you flatten the tree in-place (with `O(1)` extra space)?

<br>

### Hints

- If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

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
    input = sys.stdin.readline
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            temp = root.right
            root.right=root.left
            root.left = None
            temp2 = root
            while temp2.right:
                temp2 = temp2.right
            
            temp2.right=temp
            self.flatten(root.right)
```

<br>

### Statistics

- total accepted: 722372
- total submissions: 1184055
- acceptance rate: 61.0%
- likes: 9430
- dislikes: 497

<br>

### Similar Problems

- [Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list) (Medium)
- [Correct a Binary Tree](https://leetcode.com/problems/correct-a-binary-tree) (Medium)
