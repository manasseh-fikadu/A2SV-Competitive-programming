# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        self.dfs(root)
        return self.max_length

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        if root.left and root.left.val == root.val:
            left += 1
        else: left = 0
            
        if root.right and root.right.val == root.val:
            right += 1
        else: right = 0
            
        self.max_length = max(self.max_length, left + right)
        return max(left, right)