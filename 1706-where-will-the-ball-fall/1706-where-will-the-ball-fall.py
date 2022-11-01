class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        res = []
        for i in range(n):
            x = i
            for j in range(m):
                if grid[j][x] == 1:
                    if x == n-1 or grid[j][x+1] == -1:
                        res.append(-1)
                        break
                    else:
                        x += 1
                else:
                    if x == 0 or grid[j][x-1] == 1:
                        res.append(-1)
                        break
                    else:
                        x -= 1
            else:
                res.append(x)
        return res