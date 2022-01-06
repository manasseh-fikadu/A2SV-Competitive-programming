class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = sum(set(nums))
        non_missing = sum(nums) - res
        missing = sum(range(1,len(nums)+1)) - res
        return [non_missing, missing]
