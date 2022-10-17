class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = {}
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j, dp))
        return res
    
    def dfs(self, matrix, i, j, dp):
        if (i, j) in dp:
            return dp[(i, j)]
        m = len(matrix)
        n = len(matrix[0])
        res = 1
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                res = max(res, 1 + self.dfs(matrix, x, y, dp))
        dp[(i, j)] = res
        return res