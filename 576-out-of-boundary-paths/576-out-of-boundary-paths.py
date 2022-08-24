class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        def dfs(r, c, M):
            if (r, c, M) in memo: return memo[(r, c, M)]
            if r < 0 or c < 0 or r >= m or c >= n: return 1
            if M == 0: return 0
            
            DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            ans = 0
            for x, y in DIR:
                ans += dfs(r + x, c + y, M - 1)
            memo[(r, c, M)] = ans
            return ans
        return dfs(startRow, startColumn, maxMove) % (10**9+7)