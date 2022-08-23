# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        
        while head:
            stack.append(head.val)
            head = head.next
		
        if stack == stack[::-1]:
            return True
        else:
            return False