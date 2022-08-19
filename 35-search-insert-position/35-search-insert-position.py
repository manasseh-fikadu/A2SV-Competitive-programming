class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (r+l) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid +1
                
        return l