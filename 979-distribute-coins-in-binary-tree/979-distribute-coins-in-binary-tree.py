# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.move = 0
        def distribute(node):
            if not node:
                return 0
            l = distribute(node.left)
            r = distribute(node.right)
            ans = l + r + node.val -1
            self.move += abs(l) + abs(r)
            return ans
        
        distribute(root)
        return self.move