class Solution:
    def fib(self, n: int) -> int:
        # if n < 2:
        #     return n
        # return self.fib(n-1) + self.fib(n-2) -> Without Memo
        
        memo = { 0: 0, 1: 1 }

        if n not in memo:
            memo[n] = self.fib(n-1) + self.fib(n-2)
        return memo[n]	
		