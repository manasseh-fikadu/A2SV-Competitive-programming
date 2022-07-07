class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()

        def insert(word):
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.endOfWord = True
            
        for word in words:
            insert(word)
            
        res = ''
        
        for word in words:
            if len(word) < len(res): continue

            curr = root

            for letter in word:
                curr = curr.children[letter]
                if not curr.endOfWord: break
            
            if curr.endOfWord:
                if (len(word) > len(res) or (len(word) == len(res) and word < res)):
                    res = word        
            
        return res