class Solution:
    def tribonacci(self, n: int) -> int:
        f = [0] * 40
        f[0], f[1], f[2] = 0, 1, 1

        for i in range(n):
            f[i+3] = f[i] + f[i+1] + f[i+2]
            
        return f[n]