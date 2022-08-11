class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def recurrence(curr, i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            recurrence(curr, i+1)
            
            curr.pop()
            recurrence(curr, i+1)
            
        recurrence([], 0)
        
        return res