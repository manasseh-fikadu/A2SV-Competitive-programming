class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = [] 
        for key, val in counts.items():
            heappush(heap, (-val, key))
        
        ans = []
        for i in range(k):
            res = heappop(heap)
            ans.append(res[1])
        return ans