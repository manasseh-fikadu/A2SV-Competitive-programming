class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumCalc(n):
            _sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                _sum += digit ** 2
            return _sum
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sumCalc(n)
            
        return n == 1
            
        
