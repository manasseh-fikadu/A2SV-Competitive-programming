class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
#         cache = {}
        
#         def findPaths(x, y):
            
#             if (x,y) in cache:
#                 return cache[(x,y)]
            
#             if x == m-1 or y == n-1:
#                 return 1
#             elif x >=m or y>=n:
#                 return 0
#             else:
#                 cache[(x,y)] = findPaths(x+1,y) + findPaths(x, y+1)
#                 return cache[(x,y)]
            
#         return findPaths(0,0)

    
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            dp[i][n-1] = 1
        for j in range(n):
            dp[m-1][j] = 1
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]
            
            
            
            
            
            
            