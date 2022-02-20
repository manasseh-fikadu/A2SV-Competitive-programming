# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        sums = []
        while head:
            stack.append(head.val)
            head = head.next
        left = 0
        right = len(stack) - 1 
        while left < right:
            sums.append(stack[left] + stack[right])
            left += 1
            right -= 1
        return max(sums)
