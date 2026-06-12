# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 109
        # 255
        # 9 + 5 = 14. 14 % 10 == 4; 14 // 10 == 1
        # 4 is what we keep. 1 is what we carry on

        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        curr1, curr2 = l1, l2
        while curr1 or curr2 or carry:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0

            result = val1 + val2 + carry
            keep = result % 10
            carry = result // 10

            tail.next = ListNode(keep)
            tail = tail.next
            
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        
        
        return dummy.next
