# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        # Solution 1: make a list out of the linkedlist and use 2ptrs
        nodes = []
        curr = head
        while (curr):
            nodes.append(curr)
            curr = curr.next
        l, r = 0, len(nodes) - 1
        while (l < r):
            nodes[l].next = nodes[r]
            l += 1
            if (l >= r):
                break
            nodes[r].next = nodes[l]
            r -= 1
        nodes[r].next = None