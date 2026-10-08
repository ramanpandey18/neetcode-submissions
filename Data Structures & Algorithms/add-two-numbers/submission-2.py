# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node so you never need a special case for the head of the result.
        # Loop while l1 or l2 or carry. The carry condition is the key detail: it handles a leftover carry after both lists end (e.g. 9 + 9 gives [8, 1]).
        # Read digits safely with l1.val if l1 else 0, which treats a shorter list as having leading zeros.
        # Compute total = val1 + val2 + carry, then carry = total // 10 and digit = total % 10.
        # Append a new node with digit, and advance curr.
        # Advance l1 and l2 only if they’re not None.
        # Return dummy.next.
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            digit = total_sum % 10
            curr.next = ListNode(digit)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            digit = total_sum % 10
            curr.next = ListNode(digit)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
