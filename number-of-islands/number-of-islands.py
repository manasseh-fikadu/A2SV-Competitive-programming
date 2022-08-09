class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        count = 0
        visited = set()
        
        def dfs(row, col):
            visited.add((row, col))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            
            for x, y in directions:
                up, down = row + x, col + y
                
                if up in range(n) and down in range(m) and grid[up][down] == "1" and (up, down) not in visited:
                    dfs(up, down)
                    
        if not grid:
            return 
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        return count
    
    