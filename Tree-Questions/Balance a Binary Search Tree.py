# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root):
        # Step 1: Inorder traversal to get sorted values
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        sorted_vals = inorder(root)
        
        # Step 2: Build balanced BST from sorted array
        def buildBalancedTree(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = buildBalancedTree(arr[:mid])
            root.right = buildBalancedTree(arr[mid+1:])
            return root
        
        return buildBalancedTree(sorted_vals)
