class Solution:
    def minCut(self, s: str) -> int:
        self.s = s
        self.memo = {}
        return self.dfs(0, len(s)-1)
    
    def isPalindrome(self, s):
        return s == s[::-1]

    def dfs(self, left, right):
        if left > right:
            return 0
        if self.isPalindrome(self.s[left:right+1]):
            return 0
        if (left, right) in self.memo:
            return self.memo[(left, right)]
        minCuts = right - left
        for i in range(left, right):
            if self.isPalindrome(self.s[left:i+1]):
                minCuts = min(minCuts, 1 + self.dfs(i+1, right))
        self.memo[(left, right)] = minCuts
        return self.memo[(left, right)]

    