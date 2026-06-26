# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Key idea: goes down the tree path, each time subtracting current node's val
        # When reach leaf node, if we have 0 remaining, that means it adds up to targetSum
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val
        
        remaining = targetSum - root.val

        return (
            self.hasPathSum(root.left, remaining) or
            self.hasPathSum(root.right, remaining)
        )