class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
#         res = 0
#         store = defaultdict(list)
        
#         for word in words:
#             store[word[0]].append(word)
                
#         for char in s:
#             group = store[char]
#             store[char] = []
#             for word in group:
#                 if len(word) > 1:
#                     store[word[1]].append(word[1:])
#                 else:
#                     res += 1
            
#         return res

        hash = {}
        numOfSubs = 0
        for i in range(len(words)):
            j = 0
            z = 0
            if words[i] in hash:
                if hash[words[i]]:
                    numOfSubs += 1
                continue

            while j < len(words[i]) and z < len(s):
                if words[i][j] == s[z]:
                    j += 1
                    z += 1
                else:
                    z += 1
            if j == len(words[i]):
                hash[words[i]] = True
                numOfSubs += 1
            else:
                hash[words[i]] = False
        return numOfSubs