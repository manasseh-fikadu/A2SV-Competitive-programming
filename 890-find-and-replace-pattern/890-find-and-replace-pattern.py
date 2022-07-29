class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:      
        res = []
        
        for word in words:
            d, flag = {}, 1
            for i, char in enumerate(pattern):
                if (char in d and d[char] != word[i]) or (char not in d and word[i] in d.values()):
                    flag = 0
                    break
                d[char] = word[i]
            if flag:
                res.append(word)
        return res
    
        