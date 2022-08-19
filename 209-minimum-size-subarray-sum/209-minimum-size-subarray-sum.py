class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        left = 0
        _sum = 0
        for i in range(len(nums)):
            _sum += nums[i]
            while (_sum >= target):
                ans = min(ans, i - left + 1)
                _sum -= nums[left]
                left += 1

        if ans == float('inf'): return 0
        else: return ans
                    
            