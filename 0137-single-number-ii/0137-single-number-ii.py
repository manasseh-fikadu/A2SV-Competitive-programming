class Solution:
    def singleNumber(self, A: List[int]) -> int:
        ones = 0
        twos = 0
        for i in A:
            ones = (ones ^ i) & ~twos
            twos = (twos ^ i) & ~ones
        return ones