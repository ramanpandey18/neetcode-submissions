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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) {
            return false;
        }
        if (isSameTree(root, subRoot)) {
            return true;
        }
        if (isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)) {
            return true;
        }
        return false;
    }

    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }
        if (p == null || q == null) {
            return false;
        }
        if (p.val != q.val) {
            return false;
        }
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
// def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
//         if not root:
//             return False
//         if self.is_same_tree(root, subRoot):
//             return True
//         if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
//             return True
        
    
//     def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
//         if not p and not q:
//             return True
//         if not p or not q:
//             return False
//         if p.val != q.val:
//             return False
//         return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)