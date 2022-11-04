class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] % p == 0 else -1
        s = sum(nums)
        if s % p == 0:
            return 0
        s = s % p
        d = {0: -1}
        cur = 0
        res = n
        for i in range(n):
            cur = (cur + nums[i]) % p
            d[cur] = i
            if (cur - s) % p in d:
                res = min(res, i - d[(cur - s) % p])
        return res if res < n else -1