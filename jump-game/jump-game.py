class Solution:
    def canJump(self, nums: List[int]) -> bool:
        _max = 0
        
        for i, num in enumerate(nums):
            if i > _max:
                return False
            _max = max(_max, i + num)
        return True