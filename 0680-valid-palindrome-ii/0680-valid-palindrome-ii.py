class Solution:
    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True
        
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s[l+1:r+1]) or self.isPalindrome(s[l:r])                
            else:
                l += 1
                r -= 1
            
        return True
    
    def isPalindrome(self, s):
        return s == s[::-1]