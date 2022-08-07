class Solution:
    def countVowelPermutation(self, n: int) -> int:
        counts = {vowel: 1 for vowel in "aeiou"}
        
        for _ in range(n-1):
            store = {}

            store['a'] = counts['e'] + counts['i'] + counts['u']
            store['e'] = counts['a'] + counts['i']
            store['i'] = counts['e'] + counts['o']
            store['o'] = counts['i']
            store['u'] = counts['i'] + counts['o']
            counts = store
            
        return sum(counts.values()) % (10**9 + 7)