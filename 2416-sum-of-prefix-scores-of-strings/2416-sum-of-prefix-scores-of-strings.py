class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.count += 1
        
    def prefix(self, prefix):
        curr = self.root
        t = curr.count
        for char in prefix:
            curr = curr.children[char]
            t += curr.count
        return t
       
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        ans = []
        for word in words:
            trie.insert(word)
            
        for word in words:
            ans.append(trie.prefix(word))
            
        return ans     