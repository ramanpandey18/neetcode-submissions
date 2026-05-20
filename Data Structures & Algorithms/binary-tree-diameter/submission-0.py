# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def calculate_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # 1. Calculate the depth of both subtrees
            left_depth = calculate_depth(node.left)
            right_depth = calculate_depth(node.right)
            
            # 2. The diameter passing through the current node is the 
            #    sum of edges from its left and right maximum depths
            current_diameter = left_depth + right_depth
            
            # 3. Update the global maximum if this path is longer
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # 4. Return the depth of this node to its parent
            return max(left_depth, right_depth) + 1
            
        calculate_depth(root)
        return self.max_diameter