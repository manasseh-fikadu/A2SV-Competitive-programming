class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        max_len = 0
        for i in range(len(nums)):
            if not visited[i]:
                max_len = max(max_len, self.dfs(nums, visited, i))
        return max_len

    def dfs(self, nums, visited, i):
        if visited[i]:
            return 0
        visited[i] = True
        return 1 + self.dfs(nums, visited, nums[i])