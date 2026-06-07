# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        nodes = []
        curr = head
        while (curr):
            nodes.append(curr)
            curr = curr.next
        l, r = 0, len(nodes) - 1
        while (l < r):
            nxtTmp = nodes[l].next
            nodes[l].next = nodes[r]
            l += 1
            if (l >= r):
                break
            nodes[r].next = nxtTmp
            r -= 1
        nodes[l].next = None
        