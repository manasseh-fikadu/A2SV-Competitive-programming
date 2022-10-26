class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])
        ans = 0
        for i in range(len(fib) - 1, -1, -1):
            if k >= fib[i]:
                k -= fib[i]
                ans += 1
        return ans