class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _set = set(nums)
        n = max(nums)
        
        for i in range(n):
            if i not in _set:
                return i
            
        return n + 1