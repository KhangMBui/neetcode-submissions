# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Solution: break the list in half using slow and fast ptr
        # then merge it back
        if not head:
            return
        slowPtr = head
        fastPtr = head.next
        while (fastPtr and fastPtr.next):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        # Second list starts from slowPtr.next
        second = slowPtr.next
        # break the chain:
        slowPtr.next = None
        # Previous node of second list is null:
        prev = None
        # Now reverse second list:
        while (second):
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # Now merge them back:
        first = head
        second = prev
        while (second):
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first, second = nxt1, nxt2
            