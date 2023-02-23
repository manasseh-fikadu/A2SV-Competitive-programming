class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [{} for _ in range(len(nums))]
        res = 0
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                res = max(res, dp[i][diff])
        return res