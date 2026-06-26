# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BST:
            # All values in left subtree < root.val
            # All values in right subtree > root.val
        # For 2 nodes p and q:
            # If both values < root.val => both lie in left subtree
            # If both values > root.val => bot lie in right subtree
            # If one node < root.val < the other node, a split occur. 
                # Each node is in a different subtree, and the LCA is the current node (root)
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else: # one node < root.val < the other node, or root.val == p.val or root.val == q.val
            return root
        
