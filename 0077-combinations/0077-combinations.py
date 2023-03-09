class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        nums = [i+1 for i in range(n)]
        ans = []
        
        def solve(i, path):
            if len(path) == k:
                ans.append(path[:])
                return
            
            if i >= len(nums):
                return
            
            path.append(nums[i])
            solve(i+1, path)
            path.pop()
            
            solve(i+1, path)
        
        solve(0, [])
        
        return ans