# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy = ListNode(0, head)
        # slow = dummy
        # fast = head

        # for _ in range(n):
        #     if fast:
        #         fast = fast.next
        
        # while fast:
        #     slow = slow.next
        #     fast = fast.next
        
        # slow.next = slow.next.next
        
        # return dummy.next

class Solution:
    def removeNthFromEnd(self, head, n):

        # Data:
        # head = 1 → 2 → 3 → 4 → 5
        # n = 2

        slow = head
        fast = head

        # Move fast n nodes ahead.
        #
        # Initially:
        # 1 → 2 → 3 → 4 → 5
        # S
        # F
        #
        # After 1 move:
        # 1 → 2 → 3 → 4 → 5
        # S    F
        #
        # After 2 moves:
        # 1 → 2 → 3 → 4 → 5
        # S         F
        for _ in range(n):
            fast = fast.next

        # IMPORTANT:
        #
        # If fast is None here, it means we need
        # to remove the HEAD itself.
        #
        # Example:
        #
        # head = 1 → 2 → 3
        # n = 3
        #
        # After moving fast 3 times:
        #
        # 1 → 2 → 3 → None
        # S
        #             F
        #
        # So head must be removed.
        if fast is None:
            return head.next

        # Move both pointers together.
        #
        # Current example:
        #
        # 1 → 2 → 3 → 4 → 5
        # S         F
        #
        # After moving:
        #
        # 1 → 2 → 3 → 4 → 5
        #      S         F
        #
        # After moving again:
        #
        # 1 → 2 → 3 → 4 → 5
        #          S         F
        #
        # Eventually fast becomes None and
        # slow is at the node BEFORE the node
        # we want to remove.
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Current:
        #
        # 1 → 2 → 3 → 4 → 5
        #          S
        #
        # slow = 3
        # slow.next = 4
        # slow.next.next = 5
        #
        # Change:
        #
        # 3 → 4 → 5
        #
        # Into:
        #
        # 3 → 5
        slow.next = slow.next.next

        # Return original head.
        #
        # 1 → 2 → 3 → 5
        return head    