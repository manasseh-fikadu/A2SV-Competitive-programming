class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices) == 0:
        #     return len(prices)
        dp = [0] * len(prices)
        res = 0
        for i in range(0,len(prices)-1):
            dp[i] = prices[i+1] - prices[i]
            res = max(dp[i]+res, res)
        return res