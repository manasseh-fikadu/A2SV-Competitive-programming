class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = dict()
        count = 0
        
        for i in nums:
            if i in d:
                count += d[i]
                d[i] += 1
            else:
                d[i] = 1
                
        return count