class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSum = [0] * len(nums)
        for i in range(0, len(nums)):
            prefixSum[i] = nums[i] + prefixSum[i-1]
            
        return prefixSum