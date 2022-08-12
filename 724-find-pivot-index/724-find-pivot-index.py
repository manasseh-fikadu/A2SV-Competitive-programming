class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = 0
        total_sum = sum(nums) 
        
        for i in range(len(nums)): 
            prefix_sum = prefix_sum + nums[i]
            if prefix_sum == (total_sum + nums[i])/2:
                return i
            
        return -1