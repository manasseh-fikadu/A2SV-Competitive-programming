class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
                    self.dfs(grid, i, j)
        
        return sum([sum(row) for row in grid])

    def dfs(self, grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return
            grid[i][j] = 0
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i, j + 1)
            self.dfs(grid, i, j - 1)