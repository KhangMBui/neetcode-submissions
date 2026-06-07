# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slowPtr = fastPtr = dummy
        for i in range(n + 1):
            fastPtr = fastPtr.next
        while (fastPtr):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
        # Slow pointer will be right before the node to remove
        slowPtr.next = slowPtr.next.next
        return dummy.next