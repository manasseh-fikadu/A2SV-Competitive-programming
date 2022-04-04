class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = deque()
        visited = [[False]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j,0))
                    visited[i][j] = True

        maxDist = 0

        while queue:
            l = len(queue)
            for _ in range(l):
                r,c,d = queue.popleft()
                maxDist = max(maxDist, d)

                for x,y in directions:
                    row = r + x
                    col = c + y

                    if 0 <= row < m and 0 <= col < n and not visited[row][col]:
                        visited[row][col] = True
                        queue.append((row,col,d+1))

        return maxDist if maxDist != 0 else -1