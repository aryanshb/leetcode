# [2] Add Two Numbers

**[linked-list, math, recursion]**

### Statement

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sumas a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


**Example 1:**
![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

```

**Input:** l1 = [2,4,3], l2 = [5,6,4]
**Output:** [7,0,8]
**Explanation:** 342 + 465 = 807.

```

**Example 2:**

```

**Input:** l1 = [0], l2 = [0]
**Output:** [0]

```

**Example 3:**

```

**Input:** l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
**Output:** [8,9,9,9,0,0,0,1]

```

**Constraints:**
* The number of nodes in each linked list is in the range `[1, 100]`.
* `0 <= Node.val <= 9`
* It is guaranteed that the list represents a number that does not have leading zeros.


<br>

### Hints

None

<br>

### Solution

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a, i = [], 1
        b, j = [], 1
        while l1!=None :
            a += [str(l1.val)]
            l1 = l1.next
        while l2!=None:
            b += [str(l2.val)]
            l2 = l2.next
        a1, b1 = int("".join(a[::-1])), int("".join(b[::-1]))
        l = str(a1+b1)
        l5 = [i for i in l]
        l5 = l5[::-1]
        ans = ListNode()
        ans.val = 10**8
        def addend(data, node):
            newnode = ListNode()
            newnode.val = data
            if node.val == 10**8:
                node.val = data
                node.next = None
                return
            while(node.next):
                node = node.next
            node.next = newnode
        print("".join(l5))
        for i in l5:
            addend(i, ans)
        return ans
```

<br>

### Statistics

- total accepted: 3075782
- total submissions: 7801634
- acceptance rate: 39.4%
- likes: 21217
- dislikes: 4178

<br>

### Similar Problems

- [Multiply Strings](https://leetcode.com/problems/multiply-strings) (Medium)
- [Add Binary](https://leetcode.com/problems/add-binary) (Easy)
- [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers) (Medium)
- [Add Strings](https://leetcode.com/problems/add-strings) (Easy)
- [Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii) (Medium)
- [Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer) (Easy)
- [Add Two Polynomials Represented as Linked Lists](https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists) (Medium)
