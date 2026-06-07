# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Second solution: Split the list in half
        # with slow and fast pointers, and merge them back
        # after reversing the second list
        if not head:
            return None
        slowPtr = fastPtr = head
        while (fastPtr and fastPtr.next):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        # Slow pointer will placed directly at the middle
        second = slowPtr.next
        # Cut the linked list into two:
        slowPtr.next = None
        prev = None
        while (second):
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        first = head
        second = prev
        while (second):
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first = nxt1
            second = nxt2
