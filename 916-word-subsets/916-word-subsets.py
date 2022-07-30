class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required = defaultdict(int)
        
        for b in words2:
            freq = Counter(b)
            for letter, count in freq.items():
                required[letter] = max(required[letter], count)
         
        ans = []
        
        for a in words1:
            freq = Counter(a)
            if all(freq[letter] >= count for letter, count in required.items()):
                ans.append(a)
                
        return ans
                
                