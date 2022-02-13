class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        prev = -1
        nums.sort()
        res = 0
        for num in nums:
            if num > prev:
                prev = num
            else:
                res += (prev + 1) - num
                prev = prev + 1
        return res
