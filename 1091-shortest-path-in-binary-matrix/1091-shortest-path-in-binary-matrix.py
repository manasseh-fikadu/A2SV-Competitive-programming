class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        if len(grid) == 1:
            return 1
        queue = [(0, 0, 1)]
        while queue:
            x, y, d = queue.pop(0)
            if x == len(grid) - 1 and y == len(grid) - 1:
                return d
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if (0 <= x + i < len(grid) and 
                        0 <= y + j < len(grid) and 
                        grid[x + i][y + j] == 0):
                        grid[x + i][y + j] = 1
                        queue.append((x + i, y + j, d + 1))
        return -1