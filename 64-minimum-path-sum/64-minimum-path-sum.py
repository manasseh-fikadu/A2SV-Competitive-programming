class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        n = len(grid)
        m = len(grid[0])
        
        def dfs(i,j):
            if i == n or j == m:
                return float("inf")
            if i == n -1 and j == m - 1:
                return grid[i][j]
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            down = grid[i][j] + dfs(i+1,j)
            right = grid[i][j] + dfs(i,j+1)
            ans = min(down, right)
            memo[(i, j)] = ans
            
            return ans
        return dfs(0,0)
    

    