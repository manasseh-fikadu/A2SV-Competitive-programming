class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])
        keys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                if grid[i][j] in 'abcdef':
                    keys += 1
        queue = [(start, 0, 0)]
        visited = set()
        while queue:
            (i, j), steps, k = queue.pop(0)
            if (i, j, k) in visited:
                continue
            visited.add((i, j, k))
            if k == (1 << keys) - 1:
                return steps
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == '#':
                        continue
                    if grid[x][y] in 'abcdef':
                        queue.append(((x, y), steps+1, k | (1 << (ord(grid[x][y]) - ord('a')))))
                    elif grid[x][y] in 'ABCDEF':
                        if k & (1 << (ord(grid[x][y]) - ord('A'))):
                            queue.append(((x, y), steps+1, k))
                    else:
                        queue.append(((x, y), steps+1, k))
        return -1