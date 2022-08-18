class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0
        
        for num in nums:
            if num-1 in numSet:
                continue
            seq = 0   
            while num in numSet:
                num += 1
                seq += 1
                length = max(length, seq)
                
        return length
                