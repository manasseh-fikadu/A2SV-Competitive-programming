class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited, store = set(), set()
        
        for i in range(len(s)):
            curr = s[i:i+10]
            if curr in visited:
                store.add(curr)
            visited.add(curr)
            
        return list(store)
            