class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        dx = 0
        dy = 1
        for i in instructions:
            if i == 'G':
                x += dx
                y += dy
            elif i == 'L':
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
        return (x == 0 and y == 0) or (dx, dy) != (0, 1)