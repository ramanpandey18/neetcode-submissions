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
    public int diameterOfBinaryTree(TreeNode root) {
        int[] maxDiameter = new int[1]; // Using an array to pass by reference
        calculateDepth(root, maxDiameter);
        return maxDiameter[0];
    }

    private int calculateDepth(TreeNode node, int[] maxDiameter) {
        if (node == null) {
            return 0;
        }
        
        int leftDepth = calculateDepth(node.left, maxDiameter);
        int rightDepth = calculateDepth(node.right, maxDiameter);
        
        maxDiameter[0] = Math.max(maxDiameter[0], leftDepth + rightDepth);
        
        return Math.max(leftDepth, rightDepth) + 1;
    }
}
