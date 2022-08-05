class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dp(i, s):
            if s == target:
                return 1
            if i == len(nums) or s > target:
                return 0
            
            key = (i, s)
            if key in memo:
                return memo[key]
            
            option1 = dp(i+1, s)
            option2 = dp(0, s + nums[i])
            memo[key] = option1 + option2
            return memo[key]
        
        return dp(0, 0)