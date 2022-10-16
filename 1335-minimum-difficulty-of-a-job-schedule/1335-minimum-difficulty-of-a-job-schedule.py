class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d: return -1
        dp = [[0] * n for _ in range(d)]
        dp[0][0] = jobDifficulty[0]
        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1], jobDifficulty[i])
        for i in range(1, d):
            for j in range(i, n):
                dp[i][j] = float('inf')
                maxd = 0
                for k in range(j, i - 1, -1):
                    maxd = max(maxd, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], dp[i - 1][k - 1] + maxd)
        return dp[d - 1][n - 1]
