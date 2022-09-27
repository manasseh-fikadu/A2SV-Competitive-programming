class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dfs(i, _sum):
            if i == len(nums):
                return int(_sum == target)
            
            if (i, _sum) in memo:
                return memo[(i, _sum)]
            
            add = dfs(i + 1, _sum + nums[i])
            sub = dfs(i + 1, _sum - nums[i])
            memo[(i, _sum)] = add + sub
            return memo[(i, _sum)]
        
        return dfs(0, 0)            