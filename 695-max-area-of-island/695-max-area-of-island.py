class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        self.area = 0
        
        def dfs(row, col):
            visited.add((row, col))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            self.area += 1
            for x, y in directions:
                up, down = row + x, col + y
                
                if up in range(n) and down in range(m) and grid[up][down] == 1 and (up, down) not in visited:
                    dfs(up, down)
                    
        max_area = 0            
        if not grid:
            return 
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid[i][j] == 1:
                    self.area = 0
                    dfs(i,j)
                    max_area = max(max_area, self.area)
                    
        return max_area