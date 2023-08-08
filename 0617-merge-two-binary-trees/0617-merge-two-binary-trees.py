# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merger(root1, root2):
            if not root1 and not root2:
                return None
            elif not root1:
                new_node = TreeNode(root2.val)
                new_node.left = merger(None, root2.left)
                new_node.right = merger(None, root2.right)
                return new_node
            elif not root2:
                new_node = TreeNode(root1.val)
                new_node.left = merger(root1.left, None)
                new_node.right = merger(root1.right, None)
                return new_node
            else:
                new_node = TreeNode(root1.val + root2.val)
                new_node.left = merger(root1.left, root2.left)
                new_node.right = merger(root1.right, root2.right)
                return new_node
        
        return merger(root1, root2)
