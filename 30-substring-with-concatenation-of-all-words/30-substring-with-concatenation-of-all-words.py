class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        nsingle = len(words[0])
        cnt = Counter(words)
        
        def isValid(subs):
            split = [subs[i:i+nsingle] for i in range(0, len(subs), nsingle)]     
            if Counter(split) == cnt:
                return True
            return False
        
        i = 0
        j = n * nsingle
        ans=[]
        
        while j <= len(s):
            if isValid(s[i:j]):
                ans.append(i)
            i += 1
            j += 1
        
        return ans
