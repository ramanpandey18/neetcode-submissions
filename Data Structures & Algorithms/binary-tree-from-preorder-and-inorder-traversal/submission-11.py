# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {value: i for i, value in enumerate(inorder)}
        preorder_index = 0
        def dfs(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            root_val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_val)
            mid = inorder_map[root_val]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1 , right)
            return root
        return dfs(0, len(inorder) - 1)

        
        # value -> index in inorder
        inorder_map = {value: i for i, value in enumerate(inorder)}
        preorder_index = 0
        def dfs(left, right):
            nonlocal preorder_index
            # No nodes in this range
            if left > right:
                return None
            # First element in preorder is the root
            root_val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_val)
            # Find root position in inorder in O(1)
            mid = inorder_map[root_val]

            # Everything before root belongs to left subtree
            root.left = dfs(left, mid - 1)

            # Everything after root belongs to right subtree
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)

        # if not preorder or not inorder:
        #     return None
        # root_val = preorder[0]
        # root = TreeNode(root_val)
        # mid = inorder.index(root_val)
        # root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return root

