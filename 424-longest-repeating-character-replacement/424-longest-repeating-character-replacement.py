class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0
        
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            
            if (i - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, i - left + 1)
            
        return res