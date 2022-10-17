class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False for _ in range(n)] for _ in range(n)]
        visited[0][0] = True
        q = [(grid[0][0], 0, 0)]
        res = 0
        while q:
            t, x, y = heapq.heappop(q)
            res = max(res, t)
            if x == y == n - 1:
                return res
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(q, (grid[nx][ny], nx, ny))