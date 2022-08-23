class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        M, N = len(p), len(s)
        
        counterP = Counter(p)
        counterW = Counter(s[:M-1])
        
        for i in range(M-1, N): 
            st_idx = i - (M-1) 
            
            counterW[s[i]] += 1 
            if counterW == counterP:
                ans.append(st_idx)
            
            counterW[s[st_idx]] -= 1
            if counterW[s[st_idx]] == 0:
                counterW.pop(s[st_idx])
            
        return ans