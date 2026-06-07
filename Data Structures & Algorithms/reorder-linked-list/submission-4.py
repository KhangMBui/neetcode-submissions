# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        # Use slow and fast pointer to split the list
        curr = head
        slowPtr = curr
        fastPtr = curr.next
        while (fastPtr and fastPtr.next):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        secondList = slowPtr.next
        # Break the chain
        slowPtr.next = None
        # The previous node of the second list is null
        prev = None
        # Reverse the secondList
        while secondList:
            tmp = secondList.next
            secondList.next = prev
            prev = secondList
            secondList = tmp
        
        # merge two halfs, the new head starts at prev (the end of our iteration)
        secondList = prev
        firstList = head
        # Either equal or secondList less than firstList
        while (secondList):
            nxt1, nxt2 = firstList.next, secondList.next
            firstList.next = secondList
            secondList.next = nxt1
            firstList = nxt1
            secondList = nxt2