class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(N) space solution
#         _set = set(nums)
#         n = max(nums)
        
#         for i in range(n):
#             if i not in _set:
#                 return i
            
#         return n + 1

        # O(1) space solution
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res
        