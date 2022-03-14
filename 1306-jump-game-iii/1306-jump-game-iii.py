class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        visited = {start}
        
        while q:
            start = q.popleft()
            
            if arr[start] == 0:
                return True 
            
            plus = start + arr[start]
            minus = start - arr[start]
            
            if plus < len(arr) and plus not in visited:
                visited.add(plus)
                q.append(plus)
            if minus >= 0 and minus not in visited:
                visited.add(minus)
                q.append(minus)
            
        return False