# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        savedA, savedB = headA, headB
        
        while savedA != savedB:
            savedA = savedA.next if savedA else headB
            savedB = savedB.next if savedB else headA
                
        return savedA