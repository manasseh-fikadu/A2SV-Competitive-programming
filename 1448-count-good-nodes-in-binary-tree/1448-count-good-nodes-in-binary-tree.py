# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        _max = root.val
        count = 0
        def dfs(node, _max):
            nonlocal count
            if not node:
                return
            if node:
                if node.val >= _max:
                    _max = node.val
                    count += 1
            dfs(node.left, _max)
            dfs(node.right, _max)
        dfs(root, root.val)
        return count