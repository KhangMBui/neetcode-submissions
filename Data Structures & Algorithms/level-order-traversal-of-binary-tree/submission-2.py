# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # [1, 2, 3, 4, 5, 6, 7]
        # queue: [1]
        # [1] -> [2, 3] -> [3, 4, 5] -> [4, 5, 6, 7]

        queue = collections.deque([root])
        res = []

        while queue:
            level = []
            qLen = len(queue)
            for i in range(qLen):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if level:
                res.append(level)
        return res