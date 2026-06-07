# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Solution: use slowPtr and fastPtr to spot the element to remove
        # Ensure the two pointers are distance exactly by n
        if not head:
            return None
        dummy = ListNode(0, head)
        slowPtr = fastPtr = dummy
        # Initialize the distance between the 2 ptrs
        for i in range(n):
            fastPtr = fastPtr.next
        # Now move them until fastPtr reaches the end
        while fastPtr and fastPtr.next:
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next
        # Now slowPtr lies exactly before the node to be removed
        slowPtr.next = slowPtr.next.next
        return dummy.next