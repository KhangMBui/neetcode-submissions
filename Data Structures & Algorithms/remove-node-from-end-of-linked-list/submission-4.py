# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Solution: two pointers fast and slow
        dummy = ListNode(0, head)
        first = second = dummy
        for i in range(n + 1):
            second = second.next
        while (second):
            second = second.next
            first = first.next
        # First will be at the position before the to-be-removed node
        first.next = first.next.next
        return dummy.next