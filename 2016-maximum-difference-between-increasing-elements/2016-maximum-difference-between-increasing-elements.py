class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1
        min_num = nums[0]
        max_diff = -1
        for i in range(1, len(nums)):
            if nums[i] > min_num:
                max_diff = max(max_diff, nums[i] - min_num)
            else:
                min_num = nums[i]
        return max_diff
        