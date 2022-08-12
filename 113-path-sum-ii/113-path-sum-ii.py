# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        
        def dfs(node, path, _sum):                    
            _sum += node.val
            temp = path + [node.val]

            if node.left:
                dfs(node.left, temp, _sum)
            if node.right:
                dfs(node.right, temp, _sum) 

            if not node.left and not node.right and _sum == targetSum:
                self.ans.append(temp)
                
        if not root: return []

        dfs(root, [], 0)
        
        return self.ans                   