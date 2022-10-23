class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        for idx, num in enumerate(nums):
            tmp = num
            for i in range(idx, len(nums)):
                tmp = gcd(tmp, nums[i])
                if tmp == k:
                    ans += 1
                elif tmp < k:
                    break
        return ans