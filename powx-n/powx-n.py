class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recur(x,n):
            if n==0:
                return 1
            val = self.myPow(x,abs(n)//2)
            if n%2==1:
                return val*val*x
            return val*val
        val = recur(x,n)
        if n<0:
            return 1/val
        return val