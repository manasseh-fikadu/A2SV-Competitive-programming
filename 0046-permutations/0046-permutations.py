class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        target = (1 << n) - 1
        res = []
        intermediate = []
        
        def helper(mask):
            nonlocal res, intermediate
            if target == mask:
                res.append(list(intermediate))
                return
            for i in range(n):
                if (mask & (1 << i)) == 0:
                    intermediate.append(nums[i])
                    helper(mask | (1 << i))
                    intermediate.pop()
                    
        helper(0)
        return res
        
