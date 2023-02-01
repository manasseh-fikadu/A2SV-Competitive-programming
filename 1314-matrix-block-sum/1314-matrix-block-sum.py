class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = mat[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

        res = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                r1 = max(0, i-k)
                c1 = max(0, j-k)
                r2 = min(m-1, i+k)
                c2 = min(n-1, j+k)
                res[i][j] = dp[r2+1][c2+1] - dp[r1][c2+1] - dp[r2+1][c1] + dp[r1][c1]

        return res