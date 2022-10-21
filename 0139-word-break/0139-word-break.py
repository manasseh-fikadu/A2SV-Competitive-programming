class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endOfWord
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        can_make = [False] * (len(s) + 1)
        can_make[0] = True
        
        for word in wordDict:
            trie.insert(word)
            
        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):
                if can_make[j] and trie.search(s[j:i]):
                    can_make[i] = True
                    break
                    
        return can_make[-1]
                    
            
        
                    