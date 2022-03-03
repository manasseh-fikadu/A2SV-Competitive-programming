class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
 
        stones = [-1*i for i in stones]
		
        heapify(stones)
        
        while len(stones) > 1:
            diff = heappop(stones) - heappop(stones)
            heappush(stones, diff)
        
        return -heappop(stones)