# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        visited = set()
        
        if not head: return False
        
        while True:
            if temp.next == None:
                return False
            if temp in visited:
                return True
            if temp not in visited:
                visited.add(temp)
            
            temp = temp.next
