# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         Create a dummy node pointing to head. This handles the edge case where the node to remove is the head itself, since slow can then stop at the dummy.
#         Advance fast by n steps. Now fast is exactly n nodes ahead of slow.
#         Move both pointers together until fast becomes None. At that point, fast is past the last node, so slow sits right before the node to delete.
#         Skip the target node: slow.next = slow.next.next.
# Return dummy.next, which is the (possibly new) head.
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        for _ in range(n):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        for _ in range(n):
            if fast:
                fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
