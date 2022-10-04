class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)
        print(prefix)
        count = Counter()
        
        ans = 0
        for x in prefix:
            ans += count[x]
            count[x + goal] += 1
            
        return ans
            
        
        