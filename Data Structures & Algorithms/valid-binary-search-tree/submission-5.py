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
            node = queue.popleft()

            # node[0] = TreeNode
            # node[1] = lower bound
            # node[2] = upper bound
            if not (node[1] < node[0].val < node[2]):
                return False
            
            if node[0].left:
                queue.append((node[0].left, node[1], node[0].val))
            if node[0].right:
                queue.append((node[0].right, node[0].val, node[2]))
        
        return True
            
            