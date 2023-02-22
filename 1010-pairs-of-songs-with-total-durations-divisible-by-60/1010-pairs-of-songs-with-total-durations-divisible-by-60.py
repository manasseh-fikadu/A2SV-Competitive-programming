class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder_dict = {}
        total = 0
        
        for t in time:
            if t % 60 == 0:
                total += remainder_dict.get(0, 0)
            else:
                total += remainder_dict.get(60 - t % 60, 0)
            remainder_dict[t % 60] = remainder_dict.get(t % 60, 0) + 1
        
        return total