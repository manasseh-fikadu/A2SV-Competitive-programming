class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        low, high = 0, len(nums) - 1
        while 1:
            while low < len(nums) and nums[low] != val:
                low += 1
    
            while high >= 0 and nums[high] == val:
                high -= 1
    
            if low >= high:
                break
    
            nums[low], nums[high] = nums[high], nums[low]
        return low