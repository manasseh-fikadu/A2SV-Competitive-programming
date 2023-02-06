class Solution:
    def racecar(self, target: int) -> int:  
        q = [(0, 1)]
        steps = 0
        
        while q:
            num = len(q)
            for i in range(num):
                position, speed = q.pop(0)
                if position == target:
                    return steps
                q.append((position+speed, speed*2))
                rev_speed = -1 if speed > 0 else 1
                if (position + speed) < target and speed < 0 or (position+speed) > target and speed > 0:
                    q.append((position, rev_speed))
            steps += 1