class Solution:
    def grayCode(self, n: int) -> List[int]:
        #backtracking solution
        # if n == 1:
        #     return [0, 1]
        # else:
        #     prev = self.grayCode(n-1)
        #     return prev + [x + 2**(n-1) for x in prev[::-1]]
        
        #bit manipulation solution
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        prev = self.grayCode(n - 1)
        return [x << 1 for x in prev] + [x << 1 | 1 for x in prev[::-1]]