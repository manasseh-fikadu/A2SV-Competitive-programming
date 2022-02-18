class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            maxSum = nums[:]
            maxSum[1] = max(maxSum[0], maxSum[1])

            for i in range(2,len(nums)):
                maxSum[i] = max(maxSum[i-1], maxSum[i-2] + nums[i])
                
        return maxSum[-1]
