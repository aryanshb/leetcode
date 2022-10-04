# [21] Merge Two Sorted Lists

**[linked-list, recursion]**

### Statement

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.


**Example 1:**
![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```

**Input:** list1 = [1,2,4], list2 = [1,3,4]
**Output:** [1,1,2,3,4,4]

```

**Example 2:**

```

**Input:** list1 = [], list2 = []
**Output:** []

```

**Example 3:**

```

**Input:** list1 = [], list2 = [0]
**Output:** [0]

```

**Constraints:**
* The number of nodes in both lists is in the range `[0, 50]`.
* `-100 <= Node.val <= 100`
* Both `list1` and `list2` are sorted in **non-decreasing** order.


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
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		newlist = ListNode()
		newlistptr = newlist

		while l1 and l2:
			if l1.val <= l2.val:
				newlistptr.next = l1
				l1 = l1.next
			else:
				newlistptr.next = l2
				l2 = l2.next
			newlistptr = newlistptr.next
		if l1 != None:
			newlistptr.next = l1
		else:
			newlistptr.next = l2
		return newlist.next
```

<br>

### Statistics

- total accepted: 2664403
- total submissions: 4320029
- acceptance rate: 61.7%
- likes: 15177
- dislikes: 1332

<br>

### Similar Problems

- [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists) (Hard)
- [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array) (Easy)
- [Sort List](https://leetcode.com/problems/sort-list) (Medium)
- [Shortest Word Distance II](https://leetcode.com/problems/shortest-word-distance-ii) (Medium)
- [Add Two Polynomials Represented as Linked Lists](https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists) (Medium)
- [Longest Common Subsequence Between Sorted Arrays](https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays) (Medium)
