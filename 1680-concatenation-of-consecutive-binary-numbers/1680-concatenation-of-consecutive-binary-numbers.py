class Solution:
    def concatenatedBinary(self, n: int) -> int:
        if n == 1: return 1
        MOD = 10**9 + 7
        _str = ""
        
        for i in range(1, n + 1):
            curr = bin(i)
            _str += str(curr[2:])
        ans = int(_str, base = 2)
        
        return ans % MOD