# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node, num):
            if node is None:
                return 0
            
            num = num * 10 + node.val
            
            if node.left == None and node.right == None:
                return num
            
            return helper(node.left, num) + helper(node.right, num)
        
        return helper(root, 0)