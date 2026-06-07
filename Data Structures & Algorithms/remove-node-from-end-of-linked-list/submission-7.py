# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if n == 0:
            return head
        # Solution: use slow and fast pointers
        dummy = ListNode(0, head)
        slowPtr = fastPtr = dummy
        for i in range(n + 1):
            fastPtr = fastPtr.next
        while (fastPtr):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
        # Now slowPtr lies just before the element to remove
        slowPtr.next = slowPtr.next.next
        return dummy.next