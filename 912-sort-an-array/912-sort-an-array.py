class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        m = min(nums)
        M = max(nums)
        res = []
        
        for n in range(m, M+1):
            res.extend([n] * counts[n])
        return res
            
        