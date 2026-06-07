# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Solution: Create a tail node that goes through the 2 lists,
        # comparing their values while adding to the tail
        # while also having a dummy list that holds the head value
        # So we can return it later
        if not list1:
            return list2
        if not list2:
            return list1
        dummy = ListNode(0, list1 if list1.val < list2.val else list2)
        tail = dummy
        while (list1 and list2):
            if (list1.val < list2.val):
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if (list1):
            tail.next = list1
        elif (list2):
            tail.next = list2
        return dummy.next
