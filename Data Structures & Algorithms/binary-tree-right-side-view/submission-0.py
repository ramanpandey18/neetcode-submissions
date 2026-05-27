# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return []           # ✅ always return list, never None

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)     # snapshot current level size

            for i in range(level_size):
                node = queue.popleft()

                # ✅ Only add to result if it's the LAST node in this level
                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result