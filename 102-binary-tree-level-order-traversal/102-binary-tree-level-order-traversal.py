# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        if not root: return []
        
        res = []
        q = deque([root])
        
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    temp.append(node.val)
            
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if temp:
                res.append(temp)
                
                
        return res
    
        
#         while q :
#             l = len(q)
#             lvl = []
#             for i in range(l):
#                 node = q.popleft()
#                 if node:
#                     lvl.append(node.val)
#                     q.append(node.left)
#                     q.append(node.right)
#             if lvl:
#                 ans.append(lvl)
#         return ans
                
            