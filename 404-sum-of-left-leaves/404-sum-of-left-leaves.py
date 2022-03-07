# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def recur(root):
            if not root:
                return
            if root.left is not None and root.left.left is None and root.left.right is None:
                self.sum = self.sum+root.left.val
            
            recur(root.left)
            recur(root.right)
        recur(root)
        return self.sum