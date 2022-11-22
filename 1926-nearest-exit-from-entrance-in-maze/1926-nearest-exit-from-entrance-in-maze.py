class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        queue = [entrance]
        maze[entrance[0]][entrance[1]] = '+'
        step = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < m and 0 <= y < n and maze[x][y] == '.':
                        if x == 0 or x == m-1 or y == 0 or y == n-1:
                            return step + 1
                        maze[x][y] = '+'
                        queue.append([x, y])
            step += 1
        return -1