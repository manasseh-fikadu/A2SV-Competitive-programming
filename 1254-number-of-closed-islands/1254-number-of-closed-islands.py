class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        for i in range(len(grid)):
            self.dfs(i, 0)
            self.dfs(i, len(grid[0]) - 1)
        for j in range(len(grid[0])):
            self.dfs(0, j)
            self.dfs(len(grid) - 1, j)
        count = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 0:
                    self.dfs(i, j)
                    count += 1
        return count

    def dfs(self, i, j):
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]) or self.grid[i][j] == 1:
            return
        self.grid[i][j] = 1
        self.dfs(i + 1, j)
        self.dfs(i - 1, j)
        self.dfs(i, j + 1)
        self.dfs(i, j - 1)



        