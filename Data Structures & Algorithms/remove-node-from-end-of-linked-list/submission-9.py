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
        # Solution: use 2 pointers: slowPtr and fastPtr,
        # and keep the distance between them exactly n,
        # so when fastPtr reaches the end of the line, 
        # slowPtr can tell us which node to remove
        dummy = ListNode(0, head)
        slowPtr, fastPtr = dummy, dummy
        # Create the initial spacing between the two pointers:
        for i in range(n + 1):
            fastPtr = fastPtr.next
        # Now iterate the two pointers until fastPtr reaches the end
        while (fastPtr):
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next
        # Now slowPtr lies exactly before the node to remove
        slowPtr.next = slowPtr.next.next
        return dummy.next