class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for str_ in words:
            if str_.startswith(pref):
                count += 1
                
        return count