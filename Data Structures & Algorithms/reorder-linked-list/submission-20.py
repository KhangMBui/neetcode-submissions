# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Second solution: split the list in half
        # with slow and fast pointers, and merge them
        # back after reversing the second list
        # Space complexity: O(1)
        # Time complexity: O(n)
        if not head:
            return None
        slowPtr = fastPtr = head
        while (fastPtr and fastPtr.next):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        # Second list will lie at slowPtr.next
        second = slowPtr.next
        # Cut the list in half:
        slowPtr.next = None
        # Reverse second list:
        prev = None
        while (second):
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # Second list will lie at prev
        second = prev
        first = head
        # Merge the list back together:
        while (second):
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first = nxt1
            second = nxt2
        
        