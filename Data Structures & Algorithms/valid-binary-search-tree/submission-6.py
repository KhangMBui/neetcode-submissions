# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Store (node, leftBound, rightBound) in a queue
        # node must be larger than leftBound and smaller than rightBound
        # The root node has leftBound = float("-inf") and rightBound = float("inf")
        if not root:
            return True
        queue = collections.deque([ (root, float('-inf'), float('inf')) ])

        while queue:
            node, left_val, right_val = queue.popleft()

            if not (left_val < node.val< right_val):
                return False
            
            if node.left:
                queue.append((node.left, left_val, node.val))
            if node.right:
                queue.append((node.right, node.val, right_val))
        
        return True
            
            