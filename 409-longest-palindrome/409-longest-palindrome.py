class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        freq = Counter(s)
        oddcnt = 0
        for key in freq:
            if freq[key] % 2 != 0:
                oddcnt += 1
                freq[key] -= 1
            length += freq[key]
        return length + 1 if oddcnt > 0 else length  