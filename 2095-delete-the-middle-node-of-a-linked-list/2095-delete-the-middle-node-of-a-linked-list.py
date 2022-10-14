# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        if not head.next.next:
            head.next = None
            return head
        middle = self.findMiddle(head)
        middle.val = middle.next.val
        middle.next = middle.next.next
        return head
    
    def findMiddle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
            