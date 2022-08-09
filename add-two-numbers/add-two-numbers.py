# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        carry = 0
        i = 0
        while curr1 or curr2 or carry != 0:
            s = carry
            if curr1:
                s += curr1.val
                curr1 = curr1.next
                
            if curr2:
                s += curr2.val
                curr2 = curr2.next
            
            if s >= 10:
                carry = s // 10
                s = s % 10
            else:
                carry = 0
                
            if i == 0:
                res_head = ListNode(s)
                res_curr = res_head
                i += 1
            else: 
                res_curr.next = ListNode(s)
                res_curr = res_curr.next
                   
        return res_head