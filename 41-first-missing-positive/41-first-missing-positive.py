class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):
            ind = abs(nums[i])

            if ind > n or ind == 0:
                continue

            ind = ind - 1

            if nums[ind] > 0:
                nums[ind] = -(nums[ind])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
