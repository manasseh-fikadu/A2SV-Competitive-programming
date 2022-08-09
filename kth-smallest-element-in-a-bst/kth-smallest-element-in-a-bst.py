# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None

        answer = []
        heapq.heapify(answer)
        
        def helper(node):
            if node:
                heapq.heappush(answer, node.val)
                helper(node.left)
                helper(node.right)
        helper(root)
        
        return heapq.nsmallest(k, answer)[-1]