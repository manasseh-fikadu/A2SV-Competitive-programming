class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}   
        def dfs(i):
            if i >= len(cost):
                return 0

            if i in dp:
                return dp[i]

            oneStep = dfs(i + 1) + cost[i]
            twoStep = dfs(i + 2) + cost[i]
            dp[i] = min(oneStep, twoStep)

            return dp[i]

        return min(dfs(0), dfs(1))