class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def findIslands(i, j, grid, island):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                return
            grid[i][j] = 2
            island.append((i, j))
            findIslands(i + 1, j, grid, island)
            findIslands(i - 1, j, grid, island)
            findIslands(i, j + 1, grid, island)
            findIslands(i, j - 1, grid, island)
        
        def bfs(grid, island):
            queue = deque(island)
            step = 0
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                            continue
                        if grid[x][y] == 1:
                            return step
                        if grid[x][y] == 0:
                            grid[x][y] = 2
                            queue.append((x, y))
                step += 1
            return -1
        
        island = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    findIslands(i, j, grid, island)
                    return bfs(grid, island)