class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        d = {0: 1}
        len_ = len(nums)
        acc = 0        
        for i in range(len_):
            acc += nums[i]       
            key = acc % k
            
            if key in d:
                ans += d[key]
                d[key] += 1
            else:
                d[key] = 1
            
        return ans