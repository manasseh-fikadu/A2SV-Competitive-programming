class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left = -1
        _min = _max = -1
        res = 0

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                left = i
            if nums[i]==minK:
                _min = i
            if nums[i]==maxK:
                _max = i
            
            if _min >= 0 and _max >= 0:
                res += max(0, min(_min, _max) - left)
            
        return res 