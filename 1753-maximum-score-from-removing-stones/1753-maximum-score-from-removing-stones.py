class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        l1 = []        
        
        heappush(l1, -1*a)
        heappush(l1, -1*b)
        heappush(l1, -1*c)
        
        score = 0
        while True:            
            ans1 = heappop(l1)
            ans2 = heappop(l1)
            
            if ans1 == 0 or ans2 == 0:
                return score
            
            sub = abs(ans1) - 1
            sub1 = abs(ans2) - 1
            
            heappush(l1, -1*sub)
            heappush(l1, -1*sub1)
            
            score += 1            