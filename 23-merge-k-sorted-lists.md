# [23] Merge k Sorted Lists

**[linked-list, divide-and-conquer, heap-priority-queue, merge-sort]**

### Statement

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*
**Example 1:**

```

**Input:** lists = [[1,4,5],[1,3,4],[2,6]]
**Output:** [1,1,2,3,4,4,5,6]
**Explanation:** The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

```

**Example 2:**

```

**Input:** lists = []
**Output:** []

```

**Example 3:**

```

**Input:** lists = [[]]
**Output:** []

```

**Constraints:**
* `k == lists.length`
* `0 <= k <= 104`
* `0 <= lists[i].length <= 500`
* `-104 <= lists[i][j] <= 104`
* `lists[i]` is sorted in **ascending order**.
* The sum of `lists[i].length` will not exceed `104`.


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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        for i in lists:
            while i!=None:
                l.append(i.val)
                i = i.next
        l.sort()
        if len(l) == 0:return
        if len(l) == 1: return ListNode(l[0])
        cur = temp = ListNode(l[0])
        for i in l[1:]:
            cur.next = ListNode(i)
            cur = cur.next
        return temp
```

<br>

### Statistics

- total accepted: 1432821
- total submissions: 2968652
- acceptance rate: 48.3%
- likes: 14403
- dislikes: 539

<br>

### Similar Problems

- [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists) (Easy)
- [Ugly Number II](https://leetcode.com/problems/ugly-number-ii) (Medium)
- [Smallest Subarrays With Maximum Bitwise OR](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or) (Medium)
