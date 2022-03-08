# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.val = 0
        
        def dfs(node):
            if not node:
                return 0
            runningSumL = dfs(node.left)
            runningSumR = dfs(node.right)
            self.val += abs(runningSumL - runningSumR)
            return node.val + runningSumL + runningSumR
        
        dfs(root)
        
        return self.val