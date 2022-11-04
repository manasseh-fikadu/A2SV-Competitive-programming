class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # ax+by=1 has solution x, y if gcd(a,b) = 1 - Bézout's lemma
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        return reduce(gcd, nums) == 1
        