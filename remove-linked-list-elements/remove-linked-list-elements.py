# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''
        [1,2,6,3,4,5,6], 6
        '''
        if not head: return head
        curr = head
        prev = None
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        if head.val == val:
            head = head.next
            
        return head 
    
    '''
        while curr.next:
            if curr.next.val==val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        if head.val==val:
            head=head.next
        
        return head
    '''