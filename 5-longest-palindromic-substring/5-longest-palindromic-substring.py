class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(l, r):
            nonlocal res
            nonlocal resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
                
        res = ""
        resLen = 0

        for i in range(len(s)):
            #odd
            l, r = i, i
            helper(l, r)
            #even
            l, r = i, i+1
            helper(l, r)
            
        return res

        
        
        
        