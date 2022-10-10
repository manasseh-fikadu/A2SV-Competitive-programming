class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        counts = Counter(palindrome)
        n = len(palindrome)
        
        if n <= 1:
            return ""
        
        if 'a' in counts and len(palindrome) - counts['a'] in {0,1}:
            palindrome[-1] = 'b'
            return ''.join(palindrome)
        
        for i in range(n):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return ''.join(palindrome)
            
           