# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = second = dummy
        # Move first up a distance of n + 1
        for i in range(n + 1):
            first = first.next
        # Now move first and second up until first reaches the end:
        while (first):
            first = first.next
            second = second.next
        # Now second is at the position before the one to be removed
        second.next = second.next.next
        return dummy.next