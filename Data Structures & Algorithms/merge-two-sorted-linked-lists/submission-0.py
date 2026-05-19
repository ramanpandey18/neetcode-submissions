# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next  # Move list1 pointer forward
            else:
                tail.next = list2
                list2 = list2.next  # Move list2 pointer forward
            
            tail = tail.next  # Move the tail pointer forward
            
        # If one list is exhausted, append the remaining nodes of the other list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # The actual head of the merged list is the next node after the dummy node
        return dummy.next