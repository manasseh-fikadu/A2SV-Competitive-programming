"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root != None:
            level = [root]
            
            while len(level) > 0:
                i = 0
                while i < len(level)-1:
                    level[i].next = level[i+1]
                    i += 1
                childNodes = []
                
                for node in level:
                    childNodes.extend([node.left, node.right])
                level = [node for node in childNodes if node != None]
                
        return root
        