"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        
        while q:
            new_level = []
            for node in q:
                new_level += node.children
            res.append([node.val for node in q])
            q = new_level
            
        return res