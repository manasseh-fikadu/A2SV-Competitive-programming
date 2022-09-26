class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def recurse(i, memo = {}):
            if i in memo:
                return memo[i]
            
            if i >= len(nums):
                return 0
              
            num = nums[i]
            nextIndex = i + 1
            
            if nextIndex < len(nums) and nums[nextIndex] == num + 1:
                nextIndex += 1
            
            memo[i] = max(num * countsMap[num] + recurse(nextIndex, memo), recurse(i + 1, memo))
            return memo[i]
        
        countsMap = Counter(nums) 
        nums = (list(set(nums))) 
        
        return recurse(0)
        