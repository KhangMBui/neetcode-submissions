# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Solution 1: Create a dummy node and a tail node. Tail node 
        # iterate through list1 and list2 and add stuffs to the LinkedList.
        # The dummy is to keep track of the head to return later
        dummy = ListNode()
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