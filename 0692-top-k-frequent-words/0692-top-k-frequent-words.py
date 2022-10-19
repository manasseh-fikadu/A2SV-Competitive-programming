class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = 0
        self.word = ''
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.heap = []
        
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        for word in words:
            self.insert(word)
        node = self.root
        self.dfs(node)
        return [heappop(self.heap)[1] for i in range(k)]
        
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            
            curr = curr.children.get(ch)
        curr.freq += 1
        curr.word = word
        
    def dfs(self, node):
        if not node.children:
            return heappush(self.heap, (-node.freq, node.word))
        
        if node.freq > 0:
            heappush(self.heap, (-node.freq, node.word))
            
        for ch in node.children:
            self.dfs(node.children.get(ch))