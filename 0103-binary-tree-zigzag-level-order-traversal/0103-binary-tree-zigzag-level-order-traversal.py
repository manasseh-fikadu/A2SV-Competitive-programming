# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      res = []
      queue = deque([root])
      flag = 0 #left

      while queue:
        curr = []
        for i in range(len(queue)):
          node = queue.popleft()
          if node:
            curr.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        if curr:
          if flag == 0: res.append(curr)
          elif flag == 1: res.append(curr[::-1])

        if flag == 0: flag = 1
        elif flag == 1: flag = 0

      return res

          
        