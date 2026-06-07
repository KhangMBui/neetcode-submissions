# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Second solution: Split the list in half with slowPtr and fastPtr
        # and then reverse the second half and merge them back in
        slowPtr, fastPtr = head, head.next
        while (fastPtr and fastPtr.next):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        # The second list will starts from slowPtr.next
        second = slowPtr.next
        # Now reverse the second list:
        prev = None
        slowPtr.next = None
        while (second):
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # The second list's new head is prev
        second = prev
        first = head
        while (second):
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first = nxt1
            second = nxt2
