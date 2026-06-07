# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        # Solution 2: Split the list in half with slowptr and fastptr
        # reverse the second list and merge them back
        slowptr = fastptr = head
        while (fastptr and fastptr.next):
            fastptr = fastptr.next.next
            slowptr = slowptr.next
        # Second will lies at slowptr.next
        second = slowptr.next
        slowptr.next = prev= None
        # reverse the list:
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
        