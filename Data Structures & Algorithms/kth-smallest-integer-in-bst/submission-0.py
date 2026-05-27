# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0      # how many nodes visited so far
        self.result = 0     # stores the kth smallest value

        def dfs(node):
            if not node:
                return

            # 1. Go LEFT first (smaller values)
            dfs(node.left)

            # 2. Visit current node
            self.count += 1
            if self.count == k:         # found the kth smallest!
                self.result = node.val
                return                  # no need to go further

            # 3. Go RIGHT (larger values)
            dfs(node.right)

        dfs(root)
        return self.result




        