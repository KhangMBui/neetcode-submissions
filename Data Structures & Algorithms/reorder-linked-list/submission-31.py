# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [2, 4, 6, 8]
        # [2, 4] & [8, 6]
        # [2, 8, 4, 6]
        # First step: split the list into half with slow and fast ptr
        # Second step: reverse second list
        # Third step: reconnect everything
        if not head:
            return None
        
        # First step: split the list into half:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        first = head # first list
        second = slow.next
        slow.next = None # Cut the link between the 2 lists

        # Second step: reverse the second list
        prev = None
        while (second):
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        # Second list will lie at prev.next
        second = prev # second list

        # Third step: reconnect everything
        while (second):
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first = nxt1
            second = nxt2
