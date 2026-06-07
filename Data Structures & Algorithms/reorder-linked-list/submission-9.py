# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Solution: Split the list in half with slow and fast pointer
        # and then reverse the second list and merge them
        slowPtr = head
        fastPtr = head.next
        while (fastPtr and fastPtr.next):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        # The second list lies at slowPtr + 1
        second = slowPtr.next
        slowPtr.next = None
        prev = None
        # Now reverse the second list:
        while (second):
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # Now merge the 2 list 
        first = head
        second = prev
        while (second):
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first = nxt1
            second = nxt2
        