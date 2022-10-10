# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self._sum = 0
        
        def helper(node):
            if not node:
                return None

            else:
                helper(node.right)

                self._sum += node.val
                node.val = self._sum

                helper(node.left)

                return node
            
        self._sum = 0
                        
        return helper(root)

            
            
            