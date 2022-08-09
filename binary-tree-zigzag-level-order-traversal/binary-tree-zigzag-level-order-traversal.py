# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        flag = 0
        while q:
            currOrder = []
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if node:
                    currOrder.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if currOrder:
                if flag == 0:
                    res.append(currOrder)
                elif flag == 1:
                    res.append(currOrder[::-1])
            if flag == 0:
                flag = 1
            elif flag == 1:
                flag = 0 
        return res
        