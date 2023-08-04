# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst_helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not is_valid_bst_helper(node.left, lower, val):
                return False
            if not is_valid_bst_helper(node.right, val, upper):
                return False

            return True

        return is_valid_bst_helper(root)