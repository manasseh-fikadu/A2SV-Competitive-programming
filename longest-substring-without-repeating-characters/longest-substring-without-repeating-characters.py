class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in Set:
                Set.remove(s[left])
                left += 1

            Set.add(s[right])
            res = max(res, right - left + 1)
        return res