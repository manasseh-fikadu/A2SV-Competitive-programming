# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sums = 0
        def dfs(root, add = False):
            if not root:
                return
            if add:
                self.sums += root.val
                return
            if root.val % 2 == 0:
                if root.left:
                    dfs(root.left.left, add=True)
                    dfs(root.left.right, add=True)        

                if root.right:
                    dfs(root.right.left, add=True)        
                    dfs(root.right.right, add=True)

            dfs(root.left, add = False)
            dfs(root.right, add = False)
        
        dfs(root, add = False)
        
        return self.sums