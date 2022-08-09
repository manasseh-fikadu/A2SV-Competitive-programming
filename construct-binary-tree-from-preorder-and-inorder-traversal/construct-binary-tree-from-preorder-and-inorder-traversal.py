# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def helper(left, right):
            nonlocal preIdx
            if left > right: return None

            rootVal = preorder[preIdx]
            root = TreeNode(rootVal)

            preIdx += 1

            root.left = helper(left, inorder_map[rootVal] - 1)
            root.right = helper(inorder_map[rootVal] + 1, right)

            return root

        preIdx = 0

        inorder_map = {}
        for i, value in enumerate(inorder):
            inorder_map[value] = i

        return helper(0, len(preorder) - 1)