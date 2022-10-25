class Solution:
    def longestPrefix(self, s: str) -> str:
        fail = [0]
        for i in range(1, len(s)):
            j = fail[i-1]
            while j > 0 and s[j] != s[i]:
                j = fail[j-1]
            fail.append(j + 1 if s[j] == s[i] else j)
        return s[:fail[-1]]