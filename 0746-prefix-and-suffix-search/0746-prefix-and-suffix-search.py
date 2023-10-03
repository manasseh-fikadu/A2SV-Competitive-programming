class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.weight = -1
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, weight):
        node = self.root
        node.weight = max(node.weight, weight)
        for ch in word:
            node = node.children[ch]
            node.weight = max(node.weight, weight)
    
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return -1
            node = node.children[ch]
        return node.weight


class WordFilter:
    def __init__(self, words):
        self.prefixes_suffixes = {}
        for index, word in enumerate(words):
            for i in range(len(word) + 1):
                for j in range(len(word) + 1):
                    self.prefixes_suffixes[(word[:i], word[j:])] = index

    def f(self, prefix: str, suffix: str) -> int:
        return self.prefixes_suffixes.get((prefix, suffix), -1)


                


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)

