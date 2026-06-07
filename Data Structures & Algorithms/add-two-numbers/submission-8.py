# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        elif not l1:
            l1 = ListNode(0)
        elif not l2:
            l2 = ListNode(0)
        nodeSum = l1.val + l2.val
        curr = ListNode(nodeSum % 10)
        if nodeSum >= 10:
            if l2.next:
                l2.next.val += 1
            else:
                l2.next = ListNode(1)
        curr.next = self.addTwoNumbers(l1.next, l2.next)
        return curr