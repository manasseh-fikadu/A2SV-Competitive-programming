class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def grouper(S):
            result = []
            for k, grp in itertools.groupby(S):
                result.append((k, len(list(grp))))
            return zip(*result)
                    
        R, count = grouper(S)
        ans = 0
        for word in words:
            R2, count2 = grouper(word)
            if R2 != R: continue
            flag = True
            for c1, c2 in zip(count, count2):
                if c1 < max(c2, 3) and c1 != c2:
                    flag = False
                    break
            if flag:
                ans += 1

        return ans