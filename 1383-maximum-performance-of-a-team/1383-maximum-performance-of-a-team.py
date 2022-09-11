class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        ans = speedSum = 0
        heap = []

        for engineer in sorted(zip(efficiency, speed), reverse = True):                
            eff, spd = engineer
			
            speedSum += spd
            ans = max(ans, speedSum  * eff)
            heappush(heap, spd)
            
            while len(heap) > k - 1:
                speedSum -= heappop(heap)
            
        return ans % MOD
        