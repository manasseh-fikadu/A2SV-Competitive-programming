class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(n):
            return int(n**0.5)**2 == n

        def dfs(nums, path):
            if not nums:
                self.res += 1
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if path and not is_square(path[-1] + nums[i]):
                    continue
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])

        nums.sort()
        self.res = 0
        dfs(nums, [])
        return self.res