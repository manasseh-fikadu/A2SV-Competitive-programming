class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def __init__(self):
            self.root = TrieNode()
            self.root.endOfWord = True

    def insert(self, word) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True
        
    def longestWord(self, words: List[str]) -> str:
        for word in words:
            self.insert(word)
        return self.dfs(self.root)
    
    def dfs(self, node, string = ''):
        if  not node.endOfWord:
            return string[:-1]
        if not node.children:
            return string
        
        maxVal = ''
        
        for child in node.children:
            res = self.dfs(node.children[child], string + child)
            
            if len(res) > len(maxVal):
                maxVal = res
        
            elif len(res) < len(maxVal):
                continue
            
            elif maxVal > res:
                maxVal = res
        
        return maxVal