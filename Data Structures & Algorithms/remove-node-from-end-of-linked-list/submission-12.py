# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0, head)
        slowPtr = fastPtr = dummy
        for _ in range(n):
            fastPtr = fastPtr.next
        
        while fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
        slowPtr.next = slowPtr.next.next
        return dummy.next