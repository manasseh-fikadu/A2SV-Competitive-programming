class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for _ in range(32):
            if n % 2 == 1: 
                n = n // 2
                count += 1
            else:
                n = n // 2
                continue
                
        return count