class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Preprocess needle
        fail = [0]
        for i in range(1, len(needle)):
            j = fail[i-1]
            while j > 0 and needle[j] != needle[i]:
                j = fail[j-1]
            fail.append(j + 1 if needle[j] == needle[i] else j)
        # Find needle in haystack
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = fail[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - (j - 1)
        return -1
            
        