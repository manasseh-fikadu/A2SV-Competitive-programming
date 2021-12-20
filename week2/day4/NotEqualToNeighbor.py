class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums) -1):
            pre = nums[i-1]
            current = nums[i]
            next = nums[i+1]
            
            if (pre < current < next) or (pre > current > next):
                nums[i+1], nums[i] = nums[i], nums[i+1]
        return nums
