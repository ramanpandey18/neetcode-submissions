# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            good = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            good += dfs(node.left, new_max)
            good += dfs(node.right, new_max)

            return good
        return dfs(root, root.val)





















        def dfs(node, max_so_far):
            if not node:
                return 0                        # base case: null node

            # Is this node good?
            good = 1 if node.val >= max_so_far else 0

            # Update max for the path going downward
            new_max = max(max_so_far, node.val)

            # Recurse on both children, accumulate count
            good += dfs(node.left,  new_max)
            good += dfs(node.right, new_max)

            return good

        return dfs(root, root.val) 