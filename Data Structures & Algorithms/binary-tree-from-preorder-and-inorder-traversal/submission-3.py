# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)
        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        # root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

        # Base case: no nodes to build
        # if not preorder or not inorder:
        #     return None

        # # Step 1: first element of preorder is always the root
        # root_val = preorder[0]
        # root = TreeNode(root_val)

        # # Step 2: find root in inorder → splits left and right subtrees
        # mid = inorder.index(root_val)

        # # Step 3: recurse on left and right subtrees
        # root.left  = self.buildTree(preorder[1 : mid + 1],  # left preorder
        #                             inorder[ : mid])         # left inorder

        # root.right = self.buildTree(preorder[mid + 1 : ],   # right preorder
        #                             inorder[mid + 1 : ])     # right inorder

        # return root


        