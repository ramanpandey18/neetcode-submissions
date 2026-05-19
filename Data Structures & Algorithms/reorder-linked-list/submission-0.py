# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the list
        # 'second' will be the head of the second half
        second = slow.next
        slow.next = None  # Sever the connection between 1st and 2nd halves
        
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        # 'prev' is now the head of the reversed second half
        # 'first' is the head of the first half
        first, second = head, prev
        
        # Step 3: Merge the two sorted/separated lists
        while second:
            tmp1, tmp2 = first.next, second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2