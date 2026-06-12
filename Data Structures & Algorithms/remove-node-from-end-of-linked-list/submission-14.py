# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Removing the n-th node from the end means
        # removing the (N-nth) node from the start
        # 2 pass: 
        # first pass is to count total nodes
        # second pass: move to (N - nth) node and remove it
        if not head:
            return None
        
        # First pass:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        # Second pass:
        curr = head
        prev = None
        removeIndex = count - n

        if removeIndex == 0:
            return head.next

        for i in range(removeIndex):
            prev = curr
            curr = curr.next

        
        # curr is now the element to remove, prev is previous element
        prev.next = curr.next

        return head