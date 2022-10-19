# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        i, j = 0, 0
        
        while head:
            matrix[i][j] = head.val
            head = head.next
            next_i, next_j = i + directions[direction][0], j + directions[direction][1]
            if 0 <= next_i < m and 0 <= next_j < n and matrix[next_i][next_j] == -1:
                i, j = next_i, next_j
            else:
                direction = (direction + 1) % 4
                i, j = i + directions[direction][0], j + directions[direction][1]
        return matrix
        
        