"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # Dictionary to map: Original Node -> Cloned Node
        # We pre-populate None -> None to gracefully handle null pointers
        old_to_new = {None: None}
        
        # --- First Pass ---
        # Create all cloned nodes with values, but no pointer connections yet
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # --- Second Pass ---
        # Connect the next and random pointers of our cloned nodes
        curr = head
        while curr:
            cloned_node = old_to_new[curr]
            
            # Connect the cloned node's next to the clone of the original's next
            cloned_node.next = old_to_new[curr.next]
            
            # Connect the cloned node's random to the clone of the original's random
            cloned_node.random = old_to_new[curr.random]
            
            curr = curr.next
            
        # Return the clone of the original head node
        return old_to_new[head]