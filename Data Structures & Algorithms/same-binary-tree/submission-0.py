# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        # Base Case 2: One node is None but the other isn't (structural mismatch)
        if not p or not q:
            return False
        
        # Base Case 3: The values inside the nodes don't match (value mismatch)
        if p.val != q.val:
            return False
        
        # Recursive Step: Check if both left subtrees match AND both right subtrees match
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)