class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        ans = ''
        contains = set([''])
        for word in words:
            if word[:-1] in contains:
                contains.add(word)
                if len(word) > len(ans):
                    ans = word
        return ans