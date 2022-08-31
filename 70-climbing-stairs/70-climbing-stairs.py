class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i <= 1:
                return 1
            if i in memo:
                return memo[i]
            ans = dfs(i - 1) + dfs(i - 2)
            memo[i] = ans
            return ans
        
        return dfs(n)
            