class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        if k >= m + n - 3:
            return m + n - 2
        q = [(0, 0, 0, 0)]
        visited = set()
        while q:
            steps, i, j, obs = heapq.heappop(q)
            if (i, j, obs) in visited:
                continue
            visited.add((i, j, obs))
            if i == m - 1 and j == n - 1:
                return steps
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == 1:
                        if obs < k:
                            heapq.heappush(q, (steps + 1, ni, nj, obs + 1))
                    else:
                        heapq.heappush(q, (steps + 1, ni, nj, obs))
        return -1