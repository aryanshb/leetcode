#### Solution
```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return
        n = 0
        temp = head
        while temp!=None:
            temp = temp.next
            n+=1
        if n == 2: 
            head.next = None
            return head
        if n == 1:
            return None
        temp = head
        for i in range(n//2):
            temp = temp.next
        
        temp.val = temp.next.val
        temp.next = temp.next.next
        return head
```

