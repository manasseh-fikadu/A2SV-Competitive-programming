class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        if len(nums) == 2 and nums[0] != nums[1]: return 2

        positive, negative = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                positive = negative + 1
            elif nums[i] < nums[i-1]:
                negative = positive + 1

        return max(positive, negative)

        