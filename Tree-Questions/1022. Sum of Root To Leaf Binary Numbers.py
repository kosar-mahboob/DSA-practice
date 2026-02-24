# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        Returns the sum of all binary numbers formed by root-to-leaf paths.
        """
        self.total = 0

        def dfs(node: TreeNode, current: int) -> None:
            if not node:
                return
            # Update current number by appending node's bit
            current = (current << 1) | node.val
            # If leaf, add to total
            if not node.left and not node.right:
                self.total += current
            else:
                dfs(node.left, current)
                dfs(node.right, current)

        dfs(root, 0)
        return self.total
