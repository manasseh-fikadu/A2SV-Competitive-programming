# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node, level):
            if node:  
                if level + 1 == depth:
      
                    Leftnode = node.left
                    newnode = TreeNode(val)
                    node.left = newnode
                    newnode.left = Leftnode
                    
                    Rightnode = node.right
                    newnode = TreeNode(val)
                    node.right = newnode
                    newnode.right = Rightnode
                        
                dfs(node.left,  level+1)
                dfs(node.right, level+1)

        if depth == 1:
            newnode = TreeNode(val)
            newnode.left = root
            return newnode
            
        dfs(root, 1)
        return root