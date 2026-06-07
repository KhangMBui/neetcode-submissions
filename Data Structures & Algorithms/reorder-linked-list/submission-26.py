# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Solution 2: Use fastPtr and slowPtr to split
        # the LinkedList in half, reverse the second list,
        # and merge them back
        if not head:
            return None
        fastPtr, slowPtr = head, head
        while (fastPtr and fastPtr.next):
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
        # slowPtr will be placed at the middle of the two list
        second = slowPtr.next
        # Cut the linkedlist in half:
        slowPtr.next = None
        # Reverse the second list:
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
        