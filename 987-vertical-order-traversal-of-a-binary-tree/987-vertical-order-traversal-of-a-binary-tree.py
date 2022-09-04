# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        _map = defaultdict(list)
        
        def dfs(node, x, y):
            if not node: return
            
            _map[x].append((-y, node.val))
            dfs(node.left, x - 1, y - 1)
            dfs(node.right, x + 1, y - 1)
            
        dfs(root, 0, 0)
        res = []
        
        _list = sorted(_map.keys())
        for key in _list:
            _map[key].sort()
            res.append([val for _, val in _map[key]])
            
        return res
    