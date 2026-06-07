# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if not l1:
            l1 = ListNode(0)
        if not l2:
            l2 = ListNode(0)
        node_sum = l1.val + l2.val
        curr_node = ListNode(node_sum % 10)
        if node_sum >= 10:
            if l1.next:
                l1.next.val += 1
            else:
                l1.next = ListNode(1)
        curr_node.next = self.addTwoNumbers(l1.next, l2.next)
        return curr_node
