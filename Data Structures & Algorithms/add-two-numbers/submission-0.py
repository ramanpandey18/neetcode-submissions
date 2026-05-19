# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        
        carry = 0
        
        # Continue looping as long as there's a digit to process in l1 OR l2, 
        # OR if there's a leftover carry from the last addition
        while l1 or l2 or carry:
            # Extract values; if a list has ended, treat its value as 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum for this position
            total_sum = val1 + val2 + carry
            
            # Update the carry for the next column (will be 0 or 1)
            carry = total_sum // 10
            
            # The digit we store in the node is the remainder
            digit = total_sum % 10
            
            # Create the new node and attach it to our result list
            curr.next = ListNode(digit)
            curr = curr.next
            
            # Advance the list pointers forward if they haven't finished yet
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # Return the actual start of the summed linked list
        return dummy.next