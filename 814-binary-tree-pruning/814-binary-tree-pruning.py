# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(node):
            if not node:
                return False
            leftChild, rightChild = helper(node.left), helper(node.right)
            
            if not leftChild: node.left = None
            if not rightChild: node.right = None
            
            return node.val == 1 or leftChild or rightChild
        
        return root if helper(root) else None