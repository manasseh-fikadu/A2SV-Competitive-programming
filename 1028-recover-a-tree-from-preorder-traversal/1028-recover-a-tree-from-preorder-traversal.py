# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nums, height = [], [0]
        idx = 0
        
        while idx < len(traversal):
            num = ""
            count = 0
            if traversal[idx] == '-':
                while idx < len(traversal) and traversal[idx] == '-':
                    count += 1
                    idx += 1
                height.append(count)
            else:
                while idx < len(traversal) and traversal[idx] != '-':
                    num += traversal[idx]
                    idx += 1
                nums.append(int(num))
        root = TreeNode(nums[0])
        stack, idx = [[root, 0]], 1
        
        while idx < len(nums) and stack:
            if stack[-1][1] == height[idx] - 1 and stack[-1][0].left is None:
                newNode =  TreeNode(nums[idx])
                stack[-1][0].left = newNode
                stack.append([newNode, height[idx]])
                idx += 1
                
            elif stack[-1][1] == height[idx]-1 and stack[-1][0].right is None:
                newNode =  TreeNode(nums[idx])
                stack[-1][0].right = newNode
                stack.append([newNode, height[idx]])
                idx += 1
            elif stack[-1][1] >= height[idx]:
                stack.pop()
        return root