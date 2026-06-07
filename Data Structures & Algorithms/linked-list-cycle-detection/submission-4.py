# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Space complexity: O(1)
        # Time complexity: O(n)
        if not head:
            return False
        # Solution: Floyd's tortoise & hare
        slowPtr, fastPtr = head, head
        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                return True
        return False