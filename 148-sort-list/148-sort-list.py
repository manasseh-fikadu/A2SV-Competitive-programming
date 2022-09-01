# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        node = head
        space = []
        while node:
            space.append(node.val)
            node = node.next  
        space.sort()

        dummy = ListNode()
        for i in space[::-1]:
            newNode = ListNode(i)
            newNode.next = dummy.next
            dummy.next = newNode
        return dummy.next
        