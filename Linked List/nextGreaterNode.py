# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        
        stack = []
        res = [0] * len(arr)
        
        for i,val in enumerate(arr):
            if stack and arr[stack[-1]] < val:
                while stack and arr[stack[-1]] < val:
                    res[stack[-1]] = val
                    stack.pop()
            stack.append(i)
        return res
