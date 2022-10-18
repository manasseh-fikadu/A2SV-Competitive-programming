class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        result = []
        answer = self.dfs(s, 0, path, result)
        return answer
        
    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def dfs(self, s, start, path, result):
        if start == len(s):
            result.append(path)
            return
        for i in range(start, len(s)):
            if self.isPalindrome(s, start, i):
                self.dfs(s, i+1, path+[s[start:i+1]], result)
        return result