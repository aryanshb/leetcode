# [653] Two Sum IV - Input is a BST

**[hash-table, two-pointers, tree, depth-first-search, breadth-first-search, binary-search-tree, binary-tree]**

### Statement

Given the `root` of a Binary Search Tree and a target number `k`, return *`true` if there exist two elements in the BST such that their sum is equal to the given target*.


**Example 1:**
![](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg)

```

**Input:** root = [5,3,6,2,4,null,7], k = 9
**Output:** true

```

**Example 2:**
![](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg)

```

**Input:** root = [5,3,6,2,4,null,7], k = 28
**Output:** false

```

**Constraints:**
* The number of nodes in the tree is in the range `[1, 104]`.
* `-104<= Node.val <= 104`
* `root` is guaranteed to be a **valid** binary search tree.
* `-105<= k <= 105`


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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = {}
        def dfs(root, l):
            if not root: return
            dfs(root.left,l)
            if root.val not in l: l[root.val] = 1
            else: l[root.val]+=1
            dfs(root.right,l)
        dfs(root, l)
        for i in l:
            l[i] -=1
            if k-i in l and l[k-i]>0:return True
        return False
        
            
```

<br>

### Statistics

- total accepted: 380979
- total submissions: 633663
- acceptance rate: 60.1%
- likes: 4824
- dislikes: 221

<br>

### Similar Problems

- [Two Sum](https://leetcode.com/problems/two-sum) (Easy)
- [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted) (Medium)
- [Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design) (Easy)
- [Two Sum BSTs](https://leetcode.com/problems/two-sum-bsts) (Medium)
