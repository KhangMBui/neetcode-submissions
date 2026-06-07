# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Solution 2: Reverse and merge
        # Use fastPtr and slowPtr to split the linkedlist in half,
        # reverse the second list, and merge them back
        if not head:
            return None
        slowPtr = fastPtr = head
        while (fastPtr and fastPtr.next):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        # Once it ends, the slowPtr lies at the boundary of the two splitted lists:
        # [2, 4, 6, 8]: slowPtr at 6
        # [2, 4, 6, 8, 10]: slowPtr at 6
        second = slowPtr.next
        # Cut the two lists in half:
        slowPtr.next = None
        # [2, 4, 6] & [8, 10]
        # Reverse the second list:
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # [2, 4, 6] & [10, 8]
        first = head
        second = prev
        while (second):
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first = nxt1
            second = nxt2
        
        