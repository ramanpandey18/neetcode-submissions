/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);
        return Math.max(leftDepth, rightDepth) + 1;
    }
}
        // if not root:
        //     return 0
        // left_depth = self.maxDepth(root.left)
        // right_depth = self.maxDepth(root.right)
        // return max(left_depth, right_depth) + 1
        
        // # if not root:
        // #     return 0
        // # depth = 0
        // # queue = deque([root])
        // # while queue:
        // #     level_size = len(queue)
        // #     for _ in range(level_size):
        // #         node = queue.popleft()
        // #         if node.left:
        // #             queue.append(node.left)
        // #         if node.right:
        // #             queue.append(node.right)
        // #     depth += 1
        // # return depth