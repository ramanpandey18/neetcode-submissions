# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node: Optional[TreeNode]) -> int:
            # Base case: An empty tree has a height of 0 and is balanced
            if not node:
                return 0
            
            # 1. Check the left subtree
            left_height = check_height(node.left)
            if left_height == -1: 
                return -1  # Already unbalanced below, pass the error up
            
            # 2. Check the right subtree
            right_height = check_height(node.right)
            if right_height == -1: 
                return -1  # Already unbalanced below, pass the error up
            
            # 3. Check the current node's balance factor
            if abs(left_height - right_height) > 1:
                return -1  # Current node is unbalanced!
            
            # 4. If balanced, return the actual height of this node
            return max(left_height, right_height) + 1

        # If the helper function returns -1, the tree is unbalanced
        return check_height(root) != -1