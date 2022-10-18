class Solution:
    def spiralMatrixIII(self, R: int, C: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [(rStart, cStart)]
        
        if R * C == 1:
            return ans

        for k in range(1, 2*(R+C), 2):

            # dk represents walk length
            for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k+1), (-1, 0, k+1)):

                for _ in range(dk):
                    rStart += dr
                    cStart += dc

                    if 0 <= rStart < R and 0 <= cStart < C:
                        ans.append((rStart, cStart))
                        if len(ans) == R * C:
                            return ans
        
        