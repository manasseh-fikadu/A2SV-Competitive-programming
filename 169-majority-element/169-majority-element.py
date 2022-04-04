class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        val = 0
        for i in range(len(nums)):
            if count == 0:
                val = nums[i]
            if val == nums[i]:
                count += 1
            else:
                count -= 1
   
        return val