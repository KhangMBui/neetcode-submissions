# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Solution: use 2 pointers, distance them
        # by exactly n units, and move them until one pointer 
        # reaches the end, and then exclude the other pointer
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        slowPtr = fastPtr = dummy
        # [1, 2, 3, 4]
        for i in range(n):
            fastPtr = fastPtr.next
        # [1, 2 (fastPtr here), 3, 4]
        while fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
        # [1, 2 (slowPtr), 3, 4 (fastPtr)]
        slowPtr.next = slowPtr.next.next
        return dummy.next