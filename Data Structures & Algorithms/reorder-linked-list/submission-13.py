# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if not head or not head.next:
        #     return
        # Find the middle with slow/fast pointers.
        # Split the list at the middle (slow.next = None).
        # Reverse the second half.
        # Merge the two halves by alternating nodes.
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None #will contain the reversed list
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        
        first, second = head, prev
        while second:
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            first, second = first_next, second_next

        # first, second = head, prev
        # while second:
        #     first_next, second_next = first.next, second.next
        #     first.next = second
        #     second.next = first_next
        #     first, second = first_next, second_next
