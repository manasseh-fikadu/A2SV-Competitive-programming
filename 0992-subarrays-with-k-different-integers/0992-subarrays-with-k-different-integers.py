class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    def atMostK(self, nums, k):
        count = Counter()
        i = 0
        res = 0
        for j, num in enumerate(nums):
            if count[num] == 0:
                k -= 1
            count[num] += 1
            while k < 0:
                count[nums[i]] -= 1
                if count[nums[i]] == 0:
                    k += 1
                i += 1
            res += j - i + 1
        return res