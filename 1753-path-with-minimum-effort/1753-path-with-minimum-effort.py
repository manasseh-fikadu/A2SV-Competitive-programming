class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        _max = max(max(row) for row in heights)
        _min = min(min(row) for row in heights)
        diff = _max - _min

        def bfs(mid):
            queue = deque([(0, 0)])
            visited = set((0, 0))

            while queue:
                x, y = queue.popleft()

                if (x, y) == (m - 1, n - 1):
                    return True

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0<=nx<m and 0<=ny<n and (nx, ny) not in visited and abs(heights[x][y] - heights[nx][ny]) <= mid:
                        queue.append((nx, ny))
                        visited.add((nx, ny))

            return False


        low, high = 0, diff

        while low < high:
            mid = low + (high - low) // 2
            if bfs(mid):
                high = mid
            else:
                low = mid + 1

        return low