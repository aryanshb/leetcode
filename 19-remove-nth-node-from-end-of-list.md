# [19] Remove Nth Node From End of List

**[linked-list, two-pointers]**

### Statement

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.


**Example 1:**
![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```

**Input:** head = [1,2,3,4,5], n = 2
**Output:** [1,2,3,5]

```

**Example 2:**

```

**Input:** head = [1], n = 1
**Output:** []

```

**Example 3:**

```

**Input:** head = [1,2], n = 1
**Output:** [1]

```

**Constraints:**
* The number of nodes in the list is `sz`.
* `1 <= sz <= 30`
* `0 <= Node.val <= 100`
* `1 <= n <= sz`


**Follow up:** Could you do this in one pass?

<br>

### Hints

- Maintain two pointers and update one with a delay of n steps.

<br>

### Solution

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None: return None
        l = []
        sz = 0
        temp = None
        temp = head
        while temp!=None:
            l.append(temp)
            temp = temp.next
            sz+=1
        for i in l: print(i.val)
        print(n, sz, l[sz-n].val)
        if sz == 1: return None
        if sz == n: return l[1]
        l[sz-n-1].next = l[sz-n].next
        return head
```

<br>

### Statistics

- total accepted: 1700145
- total submissions: 4284727
- acceptance rate: 39.7%
- likes: 13075
- dislikes: 548

<br>

### Similar Problems

- [Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list) (Medium)
- [Delete N Nodes After M Nodes of a Linked List](https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list) (Easy)
- [Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list) (Medium)
