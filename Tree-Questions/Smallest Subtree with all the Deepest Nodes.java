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
    public TreeNode subtreeWithAllDeepest(TreeNode root) {
        return deep(root).getValue();
    }
    
    // Returns a pair: (depth of this subtree, LCA of deepest nodes in this subtree)
    private Pair<Integer, TreeNode> deep(TreeNode root) {
        if (root == null) return new Pair<>(0, null);
        
        Pair<Integer, TreeNode> left = deep(root.left);
        Pair<Integer, TreeNode> right = deep(root.right);
        
        int leftDepth = left.getKey();
        int rightDepth = right.getKey();
        
        if (leftDepth == rightDepth) {
            return new Pair<>(leftDepth + 1, root);
        } else if (leftDepth > rightDepth) {
            return new Pair<>(leftDepth + 1, left.getValue());
        } else {
            return new Pair<>(rightDepth + 1, right.getValue());
        }
    }
}
