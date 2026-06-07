# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Solution 2: Split the LinkedList in half with slowptr and fastptr
        # then reverse the second one and merge it back
        slowPtr = head
        fastPtr = head.next
        while (fastPtr and fastPtr.next):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        # the second list lies at slowPtr + 1
        second = slowPtr.next
        slowPtr.next = None
        prev = None
        while (second):
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # Now merge them back, first list always equal or bigger in length:
        second = prev
        first = head
        while (second):
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first = nxt1
            second = nxt2
